from dataclasses import asdict

from app.schemas import UploadPdfQualityPreviewOut
from app.services.upload_preview import parse_uploaded_content
from packages.ingestion.pdf_quality.observation import (
    pdf_parse_result_to_quality_observation,
)

PDF_QUALITY_PREVIEW_BOUNDARY = (
    "pdf_quality_observation_preview_only_no_robust_extraction_claim"
)


def preview_uploaded_pdf_quality(
    *,
    filename: str | None,
    content_type: str | None,
    source_type: str | None,
    content: bytes,
) -> UploadPdfQualityPreviewOut:
    warnings: list[str] = [
        "PDF quality preview is preview-only and does not create documents or persist parse records.",
        "PDF quality observation preview does not claim robust PDF extraction.",
    ]
    parsed, profile = parse_uploaded_content(
        source_type=source_type or "pdf",
        filename=filename,
        content_type=content_type,
        content=content,
        warnings=warnings,
    )
    if parsed.source_type != "pdf":
        warnings.append(
            "PDF quality preview expected source_type 'pdf'; observation is limited to parser boundary metadata."
        )
    observation = pdf_parse_result_to_quality_observation(parsed)

    return UploadPdfQualityPreviewOut(
        filename=filename,
        content_type=content_type,
        byte_count=len(content),
        source_type=parsed.source_type,
        parser=parsed.parser,
        quality_observation=observation,
        quality_summary=_quality_summary(observation),
        quality_boundary=PDF_QUALITY_PREVIEW_BOUNDARY,
        warnings=warnings + parsed.warnings + observation["warnings"],
        failure_case_candidate=(
            asdict(parsed.failure_case_candidate)
            if parsed.failure_case_candidate is not None
            else None
        ),
        profile=profile,
        persistence_boundary="preview_only_not_persisted",
    )


def _quality_summary(observation: dict) -> dict:
    return {
        "page_count": observation.get("page_count"),
        "extracted_page_count": observation.get("extracted_page_count"),
        "empty_page_count": observation.get("empty_page_count"),
        "digital_pdf_text_extraction": observation.get("digital_pdf_text_extraction"),
        "robust_pdf_extraction": observation.get("robust_pdf_extraction"),
        "encrypted": observation.get("encrypted"),
        "password_required": observation.get("password_required"),
        "table_candidate_count": observation.get("table_candidate_count"),
        "table_extraction_performed": observation.get("table_extraction_performed"),
        "failure_case_candidate": observation.get("failure_case_candidate"),
        "reviewer_boundary": "summary_only_not_robust_pdf_extraction_evidence",
    }
