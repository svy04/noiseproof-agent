import json
from pathlib import Path
import subprocess
import sys

REPO_ROOT = Path(__file__).resolve().parents[3]
FIXTURE_ROOT = REPO_ROOT / "examples/pdf-extraction-quality"
PACK_PATH = FIXTURE_ROOT / "missing-runtime-observations.json"
REPORT_PATH = (
    REPO_ROOT
    / "docs/evaluation/missing-pdf-runtime-observation-pack-report.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.fixture import load_pdf_extraction_quality_fixture
from packages.ingestion.pdf_quality.missing_runtime_pack import (
    REQUIRED_MISSING_PDF_RUNTIME_FIXTURE_IDS,
    build_missing_pdf_runtime_observation_pack_report,
    build_missing_pdf_runtime_observation_pack_summary,
    load_missing_pdf_runtime_observation_pack,
)


def _base_observations() -> dict:
    return json.loads((FIXTURE_ROOT / "observations.json").read_text(encoding="utf-8"))


def test_missing_pdf_runtime_observation_pack_validates_required_roles_and_boundaries():
    pack = load_missing_pdf_runtime_observation_pack(PACK_PATH)

    assert pack["packet"] == "missing_pdf_runtime_observation_pack_v0"
    assert pack["robust_pdf_extraction_claimed"] is False
    assert pack["claim_boundary"] == (
        "missing_runtime_observation_pack_only_not_robust_pdf_extraction"
    )
    assert set(pack["observations"]) == set(REQUIRED_MISSING_PDF_RUNTIME_FIXTURE_IDS)

    scanned = pack["observations"]["scanned_image_pdf"]
    assert scanned["runtime_observed"] is True
    assert scanned["ocr_performed"] is False
    assert scanned["failure_case_candidate"] == "pdf_no_extractable_text"
    assert any("OCR is required" in warning for warning in scanned["warnings"])

    image_heavy = pack["observations"]["image_heavy_pdf"]
    assert image_heavy["runtime_observed"] is True
    assert image_heavy["image_chart_interpretation_claimed"] is False
    assert "caption text" in image_heavy["extracted_text"]
    assert any("image/chart interpretation is not claimed" in warning for warning in image_heavy["warnings"])

    layout = pack["observations"]["multi_column_layout_pdf"]
    assert layout["runtime_observed"] is True
    assert layout["layout_fidelity_claimed"] is False
    assert "left column claim" in layout["extracted_text"]
    assert any("layout fidelity is not claimed" in warning for warning in layout["warnings"])

    empty = pack["observations"]["no_extractable_text_pdf"]
    assert empty["runtime_observed"] is True
    assert empty["failure_case_candidate"] == "pdf_no_extractable_text"
    assert empty["extracted_text"] == ""


def test_missing_pdf_runtime_observation_pack_summary_keeps_robust_claim_blocked():
    fixture = load_pdf_extraction_quality_fixture(FIXTURE_ROOT)
    pack = load_missing_pdf_runtime_observation_pack(PACK_PATH)
    summary = build_missing_pdf_runtime_observation_pack_summary(
        fixture,
        _base_observations(),
        pack,
    )

    assert summary["phase_marker"] == "missing_pdf_runtime_observation_pack_v0"
    assert summary["fixture_count"] == 8
    assert summary["base_observed_fixture_count"] == 4
    assert summary["pack_observed_fixture_count"] == 4
    assert summary["combined_observed_fixture_count"] == 8
    assert summary["remaining_missing_runtime_observation_fixture_ids"] == []
    assert summary["quality_gate_status"] == "blocked"
    assert summary["robust_pdf_extraction_claimed"] is False
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert "not robust PDF extraction evidence" in summary["boundary_notes"]
    assert "scanned_image_pdf" in summary["runtime_observation_fixture_ids"]
    assert "ocr_adapter_not_run" in summary["per_fixture"]["scanned_image_pdf"][
        "limitation_codes"
    ]
    assert "image_chart_interpretation_not_claimed" in summary["per_fixture"][
        "image_heavy_pdf"
    ]["limitation_codes"]
    assert "layout_fidelity_not_claimed" in summary["per_fixture"][
        "multi_column_layout_pdf"
    ]["limitation_codes"]


def test_missing_pdf_runtime_observation_pack_report_matches_committed_artifact():
    fixture = load_pdf_extraction_quality_fixture(FIXTURE_ROOT)
    pack = load_missing_pdf_runtime_observation_pack(PACK_PATH)
    summary = build_missing_pdf_runtime_observation_pack_summary(
        fixture,
        _base_observations(),
        pack,
    )
    report = build_missing_pdf_runtime_observation_pack_report(summary)
    committed = REPORT_PATH.read_text(encoding="utf-8")

    assert report == committed
    assert "Missing PDF Runtime Observation Pack" in report
    assert "missing_pdf_runtime_observation_pack_v0" in report
    assert "| fixture_count | 8 |" in report
    assert "| base_observed_fixture_count | 4 |" in report
    assert "| pack_observed_fixture_count | 4 |" in report
    assert "| combined_observed_fixture_count | 8 |" in report
    assert "| can_claim_robust_pdf_extraction | false |" in report
    assert "scanned_image_pdf" in report
    assert "image_heavy_pdf" in report
    assert "multi_column_layout_pdf" in report
    assert "no_extractable_text_pdf" in report
    assert "not robust PDF extraction evidence" in report
    assert "not OCR evidence" in report
    assert "not layout fidelity evidence" in report


def test_missing_pdf_runtime_observation_pack_command_check_mode_accepts_committed_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.missing_pdf_runtime_observation_pack_command",
            "--fixture",
            str(FIXTURE_ROOT),
            "--base-observations",
            str(FIXTURE_ROOT / "observations.json"),
            "--pack",
            str(PACK_PATH),
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
    assert "missing_pdf_runtime_observation_pack_report_current" in result.stdout
    assert "byte-for-byte regeneration" in result.stdout
    assert "not robust PDF extraction evidence" in result.stdout
