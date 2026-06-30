import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
OBSERVATION_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/source-policy-pdf-parse-observations.json"
)
REPORT_PATH = (
    REPO_ROOT
    / "docs/evaluation/source-policy-pdf-parse-observation-report.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.source_policy_pdf_parse_observation import (  # noqa: E402
    NEXT_GATE,
    PHASE_MARKER,
    build_source_policy_pdf_parse_observation_report,
    build_source_policy_pdf_parse_observation_summary,
    load_source_policy_pdf_parse_observation,
)


def test_source_policy_pdf_parse_observation_records_parse_metadata_without_raw_content():
    observation = load_source_policy_pdf_parse_observation(OBSERVATION_PATH)
    summary = build_source_policy_pdf_parse_observation_summary(observation)

    assert summary["phase_marker"] == PHASE_MARKER
    assert summary["previous_gate"] == (
        "real_world_pdf_fixture_source_policy_download_hash_v0"
    )
    assert summary["parse_observation_status"] == "passed_with_no_native_text_candidate"
    assert summary["candidate_count"] == 6
    assert summary["observed_fixture_count"] == 3
    assert summary["native_text_fixture_count"] == 2
    assert summary["no_native_text_fixture_count"] == 1
    assert summary["blocked_fixture_count"] == 2
    assert summary["external_route_count"] == 1
    assert summary["failure_case_candidate_count"] == 1
    assert summary["total_page_count"] == 94
    assert summary["total_extracted_page_count"] == 90
    assert summary["total_empty_page_count"] == 4
    assert summary["total_text_char_count"] == 309507
    assert summary["total_text_block_count"] == 3132
    assert summary["total_image_block_count"] == 0
    assert summary["parser_calls_performed"] is True
    assert summary["ocr_calls_performed"] is False
    assert summary["table_extraction_calls_performed"] is False
    assert summary["llm_calls_performed"] is False
    assert summary["binary_files_committed"] is False
    assert summary["download_cache_committed"] is False
    assert summary["raw_text_committed"] is False
    assert summary["can_claim_source_policy_pdf_parse_observation"] is True
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["next_gate"] == NEXT_GATE


def test_source_policy_pdf_parse_observation_keeps_failed_and_blocked_routes_structured():
    observation = load_source_policy_pdf_parse_observation(OBSERVATION_PATH)
    summary = build_source_policy_pdf_parse_observation_summary(observation)

    by_id = {item["fixture_id"]: item for item in summary["observed_fixtures"]}
    assert by_id["eia_steo_full_rendered_visual_fidelity_candidate"][
        "parse_status"
    ] == "metadata_observed"
    assert by_id["eia_steo_full_rendered_visual_fidelity_candidate"][
        "text_char_count"
    ] == 249238
    assert by_id["bea_wp2022_10_labeled_layout_candidate"][
        "parse_status"
    ] == "metadata_observed"
    assert by_id["bea_wp2022_10_labeled_layout_candidate"][
        "text_char_count"
    ] == 60269

    nara = by_id["nara_911_mfr_00282_no_native_text_candidate"]
    assert nara["parse_status"] == "no_native_text_observed"
    assert nara["text_char_count"] == 0
    assert nara["empty_page_count"] == 4
    assert nara["failure_case_candidate"]["failure_type"] == (
        "no_native_text_observed"
    )
    assert "OCR was not attempted" in nara["warnings"][0]

    assert summary["blocked_fixture_ids"] == [
        "bls_mlr_2011_06_reading_order_candidate",
        "bls_beyond_numbers_figures_candidate",
    ]
    assert summary["external_route_ids"] == [
        "github_issue_1_external_reviewer_route",
    ]


def test_source_policy_pdf_parse_observation_manifest_keeps_binaries_and_raw_content_out():
    observation = load_source_policy_pdf_parse_observation(OBSERVATION_PATH)

    for item in observation["observed_fixtures"]:
        assert item["binary_committed"] is False
        assert item["local_pdf_path"] is None
        assert item["raw_text_committed"] is False
        assert item["table_extraction_performed"] is False
        assert item["ocr_calls_attempted"] is False

    for field in [
        "binary_files_committed",
        "download_cache_committed",
        "raw_text_committed",
        "raw_extracted_text_committed",
        "raw_ocr_text_committed",
        "raw_table_rows_committed",
        "page_images_committed",
        "screenshots_committed",
    ]:
        assert observation[field] is False


def test_source_policy_pdf_parse_observation_report_is_current_and_bounded():
    observation = load_source_policy_pdf_parse_observation(OBSERVATION_PATH)
    summary = build_source_policy_pdf_parse_observation_summary(observation)
    report = build_source_policy_pdf_parse_observation_report(summary)

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Source-policy PDF Parse Observation" in report
    assert "source_policy_pdf_parse_observation_v0" in report
    assert "observed_fixture_count -> 3" in report
    assert "native_text_fixture_count -> 2" in report
    assert "no_native_text_fixture_count -> 1" in report
    assert "failure_case_candidate_count -> 1" in report
    assert "total_text_char_count -> 309507" in report
    assert "can_claim_robust_pdf_extraction -> false" in report
    assert "not robust PDF extraction evidence" in report
    assert "no raw text committed" in report


def test_source_policy_pdf_parse_observation_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.source_policy_pdf_parse_observation_command",
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
    assert "source_policy_pdf_parse_observation_report_current" in result.stdout
    assert "observed_fixture_count=3" in result.stdout
    assert "can_claim_robust_pdf_extraction=false" in result.stdout


def test_source_policy_pdf_parse_observation_docs_and_surfaces_are_linked():
    review_path = REPO_ROOT / "docs/review/source-policy-pdf-parse-observation.md"
    spec_path = (
        REPO_ROOT
        / "docs/specs/2026-06-30-source-policy-pdf-parse-observation.md"
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
        assert "source_policy_pdf_parse_observation_v0" in surface
        assert "source_policy_pdf_parse_quality_matrix_v0" in surface

    for boundary in [
        "not robust PDF extraction evidence",
        "not arbitrary-market PDF parsing evidence",
        "not OCR quality evidence",
        "not table extraction benchmark evidence",
        "not layout fidelity evidence",
        "not rendered visual fidelity evidence",
        "not image/chart interpretation evidence",
        "not hosted deployment evidence",
        "not external reviewer feedback",
        "not product-complete",
    ]:
        assert boundary in surfaces[0]
