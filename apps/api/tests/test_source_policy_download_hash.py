import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
MANIFEST_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/source-policy-download-hash-observations.json"
)
REPORT_PATH = (
    REPO_ROOT / "docs/evaluation/source-policy-download-hash-report.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.source_policy_download_hash import (  # noqa: E402
    NEXT_GATE,
    PHASE_MARKER,
    build_source_policy_download_hash_report,
    build_source_policy_download_hash_summary,
    load_source_policy_download_hash_manifest,
)


def test_source_policy_download_hash_records_success_blocked_and_external_routes():
    manifest = load_source_policy_download_hash_manifest(MANIFEST_PATH)
    summary = build_source_policy_download_hash_summary(manifest)

    assert summary["phase_marker"] == PHASE_MARKER
    assert summary["previous_gate"] == "targeted_real_world_pdf_fixture_expansion_v0"
    assert summary["download_hash_status"] == "passed_with_blocked_candidates"
    assert summary["candidate_count"] == 6
    assert summary["downloaded_fixture_count"] == 3
    assert summary["blocked_fixture_count"] == 2
    assert summary["external_route_count"] == 1
    assert summary["binary_files_committed"] is False
    assert summary["download_cache_committed"] is False
    assert summary["raw_text_committed"] is False
    assert summary["parser_calls_performed"] is False
    assert summary["ocr_calls_performed"] is False
    assert summary["table_extraction_calls_performed"] is False
    assert summary["can_claim_download_hash_metadata"] is True
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["next_gate"] == NEXT_GATE

    assert summary["downloaded_fixture_ids"] == [
        "eia_steo_full_rendered_visual_fidelity_candidate",
        "bea_wp2022_10_labeled_layout_candidate",
        "nara_911_mfr_00282_no_native_text_candidate",
    ]
    assert summary["blocked_fixture_ids"] == [
        "bls_mlr_2011_06_reading_order_candidate",
        "bls_beyond_numbers_figures_candidate",
    ]
    assert summary["external_route_ids"] == [
        "github_issue_1_external_reviewer_route",
    ]


def test_source_policy_download_hash_manifest_keeps_binaries_and_raw_content_out():
    manifest = load_source_policy_download_hash_manifest(MANIFEST_PATH)

    for item in manifest["downloaded_fixtures"]:
        assert item["download_status"] == "downloaded_and_hashed"
        assert item["http_status"] == 200
        assert item["byte_size"] > 0
        assert len(item["sha256"]) == 64
        assert item["pdf_magic_header"] is True
        assert item["binary_committed"] is False
        assert item["local_pdf_path"] is None
        assert item["raw_text_committed"] is False

    for item in manifest["blocked_fixtures"]:
        assert item["download_status"] == "blocked_http_403"
        assert item["http_status"] == 403
        assert item["sha256"] is None
        assert item["binary_committed"] is False
        assert item["local_pdf_path"] is None

    for item in manifest["external_routes"]:
        assert item["download_status"] == "not_applicable_external_review_route"
        assert item["sha256"] is None
        assert item["binary_committed"] is False
        assert item["local_pdf_path"] is None


def test_source_policy_download_hash_report_is_current_and_bounded():
    manifest = load_source_policy_download_hash_manifest(MANIFEST_PATH)
    summary = build_source_policy_download_hash_summary(manifest)
    report = build_source_policy_download_hash_report(summary)

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Source-policy PDF Download and Hash" in report
    assert "real_world_pdf_fixture_source_policy_download_hash_v0" in report
    assert "download_hash_status -> passed_with_blocked_candidates" in report
    assert "downloaded_fixture_count -> 3" in report
    assert "blocked_fixture_count -> 2" in report
    assert "external_route_count -> 1" in report
    assert "can_claim_robust_pdf_extraction -> false" in report
    assert "not robust PDF extraction evidence" in report
    assert "no external PDF binaries committed" in report


def test_source_policy_download_hash_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.source_policy_download_hash_command",
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
    assert "source_policy_download_hash_report_current" in result.stdout
    assert "downloaded_fixture_count=3" in result.stdout
    assert "can_claim_robust_pdf_extraction=false" in result.stdout


def test_source_policy_download_hash_docs_and_surfaces_are_linked():
    review_path = REPO_ROOT / "docs/review/source-policy-download-hash.md"
    spec_path = (
        REPO_ROOT
        / "docs/specs/2026-06-30-real-world-pdf-fixture-source-policy-download-hash.md"
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
        (REPO_ROOT / "docs/review/external-reader-proof-path.md").read_text(
            encoding="utf-8"
        ),
        (REPO_ROOT / "apps/api/app/services/proof_gap_registry.py").read_text(
            encoding="utf-8"
        ),
        (REPO_ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8"),
    ]

    for surface in surfaces:
        assert "real_world_pdf_fixture_source_policy_download_hash_v0" in surface
        assert "source_policy_pdf_parse_observation_v0" in surface

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
