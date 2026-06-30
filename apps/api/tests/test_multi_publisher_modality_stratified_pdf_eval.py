import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
EVIDENCE_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/multi-publisher-modality-stratified-pdf-eval.json"
)
REPORT_PATH = (
    REPO_ROOT
    / "docs/evaluation/multi-publisher-modality-stratified-pdf-eval-report.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.multi_publisher_modality_stratified_pdf_eval import (  # noqa: E402
    NEXT_GATE,
    PHASE_MARKER,
    build_multi_publisher_modality_stratified_pdf_eval_report,
    build_multi_publisher_modality_stratified_pdf_eval_summary,
    load_multi_publisher_modality_stratified_pdf_eval,
)


def test_multi_publisher_modality_stratified_pdf_eval_keeps_claim_blocked():
    matrix = load_multi_publisher_modality_stratified_pdf_eval(EVIDENCE_PATH)
    summary = build_multi_publisher_modality_stratified_pdf_eval_summary(matrix)

    assert summary["phase_marker"] == PHASE_MARKER
    assert summary["matrix_status"] == "passed"
    assert summary["coverage_status"] == "partial"
    assert summary["robust_pdf_eval_status"] == "blocked"
    assert summary["publisher_stratum_count"] == 3
    assert summary["modality_stratum_count"] == 9
    assert summary["matrix_cell_count"] == 12
    assert summary["covered_limited_cell_count"] == 6
    assert summary["missing_cell_count"] == 6
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["next_gate"] == NEXT_GATE

    for publisher in [
        "U.S. Bureau of Economic Analysis",
        "U.S. Energy Information Administration",
        "National Archives and Records Administration",
    ]:
        assert publisher in summary["publishers"]

    for axis in ["publisher", "modality", "failure_class", "evidence_role"]:
        assert axis in summary["stratification_axes"]

    for missing in [
        "reading_order_ground_truth_missing",
        "rendered_visual_fidelity_missing",
        "labeled_layout_ground_truth_missing",
        "image_chart_interpretation_missing",
        "real_world_no_extractable_text_failure_missing",
        "external_reviewer_validation_missing",
    ]:
        assert missing in summary["blocked_reasons"]


def test_multi_publisher_modality_stratified_pdf_eval_report_is_current_and_bounded():
    matrix = load_multi_publisher_modality_stratified_pdf_eval(EVIDENCE_PATH)
    summary = build_multi_publisher_modality_stratified_pdf_eval_summary(matrix)
    report = build_multi_publisher_modality_stratified_pdf_eval_report(summary)

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Multi-publisher Modality-stratified PDF Eval" in report
    assert "multi_publisher_modality_stratified_pdf_eval_v0" in report
    assert "matrix_status -> passed" in report
    assert "coverage_status -> partial" in report
    assert "robust_pdf_eval_status -> blocked" in report
    assert "can_claim_robust_pdf_extraction -> false" in report
    assert "targeted_real_world_pdf_fixture_expansion_v0" in report
    assert "not robust PDF extraction evidence" in report
    assert "not arbitrary-market PDF parsing evidence" in report
    assert "not table extraction benchmark evidence" in report
    assert "not OCR quality benchmark evidence" in report
    assert "does not add new runtime evidence" in report


def test_multi_publisher_modality_stratified_pdf_eval_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.multi_publisher_modality_stratified_pdf_eval_command",
            "--evidence",
            str(EVIDENCE_PATH),
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
    assert "multi_publisher_modality_stratified_pdf_eval_report_current" in result.stdout
    assert "coverage_status=partial" in result.stdout
    assert "can_claim_robust_pdf_extraction=false" in result.stdout


def test_multi_publisher_modality_stratified_pdf_eval_docs_and_surface_linked():
    review_path = (
        REPO_ROOT / "docs/review/multi-publisher-modality-stratified-pdf-eval.md"
    )
    spec_path = (
        REPO_ROOT
        / "docs/specs/2026-06-30-multi-publisher-modality-stratified-pdf-eval.md"
    )
    assert review_path.is_file()
    assert spec_path.is_file()
    assert REPORT_PATH.is_file()

    surfaces = [
        review_path.read_text(encoding="utf-8"),
        (REPO_ROOT / "README.md").read_text(encoding="utf-8"),
        (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8"),
        (REPO_ROOT / "docs/MASTER-SPEC.md").read_text(encoding="utf-8"),
        (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8"),
        (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
            encoding="utf-8"
        ),
        (REPO_ROOT / "apps/api/app/services/proof_gap_registry.py").read_text(
            encoding="utf-8"
        ),
    ]

    for surface in surfaces:
        assert "multi_publisher_modality_stratified_pdf_eval_v0" in surface
        assert "targeted_real_world_pdf_fixture_expansion_v0" in surface

    for boundary in [
        "not robust PDF extraction evidence",
        "not arbitrary-market PDF parsing evidence",
        "not table extraction benchmark evidence",
        "not OCR quality benchmark evidence",
        "not hosted deployment evidence",
        "not external reviewer feedback",
        "not product-complete",
    ]:
        assert boundary in surfaces[0]
