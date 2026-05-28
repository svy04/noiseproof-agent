import re

from packages.ingestion.types import DocumentProfile, DocumentProfileInput

URL_PATTERN = re.compile(r"https?://\S+|www\.\S+", re.IGNORECASE)
DATE_PATTERN = re.compile(
    r"\b\d{4}[-./]\d{1,2}[-./]\d{1,2}\b|\b(?:Q[1-4]|FY)\s?\d{2,4}\b",
    re.IGNORECASE,
)
NUMBER_PATTERN = re.compile(r"[-+]?\d+(?:[,.]\d+)*(?:\.\d+)?%?")
HTML_TAG_PATTERN = re.compile(r"<[a-zA-Z][^>]*>")


def profile_text(payload: DocumentProfileInput) -> DocumentProfile:
    text = payload.text or ""
    source_type = payload.source_type.lower().strip() or "unknown"
    lines = text.splitlines()
    character_count = len(text)
    line_count = len(lines)
    approximate_token_count = _approximate_tokens(character_count)
    has_tables = _has_table_shape(text, source_type)
    has_urls = bool(URL_PATTERN.search(text))
    has_dates = bool(DATE_PATTERN.search(text))
    has_numbers = bool(NUMBER_PATTERN.search(text))
    extraction_quality, warnings = _quality_and_warnings(
        text=text,
        source_type=source_type,
        character_count=character_count,
        line_count=line_count,
        has_numbers=has_numbers,
        has_dates=has_dates,
    )

    return DocumentProfile(
        source_type=source_type,
        character_count=character_count,
        line_count=line_count,
        approximate_token_count=approximate_token_count,
        has_tables=has_tables,
        has_urls=has_urls,
        has_dates=has_dates,
        has_numbers=has_numbers,
        extraction_quality=extraction_quality,
        recommended_strategy=_recommend_strategy(
            source_type=source_type,
            text=text,
            has_tables=has_tables,
            line_count=line_count,
        ),
        warnings=warnings,
    )


def _approximate_tokens(character_count: int) -> int:
    if character_count <= 0:
        return 0
    return max(1, (character_count + 3) // 4)


def _has_table_shape(text: str, source_type: str) -> bool:
    if source_type == "csv":
        return True
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    pipe_rows = sum(1 for line in lines if "|" in line)
    comma_rows = sum(1 for line in lines if line.count(",") >= 2)
    return pipe_rows >= 2 or comma_rows >= 2


def _recommend_strategy(
    source_type: str,
    text: str,
    has_tables: bool,
    line_count: int,
) -> str:
    if source_type == "csv" or has_tables:
        return "row-aware"
    if source_type in {"html", "url"} or HTML_TAG_PATTERN.search(text):
        return "html-main-content"
    if source_type in {"markdown", "md"} or re.search(r"(?m)^#{1,6}\s+", text):
        return "heading-aware"
    if line_count > 40:
        return "section-then-window"
    return "fixed-window"


def _quality_and_warnings(
    text: str,
    source_type: str,
    character_count: int,
    line_count: int,
    has_numbers: bool,
    has_dates: bool,
) -> tuple[str, list[str]]:
    warnings: list[str] = []

    if character_count == 0:
        return "empty", ["No text was provided for profiling."]

    if character_count < 120:
        warnings.append("Very short text; profile may not represent a full document.")

    if "\ufffd" in text:
        warnings.append("Replacement characters detected; extraction may be corrupted.")

    if source_type in {"html", "url"} and not HTML_TAG_PATTERN.search(text):
        warnings.append("Source type suggests HTML/URL, but no HTML tags were detected.")

    if source_type == "csv" and "," not in text:
        warnings.append("Source type is CSV, but comma-separated structure was not detected.")

    if not has_dates:
        warnings.append("No obvious source date detected.")

    if not has_numbers:
        warnings.append("No numeric signal detected.")

    if line_count <= 1 and character_count > 500:
        warnings.append("Long single-line text; upstream extraction may have lost structure.")

    if len(warnings) >= 3:
        return "low", warnings
    if warnings:
        return "medium", warnings
    return "high", warnings
