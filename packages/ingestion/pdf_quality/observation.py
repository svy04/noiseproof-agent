from typing import Any

from packages.ingestion.types import ParseResult


def pdf_parse_result_to_quality_observation(parse_result: ParseResult) -> dict[str, Any]:
    metadata = parse_result.metadata
    failure_case_candidate = parse_result.failure_case_candidate
    table_candidate_count = _non_negative_int(metadata.get("table_candidate_count"))
    table_extraction_performed = bool(metadata.get("table_extraction_performed"))
    password_required = bool(metadata.get("password_required"))
    warnings = _quality_warnings(
        list(parse_result.warnings),
        table_candidate_count=table_candidate_count,
        table_extraction_performed=table_extraction_performed,
        password_required=password_required,
    )
    return {
        "parser": parse_result.parser,
        "extracted_text": parse_result.text,
        "warnings": warnings,
        "page_count": _positive_int(metadata.get("page_count")),
        "extracted_page_count": _non_negative_int(
            metadata.get("extracted_page_count")
        ),
        "empty_page_count": _non_negative_int(metadata.get("empty_page_count")),
        "table_candidate_count": table_candidate_count,
        "table_candidate_page_counts": list(
            metadata.get("table_candidate_page_counts") or []
        ),
        "table_rows_extracted": _table_rows_extracted(metadata),
        "extracted_table_rows": _extracted_table_rows(metadata),
        "ocr_page_count": _non_negative_int(metadata.get("ocr_page_count")),
        "digital_pdf_text_extraction": bool(
            metadata.get("digital_pdf_text_extraction")
        ),
        "robust_pdf_extraction": bool(metadata.get("robust_pdf_extraction")),
        "encrypted": bool(metadata.get("encrypted")),
        "password_required": password_required,
        "table_extraction_performed": table_extraction_performed,
        "failure_case_candidate": (
            failure_case_candidate.failure_type if failure_case_candidate else None
        ),
        "failure_case_description": (
            failure_case_candidate.description if failure_case_candidate else None
        ),
        "failure_case_next_action": (
            failure_case_candidate.next_action if failure_case_candidate else None
        ),
    }


def _quality_warnings(
    warnings: list[str],
    *,
    table_candidate_count: int,
    table_extraction_performed: bool,
    password_required: bool,
) -> list[str]:
    normalized = list(warnings)
    table_boundary = "table candidate detection is not table extraction"
    if (
        table_candidate_count > 0
        and not table_extraction_performed
        and not any(table_boundary in warning.lower() for warning in normalized)
    ):
        normalized.append(table_boundary)
    password_boundary = "password required"
    if password_required and not any(password_boundary in warning.lower() for warning in normalized):
        normalized.append(password_boundary)
    return normalized


def _table_rows_extracted(metadata: dict[str, Any]) -> int:
    if not metadata.get("table_extraction_performed"):
        return 0
    return _non_negative_int(metadata.get("table_rows_extracted"))


def _extracted_table_rows(metadata: dict[str, Any]) -> list[list[str]]:
    if not metadata.get("table_extraction_performed"):
        return []
    value = metadata.get("extracted_table_rows")
    if not isinstance(value, list):
        return []
    rows: list[list[str]] = []
    for row in value:
        if not isinstance(row, list):
            continue
        rows.append([str(cell) for cell in row])
    return rows


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
