from fastapi import APIRouter, Depends

from app.db import Repository, get_repository
from app.schemas import RetrievalRunOut, RetrievalRunRequest, RetrievalRunResponse
from app.services.retrieval_run import run_retrieval

router = APIRouter(prefix="/retrieval-runs", tags=["retrieval-runs"])


@router.post("", response_model=RetrievalRunResponse, status_code=201)
def create_retrieval_run(
    payload: RetrievalRunRequest,
    repository: Repository = Depends(get_repository),
) -> RetrievalRunResponse:
    return run_retrieval(payload, repository)


@router.get("", response_model=list[RetrievalRunOut])
def list_retrieval_runs(repository: Repository = Depends(get_repository)) -> list[dict]:
    return list(repository.list_retrieval_runs())
