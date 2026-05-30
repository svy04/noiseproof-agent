from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.db import Repository, get_repository
from app.schemas import (
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
