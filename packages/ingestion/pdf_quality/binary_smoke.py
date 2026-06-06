from pathlib import Path
from typing import Any

from packages.ingestion.parsers.pdf import PdfParser
from packages.ingestion.pdf_quality.binary_fixture import (
    load_pdf_binary_fixture_provenance,
)
from packages.ingestion.pdf_quality.table_adapter import (
    extract_pdf_tables_with_pymupdf,
)
from packages.ingestion.types import ParseInput


PDF_BINARY_FIXTURE_SMOKE_BOUNDARY = (
    "binary_fixture_smoke_only_not_robust_pdf_extraction"
)


def run_pdf_binary_fixture_smoke(path: Path | str) -> dict[str, Any]:
    root = Path(path)
    packet = load_pdf_binary_fixture_provenance(root)
    parser = PdfParser()
    per_fixture: dict[str, dict[str, Any]] = {}

    for item in packet["fixtures"]:
        fixture_id = str(item["fixture_id"])
        file_path = root / str(item["path"])
        content = file_path.read_bytes()
        parse_result = parser.parse(
            ParseInput(
                source_type="pdf",
                content_bytes=content,
                filename=str(item["path"]),
            )
        )
        expected_spans = [str(span) for span in item.get("expected_spans", [])]
        expected_table_rows = _normalize_rows(item.get("expected_table_rows", []))
        table_adapter_result = (
            _table_adapter_summary(content, expected_table_rows)
            if expected_table_rows
            else None
        )
        expected_spans_found = _expected_spans_found(
            parse_result.text,
            expected_spans,
        )
        table_rows_found = (
            bool(table_adapter_result["expected_table_rows_found"])
            if table_adapter_result
            else True
        )
        passed = (
            parse_result.metadata.get("robust_pdf_extraction") is False
            and expected_spans_found
            and table_rows_found
            and parse_result.failure_case_candidate is None
        )

        per_fixture[fixture_id] = {
            "status": "passed" if passed else "failed",
            "path": item["path"],
            "parser": parse_result.parser,
            "digital_pdf_text_extraction": bool(
                parse_result.metadata.get("digital_pdf_text_extraction")
            ),
            "robust_pdf_extraction": bool(
                parse_result.metadata.get("robust_pdf_extraction")
            ),
            "expected_spans_found": expected_spans_found,
            "page_count": parse_result.metadata.get("page_count"),
            "table_candidate_count": parse_result.metadata.get(
                "table_candidate_count",
                0,
            ),
            "table_extraction_performed": bool(
                parse_result.metadata.get("table_extraction_performed")
            ),
            "failure_case_candidate": (
                parse_result.failure_case_candidate.failure_type
                if parse_result.failure_case_candidate
                else None
            ),
            "warnings": list(parse_result.warnings),
            "table_adapter": table_adapter_result,
        }

    passed_count = sum(1 for row in per_fixture.values() if row["status"] == "passed")
    failed_count = len(per_fixture) - passed_count
    return {
        "packet": packet["packet"],
        "claim_boundary": PDF_BINARY_FIXTURE_SMOKE_BOUNDARY,
        "robust_pdf_extraction_claimed": False,
        "fixture_count": len(per_fixture),
        "passed_count": passed_count,
        "failed_count": failed_count,
        "per_fixture": per_fixture,
        "boundary_notes": [
            "not robust PDF extraction evidence",
            "not OCR evidence",
            "not default PdfParser table extraction",
            "not table extraction evidence for arbitrary market PDFs",
            "not hosted deployment evidence",
            "not product-complete",
        ],
    }


def _table_adapter_summary(
    content: bytes,
    expected_table_rows: list[list[str]],
) -> dict[str, Any]:
    result = extract_pdf_tables_with_pymupdf(content)
    extracted_table_rows = _normalize_rows(result.get("extracted_table_rows", []))
    return {
        "table_extraction_engine": result["table_extraction_engine"],
        "table_extraction_performed": bool(result["table_extraction_performed"]),
        "robust_pdf_extraction": bool(result["robust_pdf_extraction"]),
        "extracted_table_rows": extracted_table_rows,
        "table_rows_extracted": result["table_rows_extracted"],
        "table_cell_count": result["table_cell_count"],
        "expected_table_rows_found": extracted_table_rows == expected_table_rows,
        "failure_case_candidate": result["failure_case_candidate"],
        "warnings": list(result["warnings"]),
    }


def _expected_spans_found(text: str, expected_spans: list[str]) -> bool:
    normalized = _normalize_text(text)
    return all(_normalize_text(span) in normalized for span in expected_spans)


def _normalize_rows(value: object) -> list[list[str]]:
    if not isinstance(value, list):
        return []
    rows: list[list[str]] = []
    for row in value:
        if not isinstance(row, list):
            continue
        rows.append([_normalize_cell(cell) for cell in row])
    return rows


def _normalize_cell(value: object) -> str:
    return " ".join(str(value).strip().split())


def _normalize_text(value: object) -> str:
    return " ".join(str(value).lower().split())
