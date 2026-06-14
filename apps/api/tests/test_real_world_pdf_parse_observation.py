import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
OBSERVATION_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/real-world-pdf-parse-observation.json"
)
REPORT_PATH = (
    REPO_ROOT
    / "docs/evaluation/real-world-pdf-parse-observation-report.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.real_world_pdf_parse_observation import (
    CLAIM_BOUNDARY,
    NEXT_GATE,
    PHASE_MARKER,
    build_real_world_pdf_parse_observation_report,
    build_real_world_pdf_parse_observation_summary,
    load_real_world_pdf_parse_observation,
)


def test_real_world_pdf_parse_observation_records_single_pdf_without_robust_claim():
    observation = load_real_world_pdf_parse_observation(OBSERVATION_PATH)

    assert observation["phase_marker"] == PHASE_MARKER
    assert observation["claim_boundary"] == CLAIM_BOUNDARY
    assert observation["source_download_hash_gate"] == (
        "owner_approved_real_world_pdf_download_and_hash_v0"
    )
    assert observation["fixture_id"] == "bea_nipa_glossary_2019"
    assert observation["parser"] == "pdf-pymupdf"
    assert observation["parse_status"] == "parsed_digital_text"
    assert observation["page_count"] == 35
    assert observation["extracted_page_count"] == 35
    assert observation["empty_page_count"] == 0
    assert observation["text_char_count"] == 92219
    assert observation["table_candidate_count"] == 35
    assert observation["table_extraction_performed"] is False
    assert observation["ocr_calls_attempted"] is False
    assert observation["robust_pdf_extraction_claimed"] is False
    assert observation["can_claim_robust_pdf_extraction"] is False
    assert observation["failure_case_candidate"] is None
    assert observation["binary_files_committed"] is False
    assert observation["download_cache_committed"] is False
    assert "GLOSSARY: NATIONAL INCOME AND PRODUCT" in observation["text_sample"]


def test_real_world_pdf_parse_observation_summary_keeps_next_gate_bounded():
    observation = load_real_world_pdf_parse_observation(OBSERVATION_PATH)
    summary = build_real_world_pdf_parse_observation_summary(observation)

    assert summary["phase_marker"] == PHASE_MARKER
    assert summary["observed_fixture_count"] == 1
    assert summary["parsed_fixture_count"] == 1
    assert summary["table_candidate_count"] == 35
    assert summary["can_claim_real_world_pdf_parse_observation"] is True
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["recommended_next_gate"] == NEXT_GATE


def test_real_world_pdf_parse_observation_report_is_current():
    observation = load_real_world_pdf_parse_observation(OBSERVATION_PATH)
    summary = build_real_world_pdf_parse_observation_summary(observation)
    report = build_real_world_pdf_parse_observation_report(summary)

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Real-world PDF Parse Observation" in report
    assert "real_world_pdf_parse_observation_without_robust_claim_v0" in report
    assert "| observed_fixture_count | 1 |" in report
    assert "| text_char_count | 92219 |" in report
    assert "| table_extraction_performed | false |" in report
    assert "| can_claim_robust_pdf_extraction | false |" in report
    assert "not robust PDF extraction evidence" in report


def test_real_world_pdf_parse_observation_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.real_world_pdf_parse_observation_command",
            "--observation",
            str(OBSERVATION_PATH),
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
    assert "real_world_pdf_parse_observation_report_current" in result.stdout
    assert "single real-world PDF parse observation only" in result.stdout
    assert "not robust PDF extraction evidence" in result.stdout


def test_real_world_pdf_parse_observation_docs_and_ci_are_wired():
    review_path = REPO_ROOT / "docs/review/real-world-pdf-parse-observation.md"
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

    assert "Real-world PDF Parse Observation" in review
    assert "text_char_count -> 92219" in review
    assert "table_candidate_count -> 35" in review
    assert "not robust PDF extraction evidence" in review
    assert "Real-world PDF parse observation v0: implemented" in readme
    assert "Phase 889 - Real-world PDF Parse Observation v0" in goal
    assert "Phase 889 adds real-world PDF parse observation v0" in runbook
    assert "docs/review/real-world-pdf-parse-observation.md" in portfolio
    assert "Real-world PDF Parse Observation" in application_ready
    assert "Check real-world PDF parse observation report staleness" in ci
    assert "real_world_pdf_parse_observation_without_robust_claim_v0" in proof_gap_registry
    assert "multi_real_world_pdf_parse_observation_matrix_v0" in proof_gap_registry
