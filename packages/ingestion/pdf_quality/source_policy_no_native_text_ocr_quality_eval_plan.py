from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PHASE_MARKER = "source_policy_no_native_text_ocr_quality_eval_plan_v0"
PREVIOUS_GATE = "source_policy_no_native_text_ocr_execution_smoke_v0"
CLAIM_BOUNDARY = "source_policy_no_native_text_ocr_quality_eval_plan_not_quality_evidence"
NEXT_GATE = "source_policy_no_native_text_ocr_quality_reference_pack_v0"

TARGET_FIXTURE_ID = "nara_911_mfr_00282_no_native_text_candidate"
TARGET_PUBLISHER = "National Archives and Records Administration"
TARGET_SOURCE_URL = (
    "https://nara-media-001.s3.amazonaws.com/arcmedia/9-11/MFR/"
    "t-0148-911MFR-00282.pdf"
)
TARGET_POLICY_URL = "https://www.archives.gov/global-pages/privacy.html"
TARGET_SHA256 = "6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba"

QUALITY_METRIC_CANDIDATES = [
    "character_error_rate",
    "word_error_rate",
    "expected_marker_precision_recall_proxy",
]
REQUIRED_REFERENCE_INPUTS = [
    "page_level_reference_transcript_or_accepted_spans",
    "reference_source_policy",
    "normalization_rules",
    "page_mapping",
    "source_sha256_binding",
    "ocr_output_acquisition_boundary",
    "raw_text_redaction_boundary",
]
STOP_CONDITIONS = [
    "no_page_level_reference_transcript_or_accepted_spans",
    "no_reference_source_policy",
    "no_normalization_rules",
    "source_sha256_not_bound_to_reference_pack",
    "quality_score_requested_from_marker_hits_only",
    "quality_score_requires_committing_raw_ocr_or_reference_text",
]
WARNING_MESSAGES = [
    "This is an OCR quality-evaluation plan only.",
    "The previous OCR execution smoke is not OCR quality evidence.",
    "Expected-marker hits and OCR text counts are proxy checks only.",
    "A reference pack is required before any quality score can be computed.",
]
BOUNDARY_NOTES = [
    "source-policy no-native-text OCR quality-evaluation plan",
    "not OCR quality evidence",
    "not robust PDF extraction evidence",
    "not arbitrary-market PDF OCR evidence",
    "not arbitrary-market PDF parsing evidence",
    "not rendered visual fidelity evidence",
    "not image/chart interpretation evidence",
    "not external reviewer feedback",
    "not product-complete",
]
_RAW_TEXT_FIELDS = {
    "recognized_text",
    "ocr_sample",
    "raw_text",
    "raw_extracted_text",
    "raw_ocr_text",
    "raw_reference_text",
    "reference_transcript",
    "reference_spans",
    "page_image",
    "page_images",
    "screenshot",
    "screenshots",
}


def build_source_policy_no_native_text_ocr_quality_eval_plan(
    execution_smoke: dict[str, Any],
) -> dict[str, Any]:
    _validate_execution_smoke(execution_smoke)
    return {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "plan_status": "planned_quality_eval_contract",
        "target_fixture_id": execution_smoke["target_fixture_id"],
        "publisher": execution_smoke["publisher"],
        "source_url": execution_smoke["source_url"],
        "policy_source_url": execution_smoke["policy_source_url"],
        "source_sha256": execution_smoke["source_sha256"],
        "source_sha256_algorithm": "sha256",
        "execution_smoke_phase_marker": execution_smoke["phase_marker"],
        "execution_smoke_run_source": execution_smoke["run_source"],
        "execution_smoke_ocr_execution_performed": execution_smoke[
            "ocr_execution_performed"
        ],
        "execution_smoke_ocr_text_char_count": execution_smoke[
            "ocr_text_char_count"
        ],
        "execution_smoke_expected_markers_found_count": execution_smoke[
            "expected_markers_found_count"
        ],
        "execution_smoke_quality_eval_performed": execution_smoke[
            "ocr_quality_eval_performed"
        ],
        "ground_truth_available": False,
        "reference_pack_required": True,
        "quality_eval_performed": False,
        "raw_reference_text_committed": False,
        "raw_ocr_text_committed": False,
        "source_pdf_committed": False,
        "download_cache_committed": False,
        "page_images_committed": False,
        "screenshots_committed": False,
        "marker_hits_are_quality_proxy_only": True,
        "quality_metric_candidates": list(QUALITY_METRIC_CANDIDATES),
        "required_reference_inputs": list(REQUIRED_REFERENCE_INPUTS),
        "stop_conditions": list(STOP_CONDITIONS),
        "warnings": list(WARNING_MESSAGES),
        "boundary_notes": list(BOUNDARY_NOTES),
        "can_claim_quality_eval_plan": True,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
        "recommended_next_gate": NEXT_GATE,
    }


def load_source_policy_no_native_text_ocr_quality_eval_plan(
    path: Path | str,
) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    validate_source_policy_no_native_text_ocr_quality_eval_plan(payload)
    return payload


def build_source_policy_no_native_text_ocr_quality_eval_plan_summary(
    plan: dict[str, Any],
) -> dict[str, Any]:
    validate_source_policy_no_native_text_ocr_quality_eval_plan(plan)
    return {
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "plan_status": plan["plan_status"],
        "target_fixture_id": plan["target_fixture_id"],
        "publisher": plan["publisher"],
        "source_url": plan["source_url"],
        "policy_source_url": plan["policy_source_url"],
        "source_sha256": plan["source_sha256"],
        "execution_smoke_phase_marker": plan["execution_smoke_phase_marker"],
        "execution_smoke_run_source": plan["execution_smoke_run_source"],
        "execution_smoke_ocr_execution_performed": plan[
            "execution_smoke_ocr_execution_performed"
        ],
        "execution_smoke_ocr_text_char_count": plan[
            "execution_smoke_ocr_text_char_count"
        ],
        "execution_smoke_expected_markers_found_count": plan[
            "execution_smoke_expected_markers_found_count"
        ],
        "execution_smoke_quality_eval_performed": plan[
            "execution_smoke_quality_eval_performed"
        ],
        "ground_truth_available": plan["ground_truth_available"],
        "reference_pack_required": plan["reference_pack_required"],
        "quality_eval_performed": plan["quality_eval_performed"],
        "raw_reference_text_committed": plan["raw_reference_text_committed"],
        "raw_ocr_text_committed": plan["raw_ocr_text_committed"],
        "source_pdf_committed": plan["source_pdf_committed"],
        "download_cache_committed": plan["download_cache_committed"],
        "page_images_committed": plan["page_images_committed"],
        "screenshots_committed": plan["screenshots_committed"],
        "marker_hits_are_quality_proxy_only": plan[
            "marker_hits_are_quality_proxy_only"
        ],
        "quality_metric_candidates": plan["quality_metric_candidates"],
        "required_reference_inputs": plan["required_reference_inputs"],
        "stop_conditions": plan["stop_conditions"],
        "warnings": plan["warnings"],
        "boundary_notes": plan["boundary_notes"],
        "can_claim_quality_eval_plan": plan["can_claim_quality_eval_plan"],
        "can_claim_ocr_quality": plan["can_claim_ocr_quality"],
        "can_claim_robust_pdf_extraction": plan["can_claim_robust_pdf_extraction"],
        "next_gate": plan["recommended_next_gate"],
    }


def build_source_policy_no_native_text_ocr_quality_eval_plan_report(
    summary: dict[str, Any],
) -> str:
    lines = [
        "# Source-policy No-native-text OCR Quality Eval Plan",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report records the evaluation contract required before the preserved NARA no-native-text OCR route can make any OCR-quality claim.",
        "",
        "It is not OCR quality evidence.",
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
        f"execution_smoke_phase_marker -> {summary['execution_smoke_phase_marker']}",
        f"execution_smoke_run_source -> {summary['execution_smoke_run_source']}",
        f"execution_smoke_ocr_execution_performed -> {_format_bool(summary['execution_smoke_ocr_execution_performed'])}",
        f"execution_smoke_ocr_text_char_count -> {summary['execution_smoke_ocr_text_char_count']}",
        f"execution_smoke_expected_markers_found_count -> {summary['execution_smoke_expected_markers_found_count']}",
        f"execution_smoke_quality_eval_performed -> {_format_bool(summary['execution_smoke_quality_eval_performed'])}",
        f"ground_truth_available -> {_format_bool(summary['ground_truth_available'])}",
        f"reference_pack_required -> {_format_bool(summary['reference_pack_required'])}",
        f"quality_eval_performed -> {_format_bool(summary['quality_eval_performed'])}",
        f"raw_reference_text_committed -> {_format_bool(summary['raw_reference_text_committed'])}",
        f"raw_ocr_text_committed -> {_format_bool(summary['raw_ocr_text_committed'])}",
        f"source_pdf_committed -> {_format_bool(summary['source_pdf_committed'])}",
        f"download_cache_committed -> {_format_bool(summary['download_cache_committed'])}",
        f"page_images_committed -> {_format_bool(summary['page_images_committed'])}",
        f"screenshots_committed -> {_format_bool(summary['screenshots_committed'])}",
        f"marker_hits_are_quality_proxy_only -> {_format_bool(summary['marker_hits_are_quality_proxy_only'])}",
        f"can_claim_quality_eval_plan -> {_format_bool(summary['can_claim_quality_eval_plan'])}",
        f"can_claim_ocr_quality -> {_format_bool(summary['can_claim_ocr_quality'])}",
        f"can_claim_robust_pdf_extraction -> {_format_bool(summary['can_claim_robust_pdf_extraction'])}",
        "",
        "## Candidate Metrics",
        "",
    ]
    for metric in summary["quality_metric_candidates"]:
        lines.append(f"- {metric}")

    lines.extend(["", "## Required Reference Inputs", ""])
    for field in summary["required_reference_inputs"]:
        lines.append(f"- {field}")

    lines.extend(["", "## Stop Conditions", ""])
    for condition in summary["stop_conditions"]:
        lines.append(f"- {condition}")

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
            "This is a deterministic plan over the previous sanitized OCR execution smoke.",
            "",
            "The previous smoke proves only that one bounded OCR execution path ran and produced sanitized metadata.",
            "",
            "Expected-marker hits and character counts are not recognition-quality scores.",
            "",
            "No OCR quality evaluation is performed until a reference pack exists with source policy, page mapping, normalization rules, and raw-text redaction boundaries.",
            "",
            "It does not commit external PDF binaries, download caches, local paths, tessdata paths, raw reference text, raw OCR text, page images, screenshots, or table rows.",
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


def validate_source_policy_no_native_text_ocr_quality_eval_plan(
    payload: dict[str, Any],
) -> None:
    for field in _RAW_TEXT_FIELDS:
        if field in payload:
            raise ValueError(f"source-policy OCR quality plan must not commit {field}")

    expected_values = {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "plan_status": "planned_quality_eval_contract",
        "target_fixture_id": TARGET_FIXTURE_ID,
        "publisher": TARGET_PUBLISHER,
        "source_url": TARGET_SOURCE_URL,
        "policy_source_url": TARGET_POLICY_URL,
        "source_sha256": TARGET_SHA256,
        "source_sha256_algorithm": "sha256",
        "execution_smoke_phase_marker": PREVIOUS_GATE,
        "execution_smoke_ocr_execution_performed": True,
        "execution_smoke_ocr_text_char_count": 8019,
        "execution_smoke_expected_markers_found_count": 2,
        "execution_smoke_quality_eval_performed": False,
        "ground_truth_available": False,
        "reference_pack_required": True,
        "quality_eval_performed": False,
        "raw_reference_text_committed": False,
        "raw_ocr_text_committed": False,
        "source_pdf_committed": False,
        "download_cache_committed": False,
        "page_images_committed": False,
        "screenshots_committed": False,
        "marker_hits_are_quality_proxy_only": True,
        "quality_metric_candidates": QUALITY_METRIC_CANDIDATES,
        "required_reference_inputs": REQUIRED_REFERENCE_INPUTS,
        "stop_conditions": STOP_CONDITIONS,
        "can_claim_quality_eval_plan": True,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
        "recommended_next_gate": NEXT_GATE,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(f"source-policy OCR quality plan {field} must be {expected!r}")

    if not isinstance(payload.get("execution_smoke_run_source"), str):
        raise ValueError("source-policy OCR quality plan execution_smoke_run_source must be set")

    for field in ["warnings", "boundary_notes"]:
        value = payload.get(field)
        if not isinstance(value, list) or not value:
            raise ValueError(f"source-policy OCR quality plan {field} must be a non-empty list")

    for note in BOUNDARY_NOTES:
        if note not in payload["boundary_notes"]:
            raise ValueError(f"source-policy OCR quality plan missing boundary note: {note}")


def _validate_execution_smoke(payload: dict[str, Any]) -> None:
    expected_values = {
        "phase_marker": PREVIOUS_GATE,
        "target_fixture_id": TARGET_FIXTURE_ID,
        "publisher": TARGET_PUBLISHER,
        "source_url": TARGET_SOURCE_URL,
        "policy_source_url": TARGET_POLICY_URL,
        "source_sha256": TARGET_SHA256,
        "ocr_execution_performed": True,
        "ocr_text_char_count": 8019,
        "expected_markers_found_count": 2,
        "ocr_quality_eval_performed": False,
        "raw_ocr_text_committed": False,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(f"execution smoke {field} must be {expected!r}")


def _format_bool(value: object) -> str:
    return "true" if value is True else "false"
