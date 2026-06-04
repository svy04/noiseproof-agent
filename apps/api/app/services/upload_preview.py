from dataclasses import asdict
from pathlib import Path

from app.schemas import DocumentProfileOut, UploadPreviewOut
from packages.ingestion.profiler import profile_text
from packages.ingestion.selector import parse_document
from packages.ingestion.types import DocumentProfileInput, ParseInput, ParseResult

EXTENSION_SOURCE_TYPES = {
    ".md": "markdown",
    ".markdown": "markdown",
    ".txt": "markdown",
    ".csv": "csv",
    ".html": "html",
    ".htm": "html",
    ".pdf": "pdf",
}

CONTENT_TYPE_SOURCE_TYPES = {
    "text/markdown": "markdown",
    "text/plain": "markdown",
    "text/csv": "csv",
    "application/csv": "csv",
    "text/html": "html",
    "application/xhtml+xml": "html",
    "application/pdf": "pdf",
}


def preview_upload(
    *,
    filename: str | None,
    content_type: str | None,
    source_type: str | None,
    content: bytes,
) -> UploadPreviewOut:
    warnings: list[str] = [
        "Upload preview is preview-only and does not create documents or persist parse records.",
        "File upload preview does not claim robust PDF extraction.",
    ]
    parsed, profile = parse_uploaded_content(
        source_type=source_type,
        filename=filename,
        content_type=content_type,
        content=content,
        warnings=warnings,
    )

    return UploadPreviewOut(
        filename=filename,
        content_type=content_type,
        byte_count=len(content),
        persistence_boundary="preview_only_not_persisted",
        source_type=parsed.source_type,
        parser=parsed.parser,
        text=parsed.text,
        metadata=parsed.metadata,
        warnings=warnings + parsed.warnings,
        failure_case_candidate=(
            asdict(parsed.failure_case_candidate)
            if parsed.failure_case_candidate is not None
            else None
        ),
        profile=profile,
    )


def parse_uploaded_content(
    *,
    filename: str | None,
    content_type: str | None,
    source_type: str | None,
    content: bytes,
    warnings: list[str],
) -> tuple[ParseResult, DocumentProfileOut]:
    inferred_source_type = infer_upload_source_type(
        source_type=source_type,
        filename=filename,
        content_type=content_type,
        warnings=warnings,
    )
    text = (
        ""
        if _looks_like_pdf_bytes(inferred_source_type, content)
        else decode_upload_content(content, warnings)
    )
    source_uri = f"upload://{filename}" if filename else "upload://unnamed"
    parsed = parse_document(
        ParseInput(
            source_type=inferred_source_type,
            content=text,
            content_bytes=content,
            filename=filename,
            source_uri=source_uri,
        )
    )
    profile = profile_text(
        DocumentProfileInput(
            source_type=parsed.source_type,
            text=parsed.text,
            filename=filename,
            source_uri=source_uri,
        )
    )
    return parsed, DocumentProfileOut(**profile.__dict__)


def infer_upload_source_type(
    *,
    source_type: str | None,
    filename: str | None,
    content_type: str | None,
    warnings: list[str],
) -> str:
    explicit = (source_type or "").strip().lower()
    if explicit:
        return explicit

    suffix = Path(filename or "").suffix.lower()
    if suffix in EXTENSION_SOURCE_TYPES:
        return EXTENSION_SOURCE_TYPES[suffix]

    normalized_content_type = (content_type or "").split(";")[0].strip().lower()
    if normalized_content_type in CONTENT_TYPE_SOURCE_TYPES:
        return CONTENT_TYPE_SOURCE_TYPES[normalized_content_type]

    warnings.append("Upload preview could not infer a supported source_type.")
    return "unknown"


def decode_upload_content(content: bytes, warnings: list[str]) -> str:
    try:
        return content.decode("utf-8")
    except UnicodeDecodeError:
        warnings.append("Uploaded bytes were decoded with replacement characters.")
        return content.decode("utf-8", errors="replace")


def _looks_like_pdf_bytes(source_type: str, content: bytes) -> bool:
    return source_type == "pdf" and content.lstrip().startswith(b"%PDF")
