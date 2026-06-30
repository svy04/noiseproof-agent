import json
import subprocess
import sys
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[3]
OWNER_DECISION_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/source-policy-no-native-text-ocr-owner-rights-decision-record.json"
)
DELIVERY_RECORD_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/source-policy-no-native-text-ocr-rights-request-delivery-record.json"
)
REPORT_PATH = (
    REPO_ROOT
    / "docs/evaluation/source-policy-no-native-text-ocr-rights-request-delivery-record-report.md"
)
REVIEW_PATH = (
    REPO_ROOT
    / "docs/review/source-policy-no-native-text-ocr-rights-request-delivery-record.md"
)
SPEC_PATH = (
    REPO_ROOT
    / "docs/specs/2026-07-01-source-policy-no-native-text-ocr-rights-request-delivery-record.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.source_policy_no_native_text_ocr_rights_request_delivery_record import (  # noqa: E402
    NEXT_GATE,
    PHASE_MARKER,
    PREVIOUS_GATE,
    build_source_policy_no_native_text_ocr_rights_request_delivery_record,
    build_source_policy_no_native_text_ocr_rights_request_delivery_record_report,
    build_source_policy_no_native_text_ocr_rights_request_delivery_record_summary,
    load_source_policy_no_native_text_ocr_rights_request_delivery_record,
    validate_source_policy_no_native_text_ocr_rights_request_delivery_record,
)


def test_rights_request_delivery_record_commits_only_not_sent_boundary():
    record = load_source_policy_no_native_text_ocr_rights_request_delivery_record(
        DELIVERY_RECORD_PATH
    )
    summary = build_source_policy_no_native_text_ocr_rights_request_delivery_record_summary(
        record
    )

    assert summary["phase_marker"] == PHASE_MARKER
    assert summary["previous_gate"] == PREVIOUS_GATE
    assert summary["delivery_status"] == "delivery_record_prepared_request_not_sent"
    assert summary["target_fixture_id"] == "nara_911_mfr_00282_no_native_text_candidate"
    assert summary["source_sha256"] == (
        "6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba"
    )
    assert summary["owner_rights_decision_record_phase_marker"] == PREVIOUS_GATE
    assert summary["delivery_scope"] == "owner_runtime_external_rights_request_delivery"
    assert summary["delivery_route_candidates"] == [
        "nara_contact_form",
        "nara_reference_staff_consultation",
        "nara_general_inquiry_channel",
    ]
    assert summary["required_delivery_evidence"] == [
        "owner_runtime_contact_identity_available",
        "delivery_channel",
        "delivery_destination",
        "delivery_timestamp",
        "delivery_receipt_or_ticket_id",
        "sent_request_summary",
        "non_commit_private_contact_boundary",
    ]
    assert summary["missing_owner_runtime_inputs"] == [
        "owner_contact_identity",
        "delivery_channel_selection",
        "delivery_destination_confirmation",
        "owner_runtime_submission",
        "delivery_receipt_or_ticket_id",
    ]
    assert summary["request_packet_prepared"] is True
    assert summary["owner_rights_decision_recorded"] is True
    assert summary["request_sent"] is False
    assert summary["source_rights_request_delivery_performed"] is False
    assert summary["delivery_channel_selected"] is False
    assert summary["delivery_destination_recorded"] is False
    assert summary["delivery_timestamp_recorded"] is False
    assert summary["delivery_receipt_recorded"] is False
    assert summary["owner_contact_identity_available"] is False
    assert summary["owner_contact_identity_committed"] is False
    assert summary["rights_response_received"] is False
    assert summary["source_rights_owner_approval_recorded"] is False
    assert summary["source_rights_owner_decision_recorded"] is False
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
        "blocked_until_owner_runtime_delivery_response_and_reference_text_exist"
    )
    assert summary["raw_reference_text_committed"] is False
    assert summary["raw_ocr_text_committed"] is False
    assert summary["can_claim_rights_request_delivery_record"] is True
    assert summary["can_claim_request_sent"] is False
    assert summary["can_claim_delivery_performed"] is False
    assert summary["can_claim_rights_clearance"] is False
    assert summary["can_claim_source_rights_owner_approval"] is False
    assert summary["can_claim_transcript_collection"] is False
    assert summary["can_claim_reference_transcript_available"] is False
    assert summary["can_claim_ocr_quality"] is False
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["next_gate"] == NEXT_GATE


def test_rights_request_delivery_record_builds_from_owner_decision():
    owner_decision = json.loads(OWNER_DECISION_PATH.read_text(encoding="utf-8"))

    record = build_source_policy_no_native_text_ocr_rights_request_delivery_record(
        owner_decision
    )

    assert record["phase_marker"] == PHASE_MARKER
    assert record["previous_gate"] == PREVIOUS_GATE
    assert record["owner_rights_decision_record_phase_marker"] == PREVIOUS_GATE
    assert record["delivery_status"] == "delivery_record_prepared_request_not_sent"
    assert record["request_packet_prepared"] is True
    assert record["owner_rights_decision_recorded"] is True
    assert record["request_sent"] is False
    assert record["source_rights_request_delivery_performed"] is False
    assert record["delivery_channel_selected"] is False
    assert record["delivery_timestamp_recorded"] is False
    assert record["delivery_receipt_recorded"] is False
    assert record["owner_contact_identity_available"] is False
    assert record["rights_response_received"] is False
    assert record["transcript_collection_allowed"] is False
    assert record["reference_text_available"] is False
    assert record["quality_eval_performed"] is False
    assert record["recommended_next_gate"] == NEXT_GATE


def test_rights_request_delivery_record_report_is_current_and_bounded():
    record = load_source_policy_no_native_text_ocr_rights_request_delivery_record(
        DELIVERY_RECORD_PATH
    )
    summary = build_source_policy_no_native_text_ocr_rights_request_delivery_record_summary(
        record
    )
    report = build_source_policy_no_native_text_ocr_rights_request_delivery_record_report(
        summary
    )

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Source-policy No-native-text OCR Rights Request Delivery Record" in report
    assert "source_policy_no_native_text_ocr_rights_request_delivery_record_v0" in report
    assert "previous_gate -> source_policy_no_native_text_ocr_owner_rights_decision_record_v0" in report
    assert "delivery_status -> delivery_record_prepared_request_not_sent" in report
    assert "request_sent -> false" in report
    assert "source_rights_request_delivery_performed -> false" in report
    assert "delivery_channel_selected -> false" in report
    assert "delivery_timestamp_recorded -> false" in report
    assert "delivery_receipt_recorded -> false" in report
    assert "owner_contact_identity_available -> false" in report
    assert "owner_contact_identity_committed -> false" in report
    assert "rights_response_received -> false" in report
    assert "source_rights_owner_approval_recorded -> false" in report
    assert "transcript_collection_allowed -> false" in report
    assert "transcript_collection_performed -> false" in report
    assert "reference_text_available -> false" in report
    assert "transcript_hash_commit_allowed -> false" in report
    assert "quality_eval_performed -> false" in report
    assert "cer_computed -> false" in report
    assert "wer_computed -> false" in report
    assert "can_claim_rights_request_delivery_record -> true" in report
    assert "can_claim_request_sent -> false" in report
    assert "can_claim_delivery_performed -> false" in report
    assert "can_claim_rights_clearance -> false" in report
    assert "can_claim_source_rights_owner_approval -> false" in report
    assert "can_claim_transcript_collection -> false" in report
    assert "can_claim_reference_transcript_available -> false" in report
    assert "can_claim_ocr_quality -> false" in report
    assert "source_policy_no_native_text_ocr_owner_runtime_rights_request_delivery_v0" in report
    assert "not rights clearance evidence" in report
    assert "not request-sent evidence" in report
    assert "not request-delivery evidence" in report
    assert "not source-rights approval evidence" in report
    assert "not transcript collection evidence" in report
    assert "not reference transcript availability" in report
    assert "not OCR quality evidence" in report
    assert "not CER/WER support" in report
    assert "not robust PDF extraction evidence" in report


def test_rights_request_delivery_record_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.source_policy_no_native_text_ocr_rights_request_delivery_record_command",
            "--rights-request-delivery-record",
            str(DELIVERY_RECORD_PATH),
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
        "source_policy_no_native_text_ocr_rights_request_delivery_record_report_current"
        in result.stdout
    )
    assert "can_claim_rights_request_delivery_record=true" in result.stdout
    assert "can_claim_request_sent=false" in result.stdout
    assert "can_claim_delivery_performed=false" in result.stdout
    assert "can_claim_rights_clearance=false" in result.stdout
    assert "can_claim_source_rights_owner_approval=false" in result.stdout
    assert "can_claim_transcript_collection=false" in result.stdout
    assert "can_claim_reference_transcript_available=false" in result.stdout
    assert "can_claim_ocr_quality=false" in result.stdout
    assert "can_claim_robust_pdf_extraction=false" in result.stdout


def test_rights_request_delivery_record_rejects_delivery_or_progress_overclaims(
    tmp_path,
):
    record = load_source_policy_no_native_text_ocr_rights_request_delivery_record(
        DELIVERY_RECORD_PATH
    )

    sent_record = dict(record)
    sent_record["request_sent"] = True
    with pytest.raises(ValueError, match="request_sent"):
        validate_source_policy_no_native_text_ocr_rights_request_delivery_record(
            sent_record
        )

    delivered_record = dict(record)
    delivered_record["source_rights_request_delivery_performed"] = True
    with pytest.raises(ValueError, match="source_rights_request_delivery_performed"):
        validate_source_policy_no_native_text_ocr_rights_request_delivery_record(
            delivered_record
        )

    timestamp_record = dict(record)
    timestamp_record["delivery_timestamp_recorded"] = True
    with pytest.raises(ValueError, match="delivery_timestamp_recorded"):
        validate_source_policy_no_native_text_ocr_rights_request_delivery_record(
            timestamp_record
        )

    identity_record = dict(record)
    identity_record["owner_contact_identity_available"] = True
    with pytest.raises(ValueError, match="owner_contact_identity_available"):
        validate_source_policy_no_native_text_ocr_rights_request_delivery_record(
            identity_record
        )

    response_record = dict(record)
    response_record["rights_response_received"] = True
    with pytest.raises(ValueError, match="rights_response_received"):
        validate_source_policy_no_native_text_ocr_rights_request_delivery_record(
            response_record
        )

    transcript_record = dict(record)
    transcript_record["reference_text_available"] = True
    with pytest.raises(ValueError, match="reference_text_available"):
        validate_source_policy_no_native_text_ocr_rights_request_delivery_record(
            transcript_record
        )

    raw_record = dict(record)
    raw_record["reference_text"] = "forbidden"
    raw_path = tmp_path / "raw-reference.json"
    raw_path.write_text(json.dumps(raw_record), encoding="utf-8")
    with pytest.raises(ValueError, match="reference_text"):
        load_source_policy_no_native_text_ocr_rights_request_delivery_record(raw_path)


def test_rights_request_delivery_record_artifacts_are_sanitized():
    artifacts = [
        DELIVERY_RECORD_PATH,
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
        "owner_email:",
        "contact_email:",
        "message_body:",
        "receipt_id:",
    ]

    for artifact in artifacts:
        text = artifact.read_text(encoding="utf-8")
        for marker in forbidden:
            assert marker not in text


def test_rights_request_delivery_record_docs_and_surfaces_are_linked():
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
            "source_policy_no_native_text_ocr_rights_request_delivery_record_v0"
            in surface
        )
        assert (
            "source_policy_no_native_text_ocr_owner_runtime_rights_request_delivery_v0"
            in surface
        )

    for boundary in [
        "not rights clearance evidence",
        "not request-sent evidence",
        "not request-delivery evidence",
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
