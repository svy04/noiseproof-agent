import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
ROUTE_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/source-policy-no-native-text-failure-route.json"
)
REPORT_PATH = (
    REPO_ROOT
    / "docs/evaluation/source-policy-no-native-text-failure-route-report.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.source_policy_no_native_text_failure_route import (  # noqa: E402
    NEXT_GATE,
    PHASE_MARKER,
    build_source_policy_no_native_text_failure_route_report,
    build_source_policy_no_native_text_failure_route_summary,
    load_source_policy_no_native_text_failure_route,
)


def test_source_policy_no_native_text_failure_route_preserves_nara_failure():
    route = load_source_policy_no_native_text_failure_route(ROUTE_PATH)
    summary = build_source_policy_no_native_text_failure_route_summary(route)

    assert summary["phase_marker"] == PHASE_MARKER
    assert summary["previous_gate"] == "source_policy_pdf_quality_gap_review_v0"
    assert summary["route_status"] == "passed_failure_route_preserved"
    assert summary["failure_route_count"] == 1
    assert summary["selected_failure_route"] == (
        "multi_publisher_no_extractable_text_failure"
    )
    assert summary["fixture_id"] == "nara_911_mfr_00282_no_native_text_candidate"
    assert summary["publisher"] == "National Archives and Records Administration"
    assert summary["failure_type"] == "no_native_text_observed"
    assert summary["root_cause"] == "image_or_scanned_pdf_without_native_text_layer"
    assert summary["fix_status"] == "planned_not_implemented"
    assert summary["page_count"] == 4
    assert summary["empty_page_count"] == 4
    assert summary["text_char_count"] == 0
    assert summary["ocr_calls_performed"] is False
    assert summary["parser_calls_performed"] is False
    assert summary["can_claim_source_policy_no_native_text_failure_route"] is True
    assert summary["can_claim_ocr_quality"] is False
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["next_gate"] == NEXT_GATE


def test_source_policy_no_native_text_failure_route_keeps_provenance_and_boundaries():
    route = load_source_policy_no_native_text_failure_route(ROUTE_PATH)
    summary = build_source_policy_no_native_text_failure_route_summary(route)

    failure_route = summary["failure_route"]
    assert failure_route["source_url"] == (
        "https://nara-media-001.s3.amazonaws.com/arcmedia/9-11/MFR/t-0148-911MFR-00282.pdf"
    )
    assert failure_route["policy_source_url"] == (
        "https://www.archives.gov/global-pages/privacy.html"
    )
    assert failure_route["source_sha256"] == (
        "6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba"
    )
    assert failure_route["binary_committed"] is False
    assert failure_route["raw_text_committed"] is False
    assert failure_route["quality_claim_ready"] is False
    assert "OCR was not attempted" in failure_route["warnings"][0]
    assert "not robust PDF extraction evidence" in failure_route["boundary"]

    for field in [
        "runtime_work_performed",
        "pdf_downloads_performed",
        "parser_calls_performed",
        "ocr_calls_performed",
        "table_extraction_calls_performed",
        "llm_calls_performed",
        "binary_files_committed",
        "download_cache_committed",
        "raw_text_committed",
    ]:
        assert summary[field] is False


def test_source_policy_no_native_text_failure_route_report_is_current_and_bounded():
    route = load_source_policy_no_native_text_failure_route(ROUTE_PATH)
    summary = build_source_policy_no_native_text_failure_route_summary(route)
    report = build_source_policy_no_native_text_failure_route_report(summary)

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Source-policy No-native-text Failure Route" in report
    assert "source_policy_no_native_text_failure_route_v0" in report
    assert "route_status -> passed_failure_route_preserved" in report
    assert "fixture_id -> nara_911_mfr_00282_no_native_text_candidate" in report
    assert "failure_type -> no_native_text_observed" in report
    assert "page_count -> 4" in report
    assert "empty_page_count -> 4" in report
    assert "text_char_count -> 0" in report
    assert "ocr_calls_performed -> false" in report
    assert "can_claim_ocr_quality -> false" in report
    assert "can_claim_robust_pdf_extraction -> false" in report
    assert "source_policy_no_native_text_ocr_readiness_review_v0" in report
    assert "not robust PDF extraction evidence" in report
    assert "not OCR quality evidence" in report


def test_source_policy_no_native_text_failure_route_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.source_policy_no_native_text_failure_route_command",
            "--route",
            str(ROUTE_PATH),
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
    assert "source_policy_no_native_text_failure_route_report_current" in result.stdout
    assert "route_status=passed_failure_route_preserved" in result.stdout
    assert "failure_type=no_native_text_observed" in result.stdout
    assert "can_claim_ocr_quality=false" in result.stdout
    assert "can_claim_robust_pdf_extraction=false" in result.stdout


def test_source_policy_no_native_text_failure_route_docs_and_surfaces_are_linked():
    review_path = REPO_ROOT / "docs/review/source-policy-no-native-text-failure-route.md"
    spec_path = (
        REPO_ROOT
        / "docs/specs/2026-06-30-source-policy-no-native-text-failure-route.md"
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
        (REPO_ROOT / "docs/review/proof-gap-action-surface.md").read_text(
            encoding="utf-8"
        ),
        (REPO_ROOT / "apps/api/app/services/proof_gap_registry.py").read_text(
            encoding="utf-8"
        ),
        (REPO_ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8"),
    ]

    for surface in surfaces:
        assert "source_policy_no_native_text_failure_route_v0" in surface
        assert "source_policy_no_native_text_ocr_readiness_review_v0" in surface

    for boundary in [
        "not robust PDF extraction evidence",
        "not arbitrary-market PDF parsing evidence",
        "not OCR quality evidence",
        "not table extraction benchmark evidence",
        "not rendered visual fidelity evidence",
        "not image/chart interpretation evidence",
        "not hosted deployment evidence",
        "not external reviewer feedback",
        "not product-complete",
    ]:
        assert boundary in surfaces[0]
