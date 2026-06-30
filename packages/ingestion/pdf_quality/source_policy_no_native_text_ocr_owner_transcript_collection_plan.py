from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PHASE_MARKER = "source_policy_no_native_text_ocr_owner_transcript_collection_plan_v0"
PREVIOUS_GATE = "source_policy_no_native_text_ocr_transcript_reference_pack_v0"
CLAIM_BOUNDARY = (
    "source_policy_no_native_text_ocr_owner_transcript_collection_plan_not_collection"
)
NEXT_GATE = "source_policy_no_native_text_ocr_source_rights_review_request_packet_v0"

TARGET_FIXTURE_ID = "nara_911_mfr_00282_no_native_text_candidate"
TARGET_PUBLISHER = "National Archives and Records Administration"
TARGET_SOURCE_URL = (
    "https://nara-media-001.s3.amazonaws.com/arcmedia/9-11/MFR/"
    "t-0148-911MFR-00282.pdf"
)
TARGET_POLICY_URL = "https://www.archives.gov/global-pages/privacy.html"
TARGET_SHA256 = "6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba"
TARGET_PAGE_COUNT = 4
PLANNED_REFERENCE_PAGE_COUNT = 4
PLANNED_COLLECTION_STEPS = [
    "confirm_item_specific_rights_status",
    "prepare_owner_runtime_workspace",
    "create_page_level_manual_reference_transcript_outside_repo",
    "apply_normalization_rules",
    "record_alignment_policy",
    "review_metric_eligibility",
    "decide_commit_or_hash_policy_after_rights_review",
]
METRIC_CANDIDATES = ["cer", "wer"]
BOUNDARY_NOTES = [
    "source-policy no-native-text OCR owner transcript collection plan",
    "not transcript collection evidence",
    "not source-rights approval evidence",
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
    "This is an owner-runtime transcript collection plan only.",
    "It does not collect or commit a reference transcript.",
    "It does not record source-rights owner approval as completed.",
    "It does not commit transcript hashes.",
    "CER/WER remain blocked until reference text and rights review exist.",
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


def build_source_policy_no_native_text_ocr_owner_transcript_collection_plan(
    transcript_reference_pack: dict[str, Any],
) -> dict[str, Any]:
    _validate_transcript_reference_pack(transcript_reference_pack)
    return {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "plan_status": "owner_transcript_collection_planned",
        "target_fixture_id": transcript_reference_pack["target_fixture_id"],
        "publisher": transcript_reference_pack["publisher"],
        "source_url": transcript_reference_pack["source_url"],
        "source_policy_url": transcript_reference_pack["source_policy_url"],
        "source_sha256": transcript_reference_pack["source_sha256"],
        "source_sha256_algorithm": "sha256",
        "transcript_reference_pack_phase_marker": transcript_reference_pack[
            "phase_marker"
        ],
        "collection_scope": "owner_runtime_manual_transcript_collection_plan_only",
        "target_page_count": TARGET_PAGE_COUNT,
        "planned_reference_page_count": PLANNED_REFERENCE_PAGE_COUNT,
        "planned_collection_steps": list(PLANNED_COLLECTION_STEPS),
        "planned_collection_step_count": len(PLANNED_COLLECTION_STEPS),
        "source_policy_review_status": "metadata_review_only",
        "source_rights_review_required": True,
        "source_rights_owner_approval_recorded": False,
        "source_rights_request_packet_required": True,
        "owner_runtime_storage_required": True,
        "repository_commit_policy": "metadata_only_no_transcript_text_or_hash",
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
            "blocked_until_reference_text_and_rights_review_exist"
        ),
        "minimum_next_artifact": "source-rights review request packet",
        "raw_reference_text_committed": False,
        "raw_ocr_text_committed": False,
        "source_pdf_committed": False,
        "download_cache_committed": False,
        "page_images_committed": False,
        "screenshots_committed": False,
        "warnings": list(WARNING_MESSAGES),
        "boundary_notes": list(BOUNDARY_NOTES),
        "can_claim_owner_transcript_collection_plan": True,
        "can_claim_transcript_collection": False,
        "can_claim_reference_transcript_available": False,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
        "recommended_next_gate": NEXT_GATE,
    }


def load_source_policy_no_native_text_ocr_owner_transcript_collection_plan(
    path: Path | str,
) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    validate_source_policy_no_native_text_ocr_owner_transcript_collection_plan(
        payload
    )
    return payload


def build_source_policy_no_native_text_ocr_owner_transcript_collection_plan_summary(
    plan: dict[str, Any],
) -> dict[str, Any]:
    validate_source_policy_no_native_text_ocr_owner_transcript_collection_plan(plan)
    return {
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "plan_status": plan["plan_status"],
        "target_fixture_id": plan["target_fixture_id"],
        "publisher": plan["publisher"],
        "source_url": plan["source_url"],
        "source_policy_url": plan["source_policy_url"],
        "source_sha256": plan["source_sha256"],
        "transcript_reference_pack_phase_marker": plan[
            "transcript_reference_pack_phase_marker"
        ],
        "collection_scope": plan["collection_scope"],
        "target_page_count": plan["target_page_count"],
        "planned_reference_page_count": plan["planned_reference_page_count"],
        "planned_collection_steps": plan["planned_collection_steps"],
        "planned_collection_step_count": plan["planned_collection_step_count"],
        "source_policy_review_status": plan["source_policy_review_status"],
        "source_rights_review_required": plan["source_rights_review_required"],
        "source_rights_owner_approval_recorded": plan[
            "source_rights_owner_approval_recorded"
        ],
        "source_rights_request_packet_required": plan[
            "source_rights_request_packet_required"
        ],
        "owner_runtime_storage_required": plan["owner_runtime_storage_required"],
        "repository_commit_policy": plan["repository_commit_policy"],
        "transcript_collection_performed": plan["transcript_collection_performed"],
        "reference_text_available": plan["reference_text_available"],
        "full_reference_transcript_available": plan[
            "full_reference_transcript_available"
        ],
        "reference_text_commit_allowed": plan["reference_text_commit_allowed"],
        "transcript_hash_committed": plan["transcript_hash_committed"],
        "reference_text_hash_committed": plan["reference_text_hash_committed"],
        "quality_eval_performed": plan["quality_eval_performed"],
        "cer_computed": plan["cer_computed"],
        "wer_computed": plan["wer_computed"],
        "metric_candidates": plan["metric_candidates"],
        "metric_candidates_status": plan["metric_candidates_status"],
        "minimum_next_artifact": plan["minimum_next_artifact"],
        "raw_reference_text_committed": plan["raw_reference_text_committed"],
        "raw_ocr_text_committed": plan["raw_ocr_text_committed"],
        "source_pdf_committed": plan["source_pdf_committed"],
        "download_cache_committed": plan["download_cache_committed"],
        "page_images_committed": plan["page_images_committed"],
        "screenshots_committed": plan["screenshots_committed"],
        "warnings": plan["warnings"],
        "boundary_notes": plan["boundary_notes"],
        "can_claim_owner_transcript_collection_plan": plan[
            "can_claim_owner_transcript_collection_plan"
        ],
        "can_claim_transcript_collection": plan["can_claim_transcript_collection"],
        "can_claim_reference_transcript_available": plan[
            "can_claim_reference_transcript_available"
        ],
        "can_claim_ocr_quality": plan["can_claim_ocr_quality"],
        "can_claim_robust_pdf_extraction": plan[
            "can_claim_robust_pdf_extraction"
        ],
        "next_gate": plan["recommended_next_gate"],
    }


def build_source_policy_no_native_text_ocr_owner_transcript_collection_plan_report(
    summary: dict[str, Any],
) -> str:
    lines = [
        "# Source-policy No-native-text OCR Owner Transcript Collection Plan",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report records an owner-runtime transcript collection plan for the preserved NARA no-native-text route.",
        "",
        "It is not transcript collection evidence.",
        "",
        "It is not source-rights approval evidence.",
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
        f"plan_status -> {summary['plan_status']}",
        f"previous_gate -> {summary['previous_gate']}",
        f"target_fixture_id -> {summary['target_fixture_id']}",
        f"publisher -> {summary['publisher']}",
        f"source_sha256 -> {summary['source_sha256']}",
        f"source_policy_url -> {summary['source_policy_url']}",
        f"transcript_reference_pack_phase_marker -> {summary['transcript_reference_pack_phase_marker']}",
        f"collection_scope -> {summary['collection_scope']}",
        f"target_page_count -> {summary['target_page_count']}",
        f"planned_reference_page_count -> {summary['planned_reference_page_count']}",
        f"planned_collection_step_count -> {summary['planned_collection_step_count']}",
        f"source_policy_review_status -> {summary['source_policy_review_status']}",
        f"source_rights_review_required -> {_format_bool(summary['source_rights_review_required'])}",
        f"source_rights_owner_approval_recorded -> {_format_bool(summary['source_rights_owner_approval_recorded'])}",
        f"source_rights_request_packet_required -> {_format_bool(summary['source_rights_request_packet_required'])}",
        f"owner_runtime_storage_required -> {_format_bool(summary['owner_runtime_storage_required'])}",
        f"repository_commit_policy -> {summary['repository_commit_policy']}",
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
        f"can_claim_owner_transcript_collection_plan -> {_format_bool(summary['can_claim_owner_transcript_collection_plan'])}",
        f"can_claim_transcript_collection -> {_format_bool(summary['can_claim_transcript_collection'])}",
        f"can_claim_reference_transcript_available -> {_format_bool(summary['can_claim_reference_transcript_available'])}",
        f"can_claim_ocr_quality -> {_format_bool(summary['can_claim_ocr_quality'])}",
        f"can_claim_robust_pdf_extraction -> {_format_bool(summary['can_claim_robust_pdf_extraction'])}",
        "",
        "## Planned Collection Steps",
        "",
    ]
    for step in summary["planned_collection_steps"]:
        lines.append(f"- {step}")

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
            "This is a deterministic owner-runtime transcript collection plan only.",
            "",
            "It does not collect, inspect, or commit a reference transcript.",
            "",
            "It does not record source-rights owner approval as completed.",
            "",
            "It does not commit transcript hashes.",
            "",
            "It keeps CER and WER blocked until reference text and item-specific rights review exist.",
            "",
            "It does not prove transcript collection, source-rights approval, reference transcript availability, OCR quality, arbitrary-market PDF OCR reliability, arbitrary-market PDF parsing reliability, layout fidelity, rendered visual fidelity, image/chart interpretation, or robust PDF extraction.",
            "",
            "This is not hosted deployment evidence.",
            "",
            "This is not external reviewer feedback.",
            "",
            "This is not product-complete.",
        ]
    )
    return "\n".join(lines) + "\n"


def validate_source_policy_no_native_text_ocr_owner_transcript_collection_plan(
    payload: dict[str, Any],
) -> None:
    _reject_raw_text_fields(payload)

    expected_values = {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "plan_status": "owner_transcript_collection_planned",
        "target_fixture_id": TARGET_FIXTURE_ID,
        "publisher": TARGET_PUBLISHER,
        "source_url": TARGET_SOURCE_URL,
        "source_policy_url": TARGET_POLICY_URL,
        "source_sha256": TARGET_SHA256,
        "source_sha256_algorithm": "sha256",
        "transcript_reference_pack_phase_marker": PREVIOUS_GATE,
        "collection_scope": "owner_runtime_manual_transcript_collection_plan_only",
        "target_page_count": TARGET_PAGE_COUNT,
        "planned_reference_page_count": PLANNED_REFERENCE_PAGE_COUNT,
        "planned_collection_steps": PLANNED_COLLECTION_STEPS,
        "planned_collection_step_count": len(PLANNED_COLLECTION_STEPS),
        "source_policy_review_status": "metadata_review_only",
        "source_rights_review_required": True,
        "source_rights_owner_approval_recorded": False,
        "source_rights_request_packet_required": True,
        "owner_runtime_storage_required": True,
        "repository_commit_policy": "metadata_only_no_transcript_text_or_hash",
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
            "blocked_until_reference_text_and_rights_review_exist"
        ),
        "minimum_next_artifact": "source-rights review request packet",
        "raw_reference_text_committed": False,
        "raw_ocr_text_committed": False,
        "source_pdf_committed": False,
        "download_cache_committed": False,
        "page_images_committed": False,
        "screenshots_committed": False,
        "can_claim_owner_transcript_collection_plan": True,
        "can_claim_transcript_collection": False,
        "can_claim_reference_transcript_available": False,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
        "recommended_next_gate": NEXT_GATE,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(
                f"source-policy OCR owner transcript collection plan {field} must be {expected!r}"
            )

    for field in ["warnings", "boundary_notes"]:
        value = payload.get(field)
        if not isinstance(value, list) or not value:
            raise ValueError(
                f"source-policy OCR owner transcript collection plan {field} must be a non-empty list"
            )

    for note in BOUNDARY_NOTES:
        if note not in payload["boundary_notes"]:
            raise ValueError(
                f"source-policy OCR owner transcript collection plan missing boundary note: {note}"
            )


def _validate_transcript_reference_pack(payload: dict[str, Any]) -> None:
    expected_values = {
        "phase_marker": PREVIOUS_GATE,
        "target_fixture_id": TARGET_FIXTURE_ID,
        "publisher": TARGET_PUBLISHER,
        "source_url": TARGET_SOURCE_URL,
        "source_policy_url": TARGET_POLICY_URL,
        "source_sha256": TARGET_SHA256,
        "reference_pack_status": "sanitized_transcript_reference_pack_boundary",
        "reference_pack_claim_scope": "sanitized_boundary_only",
        "source_policy_review_status": "reviewed_for_metadata_only",
        "project_owner_approval_recorded": True,
        "source_rights_owner_approval_recorded": False,
        "source_rights_owner_approval_required_before_transcript": True,
        "reference_text_available": False,
        "full_reference_transcript_available": False,
        "transcript_collection_performed": False,
        "quality_eval_performed": False,
        "cer_computed": False,
        "wer_computed": False,
        "raw_reference_text_committed": False,
        "raw_ocr_text_committed": False,
        "can_claim_transcript_reference_pack": True,
        "can_claim_reference_transcript_available": False,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(
                f"transcript reference pack {field} must be {expected!r}"
            )


def _reject_raw_text_fields(value: Any) -> None:
    if isinstance(value, dict):
        for key, nested in value.items():
            if key in _RAW_TEXT_FIELDS:
                raise ValueError(
                    f"source-policy OCR owner transcript collection plan must not commit {key}"
                )
            _reject_raw_text_fields(nested)
    elif isinstance(value, list):
        for nested in value:
            _reject_raw_text_fields(nested)


def _format_bool(value: object) -> str:
    return "true" if value is True else "false"
