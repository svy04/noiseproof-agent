import time
from datetime import datetime, timezone
from uuid import uuid4

from app.db import Repository
from app.schemas import (
    EvidenceLedgerCandidateIn,
    EvidenceLedgerEntryOut,
    EvidenceLedgerPersistedOut,
    EvidenceLedgerPreviewRequest,
    EvidenceLedgerStoredEntryOut,
    FailureCaseCreate,
    NoiseGatePreviewRequest,
    NoiseGateStoredRecordOut,
    ReportPreviewRequest,
    ReportStoredRecordOut,
    WorkflowStageEventCreate,
    WorkflowStageLinkCreate,
    WorkflowRunCreate,
    WorkflowRunExecutePreviewOut,
    WorkflowRunExecutePreviewRequest,
    WorkflowRunOut,
)
from app.services.evidence_ledger import preview_evidence_ledger
from app.services.noise_gate import preview_noise_gate
from app.services.report_preview import preview_report
from app.services.retrieval_run import run_retrieval


def execute_workflow_preview(
    payload: WorkflowRunExecutePreviewRequest,
    repository: Repository,
) -> WorkflowRunExecutePreviewOut:
    started_at = time.perf_counter()
    workflow_trace_id = uuid4()
    initial_trace = {
        "stage": "workflow_execute_preview",
        "workflow_trace_id": str(workflow_trace_id),
        "source_count": len(payload.sources),
        "strategy": payload.strategy,
    }
    workflow_run = repository.create_workflow_run(
        WorkflowRunCreate(
            question=payload.question,
            status="running",
            trace_json=initial_trace,
        )
    )

    active_stage_failure_context = None
    try:
        workflow_run_id = workflow_run["id"]
        retrieval_started_at, retrieval_started_perf = _stage_started()
        active_stage_failure_context = {
            "stage_name": "retrieval",
            "stage_order": 1,
            "started_at": retrieval_started_at,
            "started_perf": retrieval_started_perf,
            "input_summary_json": {
                "source_count": len(payload.sources),
                "strategy": payload.strategy,
            },
        }
        retrieval = run_retrieval(payload, repository, workflow_run_id=workflow_run_id)
        repository.create_workflow_stage_events(
            [
                _workflow_stage_event(
                    workflow_run_id=workflow_run_id,
                    workflow_trace_id=workflow_trace_id,
                    stage_name="retrieval",
                    stage_order=1,
                    started_at=retrieval_started_at,
                    started_perf=retrieval_started_perf,
                    input_summary_json={
                        "source_count": len(payload.sources),
                        "strategy": payload.strategy,
                    },
                    output_summary_json={
                        "retrieval_run_id": str(retrieval.id),
                        "retrieval_result_count": len(retrieval.results),
                    },
                )
            ]
        )
        active_stage_failure_context = None
        evidence_started_at, evidence_started_perf = _stage_started()
        active_stage_failure_context = {
            "stage_name": "evidence_ledger",
            "stage_order": 2,
            "started_at": evidence_started_at,
            "started_perf": evidence_started_perf,
            "input_summary_json": {
                "retrieval_run_id": str(retrieval.id),
                "retrieval_result_count": len(retrieval.results),
            },
        }
        evidence_preview = preview_evidence_ledger(
            EvidenceLedgerPreviewRequest(
                question=payload.question,
                retrieval_results=[
                    EvidenceLedgerCandidateIn(**candidate.model_dump())
                    for candidate in retrieval.results
                ],
            )
        )
        evidence_rows = repository.create_evidence_ledger_entries(
            evidence_preview.question,
            evidence_preview.entries,
            workflow_trace_id=workflow_trace_id,
            agent_run_id=None,
            workflow_run_id=workflow_run_id,
        )
        repository.create_workflow_stage_events(
            [
                _workflow_stage_event(
                    workflow_run_id=workflow_run_id,
                    workflow_trace_id=workflow_trace_id,
                    stage_name="evidence_ledger",
                    stage_order=2,
                    started_at=evidence_started_at,
                    started_perf=evidence_started_perf,
                    input_summary_json={
                        "retrieval_run_id": str(retrieval.id),
                        "retrieval_result_count": len(retrieval.results),
                    },
                    output_summary_json={
                        "stored_entry_count": len(evidence_rows),
                        "evidence_statuses": sorted(
                            {str(entry["status"]) for entry in evidence_rows}
                        ),
                    },
                )
            ]
        )
        active_stage_failure_context = None
        evidence = EvidenceLedgerPersistedOut(
            question=evidence_preview.question,
            entries=[EvidenceLedgerStoredEntryOut(**entry) for entry in evidence_rows],
            summary=evidence_preview.summary,
            warnings=evidence_preview.warnings,
            stored_entry_count=len(evidence_rows),
        )
        stored_evidence_entries = [EvidenceLedgerStoredEntryOut(**entry) for entry in evidence_rows]
        downstream_evidence_entries = [
            _stored_entry_to_preview_entry(entry) for entry in stored_evidence_entries
        ]
        evidence_entry_ids = [str(entry.id) for entry in stored_evidence_entries]
        gate_stage_input_manifest = {
            "input_evidence_ledger_entry_ids": evidence_entry_ids,
            "input_noise_gate_record_id": None,
            "source": "workflow_execution_preview",
        }

        draft_claims = payload.draft_claims or [
            entry.claim for entry in downstream_evidence_entries if entry.status == "supported"
        ]
        gate_started_at, gate_started_perf = _stage_started()
        active_stage_failure_context = {
            "stage_name": "noise_gate",
            "stage_order": 3,
            "started_at": gate_started_at,
            "started_perf": gate_started_perf,
            "input_summary_json": {
                "stored_entry_count": len(evidence_rows),
                "draft_claim_count": len(draft_claims),
            },
        }
        gate_preview = preview_noise_gate(
            NoiseGatePreviewRequest(
                question=payload.question,
                evidence_entries=downstream_evidence_entries,
                draft_claims=draft_claims,
            )
        )
        gate = NoiseGateStoredRecordOut(
            **repository.create_noise_gate_record(
                gate_preview,
                evidence_entry_count=len(evidence_preview.entries),
                draft_claim_count=len(draft_claims),
                workflow_trace_id=workflow_trace_id,
                agent_run_id=None,
                workflow_run_id=workflow_run_id,
                stage_input_manifest=gate_stage_input_manifest,
            )
        )
        repository.create_workflow_stage_events(
            [
                _workflow_stage_event(
                    workflow_run_id=workflow_run_id,
                    workflow_trace_id=workflow_trace_id,
                    stage_name="noise_gate",
                    stage_order=3,
                    started_at=gate_started_at,
                    started_perf=gate_started_perf,
                    input_summary_json={
                        "stored_entry_count": len(evidence_rows),
                        "draft_claim_count": len(draft_claims),
                    },
                    output_summary_json={
                        "noise_gate_record_id": str(gate.id),
                        "decision": gate.decision,
                    },
                )
            ]
        )
        active_stage_failure_context = None
        report_stage_input_manifest = {
            "input_evidence_ledger_entry_ids": evidence_entry_ids,
            "input_noise_gate_record_id": str(gate.id),
            "source": "workflow_execution_preview",
        }

        report_started_at, report_started_perf = _stage_started()
        active_stage_failure_context = {
            "stage_name": "report",
            "stage_order": 4,
            "started_at": report_started_at,
            "started_perf": report_started_perf,
            "input_summary_json": {
                "noise_gate_record_id": str(gate.id),
                "draft_claim_count": len(draft_claims),
            },
        }
        report_preview = preview_report(
            ReportPreviewRequest(
                question=payload.question,
                evidence_entries=downstream_evidence_entries,
                draft_claims=draft_claims,
            )
        )
        report = ReportStoredRecordOut(
            **repository.create_report_record(
                report_preview,
                evidence_entry_count=len(evidence_preview.entries),
                draft_claim_count=len(draft_claims),
                workflow_trace_id=workflow_trace_id,
                agent_run_id=None,
                workflow_run_id=workflow_run_id,
                stage_input_manifest=report_stage_input_manifest,
            )
        )
        repository.create_workflow_stage_events(
            [
                _workflow_stage_event(
                    workflow_run_id=workflow_run_id,
                    workflow_trace_id=workflow_trace_id,
                    stage_name="report",
                    stage_order=4,
                    started_at=report_started_at,
                    started_perf=report_started_perf,
                    input_summary_json={
                        "noise_gate_record_id": str(gate.id),
                        "draft_claim_count": len(draft_claims),
                    },
                    output_summary_json={
                        "report_record_id": str(report.id),
                        "report_status": report.status,
                    },
                )
            ]
        )
        active_stage_failure_context = None
        repository.create_workflow_stage_links(
            _workflow_stage_links(
                workflow_run_id=workflow_run_id,
                workflow_trace_id=workflow_trace_id,
                evidence_entry_ids=evidence_entry_ids,
                gate_id=gate.id,
                report_id=report.id,
            )
        )
    except Exception as exc:
        failed_stage_name = (
            active_stage_failure_context["stage_name"]
            if active_stage_failure_context is not None
            else "unknown_stage"
        )
        if active_stage_failure_context is not None:
            try:
                repository.create_workflow_stage_events(
                    [
                        _failed_workflow_stage_event(
                            workflow_run_id=workflow_run["id"],
                            workflow_trace_id=workflow_trace_id,
                            stage_name=active_stage_failure_context["stage_name"],
                            stage_order=active_stage_failure_context["stage_order"],
                            started_at=active_stage_failure_context["started_at"],
                            started_perf=active_stage_failure_context["started_perf"],
                            input_summary_json=active_stage_failure_context[
                                "input_summary_json"
                            ],
                            exc=exc,
                        )
                    ]
                )
            except Exception:
                pass
        workflow_run = repository.update_workflow_run(
            workflow_run["id"],
            status="failed",
            error_message=str(exc),
            latency_ms=_latency_ms(started_at),
            trace_json={
                **initial_trace,
                "error_type": exc.__class__.__name__,
                "failed_stage": failed_stage_name,
            },
        )
        _auto_create_workflow_failure_case(
            workflow_run=workflow_run,
            repository=repository,
            exc=exc,
            failed_stage_name=failed_stage_name,
        )
        raise

    workflow_run = repository.update_workflow_run(
        workflow_run["id"],
        status="completed",
        error_message=None,
        latency_ms=_latency_ms(started_at),
        trace_json={
            **initial_trace,
            "retrieval_run_id": str(retrieval.id),
            "evidence_entry_ids": evidence_entry_ids,
            "evidence_entry_count": evidence.stored_entry_count,
            "gate_record_id": str(gate.id),
            "gate_decision": gate.decision,
            "report_record_id": str(report.id),
            "report_status": report.status,
        },
    )

    return WorkflowRunExecutePreviewOut(
        workflow_run=WorkflowRunOut(**workflow_run),
        workflow_trace_id=workflow_trace_id,
        execution_boundary="deterministic_preview_only",
        retrieval=retrieval,
        evidence=evidence,
        gate=gate,
        report=report,
        warnings=[
            "Workflow execution preview is deterministic and does not call an LLM.",
            "child records are attached to workflow_run_id while still carrying workflow_trace_id.",
            "stage input manifests record persisted upstream ids consumed by downstream preview stages.",
            "It does not perform semantic retrieval, embeddings, external search, or free-form final answer generation.",
        ],
    )


def _latency_ms(started_at: float) -> int:
    return max(0, round((time.perf_counter() - started_at) * 1000))


def _stage_started() -> tuple[datetime, float]:
    return datetime.now(timezone.utc), time.perf_counter()


def _workflow_stage_event(
    *,
    workflow_run_id,
    workflow_trace_id,
    stage_name: str,
    stage_order: int,
    started_at: datetime,
    started_perf: float,
    input_summary_json: dict,
    output_summary_json: dict,
) -> WorkflowStageEventCreate:
    return WorkflowStageEventCreate(
        workflow_run_id=workflow_run_id,
        workflow_trace_id=workflow_trace_id,
        stage_name=stage_name,
        stage_order=stage_order,
        stage_status="completed",
        started_at=started_at,
        ended_at=datetime.now(timezone.utc),
        latency_ms=_latency_ms(started_perf),
        input_summary_json=input_summary_json,
        output_summary_json=output_summary_json,
    )


def _failed_workflow_stage_event(
    *,
    workflow_run_id,
    workflow_trace_id,
    stage_name: str,
    stage_order: int,
    started_at: datetime,
    started_perf: float,
    input_summary_json: dict,
    exc: Exception,
) -> WorkflowStageEventCreate:
    return WorkflowStageEventCreate(
        workflow_run_id=workflow_run_id,
        workflow_trace_id=workflow_trace_id,
        stage_name=stage_name,
        stage_order=stage_order,
        stage_status="failed",
        started_at=started_at,
        ended_at=datetime.now(timezone.utc),
        latency_ms=_latency_ms(started_perf),
        input_summary_json=input_summary_json,
        output_summary_json={
            "error_type": exc.__class__.__name__,
            "error_message": str(exc),
            "failed_stage_boundary": (
                "local_workflow_stage_failure_event_auto_failure_case_local_v0"
            ),
        },
    )


def _auto_create_workflow_failure_case(
    *,
    workflow_run: dict,
    repository: Repository,
    exc: Exception,
    failed_stage_name: str,
) -> None:
    try:
        failure_case = repository.create_failure_case(
            FailureCaseCreate(
                workflow_run_id=workflow_run["id"],
                agent_run_id=None,
                failure_type="workflow_stage_error",
                description=(
                    "Auto-created from workflow stage failure at "
                    f"{failed_stage_name} for question '{workflow_run['question']}'."
                ),
                root_cause=f"{exc.__class__.__name__}: {exc}",
                fix_status="open",
                next_action=(
                    "Inspect the failed workflow stage event, confirm the failure "
                    "case, and decide whether to retry, repair input data, or "
                    "adjust the stage boundary."
                ),
            )
        )
        repository.update_workflow_run(
            workflow_run["id"],
            status=workflow_run.get("status", "failed"),
            error_message=workflow_run.get("error_message"),
            latency_ms=workflow_run.get("latency_ms") or 0,
            trace_json={
                **(workflow_run.get("trace_json") or {}),
                "auto_failure_case_id": str(failure_case["id"]),
                "failure_case_persistence_boundary": (
                    "auto_created_from_workflow_failure_local_v0"
                ),
            },
        )
    except Exception:
        pass


def _workflow_stage_links(
    *,
    workflow_run_id,
    workflow_trace_id,
    evidence_entry_ids: list[str],
    gate_id,
    report_id,
) -> list[WorkflowStageLinkCreate]:
    links: list[WorkflowStageLinkCreate] = []
    for evidence_id in evidence_entry_ids:
        links.append(
            WorkflowStageLinkCreate(
                workflow_run_id=workflow_run_id,
                workflow_trace_id=workflow_trace_id,
                link_type="evidence_to_noise_gate",
                from_table="evidence_ledger_entries",
                from_id=evidence_id,
                to_table="noise_gate_records",
                to_id=gate_id,
                source_manifest_field=(
                    "noise_gate_records.stage_input_manifest."
                    "input_evidence_ledger_entry_ids"
                ),
            )
        )
        links.append(
            WorkflowStageLinkCreate(
                workflow_run_id=workflow_run_id,
                workflow_trace_id=workflow_trace_id,
                link_type="evidence_to_report",
                from_table="evidence_ledger_entries",
                from_id=evidence_id,
                to_table="report_records",
                to_id=report_id,
                source_manifest_field=(
                    "report_records.stage_input_manifest."
                    "input_evidence_ledger_entry_ids"
                ),
            )
        )
    links.append(
        WorkflowStageLinkCreate(
            workflow_run_id=workflow_run_id,
            workflow_trace_id=workflow_trace_id,
            link_type="noise_gate_to_report",
            from_table="noise_gate_records",
            from_id=gate_id,
            to_table="report_records",
            to_id=report_id,
            source_manifest_field=(
                "report_records.stage_input_manifest.input_noise_gate_record_id"
            ),
        )
    )
    return links


def _stored_entry_to_preview_entry(entry: EvidenceLedgerStoredEntryOut) -> EvidenceLedgerEntryOut:
    return EvidenceLedgerEntryOut(
        claim=entry.claim,
        source_id=entry.source_id,
        source_type=entry.source_type,
        source_date=entry.source_date,
        evidence_span=entry.evidence_span,
        confidence=entry.confidence,
        limitation=entry.limitation,
        contradicting_source_ids=entry.contradicting_source_ids,
        status=entry.status,
        matched_terms=entry.matched_terms,
        role=entry.role,
    )
