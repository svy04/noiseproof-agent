import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
MATRIX_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/source-policy-pdf-parse-quality-matrix.json"
)
REPORT_PATH = (
    REPO_ROOT
    / "docs/evaluation/source-policy-pdf-parse-quality-matrix-report.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.source_policy_pdf_parse_quality_matrix import (  # noqa: E402
    NEXT_GATE,
    PHASE_MARKER,
    build_source_policy_pdf_parse_quality_matrix_report,
    build_source_policy_pdf_parse_quality_matrix_summary,
    load_source_policy_pdf_parse_quality_matrix,
)


def test_source_policy_pdf_parse_quality_matrix_blocks_stronger_pdf_claims():
    matrix = load_source_policy_pdf_parse_quality_matrix(MATRIX_PATH)
    summary = build_source_policy_pdf_parse_quality_matrix_summary(matrix)

    assert summary["phase_marker"] == PHASE_MARKER
    assert summary["previous_gate"] == "source_policy_pdf_parse_observation_v0"
    assert summary["matrix_status"] == "passed"
    assert summary["quality_status"] == "blocked"
    assert summary["matrix_cell_count"] == 6
    assert summary["observed_fixture_cell_count"] == 3
    assert summary["native_text_observed_cell_count"] == 2
    assert summary["no_native_text_failure_cell_count"] == 1
    assert summary["blocked_download_cell_count"] == 2
    assert summary["external_route_cell_count"] == 1
    assert summary["quality_claim_ready_cell_count"] == 0
    assert summary["quality_blocked_cell_count"] == 6
    assert summary["can_claim_source_policy_pdf_parse_quality_matrix"] is True
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["can_claim_rendered_visual_fidelity"] is False
    assert summary["can_claim_labeled_layout_ground_truth"] is False
    assert summary["can_claim_reading_order"] is False
    assert summary["can_claim_image_chart_interpretation"] is False
    assert summary["can_claim_ocr_quality"] is False
    assert summary["can_claim_external_validation"] is False
    assert summary["next_gate"] == NEXT_GATE


def test_source_policy_pdf_parse_quality_matrix_preserves_each_missing_role():
    matrix = load_source_policy_pdf_parse_quality_matrix(MATRIX_PATH)
    summary = build_source_policy_pdf_parse_quality_matrix_summary(matrix)

    by_role = {cell["target_missing_cell"]: cell for cell in summary["matrix_cells"]}

    assert by_role["multi_publisher_rendered_visual_fidelity"][
        "cell_status"
    ] == "metadata_observed_quality_unproven"
    assert by_role["multi_publisher_labeled_layout_ground_truth"][
        "cell_status"
    ] == "metadata_observed_quality_unproven"
    assert by_role["multi_publisher_no_extractable_text_failure"][
        "cell_status"
    ] == "no_native_text_failure_candidate"
    assert by_role["multi_publisher_reading_order"]["cell_status"] == (
        "blocked_download"
    )
    assert by_role["multi_publisher_image_chart_interpretation"][
        "cell_status"
    ] == "blocked_download"
    assert by_role["external_reviewer_validation"]["cell_status"] == (
        "external_review_pending"
    )

    assert by_role["multi_publisher_no_extractable_text_failure"][
        "failure_case_candidate"
    ]["failure_type"] == "no_native_text_observed"

    for cell in summary["matrix_cells"]:
        assert cell["quality_claim_ready"] is False
        assert cell["missing_quality_evidence"]
        assert "not robust PDF extraction evidence" in cell["boundary"]


def test_source_policy_pdf_parse_quality_matrix_report_is_current_and_bounded():
    matrix = load_source_policy_pdf_parse_quality_matrix(MATRIX_PATH)
    summary = build_source_policy_pdf_parse_quality_matrix_summary(matrix)
    report = build_source_policy_pdf_parse_quality_matrix_report(summary)

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Source-policy PDF Parse Quality Matrix" in report
    assert "source_policy_pdf_parse_quality_matrix_v0" in report
    assert "quality_status -> blocked" in report
    assert "quality_claim_ready_cell_count -> 0" in report
    assert "can_claim_robust_pdf_extraction -> false" in report
    assert "can_claim_rendered_visual_fidelity -> false" in report
    assert "can_claim_external_validation -> false" in report
    assert "source_policy_pdf_quality_gap_review_v0" in report
    assert "not robust PDF extraction evidence" in report
    assert "does not add new runtime evidence" in report


def test_source_policy_pdf_parse_quality_matrix_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.source_policy_pdf_parse_quality_matrix_command",
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
    assert "source_policy_pdf_parse_quality_matrix_report_current" in result.stdout
    assert "quality_status=blocked" in result.stdout
    assert "can_claim_robust_pdf_extraction=false" in result.stdout


def test_source_policy_pdf_parse_quality_matrix_docs_and_surfaces_are_linked():
    review_path = REPO_ROOT / "docs/review/source-policy-pdf-parse-quality-matrix.md"
    spec_path = (
        REPO_ROOT
        / "docs/specs/2026-06-30-source-policy-pdf-parse-quality-matrix.md"
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
        assert "source_policy_pdf_parse_quality_matrix_v0" in surface
        assert "source_policy_pdf_quality_gap_review_v0" in surface

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
