import hashlib
import json
from pathlib import Path
import subprocess
import sys

REPO_ROOT = Path(__file__).resolve().parents[3]
BINARY_ROOT = REPO_ROOT / "examples/pdf-extraction-quality/binary-fixtures"
PACKET_PATH = BINARY_ROOT / "ocr-layout-image-provenance.json"
REPORT_PATH = (
    REPO_ROOT
    / "docs/evaluation/committed-ocr-layout-image-binary-fixture-provenance-report.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.ocr_layout_image_binary_fixture import (
    REQUIRED_OCR_LAYOUT_IMAGE_BINARY_FIXTURE_IDS,
    build_committed_ocr_layout_image_binary_fixture_provenance_report,
    build_committed_ocr_layout_image_binary_fixture_provenance_summary,
    load_ocr_layout_image_binary_fixture_provenance,
)


def test_committed_ocr_layout_image_binary_fixture_packet_validates_files_and_boundaries():
    packet = load_ocr_layout_image_binary_fixture_provenance(BINARY_ROOT)

    assert packet["packet"] == "committed_ocr_layout_image_binary_fixture_provenance_v0"
    assert packet["claim_boundary"] == (
        "committed_ocr_layout_image_binary_fixture_provenance_only_not_robust_pdf_extraction"
    )
    assert packet["binary_pdf_fixtures_included"] is True
    assert packet["robust_pdf_extraction_claimed"] is False
    assert {item["fixture_id"] for item in packet["fixtures"]} == set(
        REQUIRED_OCR_LAYOUT_IMAGE_BINARY_FIXTURE_IDS
    )

    for item in packet["fixtures"]:
        file_path = BINARY_ROOT / item["path"]
        assert file_path.is_file()
        content = file_path.read_bytes()
        assert hashlib.sha256(content).hexdigest() == item["sha256"]
        assert len(content) == item["size_bytes"]
        assert item["source_kind"] == "synthetic_generated"
        assert item["redistribution_allowed"] is True
        assert item["robust_pdf_extraction_claimed"] is False

    by_id = {item["fixture_id"]: item for item in packet["fixtures"]}
    assert by_id["scanned_image_pdf"]["expected_failure_case"] == (
        "pdf_no_extractable_text"
    )
    assert by_id["image_heavy_pdf"]["expected_min_image_blocks"] == 1
    assert by_id["multi_column_layout_pdf"]["expected_min_text_blocks"] == 2
    assert by_id["no_extractable_text_pdf"]["expected_failure_case"] == (
        "pdf_no_extractable_text"
    )
    assert "not robust PDF extraction evidence" in packet["boundary_notes"]
    assert "not OCR evidence" in packet["boundary_notes"]
    assert "not image/chart interpretation evidence" in packet["boundary_notes"]
    assert "not layout fidelity evidence" in packet["boundary_notes"]


def test_committed_ocr_layout_image_binary_fixture_summary_runs_parser_without_overclaiming():
    packet = load_ocr_layout_image_binary_fixture_provenance(BINARY_ROOT)
    summary = build_committed_ocr_layout_image_binary_fixture_provenance_summary(
        BINARY_ROOT,
        packet,
    )

    assert summary["phase_marker"] == (
        "committed_ocr_layout_image_binary_fixture_provenance_v0"
    )
    assert summary["committed_fixture_count"] == 4
    assert summary["parser_observed_fixture_count"] == 4
    assert summary["quality_gate_status"] == "blocked"
    assert summary["robust_pdf_extraction_claimed"] is False
    assert summary["can_claim_robust_pdf_extraction"] is False

    scanned = summary["per_fixture"]["scanned_image_pdf"]
    assert scanned["parser"] == "pdf-pymupdf"
    assert scanned["failure_case_candidate"] == "pdf_no_extractable_text"
    assert scanned["ocr_performed"] is False
    assert scanned["adapter_boundary"] == "ocr_adapter_not_implemented"

    image_heavy = summary["per_fixture"]["image_heavy_pdf"]
    assert image_heavy["image_block_count"] >= 1
    assert image_heavy["image_chart_interpretation_claimed"] is False
    assert image_heavy["expected_spans_found"] is True

    layout = summary["per_fixture"]["multi_column_layout_pdf"]
    assert layout["text_block_count"] >= 2
    assert layout["layout_fidelity_claimed"] is False
    assert layout["expected_spans_found"] is True

    empty = summary["per_fixture"]["no_extractable_text_pdf"]
    assert empty["failure_case_candidate"] == "pdf_no_extractable_text"
    assert empty["expected_failure_case_observed"] is True

    assert "not robust PDF extraction evidence" in summary["boundary_notes"]
    assert "not OCR evidence" in summary["boundary_notes"]


def test_committed_ocr_layout_image_binary_fixture_report_matches_committed_artifact():
    packet = load_ocr_layout_image_binary_fixture_provenance(BINARY_ROOT)
    summary = build_committed_ocr_layout_image_binary_fixture_provenance_summary(
        BINARY_ROOT,
        packet,
    )
    report = build_committed_ocr_layout_image_binary_fixture_provenance_report(summary)

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Committed OCR Layout Image Binary Fixture Provenance" in report
    assert "committed_ocr_layout_image_binary_fixture_provenance_v0" in report
    assert "| committed_fixture_count | 4 |" in report
    assert "| parser_observed_fixture_count | 4 |" in report
    assert "| can_claim_robust_pdf_extraction | false |" in report
    assert "scanned_image_pdf" in report
    assert "image_heavy_pdf" in report
    assert "multi_column_layout_pdf" in report
    assert "no_extractable_text_pdf" in report
    assert "not robust PDF extraction evidence" in report


def test_committed_ocr_layout_image_binary_fixture_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.committed_ocr_layout_image_binary_fixture_provenance_command",
            "--fixture-root",
            str(BINARY_ROOT),
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
    assert (
        "committed_ocr_layout_image_binary_fixture_provenance_report_current"
        in result.stdout
    )
    assert "byte-for-byte regeneration" in result.stdout
    assert "not robust PDF extraction evidence" in result.stdout


def test_committed_ocr_layout_image_binary_fixture_docs_and_ci_are_wired():
    review_path = (
        REPO_ROOT
        / "docs/review/committed-ocr-layout-image-binary-fixture-provenance.md"
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

    assert "Committed OCR Layout Image Binary Fixture Provenance" in review
    assert "committed_ocr_layout_image_binary_fixture_provenance_v0" in review
    assert "committed_fixture_count -> 4" in review
    assert "parser_observed_fixture_count -> 4" in review
    assert "not robust PDF extraction evidence" in review
    assert (
        "Committed OCR/layout/image binary fixture provenance v0: implemented"
        in readme
    )
    assert (
        "Phase 876 - Committed OCR Layout Image Binary Fixture Provenance v0"
        in goal
    )
    assert (
        "Phase 876 adds committed OCR/layout/image binary fixture provenance v0"
        in runbook
    )
    assert (
        "docs/review/committed-ocr-layout-image-binary-fixture-provenance.md"
        in portfolio
    )
    assert (
        "Latest committed OCR/layout/image binary fixture provenance"
        in application_ready
    )
    assert (
        "Check committed OCR layout image binary fixture provenance report staleness"
        in ci
    )
    assert (
        "digital_pdf_text_diagnostics_plus_multi_fixture_gap_matrix_plus_missing_runtime_observation_pack_plus_ocr_layout_image_adapter_runtime_pack_plus_committed_ocr_layout_image_binary_fixture_provenance"
        in proof_gap_registry
    )
    assert "opt_in_ocr_adapter_runtime_smoke_v0" in proof_gap_registry
