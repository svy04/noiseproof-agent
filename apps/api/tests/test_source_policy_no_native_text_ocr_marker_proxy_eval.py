import json
import subprocess
import sys
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[3]
REFERENCE_PACK_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/source-policy-no-native-text-ocr-quality-reference-pack.json"
)
SMOKE_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/source-policy-no-native-text-ocr-execution-smoke.json"
)
EVAL_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/source-policy-no-native-text-ocr-marker-proxy-eval.json"
)
REPORT_PATH = (
    REPO_ROOT
    / "docs/evaluation/source-policy-no-native-text-ocr-marker-proxy-eval-report.md"
)
REVIEW_PATH = REPO_ROOT / "docs/review/source-policy-no-native-text-ocr-marker-proxy-eval.md"
SPEC_PATH = (
    REPO_ROOT
    / "docs/specs/2026-07-01-source-policy-no-native-text-ocr-marker-proxy-eval.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.source_policy_no_native_text_ocr_marker_proxy_eval import (  # noqa: E402
    NEXT_GATE,
    PHASE_MARKER,
    PREVIOUS_GATE,
    build_source_policy_no_native_text_ocr_marker_proxy_eval,
    build_source_policy_no_native_text_ocr_marker_proxy_eval_report,
    build_source_policy_no_native_text_ocr_marker_proxy_eval_summary,
    load_source_policy_no_native_text_ocr_marker_proxy_eval,
    validate_source_policy_no_native_text_ocr_marker_proxy_eval,
)


def test_source_policy_no_native_text_ocr_marker_proxy_eval_commits_sanitized_proxy_result():
    marker_eval = load_source_policy_no_native_text_ocr_marker_proxy_eval(EVAL_PATH)
    summary = build_source_policy_no_native_text_ocr_marker_proxy_eval_summary(
        marker_eval
    )

    assert summary["phase_marker"] == PHASE_MARKER
    assert summary["previous_gate"] == PREVIOUS_GATE
    assert summary["eval_status"] == "marker_proxy_eval_completed"
    assert summary["target_fixture_id"] == "nara_911_mfr_00282_no_native_text_candidate"
    assert summary["source_sha256"] == (
        "6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba"
    )
    assert summary["reference_unit_type"] == "marker_anchor"
    assert summary["expected_marker_anchor_count"] == 2
    assert summary["observed_marker_hit_count"] == 2
    assert summary["missing_marker_anchor_count"] == 0
    assert summary["marker_proxy_hit_rate"] == 1.0
    assert summary["marker_proxy_threshold"] == 1.0
    assert summary["marker_proxy_passed"] is True
    assert summary["observed_marker_hits"] == {"commission": True, "mfr": True}
    assert summary["missing_marker_anchors"] == []
    assert summary["quality_eval_performed"] is False
    assert summary["cer_computed"] is False
    assert summary["wer_computed"] is False
    assert summary["raw_reference_text_committed"] is False
    assert summary["raw_ocr_text_committed"] is False
    assert summary["can_claim_marker_proxy_eval"] is True
    assert summary["can_claim_ocr_quality"] is False
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["next_gate"] == NEXT_GATE


def test_source_policy_no_native_text_ocr_marker_proxy_eval_builds_from_reference_pack_and_smoke():
    reference_pack = json.loads(REFERENCE_PACK_PATH.read_text(encoding="utf-8"))
    smoke = json.loads(SMOKE_PATH.read_text(encoding="utf-8"))

    marker_eval = build_source_policy_no_native_text_ocr_marker_proxy_eval(
        reference_pack,
        smoke,
    )

    assert marker_eval["phase_marker"] == PHASE_MARKER
    assert marker_eval["previous_gate"] == PREVIOUS_GATE
    assert marker_eval["reference_pack_phase_marker"] == PREVIOUS_GATE
    assert marker_eval["ocr_execution_smoke_phase_marker"] == (
        "source_policy_no_native_text_ocr_execution_smoke_v0"
    )
    assert marker_eval["eval_status"] == "marker_proxy_eval_completed"
    assert marker_eval["expected_marker_anchor_count"] == 2
    assert marker_eval["observed_marker_hit_count"] == 2
    assert marker_eval["missing_marker_anchor_count"] == 0
    assert marker_eval["marker_proxy_hit_rate"] == 1.0
    assert marker_eval["marker_proxy_passed"] is True
    assert marker_eval["quality_eval_performed"] is False
    assert marker_eval["recommended_next_gate"] == NEXT_GATE


def test_source_policy_no_native_text_ocr_marker_proxy_eval_report_is_current_and_bounded():
    marker_eval = load_source_policy_no_native_text_ocr_marker_proxy_eval(EVAL_PATH)
    summary = build_source_policy_no_native_text_ocr_marker_proxy_eval_summary(
        marker_eval
    )
    report = build_source_policy_no_native_text_ocr_marker_proxy_eval_report(summary)

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Source-policy No-native-text OCR Marker Proxy Eval" in report
    assert "source_policy_no_native_text_ocr_marker_proxy_eval_v0" in report
    assert "previous_gate -> source_policy_no_native_text_ocr_quality_reference_pack_v0" in report
    assert "eval_status -> marker_proxy_eval_completed" in report
    assert "observed_marker_hit_count -> 2" in report
    assert "missing_marker_anchor_count -> 0" in report
    assert "marker_proxy_hit_rate -> 1.0" in report
    assert "marker_proxy_passed -> true" in report
    assert "quality_eval_performed -> false" in report
    assert "cer_computed -> false" in report
    assert "wer_computed -> false" in report
    assert "can_claim_marker_proxy_eval -> true" in report
    assert "can_claim_ocr_quality -> false" in report
    assert "source_policy_no_native_text_ocr_transcript_reference_plan_v0" in report
    assert "not OCR quality evidence" in report
    assert "not robust PDF extraction evidence" in report


def test_source_policy_no_native_text_ocr_marker_proxy_eval_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.source_policy_no_native_text_ocr_marker_proxy_eval_command",
            "--marker-proxy-eval",
            str(EVAL_PATH),
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
    assert "source_policy_no_native_text_ocr_marker_proxy_eval_report_current" in result.stdout
    assert "can_claim_marker_proxy_eval=true" in result.stdout
    assert "can_claim_ocr_quality=false" in result.stdout
    assert "can_claim_robust_pdf_extraction=false" in result.stdout


def test_source_policy_no_native_text_ocr_marker_proxy_eval_rejects_quality_or_raw_text_claims(
    tmp_path,
):
    marker_eval = load_source_policy_no_native_text_ocr_marker_proxy_eval(EVAL_PATH)

    quality_eval = dict(marker_eval)
    quality_eval["quality_eval_performed"] = True
    with pytest.raises(ValueError, match="quality_eval_performed"):
        validate_source_policy_no_native_text_ocr_marker_proxy_eval(quality_eval)

    cer_eval = dict(marker_eval)
    cer_eval["cer_computed"] = True
    with pytest.raises(ValueError, match="cer_computed"):
        validate_source_policy_no_native_text_ocr_marker_proxy_eval(cer_eval)

    miss_eval = dict(marker_eval)
    miss_eval["missing_marker_anchor_count"] = 1
    with pytest.raises(ValueError, match="missing_marker_anchor_count"):
        validate_source_policy_no_native_text_ocr_marker_proxy_eval(miss_eval)

    raw_eval = dict(marker_eval)
    raw_eval["raw_ocr_text"] = "forbidden"
    raw_path = tmp_path / "raw-ocr.json"
    raw_path.write_text(json.dumps(raw_eval), encoding="utf-8")
    with pytest.raises(ValueError, match="raw_ocr_text"):
        load_source_policy_no_native_text_ocr_marker_proxy_eval(raw_path)


def test_source_policy_no_native_text_ocr_marker_proxy_eval_artifacts_are_sanitized():
    artifacts = [
        EVAL_PATH,
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


def test_source_policy_no_native_text_ocr_marker_proxy_eval_docs_and_surfaces_are_linked():
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
        assert "source_policy_no_native_text_ocr_marker_proxy_eval_v0" in surface
        assert "source_policy_no_native_text_ocr_transcript_reference_plan_v0" in surface

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
