from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.db import Repository, get_repository
from app.schemas import (
    FailureCaseCreate,
    FailureCaseDraftPreviewOut,
    FailureCaseDraftPreviewRequest,
    FailureCaseOut,
    FailureCaseWorkflowPersistenceOut,
    FailureCaseWorkflowReviewQueueOut,
)
from app.services.failure_case_draft import preview_failure_case_draft
from app.services.failure_case_review_queue import (
    REVIEWABLE_WORKFLOW_STATUSES,
    build_failure_case_workflow_review_queue,
)

router = APIRouter(prefix="/failure-cases", tags=["failure-cases"])


@router.post("", response_model=FailureCaseOut, status_code=201)
def create_failure_case(
    payload: FailureCaseCreate,
    repository: Repository = Depends(get_repository),
) -> dict:
    return repository.create_failure_case(payload)


@router.post(
    "/workflow-runs/{workflow_run_id}",
    response_model=FailureCaseWorkflowPersistenceOut,
    status_code=201,
)
def create_failure_case_from_workflow_run(
    workflow_run_id: UUID,
    repository: Repository = Depends(get_repository),
) -> FailureCaseWorkflowPersistenceOut:
    workflow_run = repository.get_workflow_run(workflow_run_id)
    if workflow_run is None:
        raise HTTPException(status_code=404, detail="workflow run not found")
    workflow_status = str(workflow_run.get("status") or "")
    if workflow_status not in REVIEWABLE_WORKFLOW_STATUSES:
        raise HTTPException(
            status_code=409,
            detail="workflow status is not reviewable for failure-case persistence",
        )
    existing_failure_cases = [
        failure_case
        for failure_case in repository.list_failure_cases()
        if str(failure_case.get("workflow_run_id")) == str(workflow_run_id)
    ]
    if existing_failure_cases:
        raise HTTPException(
            status_code=409,
            detail="failure case already exists for workflow_run_id",
        )

    draft_preview = preview_failure_case_draft(
        FailureCaseDraftPreviewRequest(
            workflow_run_id=workflow_run_id,
            question=workflow_run["question"],
            workflow_status=workflow_status,
            error_message=workflow_run.get("error_message"),
            trace_json=workflow_run.get("trace_json") or {},
        )
    )
    draft = draft_preview.draft.model_copy(
        update={
            "fix_status": "open",
            "next_action": (
                "Inspect the persisted workflow failure case, decide the retry or "
                "repair path, and keep the workflow_run_id linkage visible."
            ),
        }
    )
    failure_case = repository.create_failure_case(draft)
    return FailureCaseWorkflowPersistenceOut(
        failure_case=FailureCaseOut(**failure_case),
        source_summary=draft_preview.source_summary,
        persistence_boundary="caller_triggered_workflow_failure_case_persistence",
        warnings=[
            "This is a caller-triggered deterministic handoff from workflow_run evidence to failure_cases.",
            "It is not background automation, root-cause automation, or complete workflow failure causality.",
            "It does not retry the workflow, mutate workflow child records, or call an LLM.",
        ],
    )


@router.post("/draft-preview", response_model=FailureCaseDraftPreviewOut)
def draft_failure_case(
    payload: FailureCaseDraftPreviewRequest,
) -> FailureCaseDraftPreviewOut:
    return preview_failure_case_draft(payload)


@router.get("/workflow-review-queue", response_model=FailureCaseWorkflowReviewQueueOut)
def workflow_failure_review_queue(
    repository: Repository = Depends(get_repository),
) -> FailureCaseWorkflowReviewQueueOut:
    return build_failure_case_workflow_review_queue(
        workflow_runs=list(repository.list_workflow_runs()),
        failure_cases=list(repository.list_failure_cases()),
    )


@router.get("", response_model=list[FailureCaseOut])
def list_failure_cases(
    workflow_run_id: UUID | None = None,
    repository: Repository = Depends(get_repository),
) -> list[dict]:
    rows = list(repository.list_failure_cases())
    if workflow_run_id is not None:
        rows = [
            row
            for row in rows
            if str(row.get("workflow_run_id")) == str(workflow_run_id)
        ]
    return rows
