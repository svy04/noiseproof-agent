from pathlib import Path
import subprocess
import sys

REPO_ROOT = Path(__file__).resolve().parents[3]
FIXTURE_ROOT = REPO_ROOT / "examples/pdf-extraction-quality"
REPORT_PATH = (
    REPO_ROOT
    / "docs/evaluation/ocr-layout-image-fixture-adapter-runtime-pack-report.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.fixture import load_pdf_extraction_quality_fixture
from packages.ingestion.pdf_quality.ocr_layout_image_pack import (
    build_ocr_layout_image_adapter_runtime_pack,
    build_ocr_layout_image_adapter_runtime_pack_report,
    build_ocr_layout_image_adapter_runtime_pack_summary,
)


def test_ocr_layout_image_adapter_runtime_pack_observes_supported_roles_without_overclaiming():
    pack = build_ocr_layout_image_adapter_runtime_pack()

    assert pack["packet"] == "ocr_layout_image_fixture_adapter_runtime_pack_v0"
    assert pack["claim_boundary"] == (
        "ocr_layout_image_adapter_runtime_pack_only_not_robust_pdf_extraction"
    )
    assert pack["robust_pdf_extraction_claimed"] is False
    assert set(pack["observations"]) == {
        "scanned_image_pdf",
        "image_heavy_pdf",
        "multi_column_layout_pdf",
        "no_extractable_text_pdf",
    }

    scanned = pack["observations"]["scanned_image_pdf"]
    assert scanned["adapter_runtime_observed"] is True
    assert scanned["parser"] == "pdf-pymupdf"
    assert scanned["ocr_performed"] is False
    assert scanned["adapter_boundary"] == "ocr_adapter_not_implemented"
    assert scanned["failure_case_candidate"] == "pdf_no_extractable_text"
    assert any("OCR adapter is not implemented" in warning for warning in scanned["warnings"])

    image_heavy = pack["observations"]["image_heavy_pdf"]
    assert image_heavy["adapter_runtime_observed"] is True
    assert image_heavy["image_block_diagnostics_available"] is True
    assert image_heavy["image_block_count"] >= 1
    assert image_heavy["image_chart_interpretation_claimed"] is False
    assert "caption text" in image_heavy["extracted_text"]
    assert any(
        "image/chart interpretation is not claimed" in warning
        for warning in image_heavy["warnings"]
    )

    layout = pack["observations"]["multi_column_layout_pdf"]
    assert layout["adapter_runtime_observed"] is True
    assert layout["layout_block_diagnostics_available"] is True
    assert layout["text_block_count"] >= 2
    assert layout["layout_fidelity_claimed"] is False
    assert "left column claim" in layout["extracted_text"]
    assert any("layout fidelity is not claimed" in warning for warning in layout["warnings"])

    empty = pack["observations"]["no_extractable_text_pdf"]
    assert empty["adapter_runtime_observed"] is True
    assert empty["failure_case_candidate"] == "pdf_no_extractable_text"
    assert empty["extracted_text"] == ""


def test_ocr_layout_image_adapter_runtime_pack_summary_keeps_gap_unproven():
    fixture = load_pdf_extraction_quality_fixture(FIXTURE_ROOT)
    pack = build_ocr_layout_image_adapter_runtime_pack()
    summary = build_ocr_layout_image_adapter_runtime_pack_summary(fixture, pack)

    assert summary["phase_marker"] == "ocr_layout_image_fixture_adapter_runtime_pack_v0"
    assert summary["fixture_count"] == 8
    assert summary["adapter_runtime_observed_count"] == 4
    assert summary["quality_gate_status"] == "blocked"
    assert summary["robust_pdf_extraction_claimed"] is False
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert "not robust PDF extraction evidence" in summary["boundary_notes"]
    assert "not OCR evidence" in summary["boundary_notes"]
    assert "not image/chart interpretation evidence" in summary["boundary_notes"]
    assert "not layout fidelity evidence" in summary["boundary_notes"]
    assert summary["per_fixture"]["scanned_image_pdf"]["adapter_boundary"] == (
        "ocr_adapter_not_implemented"
    )
    assert "ocr_adapter_not_implemented" in summary["per_fixture"]["scanned_image_pdf"][
        "limitation_codes"
    ]
    assert "image_chart_interpretation_not_claimed" in summary["per_fixture"][
        "image_heavy_pdf"
    ]["limitation_codes"]
    assert "layout_fidelity_not_claimed" in summary["per_fixture"][
        "multi_column_layout_pdf"
    ]["limitation_codes"]


def test_ocr_layout_image_adapter_runtime_pack_report_matches_committed_artifact():
    fixture = load_pdf_extraction_quality_fixture(FIXTURE_ROOT)
    pack = build_ocr_layout_image_adapter_runtime_pack()
    summary = build_ocr_layout_image_adapter_runtime_pack_summary(fixture, pack)
    report = build_ocr_layout_image_adapter_runtime_pack_report(summary)
    committed = REPORT_PATH.read_text(encoding="utf-8")

    assert report == committed
    assert "OCR Layout Image Fixture Adapter Runtime Pack" in report
    assert "ocr_layout_image_fixture_adapter_runtime_pack_v0" in report
    assert "| fixture_count | 8 |" in report
    assert "| adapter_runtime_observed_count | 4 |" in report
    assert "| can_claim_robust_pdf_extraction | false |" in report
    assert "ocr_adapter_not_implemented" in report
    assert "image_chart_interpretation_not_claimed" in report
    assert "layout_fidelity_not_claimed" in report
    assert "not robust PDF extraction evidence" in report


def test_ocr_layout_image_adapter_runtime_pack_command_check_mode_accepts_committed_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.ocr_layout_image_fixture_adapter_runtime_pack_command",
            "--fixture",
            str(FIXTURE_ROOT),
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
    assert "ocr_layout_image_fixture_adapter_runtime_pack_report_current" in result.stdout
    assert "byte-for-byte regeneration" in result.stdout
    assert "not robust PDF extraction evidence" in result.stdout


def test_ocr_layout_image_adapter_runtime_pack_is_documented_and_ci_checked():
    review_path = (
        REPO_ROOT
        / "docs/review/ocr-layout-image-fixture-adapter-runtime-pack.md"
    )
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

    assert "OCR Layout Image Fixture Adapter Runtime Pack" in review
    assert "ocr_layout_image_fixture_adapter_runtime_pack_v0" in review
    assert "adapter_runtime_observed_count -> 4" in review
    assert "ocr_adapter_not_implemented" in review
    assert "image_chart_interpretation_not_claimed" in review
    assert "layout_fidelity_not_claimed" in review
    assert "not robust PDF extraction evidence" in review
    assert "not OCR evidence" in review
    assert "not image/chart interpretation evidence" in review
    assert "not layout fidelity evidence" in review

    assert (
        "OCR/layout/image fixture adapter runtime pack v0: implemented"
        in readme
    )
    assert (
        "Phase 874 - OCR Layout Image Fixture Adapter Runtime Pack v0"
        in goal
    )
    assert (
        "Phase 874 adds OCR/layout/image fixture adapter runtime pack v0"
        in runbook
    )
    assert "docs/review/ocr-layout-image-fixture-adapter-runtime-pack.md" in portfolio
    assert "Latest OCR/layout/image fixture adapter runtime pack" in application_ready
    assert "Check OCR layout image fixture adapter runtime pack report staleness" in ci
    assert (
        "digital_pdf_text_diagnostics_plus_multi_fixture_gap_matrix_plus_missing_runtime_observation_pack_plus_ocr_layout_image_adapter_runtime_pack"
        in proof_gap_registry
    )
    assert (
        "committed_ocr_layout_image_binary_fixture_provenance_v0"
        in proof_gap_registry
    )
