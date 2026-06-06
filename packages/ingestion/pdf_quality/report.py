from typing import Any

from packages.ingestion.pdf_quality.fixture import PdfExtractionQualityFixture


def build_pdf_extraction_quality_report(
    fixture: PdfExtractionQualityFixture,
    evaluation: dict[str, Any],
) -> str:
    aggregate = evaluation["aggregate"]
    per_fixture = evaluation["per_fixture"]
    lines = [
        "# PDF Extraction Quality Report",
        "",
        "Phase marker: PDF extraction quality report v0.",
        "",
        "This report records manifest fixture metric output for PDF extraction quality evaluation plumbing.",
        "",
        "It is not robust PDF extraction evidence.",
        "",
        "## Fixture",
        "",
        f"- fixture: `{fixture.packet}`",
        f"- fixture count: {len(fixture.fixtures)}",
        f"- binary PDF fixtures included: {fixture.binary_pdf_fixtures_included}",
        f"- robust PDF extraction claimed: {fixture.robust_pdf_extraction_claimed}",
        f"- claim boundary: `{evaluation['claim_boundary']}`",
        "",
        "## Aggregate Metrics",
        "",
        "| Metric | Value |",
        "|---|---:|",
    ]
    for metric in [
        "observed_fixture_count",
        "not_evaluated_fixture_count",
        "page_coverage",
        "character_coverage",
        "expected_span_recall",
        "table_row_coverage",
        "table_cell_recall",
        "ocr_page_coverage",
        "warning_correctness",
        "failure_case_candidate_correctness",
    ]:
        lines.append(f"| {metric} | {_format_metric(aggregate.get(metric))} |")

    lines.extend(
        [
            "",
            "## Per-fixture Metrics",
            "",
            "| Fixture | Status | expected_span_recall | table_cell_recall | warning_correctness | failure_case_candidate_correctness |",
            "|---|---|---:|---:|---:|---:|",
        ]
    )
    for item in fixture.fixtures:
        row = per_fixture[item.fixture_id]
        lines.append(
            "| "
            + " | ".join(
                [
                    item.fixture_id,
                    row["status"],
                    _format_metric(row["expected_span_recall"]),
                    _format_metric(row["table_cell_recall"]),
                    _format_metric(row["warning_correctness"]),
                    _format_metric(row["failure_case_candidate_correctness"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Boundary Notes",
            "",
        ]
    )
    for note in evaluation["boundary_notes"]:
        lines.append(f"- {note}")

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "This report intentionally evaluates only a partial observation fixture. Four fixture roles remain `not_evaluated`, so this artifact is useful as evaluator plumbing and gap visibility, not as extraction quality evidence.",
            "",
            "The table-heavy observation currently records zero extracted table rows. That keeps table extraction weakness visible instead of turning table candidate diagnostics into a table extraction claim.",
            "",
            "The table contract now records expected table cells separately from row count, so future table extraction must recover expected cell values instead of passing on positive row count alone.",
            "",
            "The scanned-image fixture is not evaluated here. OCR remains outside this gate.",
            "",
            "## Boundary",
            "",
            "This is not robust PDF extraction implementation.",
            "",
            "This is not OCR implementation.",
            "",
            "This is not table extraction implementation.",
            "",
            "This is not hosted deployment evidence.",
            "",
            "This is not product-complete.",
        ]
    )
    return "\n".join(lines) + "\n"


def _format_metric(value: Any) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        text = f"{value:.4f}".rstrip("0").rstrip(".")
        return text or "0"
    return str(value)
