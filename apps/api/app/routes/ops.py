from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse

from app.db import Repository, get_repository
from app.schemas import OpsSummaryOut
from app.services.ops_dashboard import render_ops_dashboard

router = APIRouter(prefix="/ops", tags=["ops"])


@router.get("/summary", response_model=OpsSummaryOut)
def ops_summary(repository: Repository = Depends(get_repository)) -> OpsSummaryOut:
    return repository.ops_summary()


@router.get("/dashboard", response_class=HTMLResponse)
def ops_dashboard(repository: Repository = Depends(get_repository)) -> HTMLResponse:
    html = render_ops_dashboard(
        summary=repository.ops_summary(),
        agent_runs=list(repository.list_agent_runs()),
        failure_cases=list(repository.list_failure_cases()),
        retrieval_runs=list(repository.list_retrieval_runs()),
        noise_gate_records=list(repository.list_noise_gate_records()),
        report_records=list(repository.list_report_records()),
    )
    return HTMLResponse(content=html)
