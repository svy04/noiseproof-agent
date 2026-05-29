from fastapi import APIRouter, Depends

from app.db import Repository, get_repository
from app.schemas import WorkflowRunCreate, WorkflowRunOut

router = APIRouter(prefix="/workflow-runs", tags=["workflow-runs"])


@router.post("", response_model=WorkflowRunOut, status_code=201)
def create_workflow_run(
    payload: WorkflowRunCreate,
    repository: Repository = Depends(get_repository),
) -> dict:
    return repository.create_workflow_run(payload)


@router.get("", response_model=list[WorkflowRunOut])
def list_workflow_runs(repository: Repository = Depends(get_repository)) -> list[dict]:
    return list(repository.list_workflow_runs())
