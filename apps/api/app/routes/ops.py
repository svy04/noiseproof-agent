from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse

from app.db import Repository, get_repository
from app.schemas import OpsSummaryOut
from app.services.failure_case_review_queue import build_failure_case_workflow_review_queue
from app.services.ops_dashboard import render_ops_dashboard

router = APIRouter(prefix="/ops", tags=["ops"])


@router.get("/summary", response_model=OpsSummaryOut)
def ops_summary(repository: Repository = Depends(get_repository)) -> OpsSummaryOut:
    return repository.ops_summary()


@router.get("/dashboard", response_class=HTMLResponse)
def ops_dashboard(repository: Repository = Depends(get_repository)) -> HTMLResponse:
    failure_cases = list(repository.list_failure_cases())
    workflow_runs = list(repository.list_workflow_runs())
    html = render_ops_dashboard(
        summary=repository.ops_summary(),
        agent_runs=list(repository.list_agent_runs()),
        failure_cases=failure_cases,
        workflow_runs=workflow_runs,
        retrieval_runs=list(repository.list_retrieval_runs()),
        evidence_ledger_entries=list(repository.list_evidence_ledger_entries()),
        noise_gate_records=list(repository.list_noise_gate_records()),
        report_records=list(repository.list_report_records()),
        failure_case_review_queue=build_failure_case_workflow_review_queue(
            workflow_runs=workflow_runs,
            failure_cases=failure_cases,
        ),
    )
    return HTMLResponse(content=html)
