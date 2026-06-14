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
    remote_verification_path = (
        REPO_ROOT
        / "docs/review/multi-real-world-pdf-parse-observation-remote-verification.md"
    )
    assert review_path.is_file()
    assert remote_verification_path.is_file()

    review = review_path.read_text(encoding="utf-8")
    remote_verification = remote_verification_path.read_text(encoding="utf-8")
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
    assert "verified_head_sha -> a37fe32f0f46c5d04008ea425a053966f063950c" in remote_verification
    assert "CI run `27496475781`: success" in remote_verification
    assert "CI job_id -> 81271370552" in remote_verification
    assert "External Feedback Screen run `27496475772`: success" in remote_verification
    assert "External Feedback Screen job_id -> 81271370589" in remote_verification
    assert "remote workflow verification only" in remote_verification
    assert "not robust PDF extraction evidence" in remote_verification
    assert "Multi real-world PDF parse observation matrix v0: implemented" in readme
    assert "Multi real-world PDF parse observation matrix remote verification v0: implemented" in readme
    assert "Phase 891 - Multi Real-world PDF Parse Observation Matrix v0" in goal
    assert "Phase 892 - Multi Real-world PDF Parse Observation Matrix Remote Verification v0" in goal
    assert "Phase 891 adds multi real-world PDF parse observation matrix v0" in runbook
    assert "Phase 892 adds multi real-world PDF parse observation matrix remote verification v0" in runbook
    assert "docs/review/multi-real-world-pdf-parse-observation.md" in portfolio
    assert (
        "docs/review/multi-real-world-pdf-parse-observation-remote-verification.md"
        in portfolio
    )
    assert "Multi Real-world PDF Parse Observation Matrix" in application_ready
    assert "Multi Real-world PDF Parse Observation Matrix Remote Verification" in application_ready
    assert "Check multi real-world PDF parse observation report staleness" in ci
    assert "multi_real_world_pdf_parse_observation_matrix_v0" in proof_gap_registry
    assert "multi_real_world_pdf_parse_observation_matrix_remote_verification_v0" in proof_gap_registry


def test_multi_real_world_pdf_parse_observation_matrix_reviewer_surfaces_route_to_latest_proof():
    route_refresh_path = (
        REPO_ROOT
        / "docs/review/external-reviewer-surfaces-multi-real-world-pdf-parse-observation-matrix-route-refresh.md"
    )
    assert route_refresh_path.is_file()

    expected_markers = [
        "docs/review/multi-real-world-pdf-parse-observation.md",
        "docs/review/multi-real-world-pdf-parse-observation-remote-verification.md",
        "observed_fixture_count -> 3",
        "a37fe32f0f46c5d04008ea425a053966f063950c",
        "27496475781",
        "27496475772",
        "not robust PDF extraction evidence",
        "not hosted deployment evidence",
        "not external reviewer feedback",
        "not product-complete",
    ]
    surfaces = [
        "README.md",
        "docs/review/external-reader-proof-path.md",
        "docs/review/external-reviewer-shortlist.md",
        "docs/review/external-reviewer-link-map.md",
        "CONTRIBUTING.md",
        ".github/ISSUE_TEMPLATE/external-review-feedback.md",
    ]
    for path in surfaces:
        content = (REPO_ROOT / path).read_text(encoding="utf-8")
        for marker in expected_markers:
            assert marker in content, f"{marker!r} missing from {path}"

    route_refresh = route_refresh_path.read_text(encoding="utf-8")
    assert (
        "External Reviewer Surfaces Multi Real-world PDF Parse Observation Matrix Route Refresh"
        in route_refresh
    )
    assert "route hygiene only" in route_refresh
    assert "not a live issue body edit" in route_refresh
    assert "Phase 893" in (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")


def test_multi_real_world_pdf_parse_observation_matrix_route_refresh_remote_verification_is_recorded():
    remote_path = (
        REPO_ROOT
        / "docs/review/external-reviewer-surfaces-multi-real-world-pdf-parse-observation-matrix-route-refresh-remote-verification.md"
    )
    assert remote_path.is_file()

    remote = remote_path.read_text(encoding="utf-8")
    expected_markers = [
        "External Reviewer Surfaces Multi Real-world PDF Parse Observation Matrix Route Refresh Remote Verification",
        "9952bbb9f14c60a7c5510fb50af49b03f485ca80",
        "CI run `27496923203`: success",
        "CI job_id -> 81272609344",
        "External Feedback Screen run `27496923199`: success",
        "External Feedback Screen job_id -> 81272609334",
        "remote workflow verification only",
        "not the route refresh itself",
        "not robust PDF extraction evidence",
        "not hosted deployment evidence",
        "not external reviewer feedback",
        "not product-complete",
    ]
    for marker in expected_markers:
        assert marker in remote

    for path in [
        "README.md",
        "docs/GOAL.md",
        "docs/runbook.md",
        "docs/application/portfolio-index.md",
        "docs/review/application-ready-review.md",
    ]:
        content = (REPO_ROOT / path).read_text(encoding="utf-8")
        assert (
            "docs/review/external-reviewer-surfaces-multi-real-world-pdf-parse-observation-matrix-route-refresh-remote-verification.md"
            in content
        ), path


def test_external_review_issue_body_multi_real_world_pdf_matrix_route_refresh_is_recorded():
    issue_refresh_path = (
        REPO_ROOT
        / "docs/review/external-review-issue-body-multi-real-world-pdf-parse-observation-matrix-route-refresh.md"
    )
    assert issue_refresh_path.is_file()

    content = issue_refresh_path.read_text(encoding="utf-8")
    expected_markers = [
        "External Review Issue Body Multi Real-world PDF Parse Observation Matrix Route Refresh",
        "external review issue body multi real-world PDF parse observation matrix route refresh v0",
        "https://github.com/svy04/noiseproof-agent/issues/1",
        "starts_with_request: true",
        "first_codepoint: 35",
        "has_leading_bom: false",
        "has_multi_real_world_pdf_matrix_latest_proof: true",
        "has_multi_real_world_pdf_matrix_remote_verification: true",
        "has_multi_real_world_pdf_matrix_route_refresh: true",
        "has_multi_real_world_pdf_matrix_route_refresh_remote_verification: true",
        "old_local_otel_latest_label_present: false",
        "docs/review/multi-real-world-pdf-parse-observation.md",
        "docs/review/multi-real-world-pdf-parse-observation-remote-verification.md",
        "docs/review/external-reviewer-surfaces-multi-real-world-pdf-parse-observation-matrix-route-refresh.md",
        "docs/review/external-reviewer-surfaces-multi-real-world-pdf-parse-observation-matrix-route-refresh-remote-verification.md",
        "observed_fixture_count -> 3",
        "9952bbb9f14c60a7c5510fb50af49b03f485ca80",
        "owner-authored issue body routing only",
        "not external reviewer feedback",
        "not robust PDF extraction evidence",
        "not hosted deployment evidence",
        "not product-complete",
    ]
    for marker in expected_markers:
        assert marker in content

    for path in [
        "README.md",
        "docs/GOAL.md",
        "docs/runbook.md",
        "docs/application/portfolio-index.md",
        "docs/review/application-ready-review.md",
    ]:
        surface = (REPO_ROOT / path).read_text(encoding="utf-8")
        assert (
            "docs/review/external-review-issue-body-multi-real-world-pdf-parse-observation-matrix-route-refresh.md"
            in surface
        ), path


def test_external_feedback_current_state_multi_real_world_pdf_matrix_issue_verification_keeps_gate_pending():
    verification_path = (
        REPO_ROOT
        / "docs/review/external-feedback-current-state-multi-real-world-pdf-parse-observation-matrix-issue-verification.md"
    )
    assert verification_path.is_file()

    content = verification_path.read_text(encoding="utf-8")
    expected_markers = [
        "External Feedback Current-state Multi Real-world PDF Parse Observation Matrix Issue Verification",
        "external feedback current-state multi real-world PDF parse observation matrix issue verification v0",
        "https://github.com/svy04/noiseproof-agent/issues/1",
        "comment_count: 1",
        "screened_comment_count: 1",
        "owner_comment_count: 1",
        "candidate_count: 0",
        "draft_count: 0",
        "reason: self_authored_comment_only",
        "status: pending",
        "does_not_close_gate: true",
        "docs/review/multi-real-world-pdf-parse-observation.md",
        "docs/review/external-review-issue-body-multi-real-world-pdf-parse-observation-matrix-route-refresh.md",
        "owner-authored comment remains non-qualifying",
        "current-state issue screen only",
        "not external reviewer feedback",
        "not robust PDF extraction evidence",
        "not hosted deployment evidence",
        "not product-complete",
    ]
    for marker in expected_markers:
        assert marker in content

    for path in [
        "README.md",
        "docs/GOAL.md",
        "docs/runbook.md",
        "docs/application/portfolio-index.md",
        "docs/review/application-ready-review.md",
    ]:
        surface = (REPO_ROOT / path).read_text(encoding="utf-8")
        assert (
            "docs/review/external-feedback-current-state-multi-real-world-pdf-parse-observation-matrix-issue-verification.md"
            in surface
        ), path


def test_external_feedback_current_state_multi_real_world_pdf_matrix_issue_verification_remote_verification_is_recorded():
    remote_path = (
        REPO_ROOT
        / "docs/review/external-feedback-current-state-multi-real-world-pdf-parse-observation-matrix-issue-verification-remote-verification.md"
    )
    assert remote_path.is_file()

    content = remote_path.read_text(encoding="utf-8")
    expected_markers = [
        "External Feedback Current-state Multi Real-world PDF Parse Observation Matrix Issue Verification Remote Verification",
        "external feedback current-state multi real-world PDF parse observation matrix issue verification remote verification v0",
        "084e3fe9fd3bf65bef873a28d7cbf8a06f3405ea",
        "CI run `27497284929`: success",
        "CI job_id -> 81273628024",
        "External Feedback Screen run `27497284920`: success",
        "External Feedback Screen job_id -> 81273628056",
        "Check multi real-world PDF parse observation report staleness -> success",
        "Run API smoke tests -> success",
        "Screen issue comments -> success",
        "docs/review/external-feedback-current-state-multi-real-world-pdf-parse-observation-matrix-issue-verification.md",
        "remote workflow verification only",
        "not the current-state issue screen itself",
        "not external reviewer feedback",
        "not robust PDF extraction evidence",
        "not hosted deployment evidence",
        "not product-complete",
    ]
    for marker in expected_markers:
        assert marker in content

    for path in [
        "README.md",
        "docs/GOAL.md",
        "docs/runbook.md",
        "docs/application/portfolio-index.md",
        "docs/review/application-ready-review.md",
    ]:
        surface = (REPO_ROOT / path).read_text(encoding="utf-8")
        assert (
            "docs/review/external-feedback-current-state-multi-real-world-pdf-parse-observation-matrix-issue-verification-remote-verification.md"
            in surface
        ), path
