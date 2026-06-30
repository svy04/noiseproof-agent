from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PHASE_MARKER = "source_policy_no_native_text_ocr_transcript_reference_plan_v0"
PREVIOUS_GATE = "source_policy_no_native_text_ocr_marker_proxy_eval_v0"
CLAIM_BOUNDARY = (
    "source_policy_no_native_text_ocr_transcript_reference_plan_not_ocr_quality"
)
NEXT_GATE = "source_policy_no_native_text_ocr_transcript_reference_pack_v0"

TARGET_FIXTURE_ID = "nara_911_mfr_00282_no_native_text_candidate"
TARGET_PUBLISHER = "National Archives and Records Administration"
TARGET_SOURCE_URL = (
    "https://nara-media-001.s3.amazonaws.com/arcmedia/9-11/MFR/"
    "t-0148-911MFR-00282.pdf"
)
TARGET_POLICY_URL = "https://www.archives.gov/global-pages/privacy.html"
TARGET_SHA256 = "6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba"
TARGET_PAGE_COUNT = 4
MINIMUM_REFERENCE_PAGES = 4
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
    "source-policy no-native-text OCR transcript reference plan",
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
    "This is a transcript/reference planning contract only.",
    "It does not collect or commit a reference transcript.",
    "It does not inspect or commit raw OCR text.",
    "CER/WER remain blocked until transcript-level reference data exists.",
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
    "page_image",
    "page_images",
    "screenshot",
    "screenshots",
}


def build_source_policy_no_native_text_ocr_transcript_reference_plan(
    marker_proxy_eval: dict[str, Any],
) -> dict[str, Any]:
    _validate_marker_proxy_eval(marker_proxy_eval)
    return {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "plan_status": "planned_transcript_reference_contract",
        "target_fixture_id": marker_proxy_eval["target_fixture_id"],
        "publisher": marker_proxy_eval["publisher"],
        "source_url": marker_proxy_eval["source_url"],
        "source_policy_url": marker_proxy_eval["source_policy_url"],
        "source_sha256": marker_proxy_eval["source_sha256"],
        "source_sha256_algorithm": "sha256",
        "marker_proxy_eval_phase_marker": marker_proxy_eval["phase_marker"],
        "reference_unit_type": "page_level_transcript_plan",
        "target_page_count": TARGET_PAGE_COUNT,
        "minimum_reference_pages": MINIMUM_REFERENCE_PAGES,
        "required_reference_units": list(REQUIRED_REFERENCE_UNITS),
        "required_reference_unit_count": len(REQUIRED_REFERENCE_UNITS),
        "owner_approval_required": True,
        "source_policy_review_required": True,
        "full_reference_transcript_required": True,
        "full_reference_transcript_available": False,
        "transcript_collection_performed": False,
        "reference_pack_created": False,
        "quality_eval_performed": False,
        "cer_computed": False,
        "wer_computed": False,
        "metric_candidates": list(METRIC_CANDIDATES),
        "metric_candidates_status": "blocked_until_reference_transcript_exists",
        "minimum_next_artifact": (
            "source-policy-reviewed owner-approved transcript reference pack"
        ),
        "raw_reference_text_committed": False,
        "raw_ocr_text_committed": False,
        "source_pdf_committed": False,
        "download_cache_committed": False,
        "page_images_committed": False,
        "screenshots_committed": False,
        "warnings": list(WARNING_MESSAGES),
        "boundary_notes": list(BOUNDARY_NOTES),
        "can_claim_transcript_reference_plan": True,
        "can_claim_transcript_reference_pack": False,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
        "recommended_next_gate": NEXT_GATE,
    }


def load_source_policy_no_native_text_ocr_transcript_reference_plan(
    path: Path | str,
) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    validate_source_policy_no_native_text_ocr_transcript_reference_plan(payload)
    return payload


def build_source_policy_no_native_text_ocr_transcript_reference_plan_summary(
    plan: dict[str, Any],
) -> dict[str, Any]:
    validate_source_policy_no_native_text_ocr_transcript_reference_plan(plan)
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
        "marker_proxy_eval_phase_marker": plan["marker_proxy_eval_phase_marker"],
        "reference_unit_type": plan["reference_unit_type"],
        "target_page_count": plan["target_page_count"],
        "minimum_reference_pages": plan["minimum_reference_pages"],
        "required_reference_units": plan["required_reference_units"],
        "required_reference_unit_count": plan["required_reference_unit_count"],
        "owner_approval_required": plan["owner_approval_required"],
        "source_policy_review_required": plan["source_policy_review_required"],
        "full_reference_transcript_required": plan[
            "full_reference_transcript_required"
        ],
        "full_reference_transcript_available": plan[
            "full_reference_transcript_available"
        ],
        "transcript_collection_performed": plan["transcript_collection_performed"],
        "reference_pack_created": plan["reference_pack_created"],
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
        "can_claim_transcript_reference_plan": plan[
            "can_claim_transcript_reference_plan"
        ],
        "can_claim_transcript_reference_pack": plan[
            "can_claim_transcript_reference_pack"
        ],
        "can_claim_ocr_quality": plan["can_claim_ocr_quality"],
        "can_claim_robust_pdf_extraction": plan[
            "can_claim_robust_pdf_extraction"
        ],
        "next_gate": plan["recommended_next_gate"],
    }


def build_source_policy_no_native_text_ocr_transcript_reference_plan_report(
    summary: dict[str, Any],
) -> str:
    lines = [
        "# Source-policy No-native-text OCR Transcript Reference Plan",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report records the bounded reference boundary needed before true OCR quality metrics can be considered for the preserved NARA no-native-text route.",
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
        f"marker_proxy_eval_phase_marker -> {summary['marker_proxy_eval_phase_marker']}",
        f"reference_unit_type -> {summary['reference_unit_type']}",
        f"target_page_count -> {summary['target_page_count']}",
        f"minimum_reference_pages -> {summary['minimum_reference_pages']}",
        f"required_reference_unit_count -> {summary['required_reference_unit_count']}",
        f"owner_approval_required -> {_format_bool(summary['owner_approval_required'])}",
        f"source_policy_review_required -> {_format_bool(summary['source_policy_review_required'])}",
        f"full_reference_transcript_required -> {_format_bool(summary['full_reference_transcript_required'])}",
        f"full_reference_transcript_available -> {_format_bool(summary['full_reference_transcript_available'])}",
        f"transcript_collection_performed -> {_format_bool(summary['transcript_collection_performed'])}",
        f"reference_pack_created -> {_format_bool(summary['reference_pack_created'])}",
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
        f"can_claim_transcript_reference_plan -> {_format_bool(summary['can_claim_transcript_reference_plan'])}",
        f"can_claim_transcript_reference_pack -> {_format_bool(summary['can_claim_transcript_reference_pack'])}",
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
            "This is a deterministic transcript/reference planning contract only.",
            "",
            "It does not collect, inspect, or commit a reference transcript.",
            "",
            "It does not inspect or commit raw OCR text.",
            "",
            "It keeps CER and WER blocked until owner-approved transcript-level reference data exists.",
            "",
            "It does not prove OCR quality, arbitrary-market PDF OCR reliability, arbitrary-market PDF parsing reliability, layout fidelity, rendered visual fidelity, image/chart interpretation, or robust PDF extraction.",
            "",
            "This is not hosted deployment evidence.",
            "",
            "This is not external reviewer feedback.",
            "",
            "This is not product-complete.",
        ]
    )
    return "\n".join(lines) + "\n"


def validate_source_policy_no_native_text_ocr_transcript_reference_plan(
    payload: dict[str, Any],
) -> None:
    for field in _RAW_TEXT_FIELDS:
        if field in payload:
            raise ValueError(
                f"source-policy OCR transcript reference plan must not commit {field}"
            )

    expected_values = {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "plan_status": "planned_transcript_reference_contract",
        "target_fixture_id": TARGET_FIXTURE_ID,
        "publisher": TARGET_PUBLISHER,
        "source_url": TARGET_SOURCE_URL,
        "source_policy_url": TARGET_POLICY_URL,
        "source_sha256": TARGET_SHA256,
        "source_sha256_algorithm": "sha256",
        "marker_proxy_eval_phase_marker": PREVIOUS_GATE,
        "reference_unit_type": "page_level_transcript_plan",
        "target_page_count": TARGET_PAGE_COUNT,
        "minimum_reference_pages": MINIMUM_REFERENCE_PAGES,
        "required_reference_units": REQUIRED_REFERENCE_UNITS,
        "required_reference_unit_count": len(REQUIRED_REFERENCE_UNITS),
        "owner_approval_required": True,
        "source_policy_review_required": True,
        "full_reference_transcript_required": True,
        "full_reference_transcript_available": False,
        "transcript_collection_performed": False,
        "reference_pack_created": False,
        "quality_eval_performed": False,
        "cer_computed": False,
        "wer_computed": False,
        "metric_candidates": METRIC_CANDIDATES,
        "metric_candidates_status": "blocked_until_reference_transcript_exists",
        "minimum_next_artifact": (
            "source-policy-reviewed owner-approved transcript reference pack"
        ),
        "raw_reference_text_committed": False,
        "raw_ocr_text_committed": False,
        "source_pdf_committed": False,
        "download_cache_committed": False,
        "page_images_committed": False,
        "screenshots_committed": False,
        "can_claim_transcript_reference_plan": True,
        "can_claim_transcript_reference_pack": False,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
        "recommended_next_gate": NEXT_GATE,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(
                f"source-policy OCR transcript reference plan {field} must be {expected!r}"
            )

    for field in ["warnings", "boundary_notes"]:
        value = payload.get(field)
        if not isinstance(value, list) or not value:
            raise ValueError(
                f"source-policy OCR transcript reference plan {field} must be a non-empty list"
            )

    for note in BOUNDARY_NOTES:
        if note not in payload["boundary_notes"]:
            raise ValueError(
                f"source-policy OCR transcript reference plan missing boundary note: {note}"
            )


def _validate_marker_proxy_eval(payload: dict[str, Any]) -> None:
    expected_values = {
        "phase_marker": PREVIOUS_GATE,
        "target_fixture_id": TARGET_FIXTURE_ID,
        "publisher": TARGET_PUBLISHER,
        "source_url": TARGET_SOURCE_URL,
        "source_policy_url": TARGET_POLICY_URL,
        "source_sha256": TARGET_SHA256,
        "eval_status": "marker_proxy_eval_completed",
        "reference_unit_type": "marker_anchor",
        "expected_marker_anchor_count": 2,
        "observed_marker_hit_count": 2,
        "missing_marker_anchor_count": 0,
        "marker_proxy_hit_rate": 1.0,
        "marker_proxy_passed": True,
        "quality_eval_performed": False,
        "cer_computed": False,
        "wer_computed": False,
        "raw_reference_text_committed": False,
        "raw_ocr_text_committed": False,
        "can_claim_marker_proxy_eval": True,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(f"marker proxy eval {field} must be {expected!r}")


def _format_bool(value: object) -> str:
    return "true" if value is True else "false"
