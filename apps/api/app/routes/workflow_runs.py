from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.db import Repository, get_repository
from app.schemas import (
    EvidenceLedgerStoredEntryOut,
    NoiseGateStoredRecordOut,
    ReportStoredRecordOut,
    WorkflowLineageOut,
    WorkflowLineageSummaryOut,
    WorkflowNoiseGateLineageOut,
    WorkflowProofBundleOut,
    WorkflowReportLineageOut,
    WorkflowRunCreate,
    WorkflowRunDetailOut,
    WorkflowRunDetailSummaryOut,
    WorkflowRunExecutePreviewOut,
    WorkflowRunExecutePreviewRequest,
    WorkflowRunOut,
    WorkflowStageEventOut,
    WorkflowStageLinkOut,
    TraceLookupOut,
    TraceLookupSummaryOut,
)
from app.services.workflow_execution import execute_workflow_preview

router = APIRouter(prefix="/workflow-runs", tags=["workflow-runs"])


@router.post("", response_model=WorkflowRunOut, status_code=201)
def create_workflow_run(
    payload: WorkflowRunCreate,
    repository: Repository = Depends(get_repository),
) -> dict:
    return repository.create_workflow_run(payload)


@router.post("/execute-preview", response_model=WorkflowRunExecutePreviewOut, status_code=201)
def execute_workflow_run_preview(
    payload: WorkflowRunExecutePreviewRequest,
    repository: Repository = Depends(get_repository),
) -> WorkflowRunExecutePreviewOut:
    return execute_workflow_preview(payload, repository)


@router.get("", response_model=list[WorkflowRunOut])
def list_workflow_runs(repository: Repository = Depends(get_repository)) -> list[dict]:
    return list(repository.list_workflow_runs())


@router.get("/{workflow_run_id}/lineage", response_model=WorkflowLineageOut)
def get_workflow_run_lineage(
    workflow_run_id: UUID,
    repository: Repository = Depends(get_repository),
) -> WorkflowLineageOut:
    workflow_run = repository.get_workflow_run(workflow_run_id)
    if workflow_run is None:
        raise HTTPException(status_code=404, detail="workflow run not found")
    children = repository.lookup_workflow_run_records(workflow_run_id)
    return _build_workflow_lineage(workflow_run, children)


@router.get("/{workflow_run_id}/proof-bundle", response_model=WorkflowProofBundleOut)
def get_workflow_run_proof_bundle(
    workflow_run_id: UUID,
    repository: Repository = Depends(get_repository),
) -> WorkflowProofBundleOut:
    workflow_run = repository.get_workflow_run(workflow_run_id)
    if workflow_run is None:
        raise HTTPException(status_code=404, detail="workflow run not found")
    children = repository.lookup_workflow_run_records(workflow_run_id)
    detail = _build_workflow_detail(workflow_run, children)
    lineage = _build_workflow_lineage(workflow_run, children)
    workflow_trace_id, trace_warning = _workflow_trace_id_from_run(workflow_run)
    trace = (
        _build_trace_lookup(workflow_trace_id, repository)
        if workflow_trace_id is not None
        else None
    )
    proof_surfaces = [
        f"/workflow-runs/{workflow_run_id}",
        f"/workflow-runs/{workflow_run_id}/lineage",
    ]
    warnings = [
        "Workflow proof bundle is a read model over existing records and creates no new storage.",
        "It is not distributed tracing, hosted observability, a quality benchmark, or product-complete evidence.",
    ]
    if workflow_trace_id is not None:
        proof_surfaces.append(f"/traces/{workflow_trace_id}")
    if trace_warning is not None:
        warnings.append(trace_warning)
    if detail.summary.failure_case_count:
        proof_surfaces.append(f"/failure-cases?workflow_run_id={workflow_run_id}")
        warnings.append(
            "Linked failure_cases are linked by workflow_run_id and surfaced read-only; "
            "this is not automatic failure causality or background automation."
        )
    return WorkflowProofBundleOut(
        workflow_run=WorkflowRunOut(**workflow_run),
        workflow_trace_id=workflow_trace_id,
        bundle_boundary="read_model_only_existing_records_no_new_storage",
        detail=detail,
        lineage=lineage,
        trace=trace,
        proof_surfaces=proof_surfaces,
        warnings=warnings,
    )


@router.get("/{workflow_run_id}", response_model=WorkflowRunDetailOut)
def get_workflow_run_detail(
    workflow_run_id: UUID,
    repository: Repository = Depends(get_repository),
) -> WorkflowRunDetailOut:
    workflow_run = repository.get_workflow_run(workflow_run_id)
    if workflow_run is None:
        raise HTTPException(status_code=404, detail="workflow run not found")
    children = repository.lookup_workflow_run_records(workflow_run_id)
    return _build_workflow_detail(workflow_run, children)


def _build_workflow_detail(
    workflow_run: dict,
    children: dict[str, list[dict]],
) -> WorkflowRunDetailOut:
    return WorkflowRunDetailOut(
        workflow_run=WorkflowRunOut(**workflow_run),
        retrieval_runs=children["retrieval_runs"],
        evidence_ledger_entries=children["evidence_ledger_entries"],
        noise_gate_records=children["noise_gate_records"],
        report_records=children["report_records"],
        failure_cases=children.get("failure_cases", []),
        stage_events=[
            WorkflowStageEventOut(**row)
            for row in children.get("stage_events", [])
        ],
        summary=WorkflowRunDetailSummaryOut(
            retrieval_run_count=len(children["retrieval_runs"]),
            evidence_ledger_entry_count=len(children["evidence_ledger_entries"]),
            noise_gate_record_count=len(children["noise_gate_records"]),
            report_record_count=len(children["report_records"]),
            failure_case_count=len(children.get("failure_cases", [])),
            workflow_stage_event_count=len(children.get("stage_events", [])),
        ),
    )


def _build_trace_lookup(
    workflow_trace_id: UUID,
    repository: Repository,
) -> TraceLookupOut:
    records = repository.lookup_trace_records(workflow_trace_id)
    agent_runs = [AgentRunOut(**row) for row in records["agent_runs"]]
    evidence_entries = [
        EvidenceLedgerStoredEntryOut(**row)
        for row in records["evidence_ledger_entries"]
    ]
    noise_gate_records = [
        NoiseGateStoredRecordOut(**row) for row in records["noise_gate_records"]
    ]
    report_records = [
        ReportStoredRecordOut(**row) for row in records["report_records"]
    ]
    return TraceLookupOut(
        workflow_trace_id=workflow_trace_id,
        agent_runs=agent_runs,
        evidence_ledger_entries=evidence_entries,
        noise_gate_records=noise_gate_records,
        report_records=report_records,
        summary=TraceLookupSummaryOut(
            agent_run_count=len(agent_runs),
            evidence_ledger_entry_count=len(evidence_entries),
            noise_gate_record_count=len(noise_gate_records),
            report_record_count=len(report_records),
        ),
    )


def _workflow_trace_id_from_run(workflow_run: dict) -> tuple[UUID | None, str | None]:
    value = (workflow_run.get("trace_json") or {}).get("workflow_trace_id")
    if value is None:
        return None, "No workflow_trace_id is present, so the bundle omits trace lookup."
    try:
        return UUID(str(value)), None
    except ValueError:
        return None, "workflow_trace_id is present but is not a valid UUID."


def _build_workflow_lineage(
    workflow_run: dict,
    children: dict[str, list[dict]],
) -> WorkflowLineageOut:
    evidence_rows = list(children["evidence_ledger_entries"])
    gate_rows = list(children["noise_gate_records"])
    report_rows = list(children["report_records"])
    direct_stage_links = [
        WorkflowStageLinkOut(**row) for row in children.get("direct_stage_links", [])
    ]
    evidence_by_id = {str(row["id"]): row for row in evidence_rows}
    gate_by_id = {str(row["id"]): row for row in gate_rows}

    manifest_shape_warnings: list[str] = []
    gate_lineage: list[WorkflowNoiseGateLineageOut] = []
    gate_input_reference_count = 0
    missing_reference_count = 0
    for row in gate_rows:
        input_ids, shape_warnings = _manifest_evidence_ids(row)
        manifest_shape_warnings.extend(shape_warnings)
        resolved_entries, missing_ids = _resolve_evidence_entries(input_ids, evidence_by_id)
        gate_input_reference_count += len(input_ids)
        missing_reference_count += len(missing_ids)
        gate_lineage.append(
            WorkflowNoiseGateLineageOut(
                record=NoiseGateStoredRecordOut(**row),
                input_evidence_entry_ids=input_ids,
                input_evidence_entries=resolved_entries,
                missing_evidence_entry_ids=missing_ids,
            )
        )

    report_lineage: list[WorkflowReportLineageOut] = []
    report_input_evidence_reference_count = 0
    report_input_gate_reference_count = 0
    for row in report_rows:
        input_ids, shape_warnings = _manifest_evidence_ids(row)
        manifest_shape_warnings.extend(shape_warnings)
        resolved_entries, missing_ids = _resolve_evidence_entries(input_ids, evidence_by_id)
        input_gate_id = _manifest_gate_id(row)
        resolved_gate = gate_by_id.get(input_gate_id) if input_gate_id else None
        missing_gate_id = input_gate_id if input_gate_id and resolved_gate is None else None
        report_input_evidence_reference_count += len(input_ids)
        report_input_gate_reference_count += 1 if input_gate_id else 0
        missing_reference_count += len(missing_ids) + (1 if missing_gate_id else 0)
        report_lineage.append(
            WorkflowReportLineageOut(
                record=ReportStoredRecordOut(**row),
                input_evidence_entry_ids=input_ids,
                input_evidence_entries=resolved_entries,
                input_noise_gate_record_id=input_gate_id,
                input_noise_gate_record=(
                    NoiseGateStoredRecordOut(**resolved_gate) if resolved_gate else None
                ),
                missing_evidence_entry_ids=missing_ids,
                missing_noise_gate_record_id=missing_gate_id,
            )
        )

    warnings = [
        "Workflow lineage remains a derived read model over stage_input_manifest values and direct workflow stage link rows for workflow-created records.",
        "Standalone gate/report endpoints remain payload-only unless they create explicit stage links.",
        "It adds no distributed tracing, LLM calls, or free-form final answer generation.",
    ]
    if missing_reference_count:
        warnings.append("One or more stage_input_manifest references could not be resolved.")
    warnings.extend(_unique_warnings(manifest_shape_warnings))
    warning_codes = ["derived_read_model_boundary", "local_workflow_scope"]
    if direct_stage_links:
        warning_codes.append("direct_stage_link_table")
    if missing_reference_count:
        warning_codes.append("missing_manifest_reference")
    if manifest_shape_warnings:
        warning_codes.append("invalid_manifest_shape")

    return WorkflowLineageOut(
        workflow_run=WorkflowRunOut(**workflow_run),
        lineage_boundary=(
            "derived_read_model_with_direct_workflow_stage_links"
            if direct_stage_links
            else "derived_read_model_only"
        ),
        evidence_ledger_entries=[EvidenceLedgerStoredEntryOut(**row) for row in evidence_rows],
        noise_gate_lineage=gate_lineage,
        report_lineage=report_lineage,
        direct_stage_links=direct_stage_links,
        summary=WorkflowLineageSummaryOut(
            evidence_ledger_entry_count=len(evidence_rows),
            noise_gate_record_count=len(gate_rows),
            report_record_count=len(report_rows),
            gate_input_evidence_reference_count=gate_input_reference_count,
            report_input_evidence_reference_count=report_input_evidence_reference_count,
            report_input_gate_reference_count=report_input_gate_reference_count,
            direct_stage_link_count=len(direct_stage_links),
            missing_reference_count=missing_reference_count,
        ),
        warnings=warnings,
        warning_codes=_unique_warnings(warning_codes),
    )


def _manifest_evidence_ids(row: dict) -> tuple[list[str], list[str]]:
    manifest = row.get("stage_input_manifest") or {}
    values = manifest.get("input_evidence_ledger_entry_ids", [])
    if values is None:
        return [], []
    if not isinstance(values, list):
        return [], [
            "Invalid stage_input_manifest shape: input_evidence_ledger_entry_ids must be a list."
        ]
    return [str(value) for value in values], []


def _manifest_gate_id(row: dict) -> str | None:
    manifest = row.get("stage_input_manifest") or {}
    value = manifest.get("input_noise_gate_record_id")
    return str(value) if value else None


def _resolve_evidence_entries(
    input_ids: list[str],
    evidence_by_id: dict[str, dict],
) -> tuple[list[EvidenceLedgerStoredEntryOut], list[str]]:
    resolved = [
        EvidenceLedgerStoredEntryOut(**evidence_by_id[evidence_id])
        for evidence_id in input_ids
        if evidence_id in evidence_by_id
    ]
    missing = [evidence_id for evidence_id in input_ids if evidence_id not in evidence_by_id]
    return resolved, missing


def _unique_warnings(warnings: list[str]) -> list[str]:
    unique = []
    for warning in warnings:
        if warning not in unique:
            unique.append(warning)
    return unique
