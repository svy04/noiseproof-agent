import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
MANIFEST_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/owner-approved-real-world-download-hash.json"
)
REPORT_PATH = (
    REPO_ROOT
    / "docs/evaluation/owner-approved-real-world-pdf-download-hash-report.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.owner_approved_real_world_pdf_download_hash import (
    CLAIM_BOUNDARY,
    NEXT_GATE,
    PHASE_MARKER,
    build_owner_approved_real_world_pdf_download_hash_report,
    build_owner_approved_real_world_pdf_download_hash_summary,
    load_owner_approved_real_world_pdf_download_hash_manifest,
)


def test_owner_approved_real_world_pdf_download_hash_manifest_records_success_and_blocked_sources():
    manifest = load_owner_approved_real_world_pdf_download_hash_manifest(MANIFEST_PATH)

    assert manifest["phase_marker"] == PHASE_MARKER
    assert manifest["claim_boundary"] == CLAIM_BOUNDARY
    assert manifest["owner_approved"] is True
    assert manifest["binary_files_committed"] is False
    assert manifest["download_cache_committed"] is False
    assert manifest["robust_pdf_extraction_claimed"] is False
    assert manifest["can_claim_robust_pdf_extraction"] is False

    downloaded = manifest["downloaded_fixtures"]
    blocked = manifest["blocked_fixtures"]
    assert len(downloaded) == 1
    assert len(blocked) == 4

    for fixture in downloaded:
        assert fixture["publisher"] == "U.S. Bureau of Economic Analysis"
        assert fixture["source_url"].startswith("https://www.bea.gov/")
        assert fixture["license_source_url"] == "https://www.bea.gov/help/faq/147"
        assert fixture["download_status"] == "downloaded_and_hashed"
        assert fixture["http_status"] == 200
        assert fixture["content_type"] == "application/pdf"
        assert fixture["byte_size"] > 100_000
        assert len(fixture["sha256"]) == 64
        assert fixture["pdf_magic_header"] is True
        assert fixture["binary_committed"] is False
        assert fixture["local_pdf_path"] is None

    for fixture in blocked:
        assert fixture["publisher"].startswith("U.S. Bureau of Labor Statistics")
        assert fixture["download_status"] == "blocked_403_in_owner_runtime"
        assert fixture["http_status"] == 403
        assert fixture["sha256"] is None
        assert fixture["binary_committed"] is False


def test_owner_approved_real_world_pdf_download_hash_summary_keeps_extraction_claim_blocked():
    manifest = load_owner_approved_real_world_pdf_download_hash_manifest(MANIFEST_PATH)
    summary = build_owner_approved_real_world_pdf_download_hash_summary(manifest)

    assert summary["phase_marker"] == PHASE_MARKER
    assert summary["downloaded_fixture_count"] == 1
    assert summary["blocked_fixture_count"] == 4
    assert summary["binary_files_committed"] is False
    assert summary["download_cache_committed"] is False
    assert summary["can_claim_real_world_pdf_download_hash"] is True
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["recommended_next_gate"] == NEXT_GATE
    assert summary["downloaded_fixture_ids"] == [
        "bea_nipa_glossary_2019",
    ]


def test_owner_approved_real_world_pdf_download_hash_report_is_current():
    manifest = load_owner_approved_real_world_pdf_download_hash_manifest(MANIFEST_PATH)
    summary = build_owner_approved_real_world_pdf_download_hash_summary(manifest)
    report = build_owner_approved_real_world_pdf_download_hash_report(summary)

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Owner-approved Real-world PDF Download and Hash" in report
    assert "owner_approved_real_world_pdf_download_and_hash_v0" in report
    assert "| downloaded_fixture_count | 1 |" in report
    assert "| blocked_fixture_count | 4 |" in report
    assert "| binary_files_committed | false |" in report
    assert "| can_claim_robust_pdf_extraction | false |" in report
    assert "bea_nipa_glossary_2019" in report
    assert "blocked_403_in_owner_runtime" in report
    assert "not robust PDF extraction evidence" in report


def test_owner_approved_real_world_pdf_download_hash_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.owner_approved_real_world_pdf_download_hash_command",
            "--manifest",
            str(MANIFEST_PATH),
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
    assert "owner_approved_real_world_pdf_download_hash_report_current" in result.stdout
    assert "download/hash metadata only" in result.stdout
    assert "not robust PDF extraction evidence" in result.stdout


def test_owner_approved_real_world_pdf_download_hash_docs_and_ci_are_wired():
    review_path = REPO_ROOT / "docs/review/owner-approved-real-world-pdf-download-hash.md"
    remote_verification_path = (
        REPO_ROOT
        / "docs/review/owner-approved-real-world-pdf-download-hash-remote-verification.md"
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

    assert "Owner-approved Real-world PDF Download and Hash" in review
    assert "downloaded_fixture_count -> 1" in review
    assert "blocked_fixture_count -> 4" in review
    assert "not robust PDF extraction evidence" in review
    assert "verified_head_sha -> 6d638fca11b02e03581a8296bb95bc9a5da3894c" in remote_verification
    assert "CI run `27495693041`: success" in remote_verification
    assert "CI job_id -> 81269226120" in remote_verification
    assert "External Feedback Screen run `27495693049`: success" in remote_verification
    assert "remote workflow verification only" in remote_verification
    assert "not robust PDF extraction evidence" in remote_verification
    assert "Owner-approved real-world PDF download/hash v0: implemented" in readme
    assert "Owner-approved real-world PDF download/hash remote verification v0: implemented" in readme
    assert "Phase 887 - Owner-approved Real-world PDF Download and Hash v0" in goal
    assert (
        "Phase 888 - Owner-approved Real-world PDF Download and Hash Remote Verification v0"
        in goal
    )
    assert "Phase 887 adds owner-approved real-world PDF download/hash v0" in runbook
    assert (
        "Phase 888 adds owner-approved real-world PDF download/hash remote verification v0"
        in runbook
    )
    assert "docs/review/owner-approved-real-world-pdf-download-hash.md" in portfolio
    assert (
        "docs/review/owner-approved-real-world-pdf-download-hash-remote-verification.md"
        in portfolio
    )
    assert "Owner-approved Real-world PDF Download and Hash" in application_ready
    assert (
        "Owner-approved Real-world PDF Download and Hash Remote Verification"
        in application_ready
    )
    assert "Check owner-approved real-world PDF download/hash report staleness" in ci
    assert "owner_approved_real_world_pdf_download_and_hash_v0" in proof_gap_registry
    assert "real_world_pdf_parse_observation_without_robust_claim_v0" in proof_gap_registry
