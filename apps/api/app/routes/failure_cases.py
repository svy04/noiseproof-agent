from fastapi import APIRouter, Depends

from app.db import Repository, get_repository
from app.schemas import (
    FailureCaseCreate,
    FailureCaseDraftPreviewOut,
    FailureCaseDraftPreviewRequest,
    FailureCaseOut,
    FailureCaseWorkflowReviewQueueOut,
)
from app.services.failure_case_draft import preview_failure_case_draft
from app.services.failure_case_review_queue import build_failure_case_workflow_review_queue

router = APIRouter(prefix="/failure-cases", tags=["failure-cases"])


@router.post("", response_model=FailureCaseOut, status_code=201)
def create_failure_case(
    payload: FailureCaseCreate,
    repository: Repository = Depends(get_repository),
) -> dict:
    return repository.create_failure_case(payload)


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
def list_failure_cases(repository: Repository = Depends(get_repository)) -> list[dict]:
    return list(repository.list_failure_cases())
