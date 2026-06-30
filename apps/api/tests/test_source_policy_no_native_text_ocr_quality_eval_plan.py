import json
import subprocess
import sys
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[3]
SMOKE_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/source-policy-no-native-text-ocr-execution-smoke.json"
)
PLAN_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/source-policy-no-native-text-ocr-quality-eval-plan.json"
)
REPORT_PATH = (
    REPO_ROOT
    / "docs/evaluation/source-policy-no-native-text-ocr-quality-eval-plan-report.md"
)
REVIEW_PATH = REPO_ROOT / "docs/review/source-policy-no-native-text-ocr-quality-eval-plan.md"
SPEC_PATH = (
    REPO_ROOT
    / "docs/specs/2026-06-30-source-policy-no-native-text-ocr-quality-eval-plan.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.source_policy_no_native_text_ocr_quality_eval_plan import (  # noqa: E402
    NEXT_GATE,
    PHASE_MARKER,
    PREVIOUS_GATE,
    build_source_policy_no_native_text_ocr_quality_eval_plan,
    build_source_policy_no_native_text_ocr_quality_eval_plan_report,
    build_source_policy_no_native_text_ocr_quality_eval_plan_summary,
    load_source_policy_no_native_text_ocr_quality_eval_plan,
    validate_source_policy_no_native_text_ocr_quality_eval_plan,
)


def test_source_policy_no_native_text_ocr_quality_eval_plan_commits_sanitized_contract():
    plan = load_source_policy_no_native_text_ocr_quality_eval_plan(PLAN_PATH)
    summary = build_source_policy_no_native_text_ocr_quality_eval_plan_summary(plan)

    assert summary["phase_marker"] == PHASE_MARKER
    assert summary["previous_gate"] == PREVIOUS_GATE
    assert summary["plan_status"] == "planned_quality_eval_contract"
    assert summary["target_fixture_id"] == "nara_911_mfr_00282_no_native_text_candidate"
    assert summary["source_sha256"] == (
        "6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba"
    )
    assert summary["execution_smoke_ocr_text_char_count"] == 8019
    assert summary["execution_smoke_expected_markers_found_count"] == 2
    assert summary["execution_smoke_quality_eval_performed"] is False
    assert summary["ground_truth_available"] is False
    assert summary["reference_pack_required"] is True
    assert summary["quality_eval_performed"] is False
    assert summary["raw_reference_text_committed"] is False
    assert summary["raw_ocr_text_committed"] is False
    assert summary["marker_hits_are_quality_proxy_only"] is True
    assert summary["can_claim_quality_eval_plan"] is True
    assert summary["can_claim_ocr_quality"] is False
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["next_gate"] == NEXT_GATE
    assert "character_error_rate" in summary["quality_metric_candidates"]
    assert "word_error_rate" in summary["quality_metric_candidates"]
    assert "expected_marker_precision_recall_proxy" in summary[
        "quality_metric_candidates"
    ]
    assert "page_level_reference_transcript_or_accepted_spans" in summary[
        "required_reference_inputs"
    ]
    assert "normalization_rules" in summary["required_reference_inputs"]
    assert "source_sha256_binding" in summary["required_reference_inputs"]


def test_source_policy_no_native_text_ocr_quality_eval_plan_builds_from_execution_smoke():
    smoke = json.loads(SMOKE_PATH.read_text(encoding="utf-8"))
    plan = build_source_policy_no_native_text_ocr_quality_eval_plan(smoke)

    assert plan["phase_marker"] == PHASE_MARKER
    assert plan["previous_gate"] == PREVIOUS_GATE
    assert plan["execution_smoke_phase_marker"] == (
        "source_policy_no_native_text_ocr_execution_smoke_v0"
    )
    assert plan["execution_smoke_ocr_execution_performed"] is True
    assert plan["execution_smoke_ocr_text_char_count"] == 8019
    assert plan["execution_smoke_expected_markers_found_count"] == 2
    assert plan["quality_eval_performed"] is False
    assert plan["ground_truth_available"] is False
    assert plan["reference_pack_required"] is True
    assert plan["recommended_next_gate"] == NEXT_GATE


def test_source_policy_no_native_text_ocr_quality_eval_plan_report_is_current_and_bounded():
    plan = load_source_policy_no_native_text_ocr_quality_eval_plan(PLAN_PATH)
    summary = build_source_policy_no_native_text_ocr_quality_eval_plan_summary(plan)
    report = build_source_policy_no_native_text_ocr_quality_eval_plan_report(summary)

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Source-policy No-native-text OCR Quality Eval Plan" in report
    assert "source_policy_no_native_text_ocr_quality_eval_plan_v0" in report
    assert "previous_gate -> source_policy_no_native_text_ocr_execution_smoke_v0" in report
    assert "quality_eval_performed -> false" in report
    assert "ground_truth_available -> false" in report
    assert "reference_pack_required -> true" in report
    assert "marker_hits_are_quality_proxy_only -> true" in report
    assert "can_claim_quality_eval_plan -> true" in report
    assert "can_claim_ocr_quality -> false" in report
    assert "can_claim_robust_pdf_extraction -> false" in report
    assert "source_policy_no_native_text_ocr_quality_reference_pack_v0" in report
    assert "not OCR quality evidence" in report
    assert "not robust PDF extraction evidence" in report


def test_source_policy_no_native_text_ocr_quality_eval_plan_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.source_policy_no_native_text_ocr_quality_eval_plan_command",
            "--plan",
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
    assert "source_policy_no_native_text_ocr_quality_eval_plan_report_current" in result.stdout
    assert "can_claim_quality_eval_plan=true" in result.stdout
    assert "can_claim_ocr_quality=false" in result.stdout
    assert "can_claim_robust_pdf_extraction=false" in result.stdout


def test_source_policy_no_native_text_ocr_quality_eval_plan_rejects_quality_or_raw_text_claims(
    tmp_path,
):
    plan = load_source_policy_no_native_text_ocr_quality_eval_plan(PLAN_PATH)

    quality_plan = dict(plan)
    quality_plan["quality_eval_performed"] = True
    with pytest.raises(ValueError, match="quality_eval_performed"):
        validate_source_policy_no_native_text_ocr_quality_eval_plan(quality_plan)

    ground_truth_plan = dict(plan)
    ground_truth_plan["ground_truth_available"] = True
    with pytest.raises(ValueError, match="ground_truth_available"):
        validate_source_policy_no_native_text_ocr_quality_eval_plan(ground_truth_plan)

    raw_plan = dict(plan)
    raw_plan["raw_reference_text"] = "forbidden"
    raw_path = tmp_path / "raw-reference.json"
    raw_path.write_text(json.dumps(raw_plan), encoding="utf-8")
    with pytest.raises(ValueError, match="raw_reference_text"):
        load_source_policy_no_native_text_ocr_quality_eval_plan(raw_path)

    proxy_plan = dict(plan)
    proxy_plan["marker_hits_are_quality_proxy_only"] = False
    with pytest.raises(ValueError, match="marker_hits_are_quality_proxy_only"):
        validate_source_policy_no_native_text_ocr_quality_eval_plan(proxy_plan)


def test_source_policy_no_native_text_ocr_quality_eval_plan_artifacts_are_sanitized():
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
        "raw_extracted_text:",
        "recognized_text:",
        "page_image:",
        "screenshot:",
    ]

    for artifact in artifacts:
        text = artifact.read_text(encoding="utf-8")
        for marker in forbidden:
            assert marker not in text


def test_source_policy_no_native_text_ocr_quality_eval_plan_docs_and_surfaces_are_linked():
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
        (REPO_ROOT / "apps/api/app/services/proof_gap_registry.py").read_text(
            encoding="utf-8"
        ),
        (REPO_ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8"),
    ]

    for surface in surfaces:
        assert "source_policy_no_native_text_ocr_quality_eval_plan_v0" in surface
        assert "source_policy_no_native_text_ocr_quality_reference_pack_v0" in surface

    for boundary in [
        "not OCR quality evidence",
        "not robust PDF extraction evidence",
        "not arbitrary-market PDF parsing evidence",
        "not rendered visual fidelity evidence",
        "not image/chart interpretation evidence",
        "not external reviewer feedback",
        "not product-complete",
    ]:
        assert boundary in surfaces[0]
