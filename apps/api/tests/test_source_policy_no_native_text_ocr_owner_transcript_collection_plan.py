import json
import subprocess
import sys
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[3]
PACK_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/source-policy-no-native-text-ocr-transcript-reference-pack.json"
)
PLAN_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/source-policy-no-native-text-ocr-owner-transcript-collection-plan.json"
)
REPORT_PATH = (
    REPO_ROOT
    / "docs/evaluation/source-policy-no-native-text-ocr-owner-transcript-collection-plan-report.md"
)
REVIEW_PATH = (
    REPO_ROOT
    / "docs/review/source-policy-no-native-text-ocr-owner-transcript-collection-plan.md"
)
SPEC_PATH = (
    REPO_ROOT
    / "docs/specs/2026-07-01-source-policy-no-native-text-ocr-owner-transcript-collection-plan.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.source_policy_no_native_text_ocr_owner_transcript_collection_plan import (  # noqa: E402
    NEXT_GATE,
    PHASE_MARKER,
    PREVIOUS_GATE,
    build_source_policy_no_native_text_ocr_owner_transcript_collection_plan,
    build_source_policy_no_native_text_ocr_owner_transcript_collection_plan_report,
    build_source_policy_no_native_text_ocr_owner_transcript_collection_plan_summary,
    load_source_policy_no_native_text_ocr_owner_transcript_collection_plan,
    validate_source_policy_no_native_text_ocr_owner_transcript_collection_plan,
)


def test_owner_transcript_collection_plan_commits_only_collection_plan():
    plan = load_source_policy_no_native_text_ocr_owner_transcript_collection_plan(
        PLAN_PATH
    )
    summary = (
        build_source_policy_no_native_text_ocr_owner_transcript_collection_plan_summary(
            plan
        )
    )

    assert summary["phase_marker"] == PHASE_MARKER
    assert summary["previous_gate"] == PREVIOUS_GATE
    assert summary["plan_status"] == "owner_transcript_collection_planned"
    assert summary["target_fixture_id"] == "nara_911_mfr_00282_no_native_text_candidate"
    assert summary["source_sha256"] == (
        "6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba"
    )
    assert summary["transcript_reference_pack_phase_marker"] == PREVIOUS_GATE
    assert summary["collection_scope"] == (
        "owner_runtime_manual_transcript_collection_plan_only"
    )
    assert summary["target_page_count"] == 4
    assert summary["planned_reference_page_count"] == 4
    assert summary["planned_collection_step_count"] == 7
    assert summary["planned_collection_steps"] == [
        "confirm_item_specific_rights_status",
        "prepare_owner_runtime_workspace",
        "create_page_level_manual_reference_transcript_outside_repo",
        "apply_normalization_rules",
        "record_alignment_policy",
        "review_metric_eligibility",
        "decide_commit_or_hash_policy_after_rights_review",
    ]
    assert summary["source_policy_review_status"] == "metadata_review_only"
    assert summary["source_rights_review_required"] is True
    assert summary["source_rights_owner_approval_recorded"] is False
    assert summary["source_rights_request_packet_required"] is True
    assert summary["owner_runtime_storage_required"] is True
    assert summary["repository_commit_policy"] == (
        "metadata_only_no_transcript_text_or_hash"
    )
    assert summary["transcript_collection_performed"] is False
    assert summary["reference_text_available"] is False
    assert summary["full_reference_transcript_available"] is False
    assert summary["reference_text_commit_allowed"] is False
    assert summary["transcript_hash_committed"] is False
    assert summary["reference_text_hash_committed"] is False
    assert summary["quality_eval_performed"] is False
    assert summary["cer_computed"] is False
    assert summary["wer_computed"] is False
    assert summary["metric_candidates"] == ["cer", "wer"]
    assert summary["metric_candidates_status"] == (
        "blocked_until_reference_text_and_rights_review_exist"
    )
    assert summary["raw_reference_text_committed"] is False
    assert summary["raw_ocr_text_committed"] is False
    assert summary["can_claim_owner_transcript_collection_plan"] is True
    assert summary["can_claim_transcript_collection"] is False
    assert summary["can_claim_reference_transcript_available"] is False
    assert summary["can_claim_ocr_quality"] is False
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["next_gate"] == NEXT_GATE


def test_owner_transcript_collection_plan_builds_from_transcript_reference_pack():
    pack = json.loads(PACK_PATH.read_text(encoding="utf-8"))

    plan = build_source_policy_no_native_text_ocr_owner_transcript_collection_plan(
        pack
    )

    assert plan["phase_marker"] == PHASE_MARKER
    assert plan["previous_gate"] == PREVIOUS_GATE
    assert plan["transcript_reference_pack_phase_marker"] == PREVIOUS_GATE
    assert plan["plan_status"] == "owner_transcript_collection_planned"
    assert plan["source_rights_review_required"] is True
    assert plan["source_rights_owner_approval_recorded"] is False
    assert plan["transcript_collection_performed"] is False
    assert plan["reference_text_available"] is False
    assert plan["quality_eval_performed"] is False
    assert plan["recommended_next_gate"] == NEXT_GATE


def test_owner_transcript_collection_plan_report_is_current_and_bounded():
    plan = load_source_policy_no_native_text_ocr_owner_transcript_collection_plan(
        PLAN_PATH
    )
    summary = (
        build_source_policy_no_native_text_ocr_owner_transcript_collection_plan_summary(
            plan
        )
    )
    report = (
        build_source_policy_no_native_text_ocr_owner_transcript_collection_plan_report(
            summary
        )
    )

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Source-policy No-native-text OCR Owner Transcript Collection Plan" in report
    assert "source_policy_no_native_text_ocr_owner_transcript_collection_plan_v0" in report
    assert "previous_gate -> source_policy_no_native_text_ocr_transcript_reference_pack_v0" in report
    assert "plan_status -> owner_transcript_collection_planned" in report
    assert "source_rights_review_required -> true" in report
    assert "source_rights_owner_approval_recorded -> false" in report
    assert "repository_commit_policy -> metadata_only_no_transcript_text_or_hash" in report
    assert "transcript_collection_performed -> false" in report
    assert "reference_text_available -> false" in report
    assert "transcript_hash_committed -> false" in report
    assert "quality_eval_performed -> false" in report
    assert "cer_computed -> false" in report
    assert "wer_computed -> false" in report
    assert "can_claim_owner_transcript_collection_plan -> true" in report
    assert "can_claim_transcript_collection -> false" in report
    assert "can_claim_reference_transcript_available -> false" in report
    assert "can_claim_ocr_quality -> false" in report
    assert "source_policy_no_native_text_ocr_source_rights_review_request_packet_v0" in report
    assert "not transcript collection evidence" in report
    assert "not source-rights approval evidence" in report
    assert "not reference transcript availability" in report
    assert "not OCR quality evidence" in report
    assert "not CER/WER support" in report
    assert "not robust PDF extraction evidence" in report


def test_owner_transcript_collection_plan_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.source_policy_no_native_text_ocr_owner_transcript_collection_plan_command",
            "--owner-transcript-collection-plan",
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
        "source_policy_no_native_text_ocr_owner_transcript_collection_plan_report_current"
        in result.stdout
    )
    assert "can_claim_owner_transcript_collection_plan=true" in result.stdout
    assert "can_claim_transcript_collection=false" in result.stdout
    assert "can_claim_reference_transcript_available=false" in result.stdout
    assert "can_claim_ocr_quality=false" in result.stdout
    assert "can_claim_robust_pdf_extraction=false" in result.stdout


def test_owner_transcript_collection_plan_rejects_collection_or_approval_overclaims(
    tmp_path,
):
    plan = load_source_policy_no_native_text_ocr_owner_transcript_collection_plan(
        PLAN_PATH
    )

    collected_plan = dict(plan)
    collected_plan["transcript_collection_performed"] = True
    with pytest.raises(ValueError, match="transcript_collection_performed"):
        validate_source_policy_no_native_text_ocr_owner_transcript_collection_plan(
            collected_plan
        )

    rights_plan = dict(plan)
    rights_plan["source_rights_owner_approval_recorded"] = True
    with pytest.raises(ValueError, match="source_rights_owner_approval_recorded"):
        validate_source_policy_no_native_text_ocr_owner_transcript_collection_plan(
            rights_plan
        )

    transcript_plan = dict(plan)
    transcript_plan["reference_text_available"] = True
    with pytest.raises(ValueError, match="reference_text_available"):
        validate_source_policy_no_native_text_ocr_owner_transcript_collection_plan(
            transcript_plan
        )

    hash_plan = dict(plan)
    hash_plan["transcript_hash_committed"] = True
    with pytest.raises(ValueError, match="transcript_hash_committed"):
        validate_source_policy_no_native_text_ocr_owner_transcript_collection_plan(
            hash_plan
        )

    raw_plan = dict(plan)
    raw_plan["reference_text"] = "forbidden"
    raw_path = tmp_path / "raw-reference.json"
    raw_path.write_text(json.dumps(raw_plan), encoding="utf-8")
    with pytest.raises(ValueError, match="reference_text"):
        load_source_policy_no_native_text_ocr_owner_transcript_collection_plan(
            raw_path
        )


def test_owner_transcript_collection_plan_artifacts_are_sanitized():
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
        "transcript_hash:",
    ]

    for artifact in artifacts:
        text = artifact.read_text(encoding="utf-8")
        for marker in forbidden:
            assert marker not in text


def test_owner_transcript_collection_plan_docs_and_surfaces_are_linked():
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
        assert (
            "source_policy_no_native_text_ocr_owner_transcript_collection_plan_v0"
            in surface
        )
        assert (
            "source_policy_no_native_text_ocr_source_rights_review_request_packet_v0"
            in surface
        )

    for boundary in [
        "not transcript collection evidence",
        "not source-rights approval evidence",
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
