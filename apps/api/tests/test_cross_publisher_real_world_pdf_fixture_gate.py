import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
BASE_MATRIX_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/multi-real-world-pdf-parse-observations.json"
)
OBSERVATION_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/cross-publisher-real-world-pdf-observation.json"
)
REPORT_PATH = (
    REPO_ROOT / "docs/evaluation/cross-publisher-real-world-pdf-fixture-gate-report.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.cross_publisher_real_world_fixture import (
    NEXT_GATE,
    PHASE_MARKER,
    build_cross_publisher_fixture_gate_report,
    build_cross_publisher_fixture_gate_summary,
    load_cross_publisher_observation,
)
from packages.ingestion.pdf_quality.multi_real_world_pdf_parse_observation import (
    load_multi_real_world_pdf_parse_observation_matrix,
)


def test_cross_publisher_fixture_gate_adds_eia_without_robust_claim():
    base_matrix = load_multi_real_world_pdf_parse_observation_matrix(BASE_MATRIX_PATH)
    observation = load_cross_publisher_observation(OBSERVATION_PATH)

    summary = build_cross_publisher_fixture_gate_summary(base_matrix, observation)

    assert summary["phase_marker"] == PHASE_MARKER
    assert summary["cross_publisher_gate_status"] == "passed"
    assert summary["base_observed_fixture_count"] == 3
    assert summary["added_observed_fixture_count"] == 1
    assert summary["combined_observed_fixture_count"] == 4
    assert summary["distinct_publisher_count"] == 2
    assert summary["publishers"] == [
        "U.S. Bureau of Economic Analysis",
        "U.S. Energy Information Administration",
    ]
    assert summary["has_cross_publisher_coverage"] is True
    assert summary["can_claim_cross_publisher_real_world_pdf_fixture_coverage"] is True
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["has_table_extraction_evidence"] is False
    assert summary["has_ocr_evidence"] is False
    assert summary["has_layout_fidelity_evidence"] is False
    assert summary["next_gate"] == NEXT_GATE
    assert "cross_publisher_coverage_visible" in summary["passed_checks"]
    assert "table_extraction_evidence_missing" in summary["blocked_reasons"]
    assert "ocr_evidence_missing" in summary["blocked_reasons"]
    assert "layout_fidelity_evidence_missing" in summary["blocked_reasons"]


def test_cross_publisher_fixture_gate_report_is_current_and_bounded():
    base_matrix = load_multi_real_world_pdf_parse_observation_matrix(BASE_MATRIX_PATH)
    observation = load_cross_publisher_observation(OBSERVATION_PATH)
    summary = build_cross_publisher_fixture_gate_summary(base_matrix, observation)
    report = build_cross_publisher_fixture_gate_report(summary)

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Cross-publisher Real-world PDF Fixture Gate" in report
    assert "cross_publisher_real_world_pdf_fixture_gate_v0" in report
    assert "cross_publisher_gate_status -> passed" in report
    assert "distinct_publisher_count -> 2" in report
    assert "U.S. Energy Information Administration" in report
    assert "can_claim_cross_publisher_real_world_pdf_fixture_coverage -> true" in report
    assert "can_claim_robust_pdf_extraction -> false" in report
    assert "real_world_table_extraction_evidence_gate_v0" in report
    assert "not robust PDF extraction evidence" in report
    assert "not table extraction evidence" in report


def test_cross_publisher_fixture_gate_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.cross_publisher_real_world_pdf_fixture_gate_command",
            "--base-matrix",
            str(BASE_MATRIX_PATH),
            "--observation",
            str(OBSERVATION_PATH),
            "--output",
            str(REPORT_PATH),
            "--check",
        ],
        cwd=REPO_ROOT / "apps/api",
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert "cross_publisher_real_world_pdf_fixture_gate_report_current" in result.stdout
    assert "cross_publisher_gate_status=passed" in result.stdout
    assert "not robust PDF extraction evidence" in result.stdout


def test_cross_publisher_fixture_gate_docs_and_proof_surface_are_linked():
    review_path = REPO_ROOT / "docs/review/cross-publisher-real-world-pdf-fixture-gate.md"
    spec_path = (
        REPO_ROOT
        / "docs/specs/2026-06-30-cross-publisher-real-world-pdf-fixture-gate.md"
    )
    assert review_path.is_file()
    assert spec_path.is_file()
    assert REPORT_PATH.is_file()

    review = review_path.read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    registry = (REPO_ROOT / "apps/api/app/services/proof_gap_registry.py").read_text(
        encoding="utf-8"
    )

    for surface in [review, readme, goal, runbook, portfolio, registry]:
        assert "cross_publisher_real_world_pdf_fixture_gate_v0" in surface
        assert "real_world_table_extraction_evidence_gate_v0" in surface

    for boundary in [
        "not robust PDF extraction evidence",
        "not arbitrary-market PDF parsing evidence",
        "not OCR evidence",
        "not table extraction evidence",
        "not layout fidelity evidence",
        "not hosted deployment evidence",
        "not external reviewer feedback",
        "not product-complete",
    ]:
        assert boundary in review

