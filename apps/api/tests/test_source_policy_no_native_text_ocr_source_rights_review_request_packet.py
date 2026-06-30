import json
import subprocess
import sys
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[3]
COLLECTION_PLAN_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/source-policy-no-native-text-ocr-owner-transcript-collection-plan.json"
)
PACKET_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/source-policy-no-native-text-ocr-source-rights-review-request-packet.json"
)
REPORT_PATH = (
    REPO_ROOT
    / "docs/evaluation/source-policy-no-native-text-ocr-source-rights-review-request-packet-report.md"
)
REVIEW_PATH = (
    REPO_ROOT
    / "docs/review/source-policy-no-native-text-ocr-source-rights-review-request-packet.md"
)
SPEC_PATH = (
    REPO_ROOT
    / "docs/specs/2026-07-01-source-policy-no-native-text-ocr-source-rights-review-request-packet.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.source_policy_no_native_text_ocr_source_rights_review_request_packet import (  # noqa: E402
    NEXT_GATE,
    PHASE_MARKER,
    PREVIOUS_GATE,
    build_source_policy_no_native_text_ocr_source_rights_review_request_packet,
    build_source_policy_no_native_text_ocr_source_rights_review_request_packet_report,
    build_source_policy_no_native_text_ocr_source_rights_review_request_packet_summary,
    load_source_policy_no_native_text_ocr_source_rights_review_request_packet,
    validate_source_policy_no_native_text_ocr_source_rights_review_request_packet,
)


def test_source_rights_review_request_packet_commits_only_request_packet():
    packet = load_source_policy_no_native_text_ocr_source_rights_review_request_packet(
        PACKET_PATH
    )
    summary = (
        build_source_policy_no_native_text_ocr_source_rights_review_request_packet_summary(
            packet
        )
    )

    assert summary["phase_marker"] == PHASE_MARKER
    assert summary["previous_gate"] == PREVIOUS_GATE
    assert summary["packet_status"] == "source_rights_review_request_packet_prepared"
    assert summary["target_fixture_id"] == "nara_911_mfr_00282_no_native_text_candidate"
    assert summary["source_sha256"] == (
        "6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba"
    )
    assert summary["owner_transcript_collection_plan_phase_marker"] == PREVIOUS_GATE
    assert summary["request_scope"] == "rights_review_request_only"
    assert summary["request_questions"] == [
        "does_item_have_known_copyright_or_access_restrictions",
        "may_owner_create_manual_reference_transcript_for_internal_ocr_quality_eval",
        "may_reference_transcript_text_be_committed_publicly",
        "may_reference_transcript_hash_or_page_level_metadata_be_committed_publicly",
        "what_attribution_or_restriction_notice_is_required",
    ]
    assert summary["request_question_count"] == 5
    assert summary["proposed_use_scope"] == (
        "internal_owner_runtime_reference_transcript_for_ocr_quality_eval"
    )
    assert summary["material_requested_for_review"] == [
        "source_url",
        "source_policy_url",
        "source_sha256",
        "target_page_count",
        "proposed_repository_commit_policy",
    ]
    assert summary["material_requested_for_review_count"] == 5
    assert summary["repository_commit_policy"] == (
        "metadata_only_no_transcript_text_or_hash"
    )
    assert summary["request_packet_prepared"] is True
    assert summary["request_sent"] is False
    assert summary["rights_response_received"] is False
    assert summary["source_rights_owner_approval_recorded"] is False
    assert summary["source_rights_decision_recorded"] is False
    assert summary["transcript_collection_performed"] is False
    assert summary["reference_text_available"] is False
    assert summary["reference_text_commit_allowed"] is False
    assert summary["transcript_hash_committed"] is False
    assert summary["quality_eval_performed"] is False
    assert summary["cer_computed"] is False
    assert summary["wer_computed"] is False
    assert summary["metric_candidates"] == ["cer", "wer"]
    assert summary["metric_candidates_status"] == (
        "blocked_until_rights_decision_and_reference_text_exist"
    )
    assert summary["raw_reference_text_committed"] is False
    assert summary["raw_ocr_text_committed"] is False
    assert summary["can_claim_source_rights_review_request_packet"] is True
    assert summary["can_claim_rights_clearance"] is False
    assert summary["can_claim_transcript_collection"] is False
    assert summary["can_claim_reference_transcript_available"] is False
    assert summary["can_claim_ocr_quality"] is False
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["next_gate"] == NEXT_GATE


def test_source_rights_review_request_packet_builds_from_collection_plan():
    collection_plan = json.loads(COLLECTION_PLAN_PATH.read_text(encoding="utf-8"))

    packet = build_source_policy_no_native_text_ocr_source_rights_review_request_packet(
        collection_plan
    )

    assert packet["phase_marker"] == PHASE_MARKER
    assert packet["previous_gate"] == PREVIOUS_GATE
    assert packet["owner_transcript_collection_plan_phase_marker"] == PREVIOUS_GATE
    assert packet["packet_status"] == "source_rights_review_request_packet_prepared"
    assert packet["request_packet_prepared"] is True
    assert packet["request_sent"] is False
    assert packet["rights_response_received"] is False
    assert packet["source_rights_owner_approval_recorded"] is False
    assert packet["transcript_collection_performed"] is False
    assert packet["reference_text_available"] is False
    assert packet["quality_eval_performed"] is False
    assert packet["recommended_next_gate"] == NEXT_GATE


def test_source_rights_review_request_packet_report_is_current_and_bounded():
    packet = load_source_policy_no_native_text_ocr_source_rights_review_request_packet(
        PACKET_PATH
    )
    summary = (
        build_source_policy_no_native_text_ocr_source_rights_review_request_packet_summary(
            packet
        )
    )
    report = (
        build_source_policy_no_native_text_ocr_source_rights_review_request_packet_report(
            summary
        )
    )

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Source-policy No-native-text OCR Source Rights Review Request Packet" in report
    assert "source_policy_no_native_text_ocr_source_rights_review_request_packet_v0" in report
    assert "previous_gate -> source_policy_no_native_text_ocr_owner_transcript_collection_plan_v0" in report
    assert "packet_status -> source_rights_review_request_packet_prepared" in report
    assert "request_sent -> false" in report
    assert "rights_response_received -> false" in report
    assert "source_rights_owner_approval_recorded -> false" in report
    assert "source_rights_decision_recorded -> false" in report
    assert "transcript_collection_performed -> false" in report
    assert "reference_text_available -> false" in report
    assert "transcript_hash_committed -> false" in report
    assert "quality_eval_performed -> false" in report
    assert "cer_computed -> false" in report
    assert "wer_computed -> false" in report
    assert "can_claim_source_rights_review_request_packet -> true" in report
    assert "can_claim_rights_clearance -> false" in report
    assert "can_claim_transcript_collection -> false" in report
    assert "can_claim_reference_transcript_available -> false" in report
    assert "can_claim_ocr_quality -> false" in report
    assert "source_policy_no_native_text_ocr_owner_rights_decision_record_v0" in report
    assert "not rights clearance evidence" in report
    assert "not request-sent evidence" in report
    assert "not source-rights approval evidence" in report
    assert "not transcript collection evidence" in report
    assert "not reference transcript availability" in report
    assert "not OCR quality evidence" in report
    assert "not CER/WER support" in report
    assert "not robust PDF extraction evidence" in report


def test_source_rights_review_request_packet_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.source_policy_no_native_text_ocr_source_rights_review_request_packet_command",
            "--source-rights-review-request-packet",
            str(PACKET_PATH),
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
        "source_policy_no_native_text_ocr_source_rights_review_request_packet_report_current"
        in result.stdout
    )
    assert "can_claim_source_rights_review_request_packet=true" in result.stdout
    assert "can_claim_rights_clearance=false" in result.stdout
    assert "can_claim_transcript_collection=false" in result.stdout
    assert "can_claim_reference_transcript_available=false" in result.stdout
    assert "can_claim_ocr_quality=false" in result.stdout
    assert "can_claim_robust_pdf_extraction=false" in result.stdout


def test_source_rights_review_request_packet_rejects_clearance_or_collection_overclaims(
    tmp_path,
):
    packet = load_source_policy_no_native_text_ocr_source_rights_review_request_packet(
        PACKET_PATH
    )

    sent_packet = dict(packet)
    sent_packet["request_sent"] = True
    with pytest.raises(ValueError, match="request_sent"):
        validate_source_policy_no_native_text_ocr_source_rights_review_request_packet(
            sent_packet
        )

    response_packet = dict(packet)
    response_packet["rights_response_received"] = True
    with pytest.raises(ValueError, match="rights_response_received"):
        validate_source_policy_no_native_text_ocr_source_rights_review_request_packet(
            response_packet
        )

    rights_packet = dict(packet)
    rights_packet["source_rights_owner_approval_recorded"] = True
    with pytest.raises(ValueError, match="source_rights_owner_approval_recorded"):
        validate_source_policy_no_native_text_ocr_source_rights_review_request_packet(
            rights_packet
        )

    transcript_packet = dict(packet)
    transcript_packet["reference_text_available"] = True
    with pytest.raises(ValueError, match="reference_text_available"):
        validate_source_policy_no_native_text_ocr_source_rights_review_request_packet(
            transcript_packet
        )

    hash_packet = dict(packet)
    hash_packet["transcript_hash_committed"] = True
    with pytest.raises(ValueError, match="transcript_hash_committed"):
        validate_source_policy_no_native_text_ocr_source_rights_review_request_packet(
            hash_packet
        )

    raw_packet = dict(packet)
    raw_packet["reference_text"] = "forbidden"
    raw_path = tmp_path / "raw-reference.json"
    raw_path.write_text(json.dumps(raw_packet), encoding="utf-8")
    with pytest.raises(ValueError, match="reference_text"):
        load_source_policy_no_native_text_ocr_source_rights_review_request_packet(
            raw_path
        )


def test_source_rights_review_request_packet_artifacts_are_sanitized():
    artifacts = [
        PACKET_PATH,
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


def test_source_rights_review_request_packet_docs_and_surfaces_are_linked():
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
            "source_policy_no_native_text_ocr_source_rights_review_request_packet_v0"
            in surface
        )
        assert (
            "source_policy_no_native_text_ocr_owner_rights_decision_record_v0"
            in surface
        )

    for boundary in [
        "not rights clearance evidence",
        "not request-sent evidence",
        "not source-rights approval evidence",
        "not transcript collection evidence",
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
