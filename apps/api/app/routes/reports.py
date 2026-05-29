from fastapi import APIRouter

from app.schemas import ReportPreviewOut, ReportPreviewRequest
from app.services.report_preview import preview_report

router = APIRouter(prefix="/reports", tags=["reports"])


@router.post("/preview", response_model=ReportPreviewOut)
def create_report_preview(payload: ReportPreviewRequest) -> ReportPreviewOut:
    return preview_report(payload)
