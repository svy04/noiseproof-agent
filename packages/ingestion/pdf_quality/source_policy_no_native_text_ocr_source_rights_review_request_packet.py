from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PHASE_MARKER = "source_policy_no_native_text_ocr_source_rights_review_request_packet_v0"
PREVIOUS_GATE = "source_policy_no_native_text_ocr_owner_transcript_collection_plan_v0"
CLAIM_BOUNDARY = (
    "source_policy_no_native_text_ocr_source_rights_review_request_packet_not_clearance"
)
NEXT_GATE = "source_policy_no_native_text_ocr_owner_rights_decision_record_v0"

TARGET_FIXTURE_ID = "nara_911_mfr_00282_no_native_text_candidate"
TARGET_PUBLISHER = "National Archives and Records Administration"
TARGET_SOURCE_URL = (
    "https://nara-media-001.s3.amazonaws.com/arcmedia/9-11/MFR/"
    "t-0148-911MFR-00282.pdf"
)
TARGET_POLICY_URL = "https://www.archives.gov/global-pages/privacy.html"
TARGET_SHA256 = "6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba"
TARGET_PAGE_COUNT = 4
RIGHTS_REVIEW_QUESTIONS = [
    "does_item_have_known_copyright_or_access_restrictions",
    "may_owner_create_manual_reference_transcript_for_internal_ocr_quality_eval",
    "may_reference_transcript_text_be_committed_publicly",
    "may_reference_transcript_hash_or_page_level_metadata_be_committed_publicly",
    "what_attribution_or_restriction_notice_is_required",
]
MATERIAL_REQUESTED_FOR_REVIEW = [
    "source_url",
    "source_policy_url",
    "source_sha256",
    "target_page_count",
    "proposed_repository_commit_policy",
]
METRIC_CANDIDATES = ["cer", "wer"]
BOUNDARY_NOTES = [
    "source-policy no-native-text OCR source rights review request packet",
    "not rights clearance evidence",
    "not request-sent evidence",
    "not source-rights approval evidence",
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
    "This is a source-rights review request packet only.",
    "It does not send a request or record a response.",
    "It does not record rights clearance or source-rights owner approval.",
    "It does not collect or commit a reference transcript.",
    "CER/WER remain blocked until rights decision and reference text exist.",
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
}


def build_source_policy_no_native_text_ocr_source_rights_review_request_packet(
    owner_transcript_collection_plan: dict[str, Any],
) -> dict[str, Any]:
    _validate_owner_transcript_collection_plan(owner_transcript_collection_plan)
    return {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "packet_status": "source_rights_review_request_packet_prepared",
        "target_fixture_id": owner_transcript_collection_plan["target_fixture_id"],
        "publisher": owner_transcript_collection_plan["publisher"],
        "source_url": owner_transcript_collection_plan["source_url"],
        "source_policy_url": owner_transcript_collection_plan["source_policy_url"],
        "source_sha256": owner_transcript_collection_plan["source_sha256"],
        "source_sha256_algorithm": "sha256",
        "owner_transcript_collection_plan_phase_marker": owner_transcript_collection_plan[
            "phase_marker"
        ],
        "request_scope": "rights_review_request_only",
        "request_questions": list(RIGHTS_REVIEW_QUESTIONS),
        "request_question_count": len(RIGHTS_REVIEW_QUESTIONS),
        "proposed_use_scope": (
            "internal_owner_runtime_reference_transcript_for_ocr_quality_eval"
        ),
        "material_requested_for_review": list(MATERIAL_REQUESTED_FOR_REVIEW),
        "material_requested_for_review_count": len(MATERIAL_REQUESTED_FOR_REVIEW),
        "target_page_count": TARGET_PAGE_COUNT,
        "repository_commit_policy": "metadata_only_no_transcript_text_or_hash",
        "request_packet_prepared": True,
        "request_sent": False,
        "rights_response_received": False,
        "source_rights_owner_approval_recorded": False,
        "source_rights_decision_recorded": False,
        "transcript_collection_performed": False,
        "reference_text_available": False,
        "full_reference_transcript_available": False,
        "reference_text_commit_allowed": False,
        "transcript_hash_committed": False,
        "reference_text_hash_committed": False,
        "quality_eval_performed": False,
        "cer_computed": False,
        "wer_computed": False,
        "metric_candidates": list(METRIC_CANDIDATES),
        "metric_candidates_status": (
            "blocked_until_rights_decision_and_reference_text_exist"
        ),
        "minimum_next_artifact": "owner rights decision record",
        "raw_reference_text_committed": False,
        "raw_ocr_text_committed": False,
        "source_pdf_committed": False,
        "download_cache_committed": False,
        "page_images_committed": False,
        "screenshots_committed": False,
        "warnings": list(WARNING_MESSAGES),
        "boundary_notes": list(BOUNDARY_NOTES),
        "can_claim_source_rights_review_request_packet": True,
        "can_claim_rights_clearance": False,
        "can_claim_transcript_collection": False,
        "can_claim_reference_transcript_available": False,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
        "recommended_next_gate": NEXT_GATE,
    }


def load_source_policy_no_native_text_ocr_source_rights_review_request_packet(
    path: Path | str,
) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    validate_source_policy_no_native_text_ocr_source_rights_review_request_packet(
        payload
    )
    return payload


def build_source_policy_no_native_text_ocr_source_rights_review_request_packet_summary(
    packet: dict[str, Any],
) -> dict[str, Any]:
    validate_source_policy_no_native_text_ocr_source_rights_review_request_packet(
        packet
    )
    return {
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "packet_status": packet["packet_status"],
        "target_fixture_id": packet["target_fixture_id"],
        "publisher": packet["publisher"],
        "source_url": packet["source_url"],
        "source_policy_url": packet["source_policy_url"],
        "source_sha256": packet["source_sha256"],
        "owner_transcript_collection_plan_phase_marker": packet[
            "owner_transcript_collection_plan_phase_marker"
        ],
        "request_scope": packet["request_scope"],
        "request_questions": packet["request_questions"],
        "request_question_count": packet["request_question_count"],
        "proposed_use_scope": packet["proposed_use_scope"],
        "material_requested_for_review": packet["material_requested_for_review"],
        "material_requested_for_review_count": packet[
            "material_requested_for_review_count"
        ],
        "target_page_count": packet["target_page_count"],
        "repository_commit_policy": packet["repository_commit_policy"],
        "request_packet_prepared": packet["request_packet_prepared"],
        "request_sent": packet["request_sent"],
        "rights_response_received": packet["rights_response_received"],
        "source_rights_owner_approval_recorded": packet[
            "source_rights_owner_approval_recorded"
        ],
        "source_rights_decision_recorded": packet[
            "source_rights_decision_recorded"
        ],
        "transcript_collection_performed": packet["transcript_collection_performed"],
        "reference_text_available": packet["reference_text_available"],
        "full_reference_transcript_available": packet[
            "full_reference_transcript_available"
        ],
        "reference_text_commit_allowed": packet["reference_text_commit_allowed"],
        "transcript_hash_committed": packet["transcript_hash_committed"],
        "reference_text_hash_committed": packet["reference_text_hash_committed"],
        "quality_eval_performed": packet["quality_eval_performed"],
        "cer_computed": packet["cer_computed"],
        "wer_computed": packet["wer_computed"],
        "metric_candidates": packet["metric_candidates"],
        "metric_candidates_status": packet["metric_candidates_status"],
        "minimum_next_artifact": packet["minimum_next_artifact"],
        "raw_reference_text_committed": packet["raw_reference_text_committed"],
        "raw_ocr_text_committed": packet["raw_ocr_text_committed"],
        "source_pdf_committed": packet["source_pdf_committed"],
        "download_cache_committed": packet["download_cache_committed"],
        "page_images_committed": packet["page_images_committed"],
        "screenshots_committed": packet["screenshots_committed"],
        "warnings": packet["warnings"],
        "boundary_notes": packet["boundary_notes"],
        "can_claim_source_rights_review_request_packet": packet[
            "can_claim_source_rights_review_request_packet"
        ],
        "can_claim_rights_clearance": packet["can_claim_rights_clearance"],
        "can_claim_transcript_collection": packet["can_claim_transcript_collection"],
        "can_claim_reference_transcript_available": packet[
            "can_claim_reference_transcript_available"
        ],
        "can_claim_ocr_quality": packet["can_claim_ocr_quality"],
        "can_claim_robust_pdf_extraction": packet[
            "can_claim_robust_pdf_extraction"
        ],
        "next_gate": packet["recommended_next_gate"],
    }


def build_source_policy_no_native_text_ocr_source_rights_review_request_packet_report(
    summary: dict[str, Any],
) -> str:
    lines = [
        "# Source-policy No-native-text OCR Source Rights Review Request Packet",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report records a source-rights review request packet for the preserved NARA no-native-text route.",
        "",
        "It is not rights clearance evidence.",
        "",
        "It is not request-sent evidence.",
        "",
        "It is not source-rights approval evidence.",
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
        f"packet_status -> {summary['packet_status']}",
        f"previous_gate -> {summary['previous_gate']}",
        f"target_fixture_id -> {summary['target_fixture_id']}",
        f"publisher -> {summary['publisher']}",
        f"source_sha256 -> {summary['source_sha256']}",
        f"source_policy_url -> {summary['source_policy_url']}",
        f"owner_transcript_collection_plan_phase_marker -> {summary['owner_transcript_collection_plan_phase_marker']}",
        f"request_scope -> {summary['request_scope']}",
        f"request_question_count -> {summary['request_question_count']}",
        f"proposed_use_scope -> {summary['proposed_use_scope']}",
        f"material_requested_for_review_count -> {summary['material_requested_for_review_count']}",
        f"target_page_count -> {summary['target_page_count']}",
        f"repository_commit_policy -> {summary['repository_commit_policy']}",
        f"request_packet_prepared -> {_format_bool(summary['request_packet_prepared'])}",
        f"request_sent -> {_format_bool(summary['request_sent'])}",
        f"rights_response_received -> {_format_bool(summary['rights_response_received'])}",
        f"source_rights_owner_approval_recorded -> {_format_bool(summary['source_rights_owner_approval_recorded'])}",
        f"source_rights_decision_recorded -> {_format_bool(summary['source_rights_decision_recorded'])}",
        f"transcript_collection_performed -> {_format_bool(summary['transcript_collection_performed'])}",
        f"reference_text_available -> {_format_bool(summary['reference_text_available'])}",
        f"full_reference_transcript_available -> {_format_bool(summary['full_reference_transcript_available'])}",
        f"reference_text_commit_allowed -> {_format_bool(summary['reference_text_commit_allowed'])}",
        f"transcript_hash_committed -> {_format_bool(summary['transcript_hash_committed'])}",
        f"reference_text_hash_committed -> {_format_bool(summary['reference_text_hash_committed'])}",
        f"quality_eval_performed -> {_format_bool(summary['quality_eval_performed'])}",
        f"cer_computed -> {_format_bool(summary['cer_computed'])}",
        f"wer_computed -> {_format_bool(summary['wer_computed'])}",
        f"metric_candidates_status -> {summary['metric_candidates_status']}",
        f"raw_reference_text_committed -> {_format_bool(summary['raw_reference_text_committed'])}",
        f"raw_ocr_text_committed -> {_format_bool(summary['raw_ocr_text_committed'])}",
        f"source_pdf_committed -> {_format_bool(summary['source_pdf_committed'])}",
        f"download_cache_committed -> {_format_bool(summary['download_cache_committed'])}",
        f"page_images_committed -> {_format_bool(summary['page_images_committed'])}",
        f"screenshots_committed -> {_format_bool(summary['screenshots_committed'])}",
        f"can_claim_source_rights_review_request_packet -> {_format_bool(summary['can_claim_source_rights_review_request_packet'])}",
        f"can_claim_rights_clearance -> {_format_bool(summary['can_claim_rights_clearance'])}",
        f"can_claim_transcript_collection -> {_format_bool(summary['can_claim_transcript_collection'])}",
        f"can_claim_reference_transcript_available -> {_format_bool(summary['can_claim_reference_transcript_available'])}",
        f"can_claim_ocr_quality -> {_format_bool(summary['can_claim_ocr_quality'])}",
        f"can_claim_robust_pdf_extraction -> {_format_bool(summary['can_claim_robust_pdf_extraction'])}",
        "",
        "## Rights Review Questions",
        "",
    ]
    for question in summary["request_questions"]:
        lines.append(f"- {question}")

    lines.extend(["", "## Material Requested For Review", ""])
    for material in summary["material_requested_for_review"]:
        lines.append(f"- {material}")

    lines.extend(["", "## Metric Candidates", ""])
    for metric in summary["metric_candidates"]:
        lines.append(f"- {metric}")
    lines.extend(["", f"Status: {summary['metric_candidates_status']}."])

    lines.extend(["", "## Warnings", ""])
    for warning in summary["warnings"]:
        lines.append(f"- {warning}")

    lines.extend(["", "## Next Gate", "", f"- {summary['next_gate']}", ""])
    lines.extend(["## Boundary Notes", ""])
    for note in summary["boundary_notes"]:
        lines.append(f"- {note}")

    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "This is a deterministic source-rights review request packet only.",
            "",
            "It does not send a request or record a response.",
            "",
            "It does not record rights clearance or source-rights owner approval.",
            "",
            "It does not collect, inspect, or commit a reference transcript.",
            "",
            "It does not commit transcript hashes.",
            "",
            "It keeps CER and WER blocked until rights decision and reference text exist.",
            "",
            "It does not prove rights clearance, request delivery, source-rights approval, transcript collection, reference transcript availability, OCR quality, arbitrary-market PDF OCR reliability, arbitrary-market PDF parsing reliability, layout fidelity, rendered visual fidelity, image/chart interpretation, or robust PDF extraction.",
            "",
            "This is not hosted deployment evidence.",
            "",
            "This is not external reviewer feedback.",
            "",
            "This is not product-complete.",
        ]
    )
    return "\n".join(lines) + "\n"


def validate_source_policy_no_native_text_ocr_source_rights_review_request_packet(
    payload: dict[str, Any],
) -> None:
    _reject_raw_text_fields(payload)

    expected_values = {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "packet_status": "source_rights_review_request_packet_prepared",
        "target_fixture_id": TARGET_FIXTURE_ID,
        "publisher": TARGET_PUBLISHER,
        "source_url": TARGET_SOURCE_URL,
        "source_policy_url": TARGET_POLICY_URL,
        "source_sha256": TARGET_SHA256,
        "source_sha256_algorithm": "sha256",
        "owner_transcript_collection_plan_phase_marker": PREVIOUS_GATE,
        "request_scope": "rights_review_request_only",
        "request_questions": RIGHTS_REVIEW_QUESTIONS,
        "request_question_count": len(RIGHTS_REVIEW_QUESTIONS),
        "proposed_use_scope": (
            "internal_owner_runtime_reference_transcript_for_ocr_quality_eval"
        ),
        "material_requested_for_review": MATERIAL_REQUESTED_FOR_REVIEW,
        "material_requested_for_review_count": len(MATERIAL_REQUESTED_FOR_REVIEW),
        "target_page_count": TARGET_PAGE_COUNT,
        "repository_commit_policy": "metadata_only_no_transcript_text_or_hash",
        "request_packet_prepared": True,
        "request_sent": False,
        "rights_response_received": False,
        "source_rights_owner_approval_recorded": False,
        "source_rights_decision_recorded": False,
        "transcript_collection_performed": False,
        "reference_text_available": False,
        "full_reference_transcript_available": False,
        "reference_text_commit_allowed": False,
        "transcript_hash_committed": False,
        "reference_text_hash_committed": False,
        "quality_eval_performed": False,
        "cer_computed": False,
        "wer_computed": False,
        "metric_candidates": METRIC_CANDIDATES,
        "metric_candidates_status": (
            "blocked_until_rights_decision_and_reference_text_exist"
        ),
        "minimum_next_artifact": "owner rights decision record",
        "raw_reference_text_committed": False,
        "raw_ocr_text_committed": False,
        "source_pdf_committed": False,
        "download_cache_committed": False,
        "page_images_committed": False,
        "screenshots_committed": False,
        "can_claim_source_rights_review_request_packet": True,
        "can_claim_rights_clearance": False,
        "can_claim_transcript_collection": False,
        "can_claim_reference_transcript_available": False,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
        "recommended_next_gate": NEXT_GATE,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(
                f"source-policy OCR source rights review request packet {field} must be {expected!r}"
            )

    for field in ["warnings", "boundary_notes"]:
        value = payload.get(field)
        if not isinstance(value, list) or not value:
            raise ValueError(
                f"source-policy OCR source rights review request packet {field} must be a non-empty list"
            )

    for note in BOUNDARY_NOTES:
        if note not in payload["boundary_notes"]:
            raise ValueError(
                f"source-policy OCR source rights review request packet missing boundary note: {note}"
            )


def _validate_owner_transcript_collection_plan(payload: dict[str, Any]) -> None:
    expected_values = {
        "phase_marker": PREVIOUS_GATE,
        "target_fixture_id": TARGET_FIXTURE_ID,
        "publisher": TARGET_PUBLISHER,
        "source_url": TARGET_SOURCE_URL,
        "source_policy_url": TARGET_POLICY_URL,
        "source_sha256": TARGET_SHA256,
        "plan_status": "owner_transcript_collection_planned",
        "collection_scope": "owner_runtime_manual_transcript_collection_plan_only",
        "source_rights_review_required": True,
        "source_rights_owner_approval_recorded": False,
        "source_rights_request_packet_required": True,
        "repository_commit_policy": "metadata_only_no_transcript_text_or_hash",
        "transcript_collection_performed": False,
        "reference_text_available": False,
        "reference_text_commit_allowed": False,
        "transcript_hash_committed": False,
        "quality_eval_performed": False,
        "cer_computed": False,
        "wer_computed": False,
        "raw_reference_text_committed": False,
        "raw_ocr_text_committed": False,
        "can_claim_owner_transcript_collection_plan": True,
        "can_claim_transcript_collection": False,
        "can_claim_reference_transcript_available": False,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(
                f"owner transcript collection plan {field} must be {expected!r}"
            )


def _reject_raw_text_fields(value: Any) -> None:
    if isinstance(value, dict):
        for key, nested in value.items():
            if key in _RAW_TEXT_FIELDS:
                raise ValueError(
                    f"source-policy OCR source rights review request packet must not commit {key}"
                )
            _reject_raw_text_fields(nested)
    elif isinstance(value, list):
        for nested in value:
            _reject_raw_text_fields(nested)


def _format_bool(value: object) -> str:
    return "true" if value is True else "false"
