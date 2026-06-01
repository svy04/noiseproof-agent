from app.schemas import (
    FailureCaseDraftPreviewRequest,
    UploadFailureCaseDraftPreviewOut,
)
from app.services.failure_case_draft import preview_failure_case_draft
from app.services.upload_report_preview import preview_uploaded_report


def preview_uploaded_failure_case_draft(
    *,
    question: str,
    filename: str | None,
    content_type: str | None,
    source_type: str | None,
    content: bytes,
    strategy: str,
    top_k: int,
    max_characters: int,
    overlap: int,
) -> UploadFailureCaseDraftPreviewOut:
    report = preview_uploaded_report(
        question=question,
        filename=filename,
        content_type=content_type,
        source_type=source_type,
        content=content,
        strategy=strategy,
        top_k=top_k,
        max_characters=max_characters,
        overlap=overlap,
    )
    failure_status = _failure_status(report.status)
    error_message = _error_message(report)
    draft_preview = preview_failure_case_draft(
        FailureCaseDraftPreviewRequest(
            question=question,
            workflow_status=failure_status,
            error_message=error_message,
            trace_json={
                "stage": "uploaded_file_report_preview",
                "error_type": _error_type(report.status),
                "report_status": report.status,
                "gate_decision": report.report.gate.decision,
            },
        )
    )
    warnings = [
        "Upload failure-case draft preview is preview-only and does not create failure_cases.",
        "A human confirmation boundary is required before any failure-case persistence.",
        "This is not automatic failure detection or root-cause automation.",
    ]

    return UploadFailureCaseDraftPreviewOut(
        filename=filename,
        content_type=content_type,
        byte_count=len(content),
        persistence_boundary="preview_only_not_persisted",
        source_type=report.source_type,
        question=question,
        status=report.status,
        report=report,
        draft_preview=draft_preview,
        warnings=warnings + report.warnings + draft_preview.warnings,
    )


def _failure_status(report_status: str) -> str:
    if report_status in {"blocked", "needs_revision"}:
        return report_status
    return "needs_revision"


def _error_type(report_status: str) -> str:
    if report_status == "blocked":
        return "UploadedReportBlocked"
    if report_status == "needs_revision":
        return "UploadedReportNeedsRevision"
    return "UploadedReportReviewNeeded"


def _error_message(report) -> str:
    if report.report.required_revisions:
        return " ".join(report.report.required_revisions)
    if report.report.fallback_message:
        return report.report.fallback_message
    return "Uploaded report preview requires human review before persistence."
