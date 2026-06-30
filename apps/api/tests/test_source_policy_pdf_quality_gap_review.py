import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
REVIEW_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/source-policy-pdf-quality-gap-review.json"
)
REPORT_PATH = (
    REPO_ROOT / "docs/evaluation/source-policy-pdf-quality-gap-review-report.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.source_policy_pdf_quality_gap_review import (  # noqa: E402
    NEXT_GATE,
    PHASE_MARKER,
    build_source_policy_pdf_quality_gap_review_report,
    build_source_policy_pdf_quality_gap_review_summary,
    load_source_policy_pdf_quality_gap_review,
)


def test_source_policy_pdf_quality_gap_review_selects_no_native_text_failure_route():
    review = load_source_policy_pdf_quality_gap_review(REVIEW_PATH)
    summary = build_source_policy_pdf_quality_gap_review_summary(review)

    assert summary["phase_marker"] == PHASE_MARKER
    assert summary["previous_gate"] == "source_policy_pdf_parse_quality_matrix_v0"
    assert summary["review_status"] == "passed"
    assert summary["quality_gap_status"] == "open"
    assert summary["reviewed_gap_count"] == 6
    assert summary["quality_claim_ready_cell_count"] == 0
    assert summary["self_completable_without_new_download_count"] == 3
    assert summary["selected_next_gap"] == "multi_publisher_no_extractable_text_failure"
    assert summary["selected_next_gate"] == NEXT_GATE
    assert summary["can_claim_source_policy_pdf_quality_gap_review"] is True
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["can_claim_ocr_quality"] is False
    assert summary["can_claim_external_validation"] is False
    assert summary["next_gate"] == NEXT_GATE


def test_source_policy_pdf_quality_gap_review_keeps_decision_matrix_bounded():
    review = load_source_policy_pdf_quality_gap_review(REVIEW_PATH)
    summary = build_source_policy_pdf_quality_gap_review_summary(review)

    by_gap = {cell["target_missing_cell"]: cell for cell in summary["reviewed_gaps"]}

    selected = by_gap["multi_publisher_no_extractable_text_failure"]
    assert selected["selected_for_next_gate"] is True
    assert selected["recommended_gate"] == "source_policy_no_native_text_failure_route_v0"
    assert selected["requires_new_download"] is False
    assert selected["requires_ocr"] is False
    assert selected["external_dependency"] == "none"
    assert selected["decision_reason"] == (
        "real observed no-native-text failure can be preserved before OCR quality work"
    )

    assert by_gap["multi_publisher_rendered_visual_fidelity"][
        "recommended_gate"
    ] == "source_policy_rendered_visual_fidelity_ground_truth_plan_v0"
    assert by_gap["multi_publisher_labeled_layout_ground_truth"][
        "recommended_gate"
    ] == "source_policy_labeled_layout_ground_truth_plan_v0"
    assert by_gap["multi_publisher_reading_order"]["external_dependency"] == (
        "source_access_or_alternate_fixture"
    )
    assert by_gap["multi_publisher_image_chart_interpretation"][
        "external_dependency"
    ] == "source_access_or_alternate_fixture"
    assert by_gap["external_reviewer_validation"]["external_dependency"] == (
        "outside_reviewer"
    )

    for cell in summary["reviewed_gaps"]:
        assert cell["quality_claim_ready"] is False
        assert "not robust PDF extraction evidence" in cell["boundary"]


def test_source_policy_pdf_quality_gap_review_report_is_current_and_bounded():
    review = load_source_policy_pdf_quality_gap_review(REVIEW_PATH)
    summary = build_source_policy_pdf_quality_gap_review_summary(review)
    report = build_source_policy_pdf_quality_gap_review_report(summary)

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Source-policy PDF Quality Gap Review" in report
    assert "source_policy_pdf_quality_gap_review_v0" in report
    assert "quality_gap_status -> open" in report
    assert "selected_next_gap -> multi_publisher_no_extractable_text_failure" in report
    assert "selected_next_gate -> source_policy_no_native_text_failure_route_v0" in report
    assert "quality_claim_ready_cell_count -> 0" in report
    assert "can_claim_robust_pdf_extraction -> false" in report
    assert "can_claim_ocr_quality -> false" in report
    assert "not robust PDF extraction evidence" in report
    assert "does not add new runtime evidence" in report


def test_source_policy_pdf_quality_gap_review_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.source_policy_pdf_quality_gap_review_command",
            "--review",
            str(REVIEW_PATH),
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
    assert "source_policy_pdf_quality_gap_review_report_current" in result.stdout
    assert "quality_gap_status=open" in result.stdout
    assert "selected_next_gate=source_policy_no_native_text_failure_route_v0" in result.stdout
    assert "can_claim_robust_pdf_extraction=false" in result.stdout


def test_source_policy_pdf_quality_gap_review_docs_and_surfaces_are_linked():
    review_doc_path = REPO_ROOT / "docs/review/source-policy-pdf-quality-gap-review.md"
    spec_path = (
        REPO_ROOT / "docs/specs/2026-06-30-source-policy-pdf-quality-gap-review.md"
    )
    assert review_doc_path.is_file()
    assert spec_path.is_file()
    assert REPORT_PATH.is_file()

    surfaces = [
        review_doc_path.read_text(encoding="utf-8"),
        (REPO_ROOT / "README.md").read_text(encoding="utf-8"),
        (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8"),
        (REPO_ROOT / "docs/MASTER-SPEC.md").read_text(encoding="utf-8"),
        (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8"),
        (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
            encoding="utf-8"
        ),
        (REPO_ROOT / "docs/review/external-reader-proof-path.md").read_text(
            encoding="utf-8"
        ),
        (REPO_ROOT / "docs/review/proof-gap-action-surface.md").read_text(
            encoding="utf-8"
        ),
        (REPO_ROOT / "apps/api/app/services/proof_gap_registry.py").read_text(
            encoding="utf-8"
        ),
        (REPO_ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8"),
    ]

    for surface in surfaces:
        assert "source_policy_pdf_quality_gap_review_v0" in surface
        assert "source_policy_no_native_text_failure_route_v0" in surface

    for boundary in [
        "not robust PDF extraction evidence",
        "not arbitrary-market PDF parsing evidence",
        "not OCR quality evidence",
        "not table extraction benchmark evidence",
        "not rendered visual fidelity evidence",
        "not image/chart interpretation evidence",
        "not hosted deployment evidence",
        "not external reviewer feedback",
        "not product-complete",
    ]:
        assert boundary in surfaces[0]
