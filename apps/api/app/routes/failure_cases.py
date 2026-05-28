from fastapi import APIRouter, Depends

from app.db import Repository, get_repository
from app.schemas import FailureCaseCreate, FailureCaseOut

router = APIRouter(prefix="/failure-cases", tags=["failure-cases"])


@router.post("", response_model=FailureCaseOut, status_code=201)
def create_failure_case(
    payload: FailureCaseCreate,
    repository: Repository = Depends(get_repository),
) -> dict:
    return repository.create_failure_case(payload)


@router.get("", response_model=list[FailureCaseOut])
def list_failure_cases(repository: Repository = Depends(get_repository)) -> list[dict]:
    return list(repository.list_failure_cases())
