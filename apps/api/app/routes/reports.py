from fastapi import APIRouter, Depends

from app.db import Repository, get_repository
from app.schemas import ReportPreviewOut, ReportPreviewRequest
from app.services.report_preview import preview_report
from app.services.run_trace import run_with_trace

router = APIRouter(prefix="/reports", tags=["reports"])


@router.post("/preview", response_model=ReportPreviewOut)
def create_report_preview(
    payload: ReportPreviewRequest,
    repository: Repository = Depends(get_repository),
) -> ReportPreviewOut:
    return run_with_trace(
        repository,
        endpoint="POST /reports/preview",
        user_question=payload.question,
        trace_json={"evidence_entry_count": len(payload.evidence_entries)},
        operation=lambda: preview_report(payload),
        trace_from_result=lambda result: {
            "report_status": result.status,
            "gate_decision": result.gate.decision,
            "claim_count": len(result.report.claims) if result.report is not None else 0,
        },
    )
