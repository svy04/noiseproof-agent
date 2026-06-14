import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
MATRIX_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/multi-real-world-pdf-parse-observations.json"
)
REPORT_PATH = (
    REPO_ROOT
    / "docs/evaluation/multi-real-world-pdf-parse-observation-report.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.multi_real_world_pdf_parse_observation import (
    CLAIM_BOUNDARY,
    NEXT_GATE,
    PHASE_MARKER,
    build_multi_real_world_pdf_parse_observation_report,
    build_multi_real_world_pdf_parse_observation_summary,
    load_multi_real_world_pdf_parse_observation_matrix,
)


EXPECTED_FIXTURE_IDS = {
    "bea_nipa_glossary_2019",
    "bea_nipa_chapter_04_2024",
    "bea_open_source_software_innovation_wp_2022_10",
}


def test_multi_real_world_pdf_parse_observation_matrix_records_multiple_pdfs_without_robust_claim():
    matrix = load_multi_real_world_pdf_parse_observation_matrix(MATRIX_PATH)

    assert matrix["phase_marker"] == PHASE_MARKER
    assert matrix["claim_boundary"] == CLAIM_BOUNDARY
    assert matrix["fixture_count"] == 3
    assert matrix["observed_fixture_count"] == 3
    assert matrix["binary_files_committed"] is False
    assert matrix["download_cache_committed"] is False
    assert matrix["raw_extracted_text_committed"] is False
    assert matrix["table_extraction_performed"] is False
    assert matrix["ocr_calls_attempted"] is False
    assert matrix["robust_pdf_extraction_claimed"] is False
    assert matrix["can_claim_robust_pdf_extraction"] is False
    assert matrix["recommended_next_gate"] == NEXT_GATE

    fixture_ids = {item["fixture_id"] for item in matrix["observations"]}
    assert fixture_ids == EXPECTED_FIXTURE_IDS

    for item in matrix["observations"]:
        assert item["publisher"] == "U.S. Bureau of Economic Analysis"
        assert item["license_source_url"] == "https://www.bea.gov/help/faq/147"
        assert item["source_url"].startswith("https://www.bea.gov/")
        assert item["parse_status"] == "parsed_digital_text"
        assert item["parser"] == "pdf-pymupdf"
        assert item["byte_size"] > 0
        assert len(item["source_sha256"]) == 64
        assert item["page_count"] > 0
        assert item["extracted_page_count"] > 0
        assert item["text_char_count"] > 0
        assert item["text_block_count"] > 0
        assert item["table_extraction_performed"] is False
        assert item["ocr_calls_attempted"] is False
        assert item["binary_committed"] is False
        assert item["local_pdf_path"] is None
        assert item["failure_case_candidate"] is None
        assert len(item["text_sample"]) <= 240


def test_multi_real_world_pdf_parse_observation_summary_keeps_claim_gate_blocked():
    matrix = load_multi_real_world_pdf_parse_observation_matrix(MATRIX_PATH)
    summary = build_multi_real_world_pdf_parse_observation_summary(matrix)

    assert summary["phase_marker"] == PHASE_MARKER
    assert summary["observed_fixture_count"] == 3
    assert summary["parsed_fixture_count"] == 3
    assert summary["fixture_ids"] == sorted(EXPECTED_FIXTURE_IDS)
    assert summary["total_page_count"] >= 3
    assert summary["total_text_char_count"] > 0
    assert summary["can_claim_multi_real_world_pdf_parse_observation"] is True
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["recommended_next_gate"] == NEXT_GATE


def test_multi_real_world_pdf_parse_observation_report_is_current():
    matrix = load_multi_real_world_pdf_parse_observation_matrix(MATRIX_PATH)
    summary = build_multi_real_world_pdf_parse_observation_summary(matrix)
    report = build_multi_real_world_pdf_parse_observation_report(summary)

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Multi Real-world PDF Parse Observation Matrix" in report
    assert "multi_real_world_pdf_parse_observation_matrix_v0" in report
    assert "| observed_fixture_count | 3 |" in report
    assert "| can_claim_robust_pdf_extraction | false |" in report
    assert "not robust PDF extraction evidence" in report
    for fixture_id in EXPECTED_FIXTURE_IDS:
        assert fixture_id in report


def test_multi_real_world_pdf_parse_observation_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.multi_real_world_pdf_parse_observation_command",
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
    assert "multi_real_world_pdf_parse_observation_report_current" in result.stdout
    assert "multiple real-world PDF parse observations" in result.stdout
    assert "not robust PDF extraction evidence" in result.stdout


def test_multi_real_world_pdf_parse_observation_docs_and_ci_are_wired():
    review_path = (
        REPO_ROOT / "docs/review/multi-real-world-pdf-parse-observation.md"
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

    assert "Multi Real-world PDF Parse Observation Matrix" in review
    assert "observed_fixture_count -> 3" in review
    assert "not robust PDF extraction evidence" in review
    assert "Multi real-world PDF parse observation matrix v0: implemented" in readme
    assert "Phase 891 - Multi Real-world PDF Parse Observation Matrix v0" in goal
    assert "Phase 891 adds multi real-world PDF parse observation matrix v0" in runbook
    assert "docs/review/multi-real-world-pdf-parse-observation.md" in portfolio
    assert "Multi Real-world PDF Parse Observation Matrix" in application_ready
    assert "Check multi real-world PDF parse observation report staleness" in ci
    assert "multi_real_world_pdf_parse_observation_matrix_v0" in proof_gap_registry
    assert "multi_real_world_pdf_parse_observation_matrix_remote_verification_v0" in proof_gap_registry
