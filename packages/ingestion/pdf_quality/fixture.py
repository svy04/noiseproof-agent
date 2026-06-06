import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class PdfExtractionQualityFixtureCase:
    fixture_id: str
    role: str
    source_shape: str
    expected_behavior: str
    expected_warnings: list[str]
    expected_spans: list[str]
    expected_table_rows: list[list[str]]


@dataclass(frozen=True)
class PdfExtractionQualityFixture:
    packet: str
    binary_pdf_fixtures_included: bool
    robust_pdf_extraction_claimed: bool
    quality_gate_required_before_robust_claim: bool
    fixtures: list[PdfExtractionQualityFixtureCase]
    quality_metrics: list[str]


def load_pdf_extraction_quality_fixture(
    path: Path | str,
) -> PdfExtractionQualityFixture:
    root = Path(path)
    manifest = json.loads((root / "fixture-manifest.json").read_text(encoding="utf-8"))
    fixtures = [
        PdfExtractionQualityFixtureCase(
            fixture_id=row["id"],
            role=row["role"],
            source_shape=row["source_shape"],
            expected_behavior=row["expected_behavior"],
            expected_warnings=list(row.get("expected_warnings", [])),
            expected_spans=list(row.get("expected_spans", [])),
            expected_table_rows=[
                [str(cell) for cell in table_row]
                for table_row in row.get("expected_table_rows", [])
            ],
        )
        for row in manifest["fixtures"]
    ]
    fixture = PdfExtractionQualityFixture(
        packet=manifest["packet"],
        binary_pdf_fixtures_included=bool(manifest["binary_pdf_fixtures_included"]),
        robust_pdf_extraction_claimed=bool(manifest["robust_pdf_extraction_claimed"]),
        quality_gate_required_before_robust_claim=bool(
            manifest["quality_gate_required_before_robust_claim"]
        ),
        fixtures=fixtures,
        quality_metrics=list(manifest["quality_metrics"]),
    )
    _validate_fixture(fixture)
    return fixture


def summarize_pdf_extraction_quality_fixture(
    fixture: PdfExtractionQualityFixture,
) -> dict[str, Any]:
    return {
        "packet": fixture.packet,
        "fixture_count": len(fixture.fixtures),
        "fixture_ids": [item.fixture_id for item in fixture.fixtures],
        "table_contract_fixture_ids": [
            item.fixture_id for item in fixture.fixtures if item.expected_table_rows
        ],
        "quality_metrics": fixture.quality_metrics,
        "binary_pdf_fixtures_included": fixture.binary_pdf_fixtures_included,
        "robust_pdf_extraction_claimed": fixture.robust_pdf_extraction_claimed,
        "quality_gate_required_before_robust_claim": (
            fixture.quality_gate_required_before_robust_claim
        ),
        "claim_boundary": "manifest_only_not_robust_pdf_extraction_evidence",
    }


def _validate_fixture(fixture: PdfExtractionQualityFixture) -> None:
    fixture_ids = [item.fixture_id for item in fixture.fixtures]
    if len(fixture_ids) != len(set(fixture_ids)):
        raise ValueError("PDF extraction quality fixture ids must be unique.")

    if fixture.robust_pdf_extraction_claimed:
        raise ValueError("Fixture packet must not claim robust PDF extraction.")

    if fixture.binary_pdf_fixtures_included:
        raise ValueError("Phase 704 evaluator expects manifest-only PDF fixtures.")

    required_metrics = {
        "page_coverage",
        "character_coverage",
        "expected_span_recall",
        "table_row_coverage",
        "table_cell_recall",
        "ocr_page_coverage",
        "warning_correctness",
        "failure_case_candidate_correctness",
    }
    missing = sorted(required_metrics.difference(fixture.quality_metrics))
    if missing:
        raise ValueError(f"Missing PDF extraction quality metrics: {missing}")

    for item in fixture.fixtures:
        if not item.expected_behavior:
            raise ValueError(f"Fixture {item.fixture_id} is missing expected_behavior.")
        if not item.expected_warnings:
            raise ValueError(f"Fixture {item.fixture_id} is missing expected_warnings.")
        if not item.expected_spans:
            raise ValueError(f"Fixture {item.fixture_id} is missing expected_spans.")
        if item.expected_table_rows and not all(item.expected_table_rows):
            raise ValueError(
                f"Fixture {item.fixture_id} has an empty expected_table_rows row."
            )
