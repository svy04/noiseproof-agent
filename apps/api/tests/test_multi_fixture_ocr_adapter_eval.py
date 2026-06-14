from pathlib import Path
import subprocess
import sys

REPO_ROOT = Path(__file__).resolve().parents[3]
FIXTURE_ROOT = REPO_ROOT / "examples/pdf-extraction-quality"
OBSERVATIONS_PATH = FIXTURE_ROOT / "observations.json"
MISSING_PACK_PATH = FIXTURE_ROOT / "missing-runtime-observations.json"
OWNER_OCR_OBSERVATION_PATH = FIXTURE_ROOT / "owner-runtime-ocr-smoke-observation.json"
REPORT_PATH = REPO_ROOT / "docs/evaluation/multi-fixture-ocr-adapter-eval-report.md"

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.fixture import load_pdf_extraction_quality_fixture
from packages.ingestion.pdf_quality.missing_runtime_pack import (
    load_missing_pdf_runtime_observation_pack,
)
from packages.ingestion.pdf_quality.multi_fixture_ocr_adapter_eval import (
    build_multi_fixture_ocr_adapter_eval_report,
    build_multi_fixture_ocr_adapter_eval_summary,
    load_owner_runtime_ocr_smoke_observation,
)


def test_multi_fixture_ocr_adapter_eval_combines_fixture_matrix_and_owner_ocr_smoke():
    fixture = load_pdf_extraction_quality_fixture(FIXTURE_ROOT)
    missing_pack = load_missing_pdf_runtime_observation_pack(MISSING_PACK_PATH)
    owner_ocr = load_owner_runtime_ocr_smoke_observation(OWNER_OCR_OBSERVATION_PATH)
    summary = build_multi_fixture_ocr_adapter_eval_summary(
        fixture=fixture,
        base_observations_path=OBSERVATIONS_PATH,
        missing_pack=missing_pack,
        owner_ocr_observation=owner_ocr,
    )

    assert summary["phase_marker"] == "multi_fixture_ocr_adapter_eval_v0"
    assert summary["base_fixture_count"] == 8
    assert summary["base_observed_fixture_count"] == 8
    assert summary["owner_runtime_ocr_smoke_count"] == 1
    assert summary["combined_fixture_signal_count"] == 9
    assert summary["owner_runtime_ocr_expected_spans_found"] is True
    assert summary["quality_gate_status"] == "blocked"
    assert summary["robust_pdf_extraction_claimed"] is False
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["ocr_evidence_scope"] == "single_synthetic_owner_runtime_fixture"
    assert summary["claim_boundary"] == (
        "multi_fixture_ocr_adapter_eval_only_not_robust_pdf_extraction"
    )
    assert "not robust PDF extraction evidence" in summary["boundary_notes"]
    assert "not arbitrary market PDF OCR evidence" in summary["boundary_notes"]

    per_signal = summary["per_signal"]
    assert per_signal["ocr_smoke_text_image_pdf"]["signal_status"] == (
        "owner_runtime_ocr_smoke_passed"
    )
    assert per_signal["ocr_smoke_text_image_pdf"]["expected_spans_found"] is True
    assert per_signal["scanned_image_pdf"]["signal_status"] == (
        "base_scanned_role_still_boundary_only"
    )
    assert "ocr_smoke_is_adjacent_not_same_fixture" in per_signal[
        "scanned_image_pdf"
    ]["limitation_codes"]
    assert per_signal["image_heavy_pdf"]["signal_status"] == (
        "image_diagnostics_only"
    )
    assert per_signal["multi_column_layout_pdf"]["signal_status"] == (
        "layout_diagnostics_only"
    )


def test_multi_fixture_ocr_adapter_eval_report_matches_committed_artifact():
    fixture = load_pdf_extraction_quality_fixture(FIXTURE_ROOT)
    missing_pack = load_missing_pdf_runtime_observation_pack(MISSING_PACK_PATH)
    owner_ocr = load_owner_runtime_ocr_smoke_observation(OWNER_OCR_OBSERVATION_PATH)
    summary = build_multi_fixture_ocr_adapter_eval_summary(
        fixture=fixture,
        base_observations_path=OBSERVATIONS_PATH,
        missing_pack=missing_pack,
        owner_ocr_observation=owner_ocr,
    )
    report = build_multi_fixture_ocr_adapter_eval_report(summary)

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Multi-fixture OCR Adapter Eval" in report
    assert "multi_fixture_ocr_adapter_eval_v0" in report
    assert "| base_fixture_count | 8 |" in report
    assert "| owner_runtime_ocr_smoke_count | 1 |" in report
    assert "| combined_fixture_signal_count | 9 |" in report
    assert "| can_claim_robust_pdf_extraction | false |" in report
    assert "owner_runtime_ocr_smoke_passed" in report
    assert "base_scanned_role_still_boundary_only" in report
    assert "not robust PDF extraction evidence" in report


def test_multi_fixture_ocr_adapter_eval_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.multi_fixture_ocr_adapter_eval_command",
            "--fixture",
            str(FIXTURE_ROOT),
            "--base-observations",
            str(OBSERVATIONS_PATH),
            "--missing-pack",
            str(MISSING_PACK_PATH),
            "--owner-ocr-observation",
            str(OWNER_OCR_OBSERVATION_PATH),
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
    assert "multi_fixture_ocr_adapter_eval_report_current" in result.stdout
    assert "byte-for-byte regeneration" in result.stdout
    assert "not robust PDF extraction evidence" in result.stdout


def test_multi_fixture_ocr_adapter_eval_docs_ci_and_proof_gap_are_wired():
    review_path = REPO_ROOT / "docs/review/multi-fixture-ocr-adapter-eval.md"
    assert review_path.is_file()

    review = review_path.read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (
        REPO_ROOT / "docs/application/portfolio-index.md"
    ).read_text(encoding="utf-8")
    application_ready = (
        REPO_ROOT / "docs/review/application-ready-review.md"
    ).read_text(encoding="utf-8")
    proof_gap_registry = (
        REPO_ROOT / "apps/api/app/services/proof_gap_registry.py"
    ).read_text(encoding="utf-8")
    ci = (REPO_ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")

    assert "Multi-fixture OCR Adapter Eval" in review
    assert "multi_fixture_ocr_adapter_eval_v0" in review
    assert "owner_runtime_ocr_smoke_count -> 1" in review
    assert "combined_fixture_signal_count -> 9" in review
    assert "not robust PDF extraction evidence" in review
    assert "not arbitrary market PDF OCR evidence" in review
    assert "Multi-fixture OCR adapter eval v0: implemented" in readme
    assert "Phase 882 - Multi-fixture OCR Adapter Eval v0" in goal
    assert "Phase 882 adds multi-fixture OCR adapter eval v0" in runbook
    assert "docs/review/multi-fixture-ocr-adapter-eval.md" in portfolio
    assert "Multi-fixture OCR Adapter Eval" in application_ready
    assert "Check multi-fixture OCR adapter eval report staleness" in ci
    assert "multi_fixture_ocr_adapter_eval_v0" in proof_gap_registry
    assert "licensed_real_world_pdf_fixture_pack_v0" in proof_gap_registry
