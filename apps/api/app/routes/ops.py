from fastapi import APIRouter, Depends

from app.db import Repository, get_repository
from app.schemas import OpsSummaryOut

router = APIRouter(prefix="/ops", tags=["ops"])


@router.get("/summary", response_model=OpsSummaryOut)
def ops_summary(repository: Repository = Depends(get_repository)) -> OpsSummaryOut:
    return repository.ops_summary()
