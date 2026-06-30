import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
REVIEW_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/source-policy-no-native-text-ocr-readiness-review.json"
)
REPORT_PATH = (
    REPO_ROOT
    / "docs/evaluation/source-policy-no-native-text-ocr-readiness-review-report.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.source_policy_no_native_text_ocr_readiness_review import (  # noqa: E402
    NEXT_GATE,
    PHASE_MARKER,
    build_source_policy_no_native_text_ocr_readiness_report,
    build_source_policy_no_native_text_ocr_readiness_summary,
    load_source_policy_no_native_text_ocr_readiness_review,
)


def test_source_policy_no_native_text_ocr_readiness_review_is_conditions_only():
    review = load_source_policy_no_native_text_ocr_readiness_review(REVIEW_PATH)
    summary = build_source_policy_no_native_text_ocr_readiness_summary(review)

    assert summary["phase_marker"] == PHASE_MARKER
    assert summary["previous_gate"] == "source_policy_no_native_text_failure_route_v0"
    assert summary["readiness_status"] == "passed_with_conditions"
    assert summary["fixture_id"] == "nara_911_mfr_00282_no_native_text_candidate"
    assert summary["failure_type"] == "no_native_text_observed"
    assert summary["page_count"] == 4
    assert summary["empty_page_count"] == 4
    assert summary["text_char_count"] == 0
    assert summary["ocr_dependency_identified"] is True
    assert summary["ocr_dependency_runtime_check_performed"] is False
    assert summary["ocr_execution_performed"] is False
    assert summary["ocr_quality_eval_performed"] is False
    assert summary["runtime_work_performed"] is False
    assert summary["pdf_downloads_performed"] is False
    assert summary["parser_calls_performed"] is False
    assert summary["can_claim_ocr_readiness_review"] is True
    assert summary["can_claim_ocr_dependency_available"] is False
    assert summary["can_claim_ocr_execution"] is False
    assert summary["can_claim_ocr_quality"] is False
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["next_gate"] == NEXT_GATE


def test_source_policy_no_native_text_ocr_readiness_review_records_sources_and_criteria():
    review = load_source_policy_no_native_text_ocr_readiness_review(REVIEW_PATH)
    summary = build_source_policy_no_native_text_ocr_readiness_summary(review)

    sources = {source["label"]: source for source in summary["sources"]}
    assert "PyMuPDF OCR recipes" in sources
    assert "PyMuPDF Page.get_textpage_ocr" in sources
    assert "OCR-D evaluation" in sources
    assert "Model Cards" in sources
    assert "Datasheets for Datasets" in sources
    assert sources["PyMuPDF OCR recipes"]["source_type"] == "official_doc"
    assert sources["OCR-D evaluation"]["source_type"] == "standard"

    criteria = {item["criterion_id"]: item for item in summary["readiness_criteria"]}
    assert criteria["preserved_failure_route"]["status"] == "met"
    assert criteria["source_policy_boundary"]["status"] == "met"
    assert criteria["ocr_dependency_boundary"]["status"] == "planned_next_gate"
    assert criteria["ocr_execution_boundary"]["status"] == "blocked_until_dependency_check"
    assert criteria["ocr_quality_boundary"]["status"] == "blocked_until_ground_truth_eval"
    assert criteria["raw_content_boundary"]["status"] == "met"


def test_source_policy_no_native_text_ocr_readiness_review_keeps_sensitive_runtime_data_out():
    review = load_source_policy_no_native_text_ocr_readiness_review(REVIEW_PATH)
    summary = build_source_policy_no_native_text_ocr_readiness_summary(review)

    for field in [
        "binary_files_committed",
        "download_cache_committed",
        "raw_text_committed",
        "raw_extracted_text_committed",
        "raw_ocr_text_committed",
        "raw_table_rows_committed",
        "page_images_committed",
        "screenshots_committed",
        "local_paths_committed",
        "tessdata_paths_committed",
    ]:
        assert summary[field] is False

    for boundary in [
        "not OCR dependency availability evidence",
        "not OCR execution evidence",
        "not OCR quality evidence",
        "not robust PDF extraction evidence",
        "not arbitrary-market PDF parsing evidence",
        "not rendered visual fidelity evidence",
        "not image/chart interpretation evidence",
        "not external reviewer feedback",
        "not product-complete",
    ]:
        assert boundary in summary["boundary_notes"]


def test_source_policy_no_native_text_ocr_readiness_report_is_current_and_bounded():
    review = load_source_policy_no_native_text_ocr_readiness_review(REVIEW_PATH)
    summary = build_source_policy_no_native_text_ocr_readiness_summary(review)
    report = build_source_policy_no_native_text_ocr_readiness_report(summary)

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Source-policy No-native-text OCR Readiness Review" in report
    assert "source_policy_no_native_text_ocr_readiness_review_v0" in report
    assert "readiness_status -> passed_with_conditions" in report
    assert "fixture_id -> nara_911_mfr_00282_no_native_text_candidate" in report
    assert "ocr_dependency_identified -> true" in report
    assert "ocr_dependency_runtime_check_performed -> false" in report
    assert "ocr_execution_performed -> false" in report
    assert "ocr_quality_eval_performed -> false" in report
    assert "can_claim_ocr_dependency_available -> false" in report
    assert "can_claim_ocr_execution -> false" in report
    assert "can_claim_ocr_quality -> false" in report
    assert "source_policy_no_native_text_ocr_dependency_check_v0" in report
    assert "not OCR execution evidence" in report
    assert "not OCR quality evidence" in report
    assert "not robust PDF extraction evidence" in report


def test_source_policy_no_native_text_ocr_readiness_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.source_policy_no_native_text_ocr_readiness_review_command",
            "--review",
            str(REVIEW_PATH),
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
    assert "source_policy_no_native_text_ocr_readiness_review_report_current" in result.stdout
    assert "readiness_status=passed_with_conditions" in result.stdout
    assert "can_claim_ocr_dependency_available=false" in result.stdout
    assert "can_claim_ocr_execution=false" in result.stdout
    assert "can_claim_ocr_quality=false" in result.stdout
    assert "can_claim_robust_pdf_extraction=false" in result.stdout


def test_source_policy_no_native_text_ocr_readiness_docs_and_surfaces_are_linked():
    review_path = (
        REPO_ROOT / "docs/review/source-policy-no-native-text-ocr-readiness-review.md"
    )
    spec_path = (
        REPO_ROOT
        / "docs/specs/2026-06-30-source-policy-no-native-text-ocr-readiness-review.md"
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
        assert "source_policy_no_native_text_ocr_readiness_review_v0" in surface
        assert "source_policy_no_native_text_ocr_dependency_check_v0" in surface

    for boundary in [
        "not OCR dependency availability evidence",
        "not OCR execution evidence",
        "not OCR quality evidence",
        "not robust PDF extraction evidence",
        "not arbitrary-market PDF parsing evidence",
        "not rendered visual fidelity evidence",
        "not image/chart interpretation evidence",
        "not external reviewer feedback",
        "not product-complete",
    ]:
        assert boundary in surfaces[0]
