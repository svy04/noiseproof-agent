import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
PLAN_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/targeted-real-world-pdf-fixture-expansion-plan.json"
)
REPORT_PATH = (
    REPO_ROOT
    / "docs/evaluation/targeted-real-world-pdf-fixture-expansion-report.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.targeted_fixture_expansion import (  # noqa: E402
    NEXT_GATE,
    PHASE_MARKER,
    build_targeted_real_world_pdf_fixture_expansion_report,
    build_targeted_real_world_pdf_fixture_expansion_summary,
    load_targeted_real_world_pdf_fixture_expansion_plan,
)


def test_targeted_real_world_pdf_fixture_expansion_covers_missing_cells_without_runtime_work():
    plan = load_targeted_real_world_pdf_fixture_expansion_plan(PLAN_PATH)
    summary = build_targeted_real_world_pdf_fixture_expansion_summary(plan)

    assert summary["phase_marker"] == PHASE_MARKER
    assert summary["previous_gate"] == "multi_publisher_modality_stratified_pdf_eval_v0"
    assert summary["plan_status"] == "passed"
    assert summary["downloaded_candidate_count"] == 0
    assert summary["runtime_work_performed"] is False
    assert summary["pdf_downloads_performed"] is False
    assert summary["parser_calls_performed"] is False
    assert summary["ocr_calls_performed"] is False
    assert summary["table_extraction_calls_performed"] is False
    assert summary["llm_calls_performed"] is False
    assert summary["binary_files_committed"] is False
    assert summary["raw_text_committed"] is False
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["candidate_count"] == 6
    assert summary["missing_cell_count"] == 6
    assert summary["covered_missing_cell_count"] == 6
    assert summary["source_policy_source_count"] >= 5
    assert summary["next_gate"] == NEXT_GATE

    expected_cells = {
        "multi_publisher_reading_order",
        "multi_publisher_rendered_visual_fidelity",
        "multi_publisher_labeled_layout_ground_truth",
        "multi_publisher_image_chart_interpretation",
        "multi_publisher_no_extractable_text_failure",
        "external_reviewer_validation",
    }
    assert set(summary["covered_missing_cells"]) == expected_cells


def test_targeted_real_world_pdf_fixture_expansion_candidates_have_policy_and_stop_conditions():
    plan = load_targeted_real_world_pdf_fixture_expansion_plan(PLAN_PATH)

    for candidate in plan["candidates"]:
        assert candidate["fixture_id"]
        assert candidate["target_missing_cell"]
        assert candidate["source_url"].startswith("https://")
        assert candidate["policy_source_url"].startswith("https://")
        assert candidate["policy_review_status"] in {
            "source_policy_reviewed_metadata_only",
            "external_review_route_only",
        }
        assert candidate["download_status"] == "not_downloaded"
        assert candidate["local_pdf_path"] is None
        assert candidate["sha256"] is None
        assert candidate["evaluation_intent"]
        assert candidate["acceptance_checks"]
        assert candidate["stop_conditions"]
        assert candidate["boundary"]


def test_targeted_real_world_pdf_fixture_expansion_report_is_current_and_bounded():
    plan = load_targeted_real_world_pdf_fixture_expansion_plan(PLAN_PATH)
    summary = build_targeted_real_world_pdf_fixture_expansion_summary(plan)
    report = build_targeted_real_world_pdf_fixture_expansion_report(summary)

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Targeted Real-world PDF Fixture Expansion Plan" in report
    assert "targeted_real_world_pdf_fixture_expansion_v0" in report
    assert "plan_status -> passed" in report
    assert "candidate_count -> 6" in report
    assert "covered_missing_cell_count -> 6" in report
    assert "downloaded_candidate_count -> 0" in report
    assert "can_claim_robust_pdf_extraction -> false" in report
    assert "not robust PDF extraction evidence" in report
    assert "does not add new runtime evidence" in report
    assert "source_policy_reviewed_metadata_only" in report


def test_targeted_real_world_pdf_fixture_expansion_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.targeted_real_world_pdf_fixture_expansion_command",
            "--plan",
            str(PLAN_PATH),
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
    assert "targeted_real_world_pdf_fixture_expansion_report_current" in result.stdout
    assert "candidate_count=6" in result.stdout
    assert "can_claim_robust_pdf_extraction=false" in result.stdout


def test_targeted_real_world_pdf_fixture_expansion_docs_and_surfaces_are_linked():
    review_path = (
        REPO_ROOT / "docs/review/targeted-real-world-pdf-fixture-expansion.md"
    )
    spec_path = (
        REPO_ROOT
        / "docs/specs/2026-06-30-targeted-real-world-pdf-fixture-expansion.md"
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
        (REPO_ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8"),
    ]

    for surface in surfaces:
        assert "targeted_real_world_pdf_fixture_expansion_v0" in surface
        assert "real_world_pdf_fixture_source_policy_download_hash_v0" in surface

    for boundary in [
        "not robust PDF extraction evidence",
        "not arbitrary-market PDF parsing evidence",
        "not OCR quality evidence",
        "not table extraction benchmark evidence",
        "not layout fidelity evidence",
        "not hosted deployment evidence",
        "not external reviewer feedback",
        "not product-complete",
    ]:
        assert boundary in surfaces[0]
