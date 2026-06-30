import json
import subprocess
import sys
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[3]
MARKER_PROXY_EVAL_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/source-policy-no-native-text-ocr-marker-proxy-eval.json"
)
PLAN_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/source-policy-no-native-text-ocr-transcript-reference-plan.json"
)
REPORT_PATH = (
    REPO_ROOT
    / "docs/evaluation/source-policy-no-native-text-ocr-transcript-reference-plan-report.md"
)
REVIEW_PATH = (
    REPO_ROOT / "docs/review/source-policy-no-native-text-ocr-transcript-reference-plan.md"
)
SPEC_PATH = (
    REPO_ROOT
    / "docs/specs/2026-07-01-source-policy-no-native-text-ocr-transcript-reference-plan.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.source_policy_no_native_text_ocr_transcript_reference_plan import (  # noqa: E402
    NEXT_GATE,
    PHASE_MARKER,
    PREVIOUS_GATE,
    build_source_policy_no_native_text_ocr_transcript_reference_plan,
    build_source_policy_no_native_text_ocr_transcript_reference_plan_report,
    build_source_policy_no_native_text_ocr_transcript_reference_plan_summary,
    load_source_policy_no_native_text_ocr_transcript_reference_plan,
    validate_source_policy_no_native_text_ocr_transcript_reference_plan,
)


def test_source_policy_no_native_text_ocr_transcript_reference_plan_commits_sanitized_plan():
    plan = load_source_policy_no_native_text_ocr_transcript_reference_plan(PLAN_PATH)
    summary = build_source_policy_no_native_text_ocr_transcript_reference_plan_summary(
        plan
    )

    assert summary["phase_marker"] == PHASE_MARKER
    assert summary["previous_gate"] == PREVIOUS_GATE
    assert summary["plan_status"] == "planned_transcript_reference_contract"
    assert summary["target_fixture_id"] == "nara_911_mfr_00282_no_native_text_candidate"
    assert summary["source_sha256"] == (
        "6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba"
    )
    assert summary["marker_proxy_eval_phase_marker"] == PREVIOUS_GATE
    assert summary["reference_unit_type"] == "page_level_transcript_plan"
    assert summary["target_page_count"] == 4
    assert summary["minimum_reference_pages"] == 4
    assert summary["required_reference_unit_count"] == 6
    assert summary["required_reference_units"] == [
        "source_policy_review",
        "owner_approval",
        "page_level_reference_transcript",
        "normalization_rules",
        "alignment_policy",
        "metric_eligibility_review",
    ]
    assert summary["metric_candidates"] == ["cer", "wer"]
    assert (
        summary["metric_candidates_status"]
        == "blocked_until_reference_transcript_exists"
    )
    assert summary["owner_approval_required"] is True
    assert summary["source_policy_review_required"] is True
    assert summary["full_reference_transcript_required"] is True
    assert summary["full_reference_transcript_available"] is False
    assert summary["transcript_collection_performed"] is False
    assert summary["reference_pack_created"] is False
    assert summary["quality_eval_performed"] is False
    assert summary["cer_computed"] is False
    assert summary["wer_computed"] is False
    assert summary["raw_reference_text_committed"] is False
    assert summary["raw_ocr_text_committed"] is False
    assert summary["can_claim_transcript_reference_plan"] is True
    assert summary["can_claim_transcript_reference_pack"] is False
    assert summary["can_claim_ocr_quality"] is False
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["next_gate"] == NEXT_GATE


def test_source_policy_no_native_text_ocr_transcript_reference_plan_builds_from_marker_proxy_eval():
    marker_proxy_eval = json.loads(
        MARKER_PROXY_EVAL_PATH.read_text(encoding="utf-8")
    )

    plan = build_source_policy_no_native_text_ocr_transcript_reference_plan(
        marker_proxy_eval
    )

    assert plan["phase_marker"] == PHASE_MARKER
    assert plan["previous_gate"] == PREVIOUS_GATE
    assert plan["marker_proxy_eval_phase_marker"] == PREVIOUS_GATE
    assert plan["plan_status"] == "planned_transcript_reference_contract"
    assert plan["required_reference_unit_count"] == 6
    assert plan["target_page_count"] == 4
    assert plan["metric_candidates_status"] == (
        "blocked_until_reference_transcript_exists"
    )
    assert plan["full_reference_transcript_available"] is False
    assert plan["quality_eval_performed"] is False
    assert plan["recommended_next_gate"] == NEXT_GATE


def test_source_policy_no_native_text_ocr_transcript_reference_plan_report_is_current_and_bounded():
    plan = load_source_policy_no_native_text_ocr_transcript_reference_plan(PLAN_PATH)
    summary = build_source_policy_no_native_text_ocr_transcript_reference_plan_summary(
        plan
    )
    report = build_source_policy_no_native_text_ocr_transcript_reference_plan_report(
        summary
    )

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Source-policy No-native-text OCR Transcript Reference Plan" in report
    assert "source_policy_no_native_text_ocr_transcript_reference_plan_v0" in report
    assert "previous_gate -> source_policy_no_native_text_ocr_marker_proxy_eval_v0" in report
    assert "plan_status -> planned_transcript_reference_contract" in report
    assert "full_reference_transcript_required -> true" in report
    assert "full_reference_transcript_available -> false" in report
    assert "transcript_collection_performed -> false" in report
    assert "reference_pack_created -> false" in report
    assert "quality_eval_performed -> false" in report
    assert "cer_computed -> false" in report
    assert "wer_computed -> false" in report
    assert "can_claim_transcript_reference_plan -> true" in report
    assert "can_claim_transcript_reference_pack -> false" in report
    assert "can_claim_ocr_quality -> false" in report
    assert "source_policy_no_native_text_ocr_transcript_reference_pack_v0" in report
    assert "not OCR quality evidence" in report
    assert "not CER/WER support" in report
    assert "not robust PDF extraction evidence" in report


def test_source_policy_no_native_text_ocr_transcript_reference_plan_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.source_policy_no_native_text_ocr_transcript_reference_plan_command",
            "--transcript-reference-plan",
            str(PLAN_PATH),
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
        "source_policy_no_native_text_ocr_transcript_reference_plan_report_current"
        in result.stdout
    )
    assert "can_claim_transcript_reference_plan=true" in result.stdout
    assert "can_claim_ocr_quality=false" in result.stdout
    assert "can_claim_robust_pdf_extraction=false" in result.stdout


def test_source_policy_no_native_text_ocr_transcript_reference_plan_rejects_transcript_or_quality_overclaims(
    tmp_path,
):
    plan = load_source_policy_no_native_text_ocr_transcript_reference_plan(PLAN_PATH)

    transcript_plan = dict(plan)
    transcript_plan["full_reference_transcript_available"] = True
    with pytest.raises(ValueError, match="full_reference_transcript_available"):
        validate_source_policy_no_native_text_ocr_transcript_reference_plan(
            transcript_plan
        )

    quality_plan = dict(plan)
    quality_plan["quality_eval_performed"] = True
    with pytest.raises(ValueError, match="quality_eval_performed"):
        validate_source_policy_no_native_text_ocr_transcript_reference_plan(
            quality_plan
        )

    cer_plan = dict(plan)
    cer_plan["cer_computed"] = True
    with pytest.raises(ValueError, match="cer_computed"):
        validate_source_policy_no_native_text_ocr_transcript_reference_plan(cer_plan)

    raw_plan = dict(plan)
    raw_plan["raw_reference_text"] = "forbidden"
    raw_path = tmp_path / "raw-reference.json"
    raw_path.write_text(json.dumps(raw_plan), encoding="utf-8")
    with pytest.raises(ValueError, match="raw_reference_text"):
        load_source_policy_no_native_text_ocr_transcript_reference_plan(raw_path)


def test_source_policy_no_native_text_ocr_transcript_reference_plan_artifacts_are_sanitized():
    artifacts = [
        PLAN_PATH,
        REPORT_PATH,
        REVIEW_PATH,
        SPEC_PATH,
    ]
    forbidden = [
        "Users\\admin",
        "C:\\",
        "tessdata_path:",
        "tesseract_path:",
        "raw_text:",
        "raw_ocr_text:",
        "raw_reference_text:",
        "reference_transcript:",
        "raw_extracted_text:",
        "recognized_text:",
        "page_image:",
        "screenshot:",
    ]

    for artifact in artifacts:
        text = artifact.read_text(encoding="utf-8")
        for marker in forbidden:
            assert marker not in text


def test_source_policy_no_native_text_ocr_transcript_reference_plan_docs_and_surfaces_are_linked():
    assert REVIEW_PATH.is_file()
    assert SPEC_PATH.is_file()
    assert REPORT_PATH.is_file()

    surfaces = [
        REVIEW_PATH.read_text(encoding="utf-8"),
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
        (REPO_ROOT / "docs/research/source-assimilation-registry.md").read_text(
            encoding="utf-8"
        ),
        (REPO_ROOT / "apps/api/app/services/proof_gap_registry.py").read_text(
            encoding="utf-8"
        ),
        (REPO_ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8"),
    ]

    for surface in surfaces:
        assert "source_policy_no_native_text_ocr_transcript_reference_plan_v0" in surface
        assert "source_policy_no_native_text_ocr_transcript_reference_pack_v0" in surface

    for boundary in [
        "not OCR quality evidence",
        "not CER/WER support",
        "not robust PDF extraction evidence",
        "not arbitrary-market PDF parsing evidence",
        "not rendered visual fidelity evidence",
        "not image/chart interpretation evidence",
        "not external reviewer feedback",
        "not product-complete",
    ]:
        assert boundary in surfaces[0]
