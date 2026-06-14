import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
PACK_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/licensed-real-world-candidates.json"
)
REPORT_PATH = (
    REPO_ROOT
    / "docs/evaluation/licensed-real-world-pdf-fixture-pack-report.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.licensed_real_world_fixture_pack import (
    CLAIM_BOUNDARY,
    NEXT_GATE,
    PHASE_MARKER,
    build_licensed_real_world_fixture_pack_report,
    build_licensed_real_world_fixture_pack_summary,
    load_licensed_real_world_fixture_pack,
)


def test_licensed_real_world_fixture_pack_validates_candidate_boundaries():
    pack = load_licensed_real_world_fixture_pack(PACK_PATH)

    assert pack["phase_marker"] == PHASE_MARKER
    assert pack["claim_boundary"] == CLAIM_BOUNDARY
    assert pack["robust_pdf_extraction_claimed"] is False
    assert pack["binary_files_committed"] is False
    assert pack["download_status"] == "candidate_metadata_only"
    assert len(pack["candidates"]) == 4

    role_ids = {candidate["fixture_role"] for candidate in pack["candidates"]}
    assert role_ids == {
        "digital_text_tables",
        "long_report_tables",
        "multi_column_article",
        "article_with_figures",
    }

    for candidate in pack["candidates"]:
        assert candidate["source_url"].startswith("https://")
        assert candidate["license_source_url"].startswith("https://")
        assert candidate["redistribution_status"] in {
            "public_domain_with_citation_requested",
            "public_domain_unless_stated_otherwise",
        }
        assert candidate["download_status"] == "not_downloaded"
        assert candidate["local_pdf_path"] is None
        assert candidate["sha256"] is None
        assert candidate["expected_signals"]
        assert candidate["known_risks"]


def test_licensed_real_world_fixture_pack_summary_keeps_download_gate_closed():
    pack = load_licensed_real_world_fixture_pack(PACK_PATH)
    summary = build_licensed_real_world_fixture_pack_summary(pack)

    assert summary["phase_marker"] == PHASE_MARKER
    assert summary["candidate_count"] == 4
    assert summary["downloaded_candidate_count"] == 0
    assert summary["binary_files_committed"] is False
    assert summary["robust_pdf_extraction_claimed"] is False
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["license_review_status"] == "candidate_metadata_only"
    assert summary["recommended_next_gate"] == NEXT_GATE
    assert summary["candidate_ids"] == [
        "bls_employment_situation_2025_01",
        "bls_women_labor_force_databook_2016",
        "bls_monthly_labor_review_2011_06",
        "bls_beyond_numbers_not_in_labor_force_2015",
    ]


def test_licensed_real_world_fixture_pack_report_is_current():
    pack = load_licensed_real_world_fixture_pack(PACK_PATH)
    summary = build_licensed_real_world_fixture_pack_summary(pack)
    report = build_licensed_real_world_fixture_pack_report(summary)

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Licensed Real-world PDF Fixture Pack" in report
    assert "licensed_real_world_pdf_fixture_pack_v0" in report
    assert "| candidate_count | 4 |" in report
    assert "| downloaded_candidate_count | 0 |" in report
    assert "| binary_files_committed | false |" in report
    assert "| can_claim_robust_pdf_extraction | false |" in report
    assert "owner_approved_real_world_pdf_download_and_hash_v0" in report
    assert "not robust PDF extraction evidence" in report


def test_licensed_real_world_fixture_pack_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.licensed_real_world_fixture_pack_command",
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
    assert "licensed_real_world_pdf_fixture_pack_report_current" in result.stdout
    assert "candidate metadata only" in result.stdout
    assert "not robust PDF extraction evidence" in result.stdout


def test_licensed_real_world_fixture_pack_docs_ci_and_proof_gap_are_wired():
    review_path = REPO_ROOT / "docs/review/licensed-real-world-pdf-fixture-pack.md"
    remote_verification_path = (
        REPO_ROOT
        / "docs/review/licensed-real-world-pdf-fixture-pack-remote-verification.md"
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

    assert "Licensed Real-world PDF Fixture Pack" in review
    assert "candidate_count -> 4" in review
    assert "downloaded_candidate_count -> 0" in review
    assert "not robust PDF extraction evidence" in review
    assert "verified_head_sha -> fbb871bb02d5b1a2250e12bc769996aecdba06b4" in remote_verification
    assert "CI run `27494850142`: success" in remote_verification
    assert "CI job_id -> 81266891718" in remote_verification
    assert "External Feedback Screen run `27494850152`: success" in remote_verification
    assert "External Feedback Screen job_id -> 81266891669" in remote_verification
    assert "Check licensed real-world PDF fixture pack report staleness -> success" in remote_verification
    assert "remote workflow verification only" in remote_verification
    assert "not robust PDF extraction evidence" in remote_verification
    assert "Licensed real-world PDF fixture pack v0: implemented" in readme
    assert "Licensed real-world PDF fixture pack remote verification v0: implemented" in readme
    assert "Phase 884 - Licensed Real-world PDF Fixture Pack v0" in goal
    assert "Phase 885 - Licensed Real-world PDF Fixture Pack Remote Verification v0" in goal
    assert "Phase 884 adds licensed real-world PDF fixture pack v0" in runbook
    assert "Phase 885 adds licensed real-world PDF fixture pack remote verification v0" in runbook
    assert "docs/review/licensed-real-world-pdf-fixture-pack.md" in portfolio
    assert "docs/review/licensed-real-world-pdf-fixture-pack-remote-verification.md" in portfolio
    assert "Licensed Real-world PDF Fixture Pack" in application_ready
    assert "Licensed Real-world PDF Fixture Pack Remote Verification" in application_ready
    assert "Check licensed real-world PDF fixture pack report staleness" in ci
    assert "licensed_real_world_pdf_fixture_pack_v0" in proof_gap_registry
    assert "owner_approved_real_world_pdf_download_and_hash_v0" in proof_gap_registry
