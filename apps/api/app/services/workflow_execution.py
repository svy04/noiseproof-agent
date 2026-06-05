import time
from uuid import uuid4

from app.db import Repository
from app.schemas import (
    EvidenceLedgerCandidateIn,
    EvidenceLedgerEntryOut,
    EvidenceLedgerPersistedOut,
    EvidenceLedgerPreviewRequest,
    EvidenceLedgerStoredEntryOut,
    NoiseGatePreviewRequest,
    NoiseGateStoredRecordOut,
    ReportPreviewRequest,
    ReportStoredRecordOut,
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

    try:
        workflow_run_id = workflow_run["id"]
        retrieval = run_retrieval(payload, repository, workflow_run_id=workflow_run_id)
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
        report_stage_input_manifest = {
            "input_evidence_ledger_entry_ids": evidence_entry_ids,
            "input_noise_gate_record_id": str(gate.id),
            "source": "workflow_execution_preview",
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
        workflow_run = repository.update_workflow_run(
            workflow_run["id"],
            status="failed",
            error_message=str(exc),
            latency_ms=_latency_ms(started_at),
            trace_json={
                **initial_trace,
                "error_type": exc.__class__.__name__,
            },
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
