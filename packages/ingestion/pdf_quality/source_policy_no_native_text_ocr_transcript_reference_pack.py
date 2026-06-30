from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PHASE_MARKER = "source_policy_no_native_text_ocr_transcript_reference_pack_v0"
PREVIOUS_GATE = "source_policy_no_native_text_ocr_transcript_reference_plan_v0"
CLAIM_BOUNDARY = (
    "source_policy_no_native_text_ocr_transcript_reference_pack_boundary_not_transcript"
)
NEXT_GATE = "source_policy_no_native_text_ocr_owner_transcript_collection_plan_v0"

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
REQUIRED_REFERENCE_UNITS = [
    "source_policy_review",
    "owner_approval",
    "page_level_reference_transcript",
    "normalization_rules",
    "alignment_policy",
    "metric_eligibility_review",
]
METRIC_CANDIDATES = ["cer", "wer"]
BOUNDARY_NOTES = [
    "source-policy no-native-text OCR transcript reference pack boundary",
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
    "This is a sanitized transcript-reference pack boundary only.",
    "It does not collect or commit a reference transcript.",
    "It does not inspect or commit raw OCR text.",
    "The source rights owner has not approved committing transcript text.",
    "CER/WER remain blocked until reference text exists.",
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


def build_source_policy_no_native_text_ocr_transcript_reference_pack(
    transcript_reference_plan: dict[str, Any],
) -> dict[str, Any]:
    _validate_transcript_reference_plan(transcript_reference_plan)
    return {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "reference_pack_status": "sanitized_transcript_reference_pack_boundary",
        "target_fixture_id": transcript_reference_plan["target_fixture_id"],
        "publisher": transcript_reference_plan["publisher"],
        "source_url": transcript_reference_plan["source_url"],
        "source_policy_url": transcript_reference_plan["source_policy_url"],
        "source_sha256": transcript_reference_plan["source_sha256"],
        "source_sha256_algorithm": "sha256",
        "transcript_reference_plan_phase_marker": transcript_reference_plan[
            "phase_marker"
        ],
        "reference_unit_type": "page_level_transcript_reference_pack_boundary",
        "target_page_count": TARGET_PAGE_COUNT,
        "planned_reference_page_count": PLANNED_REFERENCE_PAGE_COUNT,
        "required_reference_units": list(REQUIRED_REFERENCE_UNITS),
        "required_reference_unit_count": len(REQUIRED_REFERENCE_UNITS),
        "reference_pack_created": True,
        "reference_pack_claim_scope": "sanitized_boundary_only",
        "source_policy_review_status": "reviewed_for_metadata_only",
        "project_owner_approval_recorded": True,
        "source_rights_owner_approval_recorded": False,
        "source_rights_owner_approval_required_before_transcript": True,
        "reference_text_available": False,
        "full_reference_transcript_available": False,
        "transcript_collection_performed": False,
        "transcript_hash_committed": False,
        "reference_text_hash_committed": False,
        "quality_eval_performed": False,
        "cer_computed": False,
        "wer_computed": False,
        "metric_candidates": list(METRIC_CANDIDATES),
        "metric_candidates_status": "blocked_until_reference_text_exists",
        "minimum_next_artifact": (
            "source-policy-reviewed owner transcript collection plan"
        ),
        "raw_reference_text_committed": False,
        "raw_ocr_text_committed": False,
        "source_pdf_committed": False,
        "download_cache_committed": False,
        "page_images_committed": False,
        "screenshots_committed": False,
        "warnings": list(WARNING_MESSAGES),
        "boundary_notes": list(BOUNDARY_NOTES),
        "can_claim_transcript_reference_pack": True,
        "can_claim_reference_transcript_available": False,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
        "recommended_next_gate": NEXT_GATE,
    }


def load_source_policy_no_native_text_ocr_transcript_reference_pack(
    path: Path | str,
) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    validate_source_policy_no_native_text_ocr_transcript_reference_pack(payload)
    return payload


def build_source_policy_no_native_text_ocr_transcript_reference_pack_summary(
    pack: dict[str, Any],
) -> dict[str, Any]:
    validate_source_policy_no_native_text_ocr_transcript_reference_pack(pack)
    return {
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "reference_pack_status": pack["reference_pack_status"],
        "target_fixture_id": pack["target_fixture_id"],
        "publisher": pack["publisher"],
        "source_url": pack["source_url"],
        "source_policy_url": pack["source_policy_url"],
        "source_sha256": pack["source_sha256"],
        "transcript_reference_plan_phase_marker": pack[
            "transcript_reference_plan_phase_marker"
        ],
        "reference_unit_type": pack["reference_unit_type"],
        "target_page_count": pack["target_page_count"],
        "planned_reference_page_count": pack["planned_reference_page_count"],
        "required_reference_units": pack["required_reference_units"],
        "required_reference_unit_count": pack["required_reference_unit_count"],
        "reference_pack_created": pack["reference_pack_created"],
        "reference_pack_claim_scope": pack["reference_pack_claim_scope"],
        "source_policy_review_status": pack["source_policy_review_status"],
        "project_owner_approval_recorded": pack["project_owner_approval_recorded"],
        "source_rights_owner_approval_recorded": pack[
            "source_rights_owner_approval_recorded"
        ],
        "source_rights_owner_approval_required_before_transcript": pack[
            "source_rights_owner_approval_required_before_transcript"
        ],
        "reference_text_available": pack["reference_text_available"],
        "full_reference_transcript_available": pack[
            "full_reference_transcript_available"
        ],
        "transcript_collection_performed": pack["transcript_collection_performed"],
        "transcript_hash_committed": pack["transcript_hash_committed"],
        "reference_text_hash_committed": pack["reference_text_hash_committed"],
        "quality_eval_performed": pack["quality_eval_performed"],
        "cer_computed": pack["cer_computed"],
        "wer_computed": pack["wer_computed"],
        "metric_candidates": pack["metric_candidates"],
        "metric_candidates_status": pack["metric_candidates_status"],
        "minimum_next_artifact": pack["minimum_next_artifact"],
        "raw_reference_text_committed": pack["raw_reference_text_committed"],
        "raw_ocr_text_committed": pack["raw_ocr_text_committed"],
        "source_pdf_committed": pack["source_pdf_committed"],
        "download_cache_committed": pack["download_cache_committed"],
        "page_images_committed": pack["page_images_committed"],
        "screenshots_committed": pack["screenshots_committed"],
        "warnings": pack["warnings"],
        "boundary_notes": pack["boundary_notes"],
        "can_claim_transcript_reference_pack": pack[
            "can_claim_transcript_reference_pack"
        ],
        "can_claim_reference_transcript_available": pack[
            "can_claim_reference_transcript_available"
        ],
        "can_claim_ocr_quality": pack["can_claim_ocr_quality"],
        "can_claim_robust_pdf_extraction": pack[
            "can_claim_robust_pdf_extraction"
        ],
        "next_gate": pack["recommended_next_gate"],
    }


def build_source_policy_no_native_text_ocr_transcript_reference_pack_report(
    summary: dict[str, Any],
) -> str:
    lines = [
        "# Source-policy No-native-text OCR Transcript Reference Pack",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report records a sanitized transcript-reference pack boundary for the preserved NARA no-native-text route.",
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
        f"reference_pack_status -> {summary['reference_pack_status']}",
        f"previous_gate -> {summary['previous_gate']}",
        f"target_fixture_id -> {summary['target_fixture_id']}",
        f"publisher -> {summary['publisher']}",
        f"source_sha256 -> {summary['source_sha256']}",
        f"source_policy_url -> {summary['source_policy_url']}",
        f"transcript_reference_plan_phase_marker -> {summary['transcript_reference_plan_phase_marker']}",
        f"reference_unit_type -> {summary['reference_unit_type']}",
        f"target_page_count -> {summary['target_page_count']}",
        f"planned_reference_page_count -> {summary['planned_reference_page_count']}",
        f"required_reference_unit_count -> {summary['required_reference_unit_count']}",
        f"reference_pack_created -> {_format_bool(summary['reference_pack_created'])}",
        f"reference_pack_claim_scope -> {summary['reference_pack_claim_scope']}",
        f"source_policy_review_status -> {summary['source_policy_review_status']}",
        f"project_owner_approval_recorded -> {_format_bool(summary['project_owner_approval_recorded'])}",
        f"source_rights_owner_approval_recorded -> {_format_bool(summary['source_rights_owner_approval_recorded'])}",
        f"source_rights_owner_approval_required_before_transcript -> {_format_bool(summary['source_rights_owner_approval_required_before_transcript'])}",
        f"reference_text_available -> {_format_bool(summary['reference_text_available'])}",
        f"full_reference_transcript_available -> {_format_bool(summary['full_reference_transcript_available'])}",
        f"transcript_collection_performed -> {_format_bool(summary['transcript_collection_performed'])}",
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
        f"can_claim_transcript_reference_pack -> {_format_bool(summary['can_claim_transcript_reference_pack'])}",
        f"can_claim_reference_transcript_available -> {_format_bool(summary['can_claim_reference_transcript_available'])}",
        f"can_claim_ocr_quality -> {_format_bool(summary['can_claim_ocr_quality'])}",
        f"can_claim_robust_pdf_extraction -> {_format_bool(summary['can_claim_robust_pdf_extraction'])}",
        "",
        "## Required Future Reference Units",
        "",
    ]
    for unit in summary["required_reference_units"]:
        lines.append(f"- {unit}")

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
            "This is a deterministic sanitized transcript-reference pack boundary only.",
            "",
            "It does not collect, inspect, or commit a reference transcript.",
            "",
            "It does not inspect or commit raw OCR text.",
            "",
            "It keeps CER and WER blocked until owner-approved transcript-level reference data exists.",
            "",
            "It does not prove reference transcript availability, OCR quality, arbitrary-market PDF OCR reliability, arbitrary-market PDF parsing reliability, layout fidelity, rendered visual fidelity, image/chart interpretation, or robust PDF extraction.",
            "",
            "This is not hosted deployment evidence.",
            "",
            "This is not external reviewer feedback.",
            "",
            "This is not product-complete.",
        ]
    )
    return "\n".join(lines) + "\n"


def validate_source_policy_no_native_text_ocr_transcript_reference_pack(
    payload: dict[str, Any],
) -> None:
    _reject_raw_text_fields(payload)

    expected_values = {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "reference_pack_status": "sanitized_transcript_reference_pack_boundary",
        "target_fixture_id": TARGET_FIXTURE_ID,
        "publisher": TARGET_PUBLISHER,
        "source_url": TARGET_SOURCE_URL,
        "source_policy_url": TARGET_POLICY_URL,
        "source_sha256": TARGET_SHA256,
        "source_sha256_algorithm": "sha256",
        "transcript_reference_plan_phase_marker": PREVIOUS_GATE,
        "reference_unit_type": "page_level_transcript_reference_pack_boundary",
        "target_page_count": TARGET_PAGE_COUNT,
        "planned_reference_page_count": PLANNED_REFERENCE_PAGE_COUNT,
        "required_reference_units": REQUIRED_REFERENCE_UNITS,
        "required_reference_unit_count": len(REQUIRED_REFERENCE_UNITS),
        "reference_pack_created": True,
        "reference_pack_claim_scope": "sanitized_boundary_only",
        "source_policy_review_status": "reviewed_for_metadata_only",
        "project_owner_approval_recorded": True,
        "source_rights_owner_approval_recorded": False,
        "source_rights_owner_approval_required_before_transcript": True,
        "reference_text_available": False,
        "full_reference_transcript_available": False,
        "transcript_collection_performed": False,
        "transcript_hash_committed": False,
        "reference_text_hash_committed": False,
        "quality_eval_performed": False,
        "cer_computed": False,
        "wer_computed": False,
        "metric_candidates": METRIC_CANDIDATES,
        "metric_candidates_status": "blocked_until_reference_text_exists",
        "minimum_next_artifact": (
            "source-policy-reviewed owner transcript collection plan"
        ),
        "raw_reference_text_committed": False,
        "raw_ocr_text_committed": False,
        "source_pdf_committed": False,
        "download_cache_committed": False,
        "page_images_committed": False,
        "screenshots_committed": False,
        "can_claim_transcript_reference_pack": True,
        "can_claim_reference_transcript_available": False,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
        "recommended_next_gate": NEXT_GATE,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(
                f"source-policy OCR transcript reference pack {field} must be {expected!r}"
            )

    for field in ["warnings", "boundary_notes"]:
        value = payload.get(field)
        if not isinstance(value, list) or not value:
            raise ValueError(
                f"source-policy OCR transcript reference pack {field} must be a non-empty list"
            )

    for note in BOUNDARY_NOTES:
        if note not in payload["boundary_notes"]:
            raise ValueError(
                f"source-policy OCR transcript reference pack missing boundary note: {note}"
            )


def _validate_transcript_reference_plan(payload: dict[str, Any]) -> None:
    expected_values = {
        "phase_marker": PREVIOUS_GATE,
        "target_fixture_id": TARGET_FIXTURE_ID,
        "publisher": TARGET_PUBLISHER,
        "source_url": TARGET_SOURCE_URL,
        "source_policy_url": TARGET_POLICY_URL,
        "source_sha256": TARGET_SHA256,
        "plan_status": "planned_transcript_reference_contract",
        "reference_unit_type": "page_level_transcript_plan",
        "target_page_count": TARGET_PAGE_COUNT,
        "minimum_reference_pages": PLANNED_REFERENCE_PAGE_COUNT,
        "required_reference_units": REQUIRED_REFERENCE_UNITS,
        "required_reference_unit_count": len(REQUIRED_REFERENCE_UNITS),
        "full_reference_transcript_available": False,
        "transcript_collection_performed": False,
        "reference_pack_created": False,
        "quality_eval_performed": False,
        "cer_computed": False,
        "wer_computed": False,
        "raw_reference_text_committed": False,
        "raw_ocr_text_committed": False,
        "can_claim_transcript_reference_plan": True,
        "can_claim_transcript_reference_pack": False,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(f"transcript reference plan {field} must be {expected!r}")


def _reject_raw_text_fields(value: Any) -> None:
    if isinstance(value, dict):
        for key, nested in value.items():
            if key in _RAW_TEXT_FIELDS:
                raise ValueError(
                    f"source-policy OCR transcript reference pack must not commit {key}"
                )
            _reject_raw_text_fields(nested)
    elif isinstance(value, list):
        for nested in value:
            _reject_raw_text_fields(nested)


def _format_bool(value: object) -> str:
    return "true" if value is True else "false"
