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
    WorkflowReportLineageOut,
    WorkflowRunCreate,
    WorkflowRunDetailOut,
    WorkflowRunDetailSummaryOut,
    WorkflowRunExecutePreviewOut,
    WorkflowRunExecutePreviewRequest,
    WorkflowRunOut,
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


@router.get("/{workflow_run_id}", response_model=WorkflowRunDetailOut)
def get_workflow_run_detail(
    workflow_run_id: UUID,
    repository: Repository = Depends(get_repository),
) -> WorkflowRunDetailOut:
    workflow_run = repository.get_workflow_run(workflow_run_id)
    if workflow_run is None:
        raise HTTPException(status_code=404, detail="workflow run not found")
    children = repository.lookup_workflow_run_records(workflow_run_id)
    return WorkflowRunDetailOut(
        workflow_run=WorkflowRunOut(**workflow_run),
        retrieval_runs=children["retrieval_runs"],
        evidence_ledger_entries=children["evidence_ledger_entries"],
        noise_gate_records=children["noise_gate_records"],
        report_records=children["report_records"],
        summary=WorkflowRunDetailSummaryOut(
            retrieval_run_count=len(children["retrieval_runs"]),
            evidence_ledger_entry_count=len(children["evidence_ledger_entries"]),
            noise_gate_record_count=len(children["noise_gate_records"]),
            report_record_count=len(children["report_records"]),
        ),
    )


def _build_workflow_lineage(
    workflow_run: dict,
    children: dict[str, list[dict]],
) -> WorkflowLineageOut:
    evidence_rows = list(children["evidence_ledger_entries"])
    gate_rows = list(children["noise_gate_records"])
    report_rows = list(children["report_records"])
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
        "Workflow lineage read model is a derived read model over existing workflow child records and stage_input_manifest values.",
        "It adds no storage, foreign-key links, join tables, distributed tracing, LLM calls, or free-form final answer generation.",
    ]
    if missing_reference_count:
        warnings.append("One or more stage_input_manifest references could not be resolved.")
    warnings.extend(_unique_warnings(manifest_shape_warnings))

    return WorkflowLineageOut(
        workflow_run=WorkflowRunOut(**workflow_run),
        lineage_boundary="derived_read_model_only",
        evidence_ledger_entries=[EvidenceLedgerStoredEntryOut(**row) for row in evidence_rows],
        noise_gate_lineage=gate_lineage,
        report_lineage=report_lineage,
        summary=WorkflowLineageSummaryOut(
            evidence_ledger_entry_count=len(evidence_rows),
            noise_gate_record_count=len(gate_rows),
            report_record_count=len(report_rows),
            gate_input_evidence_reference_count=gate_input_reference_count,
            report_input_evidence_reference_count=report_input_evidence_reference_count,
            report_input_gate_reference_count=report_input_gate_reference_count,
            missing_reference_count=missing_reference_count,
        ),
        warnings=warnings,
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
