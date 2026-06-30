import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
MATRIX_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/multi-real-world-pdf-parse-observations.json"
)
REPORT_PATH = (
    REPO_ROOT / "docs/evaluation/robust-pdf-real-world-quality-gate-report.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.real_world_quality_gate import (
    NEXT_GATE,
    PHASE_MARKER,
    build_real_world_quality_gate_report,
    build_real_world_quality_gate_summary,
)
from packages.ingestion.pdf_quality.multi_real_world_pdf_parse_observation import (
    load_multi_real_world_pdf_parse_observation_matrix,
)


def test_real_world_quality_gate_blocks_robust_pdf_claim_with_current_matrix():
    matrix = load_multi_real_world_pdf_parse_observation_matrix(MATRIX_PATH)
    summary = build_real_world_quality_gate_summary(matrix)

    assert summary["phase_marker"] == PHASE_MARKER
    assert summary["input_matrix_phase"] == "multi_real_world_pdf_parse_observation_matrix_v0"
    assert summary["quality_gate_status"] == "blocked"
    assert summary["observed_fixture_count"] == 3
    assert summary["distinct_publisher_count"] == 1
    assert summary["digital_text_coverage_ratio"] == 1.0
    assert summary["has_cross_publisher_coverage"] is False
    assert summary["has_table_extraction_evidence"] is False
    assert summary["has_ocr_evidence"] is False
    assert summary["has_layout_fidelity_evidence"] is False
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["next_gate"] == NEXT_GATE
    assert "cross_publisher_coverage_missing" in summary["blocked_reasons"]
    assert "table_extraction_evidence_missing" in summary["blocked_reasons"]
    assert "ocr_evidence_missing" in summary["blocked_reasons"]
    assert "layout_fidelity_evidence_missing" in summary["blocked_reasons"]
    assert "source_policy_visible" in summary["passed_checks"]
    assert "sha256_visible" in summary["passed_checks"]


def test_real_world_quality_gate_report_is_current_and_bounded():
    matrix = load_multi_real_world_pdf_parse_observation_matrix(MATRIX_PATH)
    summary = build_real_world_quality_gate_summary(matrix)
    report = build_real_world_quality_gate_report(summary)

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Robust PDF Real-world Quality Gate" in report
    assert "robust_pdf_extraction_next_real_world_quality_gate_v0" in report
    assert "quality_gate_status -> blocked" in report
    assert "can_claim_robust_pdf_extraction -> false" in report
    assert "cross_publisher_real_world_pdf_fixture_gate_v0" in report
    assert "not robust PDF extraction evidence" in report
    assert "not OCR evidence" in report
    assert "not table extraction evidence" in report


def test_real_world_quality_gate_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.robust_pdf_real_world_quality_gate_command",
            "--matrix",
            str(MATRIX_PATH),
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
    assert "robust_pdf_real_world_quality_gate_report_current" in result.stdout
    assert "quality_gate_status=blocked" in result.stdout
    assert "not robust PDF extraction evidence" in result.stdout


def test_real_world_quality_gate_docs_and_action_surface_are_linked():
    review_path = (
        REPO_ROOT
        / "docs/review/robust-pdf-extraction-next-real-world-quality-gate.md"
    )
    spec_path = (
        REPO_ROOT
        / "docs/specs/2026-06-30-robust-pdf-extraction-next-real-world-quality-gate.md"
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
    proof_gap_registry = (
        REPO_ROOT / "apps/api/app/services/proof_gap_registry.py"
    ).read_text(encoding="utf-8")

    for surface in [review, readme, goal, runbook, portfolio, proof_gap_registry]:
        assert "robust_pdf_extraction_next_real_world_quality_gate_v0" in surface
        assert "cross_publisher_real_world_pdf_fixture_gate_v0" in surface

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
