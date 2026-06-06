from typing import Any

from packages.ingestion.types import ParseResult


def pdf_parse_result_to_quality_observation(parse_result: ParseResult) -> dict[str, Any]:
    metadata = parse_result.metadata
    failure_case_candidate = parse_result.failure_case_candidate
    return {
        "parser": parse_result.parser,
        "extracted_text": parse_result.text,
        "warnings": list(parse_result.warnings),
        "page_count": _positive_int(metadata.get("page_count")),
        "extracted_page_count": _non_negative_int(
            metadata.get("extracted_page_count")
        ),
        "empty_page_count": _non_negative_int(metadata.get("empty_page_count")),
        "table_rows_extracted": _table_rows_extracted(metadata),
        "ocr_page_count": _non_negative_int(metadata.get("ocr_page_count")),
        "digital_pdf_text_extraction": bool(
            metadata.get("digital_pdf_text_extraction")
        ),
        "robust_pdf_extraction": bool(metadata.get("robust_pdf_extraction")),
        "table_extraction_performed": bool(
            metadata.get("table_extraction_performed")
        ),
        "failure_case_candidate": (
            failure_case_candidate.failure_type if failure_case_candidate else None
        ),
    }


def _table_rows_extracted(metadata: dict[str, Any]) -> int:
    if not metadata.get("table_extraction_performed"):
        return 0
    return _non_negative_int(metadata.get("table_rows_extracted"))


def _positive_int(value: Any) -> int:
    if isinstance(value, bool):
        return 1
    if isinstance(value, int) and value > 0:
        return value
    return 1


def _non_negative_int(value: Any) -> int:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return max(value, 0)
    return 0
