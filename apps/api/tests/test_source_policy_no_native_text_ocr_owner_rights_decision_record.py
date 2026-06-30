import json
import subprocess
import sys
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[3]
REQUEST_PACKET_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/source-policy-no-native-text-ocr-source-rights-review-request-packet.json"
)
DECISION_RECORD_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/source-policy-no-native-text-ocr-owner-rights-decision-record.json"
)
REPORT_PATH = (
    REPO_ROOT
    / "docs/evaluation/source-policy-no-native-text-ocr-owner-rights-decision-record-report.md"
)
REVIEW_PATH = (
    REPO_ROOT
    / "docs/review/source-policy-no-native-text-ocr-owner-rights-decision-record.md"
)
SPEC_PATH = (
    REPO_ROOT
    / "docs/specs/2026-07-01-source-policy-no-native-text-ocr-owner-rights-decision-record.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.source_policy_no_native_text_ocr_owner_rights_decision_record import (  # noqa: E402
    NEXT_GATE,
    PHASE_MARKER,
    PREVIOUS_GATE,
    build_source_policy_no_native_text_ocr_owner_rights_decision_record,
    build_source_policy_no_native_text_ocr_owner_rights_decision_record_report,
    build_source_policy_no_native_text_ocr_owner_rights_decision_record_summary,
    load_source_policy_no_native_text_ocr_owner_rights_decision_record,
    validate_source_policy_no_native_text_ocr_owner_rights_decision_record,
)


def test_owner_rights_decision_record_commits_only_blocking_decision():
    record = load_source_policy_no_native_text_ocr_owner_rights_decision_record(
        DECISION_RECORD_PATH
    )
    summary = build_source_policy_no_native_text_ocr_owner_rights_decision_record_summary(
        record
    )

    assert summary["phase_marker"] == PHASE_MARKER
    assert summary["previous_gate"] == PREVIOUS_GATE
    assert summary["decision_status"] == (
        "owner_decision_recorded_blocked_pending_source_rights_response"
    )
    assert summary["target_fixture_id"] == "nara_911_mfr_00282_no_native_text_candidate"
    assert summary["source_sha256"] == (
        "6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba"
    )
    assert summary["source_rights_review_request_packet_phase_marker"] == PREVIOUS_GATE
    assert summary["decision_scope"] == "repository_transcript_and_hash_commit_boundary"
    assert summary["owner_decision"] == (
        "do_not_collect_or_commit_transcript_until_source_rights_response_exists"
    )
    assert summary["decision_basis"] == [
        "request_packet_prepared",
        "request_not_sent",
        "no_rights_response_received",
        "no_source_rights_owner_approval_recorded",
        "nara_policy_does_not_guarantee_item_specific_rights_status",
        "ocr_quality_metrics_require_reference_text",
    ]
    assert summary["blocked_actions"] == [
        "collect_reference_transcript",
        "commit_reference_transcript_text",
        "commit_reference_transcript_hash",
        "compute_cer",
        "compute_wer",
        "claim_ocr_quality",
        "claim_robust_pdf_extraction",
    ]
    assert summary["allowed_actions"] == [
        "keep_metadata_only_request_packet",
        "prepare_or_send_owner_runtime_rights_request",
        "record_future_rights_response_metadata",
        "keep_public_claims_blocked",
    ]
    assert summary["request_packet_prepared"] is True
    assert summary["request_sent"] is False
    assert summary["rights_response_received"] is False
    assert summary["source_rights_owner_approval_recorded"] is False
    assert summary["source_rights_owner_decision_recorded"] is False
    assert summary["owner_rights_decision_recorded"] is True
    assert summary["source_rights_request_delivery_needed"] is True
    assert summary["source_rights_request_delivery_performed"] is False
    assert summary["transcript_collection_allowed"] is False
    assert summary["transcript_collection_performed"] is False
    assert summary["reference_text_available"] is False
    assert summary["reference_text_commit_allowed"] is False
    assert summary["transcript_hash_commit_allowed"] is False
    assert summary["transcript_hash_committed"] is False
    assert summary["quality_eval_performed"] is False
    assert summary["cer_computed"] is False
    assert summary["wer_computed"] is False
    assert summary["metric_candidates"] == ["cer", "wer"]
    assert summary["metric_candidates_status"] == (
        "blocked_until_request_sent_rights_response_and_reference_text_exist"
    )
    assert summary["raw_reference_text_committed"] is False
    assert summary["raw_ocr_text_committed"] is False
    assert summary["can_claim_owner_rights_decision_record"] is True
    assert summary["can_claim_rights_clearance"] is False
    assert summary["can_claim_request_sent"] is False
    assert summary["can_claim_source_rights_owner_approval"] is False
    assert summary["can_claim_transcript_collection"] is False
    assert summary["can_claim_reference_transcript_available"] is False
    assert summary["can_claim_ocr_quality"] is False
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["next_gate"] == NEXT_GATE


def test_owner_rights_decision_record_builds_from_request_packet():
    request_packet = json.loads(REQUEST_PACKET_PATH.read_text(encoding="utf-8"))

    record = build_source_policy_no_native_text_ocr_owner_rights_decision_record(
        request_packet
    )

    assert record["phase_marker"] == PHASE_MARKER
    assert record["previous_gate"] == PREVIOUS_GATE
    assert record["source_rights_review_request_packet_phase_marker"] == PREVIOUS_GATE
    assert record["decision_status"] == (
        "owner_decision_recorded_blocked_pending_source_rights_response"
    )
    assert record["owner_rights_decision_recorded"] is True
    assert record["request_sent"] is False
    assert record["rights_response_received"] is False
    assert record["source_rights_owner_approval_recorded"] is False
    assert record["source_rights_request_delivery_needed"] is True
    assert record["source_rights_request_delivery_performed"] is False
    assert record["transcript_collection_allowed"] is False
    assert record["reference_text_available"] is False
    assert record["quality_eval_performed"] is False
    assert record["recommended_next_gate"] == NEXT_GATE


def test_owner_rights_decision_record_report_is_current_and_bounded():
    record = load_source_policy_no_native_text_ocr_owner_rights_decision_record(
        DECISION_RECORD_PATH
    )
    summary = build_source_policy_no_native_text_ocr_owner_rights_decision_record_summary(
        record
    )
    report = build_source_policy_no_native_text_ocr_owner_rights_decision_record_report(
        summary
    )

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Source-policy No-native-text OCR Owner Rights Decision Record" in report
    assert "source_policy_no_native_text_ocr_owner_rights_decision_record_v0" in report
    assert "previous_gate -> source_policy_no_native_text_ocr_source_rights_review_request_packet_v0" in report
    assert "decision_status -> owner_decision_recorded_blocked_pending_source_rights_response" in report
    assert "owner_rights_decision_recorded -> true" in report
    assert "request_sent -> false" in report
    assert "rights_response_received -> false" in report
    assert "source_rights_owner_approval_recorded -> false" in report
    assert "source_rights_owner_decision_recorded -> false" in report
    assert "source_rights_request_delivery_needed -> true" in report
    assert "source_rights_request_delivery_performed -> false" in report
    assert "transcript_collection_allowed -> false" in report
    assert "transcript_collection_performed -> false" in report
    assert "reference_text_available -> false" in report
    assert "transcript_hash_commit_allowed -> false" in report
    assert "transcript_hash_committed -> false" in report
    assert "quality_eval_performed -> false" in report
    assert "cer_computed -> false" in report
    assert "wer_computed -> false" in report
    assert "can_claim_owner_rights_decision_record -> true" in report
    assert "can_claim_rights_clearance -> false" in report
    assert "can_claim_request_sent -> false" in report
    assert "can_claim_source_rights_owner_approval -> false" in report
    assert "can_claim_transcript_collection -> false" in report
    assert "can_claim_reference_transcript_available -> false" in report
    assert "can_claim_ocr_quality -> false" in report
    assert "source_policy_no_native_text_ocr_rights_request_delivery_record_v0" in report
    assert "not rights clearance evidence" in report
    assert "not request-sent evidence" in report
    assert "not source-rights approval evidence" in report
    assert "not source-rights owner decision evidence" in report
    assert "not transcript collection evidence" in report
    assert "not reference transcript availability" in report
    assert "not OCR quality evidence" in report
    assert "not CER/WER support" in report
    assert "not robust PDF extraction evidence" in report


def test_owner_rights_decision_record_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.source_policy_no_native_text_ocr_owner_rights_decision_record_command",
            "--owner-rights-decision-record",
            str(DECISION_RECORD_PATH),
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
        "source_policy_no_native_text_ocr_owner_rights_decision_record_report_current"
        in result.stdout
    )
    assert "can_claim_owner_rights_decision_record=true" in result.stdout
    assert "can_claim_rights_clearance=false" in result.stdout
    assert "can_claim_request_sent=false" in result.stdout
    assert "can_claim_source_rights_owner_approval=false" in result.stdout
    assert "can_claim_transcript_collection=false" in result.stdout
    assert "can_claim_reference_transcript_available=false" in result.stdout
    assert "can_claim_ocr_quality=false" in result.stdout
    assert "can_claim_robust_pdf_extraction=false" in result.stdout


def test_owner_rights_decision_record_rejects_clearance_or_progress_overclaims(
    tmp_path,
):
    record = load_source_policy_no_native_text_ocr_owner_rights_decision_record(
        DECISION_RECORD_PATH
    )

    sent_record = dict(record)
    sent_record["request_sent"] = True
    with pytest.raises(ValueError, match="request_sent"):
        validate_source_policy_no_native_text_ocr_owner_rights_decision_record(
            sent_record
        )

    response_record = dict(record)
    response_record["rights_response_received"] = True
    with pytest.raises(ValueError, match="rights_response_received"):
        validate_source_policy_no_native_text_ocr_owner_rights_decision_record(
            response_record
        )

    rights_record = dict(record)
    rights_record["source_rights_owner_approval_recorded"] = True
    with pytest.raises(ValueError, match="source_rights_owner_approval_recorded"):
        validate_source_policy_no_native_text_ocr_owner_rights_decision_record(
            rights_record
        )

    collection_record = dict(record)
    collection_record["transcript_collection_allowed"] = True
    with pytest.raises(ValueError, match="transcript_collection_allowed"):
        validate_source_policy_no_native_text_ocr_owner_rights_decision_record(
            collection_record
        )

    transcript_record = dict(record)
    transcript_record["reference_text_available"] = True
    with pytest.raises(ValueError, match="reference_text_available"):
        validate_source_policy_no_native_text_ocr_owner_rights_decision_record(
            transcript_record
        )

    hash_record = dict(record)
    hash_record["transcript_hash_commit_allowed"] = True
    with pytest.raises(ValueError, match="transcript_hash_commit_allowed"):
        validate_source_policy_no_native_text_ocr_owner_rights_decision_record(
            hash_record
        )

    raw_record = dict(record)
    raw_record["reference_text"] = "forbidden"
    raw_path = tmp_path / "raw-reference.json"
    raw_path.write_text(json.dumps(raw_record), encoding="utf-8")
    with pytest.raises(ValueError, match="reference_text"):
        load_source_policy_no_native_text_ocr_owner_rights_decision_record(raw_path)


def test_owner_rights_decision_record_artifacts_are_sanitized():
    artifacts = [
        DECISION_RECORD_PATH,
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


def test_owner_rights_decision_record_docs_and_surfaces_are_linked():
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
            "source_policy_no_native_text_ocr_owner_rights_decision_record_v0"
            in surface
        )
        assert (
            "source_policy_no_native_text_ocr_rights_request_delivery_record_v0"
            in surface
        )

    for boundary in [
        "not rights clearance evidence",
        "not request-sent evidence",
        "not source-rights approval evidence",
        "not source-rights owner decision evidence",
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
