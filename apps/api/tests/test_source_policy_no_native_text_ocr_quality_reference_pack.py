import json
import subprocess
import sys
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[3]
PLAN_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/source-policy-no-native-text-ocr-quality-eval-plan.json"
)
REFERENCE_PACK_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/source-policy-no-native-text-ocr-quality-reference-pack.json"
)
REPORT_PATH = (
    REPO_ROOT
    / "docs/evaluation/source-policy-no-native-text-ocr-quality-reference-pack-report.md"
)
REVIEW_PATH = (
    REPO_ROOT / "docs/review/source-policy-no-native-text-ocr-quality-reference-pack.md"
)
SPEC_PATH = (
    REPO_ROOT
    / "docs/specs/2026-06-30-source-policy-no-native-text-ocr-quality-reference-pack.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.source_policy_no_native_text_ocr_quality_reference_pack import (  # noqa: E402
    NEXT_GATE,
    PHASE_MARKER,
    PREVIOUS_GATE,
    build_source_policy_no_native_text_ocr_quality_reference_pack,
    build_source_policy_no_native_text_ocr_quality_reference_pack_report,
    build_source_policy_no_native_text_ocr_quality_reference_pack_summary,
    load_source_policy_no_native_text_ocr_quality_reference_pack,
    validate_source_policy_no_native_text_ocr_quality_reference_pack,
)


def test_source_policy_no_native_text_ocr_quality_reference_pack_commits_sanitized_marker_anchors():
    reference_pack = load_source_policy_no_native_text_ocr_quality_reference_pack(
        REFERENCE_PACK_PATH
    )
    summary = build_source_policy_no_native_text_ocr_quality_reference_pack_summary(
        reference_pack
    )

    assert summary["phase_marker"] == PHASE_MARKER
    assert summary["previous_gate"] == PREVIOUS_GATE
    assert summary["reference_pack_status"] == "marker_anchor_reference_pack"
    assert summary["target_fixture_id"] == "nara_911_mfr_00282_no_native_text_candidate"
    assert summary["source_sha256"] == (
        "6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba"
    )
    assert summary["source_policy_url"] == (
        "https://www.archives.gov/global-pages/privacy.html"
    )
    assert summary["page_count"] == 4
    assert summary["page_mapping_available"] is True
    assert summary["reference_unit_type"] == "marker_anchor"
    assert summary["accepted_marker_anchor_count"] == 2
    assert summary["accepted_marker_anchors"] == ["commission", "mfr"]
    assert summary["full_reference_transcript_available"] is False
    assert summary["supports_marker_proxy_eval"] is True
    assert summary["supports_cer"] is False
    assert summary["supports_wer"] is False
    assert summary["quality_eval_performed"] is False
    assert summary["raw_reference_text_committed"] is False
    assert summary["raw_ocr_text_committed"] is False
    assert summary["can_claim_reference_pack"] is True
    assert summary["can_claim_ocr_quality"] is False
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["next_gate"] == NEXT_GATE
    assert summary["normalization_rules"]["unicode_normalization"] == "NFC"
    assert summary["normalization_rules"]["casefold"] is True
    assert summary["normalization_rules"]["collapse_internal_whitespace"] is True


def test_source_policy_no_native_text_ocr_quality_reference_pack_builds_from_quality_plan():
    plan = json.loads(PLAN_PATH.read_text(encoding="utf-8"))
    reference_pack = build_source_policy_no_native_text_ocr_quality_reference_pack(
        plan
    )

    assert reference_pack["phase_marker"] == PHASE_MARKER
    assert reference_pack["previous_gate"] == PREVIOUS_GATE
    assert reference_pack["quality_eval_plan_phase_marker"] == PREVIOUS_GATE
    assert reference_pack["reference_pack_status"] == "marker_anchor_reference_pack"
    assert reference_pack["accepted_marker_anchor_count"] == 2
    assert reference_pack["accepted_marker_anchors"] == ["commission", "mfr"]
    assert reference_pack["supports_marker_proxy_eval"] is True
    assert reference_pack["supports_cer"] is False
    assert reference_pack["supports_wer"] is False
    assert reference_pack["quality_eval_performed"] is False
    assert reference_pack["recommended_next_gate"] == NEXT_GATE


def test_source_policy_no_native_text_ocr_quality_reference_pack_report_is_current_and_bounded():
    reference_pack = load_source_policy_no_native_text_ocr_quality_reference_pack(
        REFERENCE_PACK_PATH
    )
    summary = build_source_policy_no_native_text_ocr_quality_reference_pack_summary(
        reference_pack
    )
    report = build_source_policy_no_native_text_ocr_quality_reference_pack_report(
        summary
    )

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Source-policy No-native-text OCR Quality Reference Pack" in report
    assert "source_policy_no_native_text_ocr_quality_reference_pack_v0" in report
    assert "previous_gate -> source_policy_no_native_text_ocr_quality_eval_plan_v0" in report
    assert "reference_pack_status -> marker_anchor_reference_pack" in report
    assert "accepted_marker_anchor_count -> 2" in report
    assert "supports_marker_proxy_eval -> true" in report
    assert "supports_cer -> false" in report
    assert "supports_wer -> false" in report
    assert "quality_eval_performed -> false" in report
    assert "can_claim_reference_pack -> true" in report
    assert "can_claim_ocr_quality -> false" in report
    assert "source_policy_no_native_text_ocr_marker_proxy_eval_v0" in report
    assert "not OCR quality evidence" in report
    assert "not robust PDF extraction evidence" in report


def test_source_policy_no_native_text_ocr_quality_reference_pack_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.source_policy_no_native_text_ocr_quality_reference_pack_command",
            "--reference-pack",
            str(REFERENCE_PACK_PATH),
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
        "source_policy_no_native_text_ocr_quality_reference_pack_report_current"
        in result.stdout
    )
    assert "can_claim_reference_pack=true" in result.stdout
    assert "can_claim_ocr_quality=false" in result.stdout
    assert "can_claim_robust_pdf_extraction=false" in result.stdout


def test_source_policy_no_native_text_ocr_quality_reference_pack_rejects_transcript_or_metric_overclaim(
    tmp_path,
):
    reference_pack = load_source_policy_no_native_text_ocr_quality_reference_pack(
        REFERENCE_PACK_PATH
    )

    cer_pack = dict(reference_pack)
    cer_pack["supports_cer"] = True
    with pytest.raises(ValueError, match="supports_cer"):
        validate_source_policy_no_native_text_ocr_quality_reference_pack(cer_pack)

    quality_pack = dict(reference_pack)
    quality_pack["quality_eval_performed"] = True
    with pytest.raises(ValueError, match="quality_eval_performed"):
        validate_source_policy_no_native_text_ocr_quality_reference_pack(quality_pack)

    transcript_pack = dict(reference_pack)
    transcript_pack["reference_transcript"] = "forbidden"
    transcript_path = tmp_path / "reference-transcript.json"
    transcript_path.write_text(json.dumps(transcript_pack), encoding="utf-8")
    with pytest.raises(ValueError, match="reference_transcript"):
        load_source_policy_no_native_text_ocr_quality_reference_pack(transcript_path)


def test_source_policy_no_native_text_ocr_quality_reference_pack_artifacts_are_sanitized():
    artifacts = [
        REFERENCE_PACK_PATH,
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


def test_source_policy_no_native_text_ocr_quality_reference_pack_docs_and_surfaces_are_linked():
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
        assert "source_policy_no_native_text_ocr_quality_reference_pack_v0" in surface
        assert "source_policy_no_native_text_ocr_marker_proxy_eval_v0" in surface

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
