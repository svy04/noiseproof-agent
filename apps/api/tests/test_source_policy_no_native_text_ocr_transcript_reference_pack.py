import json
import subprocess
import sys
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[3]
PLAN_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/source-policy-no-native-text-ocr-transcript-reference-plan.json"
)
PACK_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/source-policy-no-native-text-ocr-transcript-reference-pack.json"
)
REPORT_PATH = (
    REPO_ROOT
    / "docs/evaluation/source-policy-no-native-text-ocr-transcript-reference-pack-report.md"
)
REVIEW_PATH = (
    REPO_ROOT / "docs/review/source-policy-no-native-text-ocr-transcript-reference-pack.md"
)
SPEC_PATH = (
    REPO_ROOT
    / "docs/specs/2026-07-01-source-policy-no-native-text-ocr-transcript-reference-pack.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.source_policy_no_native_text_ocr_transcript_reference_pack import (  # noqa: E402
    NEXT_GATE,
    PHASE_MARKER,
    PREVIOUS_GATE,
    build_source_policy_no_native_text_ocr_transcript_reference_pack,
    build_source_policy_no_native_text_ocr_transcript_reference_pack_report,
    build_source_policy_no_native_text_ocr_transcript_reference_pack_summary,
    load_source_policy_no_native_text_ocr_transcript_reference_pack,
    validate_source_policy_no_native_text_ocr_transcript_reference_pack,
)


def test_source_policy_no_native_text_ocr_transcript_reference_pack_commits_sanitized_boundary():
    pack = load_source_policy_no_native_text_ocr_transcript_reference_pack(PACK_PATH)
    summary = build_source_policy_no_native_text_ocr_transcript_reference_pack_summary(
        pack
    )

    assert summary["phase_marker"] == PHASE_MARKER
    assert summary["previous_gate"] == PREVIOUS_GATE
    assert summary["reference_pack_status"] == (
        "sanitized_transcript_reference_pack_boundary"
    )
    assert summary["target_fixture_id"] == "nara_911_mfr_00282_no_native_text_candidate"
    assert summary["source_sha256"] == (
        "6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba"
    )
    assert summary["transcript_reference_plan_phase_marker"] == PREVIOUS_GATE
    assert summary["reference_unit_type"] == (
        "page_level_transcript_reference_pack_boundary"
    )
    assert summary["target_page_count"] == 4
    assert summary["planned_reference_page_count"] == 4
    assert summary["required_reference_unit_count"] == 6
    assert summary["required_reference_units"] == [
        "source_policy_review",
        "owner_approval",
        "page_level_reference_transcript",
        "normalization_rules",
        "alignment_policy",
        "metric_eligibility_review",
    ]
    assert summary["reference_pack_created"] is True
    assert summary["reference_pack_claim_scope"] == "sanitized_boundary_only"
    assert summary["source_policy_review_status"] == "reviewed_for_metadata_only"
    assert summary["project_owner_approval_recorded"] is True
    assert summary["source_rights_owner_approval_recorded"] is False
    assert summary["source_rights_owner_approval_required_before_transcript"] is True
    assert summary["reference_text_available"] is False
    assert summary["full_reference_transcript_available"] is False
    assert summary["transcript_collection_performed"] is False
    assert summary["transcript_hash_committed"] is False
    assert summary["reference_text_hash_committed"] is False
    assert summary["quality_eval_performed"] is False
    assert summary["cer_computed"] is False
    assert summary["wer_computed"] is False
    assert summary["metric_candidates"] == ["cer", "wer"]
    assert summary["metric_candidates_status"] == (
        "blocked_until_reference_text_exists"
    )
    assert summary["raw_reference_text_committed"] is False
    assert summary["raw_ocr_text_committed"] is False
    assert summary["can_claim_transcript_reference_pack"] is True
    assert summary["can_claim_reference_transcript_available"] is False
    assert summary["can_claim_ocr_quality"] is False
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["next_gate"] == NEXT_GATE


def test_source_policy_no_native_text_ocr_transcript_reference_pack_builds_from_plan():
    plan = json.loads(PLAN_PATH.read_text(encoding="utf-8"))

    pack = build_source_policy_no_native_text_ocr_transcript_reference_pack(plan)

    assert pack["phase_marker"] == PHASE_MARKER
    assert pack["previous_gate"] == PREVIOUS_GATE
    assert pack["transcript_reference_plan_phase_marker"] == PREVIOUS_GATE
    assert pack["reference_pack_status"] == (
        "sanitized_transcript_reference_pack_boundary"
    )
    assert pack["reference_pack_created"] is True
    assert pack["reference_text_available"] is False
    assert pack["full_reference_transcript_available"] is False
    assert pack["quality_eval_performed"] is False
    assert pack["recommended_next_gate"] == NEXT_GATE


def test_source_policy_no_native_text_ocr_transcript_reference_pack_report_is_current_and_bounded():
    pack = load_source_policy_no_native_text_ocr_transcript_reference_pack(PACK_PATH)
    summary = build_source_policy_no_native_text_ocr_transcript_reference_pack_summary(
        pack
    )
    report = build_source_policy_no_native_text_ocr_transcript_reference_pack_report(
        summary
    )

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Source-policy No-native-text OCR Transcript Reference Pack" in report
    assert "source_policy_no_native_text_ocr_transcript_reference_pack_v0" in report
    assert "previous_gate -> source_policy_no_native_text_ocr_transcript_reference_plan_v0" in report
    assert "reference_pack_status -> sanitized_transcript_reference_pack_boundary" in report
    assert "reference_pack_claim_scope -> sanitized_boundary_only" in report
    assert "reference_text_available -> false" in report
    assert "full_reference_transcript_available -> false" in report
    assert "transcript_collection_performed -> false" in report
    assert "quality_eval_performed -> false" in report
    assert "cer_computed -> false" in report
    assert "wer_computed -> false" in report
    assert "can_claim_transcript_reference_pack -> true" in report
    assert "can_claim_reference_transcript_available -> false" in report
    assert "can_claim_ocr_quality -> false" in report
    assert "source_policy_no_native_text_ocr_owner_transcript_collection_plan_v0" in report
    assert "not reference transcript availability" in report
    assert "not OCR quality evidence" in report
    assert "not CER/WER support" in report
    assert "not robust PDF extraction evidence" in report


def test_source_policy_no_native_text_ocr_transcript_reference_pack_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.source_policy_no_native_text_ocr_transcript_reference_pack_command",
            "--transcript-reference-pack",
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
    assert (
        "source_policy_no_native_text_ocr_transcript_reference_pack_report_current"
        in result.stdout
    )
    assert "can_claim_transcript_reference_pack=true" in result.stdout
    assert "can_claim_reference_transcript_available=false" in result.stdout
    assert "can_claim_ocr_quality=false" in result.stdout
    assert "can_claim_robust_pdf_extraction=false" in result.stdout


def test_source_policy_no_native_text_ocr_transcript_reference_pack_rejects_transcript_or_quality_overclaims(
    tmp_path,
):
    pack = load_source_policy_no_native_text_ocr_transcript_reference_pack(PACK_PATH)

    transcript_pack = dict(pack)
    transcript_pack["reference_text_available"] = True
    with pytest.raises(ValueError, match="reference_text_available"):
        validate_source_policy_no_native_text_ocr_transcript_reference_pack(
            transcript_pack
        )

    reference_pack = dict(pack)
    reference_pack["full_reference_transcript_available"] = True
    with pytest.raises(ValueError, match="full_reference_transcript_available"):
        validate_source_policy_no_native_text_ocr_transcript_reference_pack(
            reference_pack
        )

    quality_pack = dict(pack)
    quality_pack["quality_eval_performed"] = True
    with pytest.raises(ValueError, match="quality_eval_performed"):
        validate_source_policy_no_native_text_ocr_transcript_reference_pack(
            quality_pack
        )

    cer_pack = dict(pack)
    cer_pack["cer_computed"] = True
    with pytest.raises(ValueError, match="cer_computed"):
        validate_source_policy_no_native_text_ocr_transcript_reference_pack(cer_pack)

    raw_pack = dict(pack)
    raw_pack["reference_text"] = "forbidden"
    raw_path = tmp_path / "raw-reference.json"
    raw_path.write_text(json.dumps(raw_pack), encoding="utf-8")
    with pytest.raises(ValueError, match="reference_text"):
        load_source_policy_no_native_text_ocr_transcript_reference_pack(raw_path)


def test_source_policy_no_native_text_ocr_transcript_reference_pack_artifacts_are_sanitized():
    artifacts = [
        PACK_PATH,
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


def test_source_policy_no_native_text_ocr_transcript_reference_pack_docs_and_surfaces_are_linked():
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
        assert "source_policy_no_native_text_ocr_transcript_reference_pack_v0" in surface
        assert (
            "source_policy_no_native_text_ocr_owner_transcript_collection_plan_v0"
            in surface
        )

    for boundary in [
        "not reference transcript availability",
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
