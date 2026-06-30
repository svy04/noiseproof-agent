from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PHASE_MARKER = "source_policy_no_native_text_ocr_rights_request_delivery_record_v0"
PREVIOUS_GATE = "source_policy_no_native_text_ocr_owner_rights_decision_record_v0"
CLAIM_BOUNDARY = (
    "source_policy_no_native_text_ocr_rights_request_delivery_record_not_delivered"
)
NEXT_GATE = (
    "source_policy_no_native_text_ocr_owner_runtime_rights_request_delivery_v0"
)

TARGET_FIXTURE_ID = "nara_911_mfr_00282_no_native_text_candidate"
TARGET_PUBLISHER = "National Archives and Records Administration"
TARGET_SOURCE_URL = (
    "https://nara-media-001.s3.amazonaws.com/arcmedia/9-11/MFR/"
    "t-0148-911MFR-00282.pdf"
)
TARGET_POLICY_URL = "https://www.archives.gov/global-pages/privacy.html"
TARGET_SHA256 = "6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba"
TARGET_PAGE_COUNT = 4
DELIVERY_ROUTE_CANDIDATES = [
    "nara_contact_form",
    "nara_reference_staff_consultation",
    "nara_general_inquiry_channel",
]
REQUIRED_DELIVERY_EVIDENCE = [
    "owner_runtime_contact_identity_available",
    "delivery_channel",
    "delivery_destination",
    "delivery_timestamp",
    "delivery_receipt_or_ticket_id",
    "sent_request_summary",
    "non_commit_private_contact_boundary",
]
MISSING_OWNER_RUNTIME_INPUTS = [
    "owner_contact_identity",
    "delivery_channel_selection",
    "delivery_destination_confirmation",
    "owner_runtime_submission",
    "delivery_receipt_or_ticket_id",
]
BLOCKED_ACTIONS = [
    "mark_request_sent",
    "mark_delivery_performed",
    "record_delivery_receipt",
    "record_rights_response",
    "collect_reference_transcript",
    "commit_reference_transcript_text",
    "commit_reference_transcript_hash",
    "compute_cer",
    "compute_wer",
    "claim_ocr_quality",
    "claim_robust_pdf_extraction",
]
ALLOWED_ACTIONS = [
    "keep_metadata_only_delivery_record",
    "prepare_owner_runtime_submission_outside_repository",
    "record_future_delivery_receipt_metadata_after_owner_runtime_submission",
    "keep_public_claims_blocked",
]
METRIC_CANDIDATES = ["cer", "wer"]
BOUNDARY_NOTES = [
    "source-policy no-native-text OCR rights request delivery record",
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
    "not arbitrary-market PDF OCR evidence",
    "not arbitrary-market PDF parsing evidence",
    "not rendered visual fidelity evidence",
    "not image/chart interpretation evidence",
    "not external reviewer feedback",
    "not product-complete",
]
WARNING_MESSAGES = [
    "This is a delivery record boundary only.",
    "It does not send a rights request or record delivery evidence.",
    "Owner contact identity and submission evidence must stay out of the repository.",
    "It does not record rights clearance or source-rights owner approval.",
    "CER/WER remain blocked until owner-runtime delivery, rights response, and reference text exist.",
]
_RAW_TEXT_FIELDS = {
    "recognized_text",
    "ocr_sample",
    "raw_text",
    "raw_extracted_text",
    "raw_ocr_text",
    "raw_reference_text",
    "reference_text",
    "reference_transcript",
    "reference_spans",
    "transcript_text",
    "page_level_reference_text",
    "page_image",
    "page_images",
    "screenshot",
    "screenshots",
    "owner_email",
    "contact_email",
    "message_body",
    "receipt_id",
    "ticket_id",
}


def build_source_policy_no_native_text_ocr_rights_request_delivery_record(
    owner_rights_decision_record: dict[str, Any],
) -> dict[str, Any]:
    _validate_owner_rights_decision_record(owner_rights_decision_record)
    return {
        "record": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "delivery_status": "delivery_record_prepared_request_not_sent",
        "target_fixture_id": owner_rights_decision_record["target_fixture_id"],
        "publisher": owner_rights_decision_record["publisher"],
        "source_url": owner_rights_decision_record["source_url"],
        "source_policy_url": owner_rights_decision_record["source_policy_url"],
        "source_sha256": owner_rights_decision_record["source_sha256"],
        "source_sha256_algorithm": "sha256",
        "owner_rights_decision_record_phase_marker": owner_rights_decision_record[
            "phase_marker"
        ],
        "delivery_scope": "owner_runtime_external_rights_request_delivery",
        "delivery_route_candidates": list(DELIVERY_ROUTE_CANDIDATES),
        "required_delivery_evidence": list(REQUIRED_DELIVERY_EVIDENCE),
        "missing_owner_runtime_inputs": list(MISSING_OWNER_RUNTIME_INPUTS),
        "blocked_actions": list(BLOCKED_ACTIONS),
        "allowed_actions": list(ALLOWED_ACTIONS),
        "request_packet_prepared": True,
        "owner_rights_decision_recorded": True,
        "request_sent": False,
        "source_rights_request_delivery_performed": False,
        "delivery_channel_selected": False,
        "delivery_destination_recorded": False,
        "delivery_timestamp_recorded": False,
        "delivery_receipt_recorded": False,
        "owner_contact_identity_available": False,
        "owner_contact_identity_committed": False,
        "rights_response_received": False,
        "source_rights_owner_approval_recorded": False,
        "source_rights_owner_decision_recorded": False,
        "target_page_count": TARGET_PAGE_COUNT,
        "repository_commit_policy": "metadata_only_no_transcript_text_or_hash",
        "transcript_collection_allowed": False,
        "transcript_collection_performed": False,
        "reference_text_available": False,
        "full_reference_transcript_available": False,
        "reference_text_commit_allowed": False,
        "transcript_hash_commit_allowed": False,
        "transcript_hash_committed": False,
        "reference_text_hash_committed": False,
        "quality_eval_performed": False,
        "cer_computed": False,
        "wer_computed": False,
        "metric_candidates": list(METRIC_CANDIDATES),
        "metric_candidates_status": (
            "blocked_until_owner_runtime_delivery_response_and_reference_text_exist"
        ),
        "minimum_next_artifact": "owner runtime rights request delivery execution",
        "raw_reference_text_committed": False,
        "raw_ocr_text_committed": False,
        "source_pdf_committed": False,
        "download_cache_committed": False,
        "page_images_committed": False,
        "screenshots_committed": False,
        "warnings": list(WARNING_MESSAGES),
        "boundary_notes": list(BOUNDARY_NOTES),
        "can_claim_rights_request_delivery_record": True,
        "can_claim_request_sent": False,
        "can_claim_delivery_performed": False,
        "can_claim_rights_clearance": False,
        "can_claim_source_rights_owner_approval": False,
        "can_claim_transcript_collection": False,
        "can_claim_reference_transcript_available": False,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
        "recommended_next_gate": NEXT_GATE,
    }


def load_source_policy_no_native_text_ocr_rights_request_delivery_record(
    path: Path | str,
) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    validate_source_policy_no_native_text_ocr_rights_request_delivery_record(
        payload
    )
    return payload


def build_source_policy_no_native_text_ocr_rights_request_delivery_record_summary(
    record: dict[str, Any],
) -> dict[str, Any]:
    validate_source_policy_no_native_text_ocr_rights_request_delivery_record(
        record
    )
    return {
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "delivery_status": record["delivery_status"],
        "target_fixture_id": record["target_fixture_id"],
        "publisher": record["publisher"],
        "source_url": record["source_url"],
        "source_policy_url": record["source_policy_url"],
        "source_sha256": record["source_sha256"],
        "owner_rights_decision_record_phase_marker": record[
            "owner_rights_decision_record_phase_marker"
        ],
        "delivery_scope": record["delivery_scope"],
        "delivery_route_candidates": record["delivery_route_candidates"],
        "required_delivery_evidence": record["required_delivery_evidence"],
        "missing_owner_runtime_inputs": record["missing_owner_runtime_inputs"],
        "blocked_actions": record["blocked_actions"],
        "allowed_actions": record["allowed_actions"],
        "request_packet_prepared": record["request_packet_prepared"],
        "owner_rights_decision_recorded": record["owner_rights_decision_recorded"],
        "request_sent": record["request_sent"],
        "source_rights_request_delivery_performed": record[
            "source_rights_request_delivery_performed"
        ],
        "delivery_channel_selected": record["delivery_channel_selected"],
        "delivery_destination_recorded": record["delivery_destination_recorded"],
        "delivery_timestamp_recorded": record["delivery_timestamp_recorded"],
        "delivery_receipt_recorded": record["delivery_receipt_recorded"],
        "owner_contact_identity_available": record[
            "owner_contact_identity_available"
        ],
        "owner_contact_identity_committed": record[
            "owner_contact_identity_committed"
        ],
        "rights_response_received": record["rights_response_received"],
        "source_rights_owner_approval_recorded": record[
            "source_rights_owner_approval_recorded"
        ],
        "source_rights_owner_decision_recorded": record[
            "source_rights_owner_decision_recorded"
        ],
        "target_page_count": record["target_page_count"],
        "repository_commit_policy": record["repository_commit_policy"],
        "transcript_collection_allowed": record["transcript_collection_allowed"],
        "transcript_collection_performed": record[
            "transcript_collection_performed"
        ],
        "reference_text_available": record["reference_text_available"],
        "full_reference_transcript_available": record[
            "full_reference_transcript_available"
        ],
        "reference_text_commit_allowed": record["reference_text_commit_allowed"],
        "transcript_hash_commit_allowed": record["transcript_hash_commit_allowed"],
        "transcript_hash_committed": record["transcript_hash_committed"],
        "reference_text_hash_committed": record["reference_text_hash_committed"],
        "quality_eval_performed": record["quality_eval_performed"],
        "cer_computed": record["cer_computed"],
        "wer_computed": record["wer_computed"],
        "metric_candidates": record["metric_candidates"],
        "metric_candidates_status": record["metric_candidates_status"],
        "minimum_next_artifact": record["minimum_next_artifact"],
        "raw_reference_text_committed": record["raw_reference_text_committed"],
        "raw_ocr_text_committed": record["raw_ocr_text_committed"],
        "source_pdf_committed": record["source_pdf_committed"],
        "download_cache_committed": record["download_cache_committed"],
        "page_images_committed": record["page_images_committed"],
        "screenshots_committed": record["screenshots_committed"],
        "warnings": record["warnings"],
        "boundary_notes": record["boundary_notes"],
        "can_claim_rights_request_delivery_record": record[
            "can_claim_rights_request_delivery_record"
        ],
        "can_claim_request_sent": record["can_claim_request_sent"],
        "can_claim_delivery_performed": record["can_claim_delivery_performed"],
        "can_claim_rights_clearance": record["can_claim_rights_clearance"],
        "can_claim_source_rights_owner_approval": record[
            "can_claim_source_rights_owner_approval"
        ],
        "can_claim_transcript_collection": record[
            "can_claim_transcript_collection"
        ],
        "can_claim_reference_transcript_available": record[
            "can_claim_reference_transcript_available"
        ],
        "can_claim_ocr_quality": record["can_claim_ocr_quality"],
        "can_claim_robust_pdf_extraction": record[
            "can_claim_robust_pdf_extraction"
        ],
        "next_gate": record["recommended_next_gate"],
    }


def build_source_policy_no_native_text_ocr_rights_request_delivery_record_report(
    summary: dict[str, Any],
) -> str:
    lines = [
        "# Source-policy No-native-text OCR Rights Request Delivery Record",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report records the request-delivery boundary for the preserved NARA no-native-text route.",
        "",
        "It is not rights clearance evidence.",
        "",
        "It is not request-sent evidence.",
        "",
        "It is not request-delivery evidence.",
        "",
        "It is not source-rights approval evidence.",
        "",
        "It is not source-rights owner decision evidence.",
        "",
        "It is not transcript collection evidence.",
        "",
        "It is not reference transcript availability.",
        "",
        "It is not OCR quality evidence.",
        "",
        "It is not CER/WER support.",
        "",
        "It is not robust PDF extraction evidence.",
        "",
        "## Gate Result",
        "",
        f"previous_gate -> {summary['previous_gate']}",
        f"delivery_status -> {summary['delivery_status']}",
        f"delivery_scope -> {summary['delivery_scope']}",
        f"request_packet_prepared -> {_format_bool(summary['request_packet_prepared'])}",
        "owner_rights_decision_recorded -> "
        + _format_bool(summary["owner_rights_decision_recorded"]),
        f"request_sent -> {_format_bool(summary['request_sent'])}",
        "source_rights_request_delivery_performed -> "
        + _format_bool(summary["source_rights_request_delivery_performed"]),
        f"delivery_channel_selected -> {_format_bool(summary['delivery_channel_selected'])}",
        f"delivery_destination_recorded -> {_format_bool(summary['delivery_destination_recorded'])}",
        f"delivery_timestamp_recorded -> {_format_bool(summary['delivery_timestamp_recorded'])}",
        f"delivery_receipt_recorded -> {_format_bool(summary['delivery_receipt_recorded'])}",
        "owner_contact_identity_available -> "
        + _format_bool(summary["owner_contact_identity_available"]),
        "owner_contact_identity_committed -> "
        + _format_bool(summary["owner_contact_identity_committed"]),
        f"rights_response_received -> {_format_bool(summary['rights_response_received'])}",
        "source_rights_owner_approval_recorded -> "
        + _format_bool(summary["source_rights_owner_approval_recorded"]),
        f"target_fixture_id -> {summary['target_fixture_id']}",
        f"source_sha256 -> {summary['source_sha256']}",
        f"source_policy_url -> {summary['source_policy_url']}",
        f"repository_commit_policy -> {summary['repository_commit_policy']}",
        f"transcript_collection_allowed -> {_format_bool(summary['transcript_collection_allowed'])}",
        f"transcript_collection_performed -> {_format_bool(summary['transcript_collection_performed'])}",
        f"reference_text_available -> {_format_bool(summary['reference_text_available'])}",
        f"reference_text_commit_allowed -> {_format_bool(summary['reference_text_commit_allowed'])}",
        f"transcript_hash_commit_allowed -> {_format_bool(summary['transcript_hash_commit_allowed'])}",
        f"transcript_hash_committed -> {_format_bool(summary['transcript_hash_committed'])}",
        f"quality_eval_performed -> {_format_bool(summary['quality_eval_performed'])}",
        f"cer_computed -> {_format_bool(summary['cer_computed'])}",
        f"wer_computed -> {_format_bool(summary['wer_computed'])}",
        f"metric_candidates -> {', '.join(summary['metric_candidates'])}",
        f"metric_candidates_status -> {summary['metric_candidates_status']}",
        "",
        "## Delivery Route Candidates",
        "",
        *[f"- {item}" for item in summary["delivery_route_candidates"]],
        "",
        "## Required Future Delivery Evidence",
        "",
        *[f"- {item}" for item in summary["required_delivery_evidence"]],
        "",
        "## Missing Owner-runtime Inputs",
        "",
        *[f"- {item}" for item in summary["missing_owner_runtime_inputs"]],
        "",
        "## Blocked Actions",
        "",
        *[f"- {item}" for item in summary["blocked_actions"]],
        "",
        "## Claim Boundary",
        "",
        "can_claim_rights_request_delivery_record -> "
        + _format_bool(summary["can_claim_rights_request_delivery_record"]),
        f"can_claim_request_sent -> {_format_bool(summary['can_claim_request_sent'])}",
        "can_claim_delivery_performed -> "
        + _format_bool(summary["can_claim_delivery_performed"]),
        f"can_claim_rights_clearance -> {_format_bool(summary['can_claim_rights_clearance'])}",
        "can_claim_source_rights_owner_approval -> "
        + _format_bool(summary["can_claim_source_rights_owner_approval"]),
        f"can_claim_transcript_collection -> {_format_bool(summary['can_claim_transcript_collection'])}",
        "can_claim_reference_transcript_available -> "
        + _format_bool(summary["can_claim_reference_transcript_available"]),
        f"can_claim_ocr_quality -> {_format_bool(summary['can_claim_ocr_quality'])}",
        f"can_claim_robust_pdf_extraction -> {_format_bool(summary['can_claim_robust_pdf_extraction'])}",
        "",
        "## Warnings",
        "",
        *[f"- {item}" for item in summary["warnings"]],
        "",
        "## Next Gate",
        "",
        summary["next_gate"],
        "",
    ]
    return "\n".join(lines)


def validate_source_policy_no_native_text_ocr_rights_request_delivery_record(
    payload: dict[str, Any],
) -> None:
    _reject_raw_text_fields(payload)
    expected_values = {
        "record": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "delivery_status": "delivery_record_prepared_request_not_sent",
        "target_fixture_id": TARGET_FIXTURE_ID,
        "publisher": TARGET_PUBLISHER,
        "source_url": TARGET_SOURCE_URL,
        "source_policy_url": TARGET_POLICY_URL,
        "source_sha256": TARGET_SHA256,
        "source_sha256_algorithm": "sha256",
        "owner_rights_decision_record_phase_marker": PREVIOUS_GATE,
        "delivery_scope": "owner_runtime_external_rights_request_delivery",
        "delivery_route_candidates": DELIVERY_ROUTE_CANDIDATES,
        "required_delivery_evidence": REQUIRED_DELIVERY_EVIDENCE,
        "missing_owner_runtime_inputs": MISSING_OWNER_RUNTIME_INPUTS,
        "blocked_actions": BLOCKED_ACTIONS,
        "allowed_actions": ALLOWED_ACTIONS,
        "request_packet_prepared": True,
        "owner_rights_decision_recorded": True,
        "request_sent": False,
        "source_rights_request_delivery_performed": False,
        "delivery_channel_selected": False,
        "delivery_destination_recorded": False,
        "delivery_timestamp_recorded": False,
        "delivery_receipt_recorded": False,
        "owner_contact_identity_available": False,
        "owner_contact_identity_committed": False,
        "rights_response_received": False,
        "source_rights_owner_approval_recorded": False,
        "source_rights_owner_decision_recorded": False,
        "target_page_count": TARGET_PAGE_COUNT,
        "repository_commit_policy": "metadata_only_no_transcript_text_or_hash",
        "transcript_collection_allowed": False,
        "transcript_collection_performed": False,
        "reference_text_available": False,
        "full_reference_transcript_available": False,
        "reference_text_commit_allowed": False,
        "transcript_hash_commit_allowed": False,
        "transcript_hash_committed": False,
        "reference_text_hash_committed": False,
        "quality_eval_performed": False,
        "cer_computed": False,
        "wer_computed": False,
        "metric_candidates": METRIC_CANDIDATES,
        "metric_candidates_status": (
            "blocked_until_owner_runtime_delivery_response_and_reference_text_exist"
        ),
        "minimum_next_artifact": "owner runtime rights request delivery execution",
        "raw_reference_text_committed": False,
        "raw_ocr_text_committed": False,
        "source_pdf_committed": False,
        "download_cache_committed": False,
        "page_images_committed": False,
        "screenshots_committed": False,
        "can_claim_rights_request_delivery_record": True,
        "can_claim_request_sent": False,
        "can_claim_delivery_performed": False,
        "can_claim_rights_clearance": False,
        "can_claim_source_rights_owner_approval": False,
        "can_claim_transcript_collection": False,
        "can_claim_reference_transcript_available": False,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
        "recommended_next_gate": NEXT_GATE,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(
                f"source-policy OCR rights request delivery record {field} must be {expected!r}"
            )

    for field in ["warnings", "boundary_notes"]:
        value = payload.get(field)
        if not isinstance(value, list) or not value:
            raise ValueError(
                f"source-policy OCR rights request delivery record {field} must be a non-empty list"
            )

    for note in BOUNDARY_NOTES:
        if note not in payload["boundary_notes"]:
            raise ValueError(
                f"source-policy OCR rights request delivery record missing boundary note: {note}"
            )


def _validate_owner_rights_decision_record(payload: dict[str, Any]) -> None:
    expected_values = {
        "phase_marker": PREVIOUS_GATE,
        "previous_gate": "source_policy_no_native_text_ocr_source_rights_review_request_packet_v0",
        "target_fixture_id": TARGET_FIXTURE_ID,
        "publisher": TARGET_PUBLISHER,
        "source_url": TARGET_SOURCE_URL,
        "source_policy_url": TARGET_POLICY_URL,
        "source_sha256": TARGET_SHA256,
        "decision_status": "owner_decision_recorded_blocked_pending_source_rights_response",
        "request_packet_prepared": True,
        "request_sent": False,
        "rights_response_received": False,
        "source_rights_owner_approval_recorded": False,
        "source_rights_owner_decision_recorded": False,
        "owner_rights_decision_recorded": True,
        "source_rights_request_delivery_needed": True,
        "source_rights_request_delivery_performed": False,
        "repository_commit_policy": "metadata_only_no_transcript_text_or_hash",
        "transcript_collection_allowed": False,
        "reference_text_available": False,
        "transcript_hash_commit_allowed": False,
        "quality_eval_performed": False,
        "cer_computed": False,
        "wer_computed": False,
        "raw_reference_text_committed": False,
        "raw_ocr_text_committed": False,
        "can_claim_owner_rights_decision_record": True,
        "can_claim_rights_clearance": False,
        "can_claim_request_sent": False,
        "can_claim_source_rights_owner_approval": False,
        "can_claim_transcript_collection": False,
        "can_claim_reference_transcript_available": False,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
        "recommended_next_gate": PHASE_MARKER,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(
                f"owner rights decision record {field} must be {expected!r}"
            )


def _reject_raw_text_fields(value: Any) -> None:
    if isinstance(value, dict):
        for key, nested in value.items():
            if key in _RAW_TEXT_FIELDS:
                raise ValueError(
                    f"source-policy OCR rights request delivery record must not commit {key}"
                )
            _reject_raw_text_fields(nested)
    elif isinstance(value, list):
        for nested in value:
            _reject_raw_text_fields(nested)


def _format_bool(value: object) -> str:
    return "true" if value is True else "false"
