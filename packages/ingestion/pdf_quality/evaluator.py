from typing import Any

from packages.ingestion.pdf_quality.fixture import PdfExtractionQualityFixture

FAILURE_EXPECTED_FIXTURE_IDS = {
    "scanned_image_pdf",
    "encrypted_pdf",
    "no_extractable_text_pdf",
}


def evaluate_pdf_extraction_quality(
    fixture: PdfExtractionQualityFixture,
    observations: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    per_fixture: dict[str, dict[str, Any]] = {}

    for item in fixture.fixtures:
        observation = observations.get(item.fixture_id)
        if observation is None:
            per_fixture[item.fixture_id] = _not_evaluated_metrics()
            continue

        text = str(observation.get("extracted_text") or "")
        warnings = [str(warning) for warning in observation.get("warnings", [])]
        page_count = _positive_int(observation.get("page_count"))
        extracted_page_count = _non_negative_int(observation.get("extracted_page_count"))
        table_rows_extracted = _non_negative_int(observation.get("table_rows_extracted"))
        ocr_page_count = _non_negative_int(observation.get("ocr_page_count"))
        failure_case_candidate = observation.get("failure_case_candidate")

        per_fixture[item.fixture_id] = {
            "status": "evaluated",
            "page_coverage": _round(extracted_page_count / page_count),
            "character_coverage": 1.0 if text.strip() else 0.0,
            "expected_span_recall": _expected_span_recall(item.expected_spans, text),
            "table_row_coverage": _table_row_coverage(
                item.fixture_id,
                table_rows_extracted,
            ),
            "ocr_page_coverage": _ocr_page_coverage(
                item.fixture_id,
                ocr_page_count,
                page_count,
            ),
            "warning_correctness": _warning_correctness(
                item.expected_warnings,
                warnings,
            ),
            "failure_case_candidate_correctness": (
                _failure_case_candidate_correctness(
                    item.fixture_id,
                    failure_case_candidate,
                )
            ),
        }

    return {
        "fixture": fixture.packet,
        "per_fixture": per_fixture,
        "aggregate": _aggregate(per_fixture),
        "claim_boundary": "manifest_metric_only_not_robust_pdf_extraction",
        "robust_pdf_extraction_claimed": False,
        "boundary_notes": [
            "not robust PDF extraction evidence",
            "not OCR evidence",
            "not table extraction evidence",
            "not hosted deployment evidence",
        ],
    }


def _not_evaluated_metrics() -> dict[str, Any]:
    return {
        "status": "not_evaluated",
        "page_coverage": 0.0,
        "character_coverage": 0.0,
        "expected_span_recall": 0.0,
        "table_row_coverage": 0.0,
        "ocr_page_coverage": 0.0,
        "warning_correctness": 0.0,
        "failure_case_candidate_correctness": 0.0,
    }


def _expected_span_recall(expected_spans: list[str], text: str) -> float:
    expected = [span for span in expected_spans if not span.startswith("no span expected")]
    if not expected:
        return 1.0
    normalized_text = text.lower()
    hits = sum(1 for span in expected if span.lower() in normalized_text)
    return _round(hits / max(len(expected), 1))


def _warning_correctness(expected_warnings: list[str], warnings: list[str]) -> float:
    if not expected_warnings:
        return 1.0
    normalized_warnings = [warning.lower() for warning in warnings]
    hits = 0
    for expected in expected_warnings:
        expected_lower = expected.lower()
        if any(expected_lower in warning for warning in normalized_warnings):
            hits += 1
    return _round(hits / len(expected_warnings))


def _failure_case_candidate_correctness(
    fixture_id: str,
    failure_case_candidate: Any,
) -> float:
    failure_expected = fixture_id in FAILURE_EXPECTED_FIXTURE_IDS
    if failure_expected:
        return 1.0 if failure_case_candidate else 0.0
    return 0.0 if failure_case_candidate else 1.0


def _table_row_coverage(fixture_id: str, table_rows_extracted: int) -> float:
    if fixture_id != "table_heavy_report":
        return 1.0
    return 1.0 if table_rows_extracted > 0 else 0.0


def _ocr_page_coverage(fixture_id: str, ocr_page_count: int, page_count: int) -> float:
    if fixture_id != "scanned_image_pdf":
        return 1.0
    return _round(ocr_page_count / page_count)


def _aggregate(per_fixture: dict[str, dict[str, Any]]) -> dict[str, Any]:
    metrics = [
        "page_coverage",
        "character_coverage",
        "expected_span_recall",
        "table_row_coverage",
        "ocr_page_coverage",
        "warning_correctness",
        "failure_case_candidate_correctness",
    ]
    evaluated_rows = [
        row for row in per_fixture.values() if row["status"] == "evaluated"
    ]
    aggregate = {
        metric: _round(
            sum(float(row[metric]) for row in evaluated_rows)
            / max(len(evaluated_rows), 1)
        )
        for metric in metrics
    }
    aggregate["observed_fixture_count"] = len(evaluated_rows)
    aggregate["not_evaluated_fixture_count"] = sum(
        1 for row in per_fixture.values() if row["status"] == "not_evaluated"
    )
    return aggregate


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


def _round(value: float) -> float:
    return round(value, 4)
