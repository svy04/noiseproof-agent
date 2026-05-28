from fastapi import APIRouter, Depends

from app.db import Repository, get_repository
from app.schemas import AgentRunCreate, AgentRunOut

router = APIRouter(prefix="/agent-runs", tags=["agent-runs"])


@router.post("", response_model=AgentRunOut, status_code=201)
def create_agent_run(
    payload: AgentRunCreate,
    repository: Repository = Depends(get_repository),
) -> dict:
    return repository.create_agent_run(payload)


@router.get("", response_model=list[AgentRunOut])
def list_agent_runs(repository: Repository = Depends(get_repository)) -> list[dict]:
    return list(repository.list_agent_runs())
