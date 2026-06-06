from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[3]

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.evaluator import evaluate_pdf_extraction_quality
from packages.ingestion.pdf_quality.fixture import (
    load_pdf_extraction_quality_fixture,
    summarize_pdf_extraction_quality_fixture,
)


def test_pdf_extraction_quality_fixture_loader_keeps_boundaries_visible():
    fixture = load_pdf_extraction_quality_fixture(
        REPO_ROOT / "examples/pdf-extraction-quality"
    )

    assert fixture.packet == "pdf_extraction_quality_fixture_packet_v0"
    assert fixture.binary_pdf_fixtures_included is False
    assert fixture.robust_pdf_extraction_claimed is False
    assert fixture.quality_gate_required_before_robust_claim is True
    assert len(fixture.fixtures) == 7
    assert fixture.fixtures[0].fixture_id == "born_digital_text"

    summary = summarize_pdf_extraction_quality_fixture(fixture)

    assert summary["fixture_count"] == 7
    assert summary["binary_pdf_fixtures_included"] is False
    assert summary["robust_pdf_extraction_claimed"] is False
    assert summary["quality_gate_required_before_robust_claim"] is True
    assert "table_heavy_report" in summary["fixture_ids"]
    assert "scanned_image_pdf" in summary["fixture_ids"]
    assert "page_coverage" in summary["quality_metrics"]
    assert summary["claim_boundary"] == (
        "manifest_only_not_robust_pdf_extraction_evidence"
    )


def test_pdf_extraction_quality_evaluator_scores_observations_without_robust_claim():
    fixture = load_pdf_extraction_quality_fixture(
        REPO_ROOT / "examples/pdf-extraction-quality"
    )
    observations = {
        "born_digital_text": {
            "extracted_text": "company revenue increased and source date visible",
            "warnings": ["robust PDF extraction is not claimed"],
            "page_count": 2,
            "extracted_page_count": 2,
            "empty_page_count": 0,
            "failure_case_candidate": None,
        },
        "table_heavy_report": {
            "extracted_text": "quarterly volume table with region row label",
            "warnings": ["table candidate detection is not table extraction"],
            "page_count": 1,
            "extracted_page_count": 1,
            "table_rows_extracted": 0,
            "failure_case_candidate": None,
        },
        "encrypted_pdf": {
            "extracted_text": "",
            "warnings": ["password required"],
            "page_count": 1,
            "extracted_page_count": 0,
            "failure_case_candidate": "pdf_encrypted_requires_password",
        },
    }

    result = evaluate_pdf_extraction_quality(fixture, observations)

    assert result["claim_boundary"] == (
        "manifest_metric_only_not_robust_pdf_extraction"
    )
    assert result["robust_pdf_extraction_claimed"] is False
    assert result["aggregate"]["observed_fixture_count"] == 3
    assert result["aggregate"]["not_evaluated_fixture_count"] == 4
    assert result["per_fixture"]["born_digital_text"]["status"] == "evaluated"
    assert result["per_fixture"]["born_digital_text"]["expected_span_recall"] == 1.0
    assert result["per_fixture"]["born_digital_text"]["warning_correctness"] == 1.0
    assert result["per_fixture"]["encrypted_pdf"][
        "failure_case_candidate_correctness"
    ] == 1.0
    assert result["per_fixture"]["scanned_image_pdf"]["status"] == "not_evaluated"
    assert "not robust PDF extraction evidence" in result["boundary_notes"]
    assert "not OCR evidence" in result["boundary_notes"]
    assert "not table extraction evidence" in result["boundary_notes"]
