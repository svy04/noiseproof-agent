import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
EVIDENCE_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/robust-pdf-generalization-gap-review.json"
)
REPORT_PATH = (
    REPO_ROOT
    / "docs/evaluation/robust-pdf-generalization-gap-review-report.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.robust_pdf_generalization_gap_review import (  # noqa: E402
    NEXT_GATE,
    PHASE_MARKER,
    build_robust_pdf_generalization_gap_review_report,
    build_robust_pdf_generalization_gap_review_summary,
    load_robust_pdf_generalization_gap_review,
)


def test_robust_pdf_generalization_gap_review_keeps_robust_claim_blocked():
    review = load_robust_pdf_generalization_gap_review(EVIDENCE_PATH)
    summary = build_robust_pdf_generalization_gap_review_summary(review)

    assert summary["phase_marker"] == PHASE_MARKER
    assert summary["review_status"] == "passed"
    assert summary["generalization_gap_status"] == "open"
    assert summary["evidence_chain_count"] == 5
    assert summary["covered_capability_count"] == 5
    assert summary["missing_capability_count"] == 6
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["next_gate"] == NEXT_GATE

    for covered in [
        "digital_text_parse_observation",
        "cross_publisher_fixture_coverage",
        "table_extraction_observation",
        "ocr_observation",
        "layout_metadata_sanity_observation",
    ]:
        assert covered in summary["covered_capabilities"]

    for missing in [
        "labeled_layout_ground_truth",
        "natural_reading_order_benchmark",
        "rendered_visual_fidelity_comparison",
        "image_chart_interpretation_evidence",
        "arbitrary_market_pdf_coverage",
        "external_reviewer_validation",
    ]:
        assert missing in summary["missing_capabilities"]
        assert f"{missing}_missing" in summary["blocked_reasons"]


def test_robust_pdf_generalization_gap_review_report_is_current_and_bounded():
    review = load_robust_pdf_generalization_gap_review(EVIDENCE_PATH)
    summary = build_robust_pdf_generalization_gap_review_summary(review)
    report = build_robust_pdf_generalization_gap_review_report(summary)

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Robust PDF Extraction Generalization Gap Review" in report
    assert "robust_pdf_extraction_generalization_gap_review_v0" in report
    assert "review_status -> passed" in report
    assert "generalization_gap_status -> open" in report
    assert "can_claim_robust_pdf_extraction -> false" in report
    assert "multi_publisher_modality_stratified_pdf_eval_v0" in report
    assert "not robust PDF extraction evidence" in report
    assert "not arbitrary-market PDF parsing evidence" in report
    assert "not natural reading order correctness evidence" in report
    assert "not rendered visual fidelity evidence" in report
    assert "does not add new runtime evidence" in report


def test_robust_pdf_generalization_gap_review_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.robust_pdf_generalization_gap_review_command",
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
    assert "robust_pdf_generalization_gap_review_report_current" in result.stdout
    assert "generalization_gap_status=open" in result.stdout
    assert "can_claim_robust_pdf_extraction=false" in result.stdout


def test_robust_pdf_generalization_gap_review_docs_and_proof_surface_are_linked():
    review_path = REPO_ROOT / "docs/review/robust-pdf-generalization-gap-review.md"
    spec_path = (
        REPO_ROOT
        / "docs/specs/2026-06-30-robust-pdf-extraction-generalization-gap-review.md"
    )
    assert review_path.is_file()
    assert spec_path.is_file()
    assert REPORT_PATH.is_file()

    review_doc = review_path.read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    master_spec = (REPO_ROOT / "docs/MASTER-SPEC.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    registry = (REPO_ROOT / "apps/api/app/services/proof_gap_registry.py").read_text(
        encoding="utf-8"
    )

    for surface in [review_doc, readme, goal, master_spec, runbook, portfolio, registry]:
        assert "robust_pdf_extraction_generalization_gap_review_v0" in surface
        assert "multi_publisher_modality_stratified_pdf_eval_v0" in surface

    for boundary in [
        "not robust PDF extraction evidence",
        "not arbitrary-market PDF parsing evidence",
        "not natural reading order correctness evidence",
        "not rendered visual fidelity evidence",
        "not hosted deployment evidence",
        "not external reviewer feedback",
        "not product-complete",
    ]:
        assert boundary in review_doc
