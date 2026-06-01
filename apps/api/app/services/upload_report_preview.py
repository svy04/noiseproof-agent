from app.schemas import ReportPreviewRequest, UploadReportPreviewOut
from app.services.report_preview import preview_report
from app.services.upload_evidence_preview import preview_uploaded_evidence


def preview_uploaded_report(
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
) -> UploadReportPreviewOut:
    evidence = preview_uploaded_evidence(
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
    report = preview_report(
        ReportPreviewRequest(
            question=question,
            evidence_entries=evidence.evidence.entries,
        )
    )
    warnings = [
        "Upload report preview is preview-only and does not create report records.",
        "Upload report preview does not create retrieval_runs, Evidence Ledger entries, Noise Gate records, documents, chunks, workflow runs, or failure cases.",
    ]

    return UploadReportPreviewOut(
        filename=filename,
        content_type=content_type,
        byte_count=len(content),
        persistence_boundary="preview_only_not_persisted",
        source_type=evidence.source_type,
        question=question,
        status=report.status,
        retrieval=evidence.retrieval,
        evidence=evidence.evidence,
        report=report,
        warnings=warnings + evidence.warnings + report.warnings,
    )
