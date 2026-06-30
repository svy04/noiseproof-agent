from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PHASE_MARKER = "source_policy_no_native_text_ocr_quality_reference_pack_v0"
PREVIOUS_GATE = "source_policy_no_native_text_ocr_quality_eval_plan_v0"
CLAIM_BOUNDARY = "source_policy_no_native_text_ocr_quality_reference_pack_not_quality_evidence"
NEXT_GATE = "source_policy_no_native_text_ocr_marker_proxy_eval_v0"

TARGET_FIXTURE_ID = "nara_911_mfr_00282_no_native_text_candidate"
TARGET_PUBLISHER = "National Archives and Records Administration"
TARGET_SOURCE_URL = (
    "https://nara-media-001.s3.amazonaws.com/arcmedia/9-11/MFR/"
    "t-0148-911MFR-00282.pdf"
)
TARGET_POLICY_URL = "https://www.archives.gov/global-pages/privacy.html"
TARGET_SHA256 = "6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba"

ACCEPTED_MARKER_ANCHORS = ["commission", "mfr"]
PAGE_MAPPING = [
    {"page_number": 1, "page_scope": "source_pdf_page_1"},
    {"page_number": 2, "page_scope": "source_pdf_page_2"},
    {"page_number": 3, "page_scope": "source_pdf_page_3"},
    {"page_number": 4, "page_scope": "source_pdf_page_4"},
]
NORMALIZATION_RULES = {
    "unicode_normalization": "NFC",
    "casefold": True,
    "strip_outer_whitespace": True,
    "collapse_internal_whitespace": True,
    "punctuation_policy": "preserve_for_future_transcript_metrics",
}
SUPPORTED_METRIC_CLASSES = ["expected_marker_presence_proxy"]
BLOCKED_METRIC_CLASSES = ["character_error_rate", "word_error_rate"]
BOUNDARY_NOTES = [
    "source-policy no-native-text OCR marker-anchor reference pack",
    "not OCR quality evidence",
    "not robust PDF extraction evidence",
    "not arbitrary-market PDF OCR evidence",
    "not arbitrary-market PDF parsing evidence",
    "not rendered visual fidelity evidence",
    "not image/chart interpretation evidence",
    "not external reviewer feedback",
    "not product-complete",
]
WARNING_MESSAGES = [
    "This is a marker-anchor reference pack only.",
    "It does not include a full reference transcript.",
    "It can support a future marker proxy check only.",
    "It cannot support CER or WER without full reference text.",
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


def build_source_policy_no_native_text_ocr_quality_reference_pack(
    quality_eval_plan: dict[str, Any],
) -> dict[str, Any]:
    _validate_quality_eval_plan(quality_eval_plan)
    return {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "reference_pack_status": "marker_anchor_reference_pack",
        "target_fixture_id": quality_eval_plan["target_fixture_id"],
        "publisher": quality_eval_plan["publisher"],
        "source_url": quality_eval_plan["source_url"],
        "source_policy_url": quality_eval_plan["policy_source_url"],
        "source_sha256": quality_eval_plan["source_sha256"],
        "source_sha256_algorithm": "sha256",
        "quality_eval_plan_phase_marker": quality_eval_plan["phase_marker"],
        "quality_eval_plan_reference_pack_required": quality_eval_plan[
            "reference_pack_required"
        ],
        "quality_eval_plan_quality_eval_performed": quality_eval_plan[
            "quality_eval_performed"
        ],
        "page_count": len(PAGE_MAPPING),
        "page_mapping_available": True,
        "page_mapping": list(PAGE_MAPPING),
        "reference_unit_type": "marker_anchor",
        "accepted_marker_anchors": list(ACCEPTED_MARKER_ANCHORS),
        "accepted_marker_anchor_count": len(ACCEPTED_MARKER_ANCHORS),
        "normalization_rules": dict(NORMALIZATION_RULES),
        "full_reference_transcript_available": False,
        "supports_marker_proxy_eval": True,
        "supports_cer": False,
        "supports_wer": False,
        "supported_metric_classes": list(SUPPORTED_METRIC_CLASSES),
        "blocked_metric_classes": list(BLOCKED_METRIC_CLASSES),
        "quality_eval_performed": False,
        "raw_reference_text_committed": False,
        "raw_ocr_text_committed": False,
        "source_pdf_committed": False,
        "download_cache_committed": False,
        "page_images_committed": False,
        "screenshots_committed": False,
        "warnings": list(WARNING_MESSAGES),
        "boundary_notes": list(BOUNDARY_NOTES),
        "can_claim_reference_pack": True,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
        "recommended_next_gate": NEXT_GATE,
    }


def load_source_policy_no_native_text_ocr_quality_reference_pack(
    path: Path | str,
) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    validate_source_policy_no_native_text_ocr_quality_reference_pack(payload)
    return payload


def build_source_policy_no_native_text_ocr_quality_reference_pack_summary(
    reference_pack: dict[str, Any],
) -> dict[str, Any]:
    validate_source_policy_no_native_text_ocr_quality_reference_pack(reference_pack)
    return {
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "reference_pack_status": reference_pack["reference_pack_status"],
        "target_fixture_id": reference_pack["target_fixture_id"],
        "publisher": reference_pack["publisher"],
        "source_url": reference_pack["source_url"],
        "source_policy_url": reference_pack["source_policy_url"],
        "source_sha256": reference_pack["source_sha256"],
        "quality_eval_plan_phase_marker": reference_pack[
            "quality_eval_plan_phase_marker"
        ],
        "page_count": reference_pack["page_count"],
        "page_mapping_available": reference_pack["page_mapping_available"],
        "page_mapping": reference_pack["page_mapping"],
        "reference_unit_type": reference_pack["reference_unit_type"],
        "accepted_marker_anchors": reference_pack["accepted_marker_anchors"],
        "accepted_marker_anchor_count": reference_pack[
            "accepted_marker_anchor_count"
        ],
        "normalization_rules": reference_pack["normalization_rules"],
        "full_reference_transcript_available": reference_pack[
            "full_reference_transcript_available"
        ],
        "supports_marker_proxy_eval": reference_pack["supports_marker_proxy_eval"],
        "supports_cer": reference_pack["supports_cer"],
        "supports_wer": reference_pack["supports_wer"],
        "supported_metric_classes": reference_pack["supported_metric_classes"],
        "blocked_metric_classes": reference_pack["blocked_metric_classes"],
        "quality_eval_performed": reference_pack["quality_eval_performed"],
        "raw_reference_text_committed": reference_pack[
            "raw_reference_text_committed"
        ],
        "raw_ocr_text_committed": reference_pack["raw_ocr_text_committed"],
        "source_pdf_committed": reference_pack["source_pdf_committed"],
        "download_cache_committed": reference_pack["download_cache_committed"],
        "page_images_committed": reference_pack["page_images_committed"],
        "screenshots_committed": reference_pack["screenshots_committed"],
        "warnings": reference_pack["warnings"],
        "boundary_notes": reference_pack["boundary_notes"],
        "can_claim_reference_pack": reference_pack["can_claim_reference_pack"],
        "can_claim_ocr_quality": reference_pack["can_claim_ocr_quality"],
        "can_claim_robust_pdf_extraction": reference_pack[
            "can_claim_robust_pdf_extraction"
        ],
        "next_gate": reference_pack["recommended_next_gate"],
    }


def build_source_policy_no_native_text_ocr_quality_reference_pack_report(
    summary: dict[str, Any],
) -> str:
    lines = [
        "# Source-policy No-native-text OCR Quality Reference Pack",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report records a sanitized marker-anchor reference pack for the preserved NARA no-native-text OCR route.",
        "",
        "It is not OCR quality evidence.",
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
        f"quality_eval_plan_phase_marker -> {summary['quality_eval_plan_phase_marker']}",
        f"page_count -> {summary['page_count']}",
        f"page_mapping_available -> {_format_bool(summary['page_mapping_available'])}",
        f"reference_unit_type -> {summary['reference_unit_type']}",
        f"accepted_marker_anchor_count -> {summary['accepted_marker_anchor_count']}",
        f"full_reference_transcript_available -> {_format_bool(summary['full_reference_transcript_available'])}",
        f"supports_marker_proxy_eval -> {_format_bool(summary['supports_marker_proxy_eval'])}",
        f"supports_cer -> {_format_bool(summary['supports_cer'])}",
        f"supports_wer -> {_format_bool(summary['supports_wer'])}",
        f"quality_eval_performed -> {_format_bool(summary['quality_eval_performed'])}",
        f"raw_reference_text_committed -> {_format_bool(summary['raw_reference_text_committed'])}",
        f"raw_ocr_text_committed -> {_format_bool(summary['raw_ocr_text_committed'])}",
        f"source_pdf_committed -> {_format_bool(summary['source_pdf_committed'])}",
        f"download_cache_committed -> {_format_bool(summary['download_cache_committed'])}",
        f"page_images_committed -> {_format_bool(summary['page_images_committed'])}",
        f"screenshots_committed -> {_format_bool(summary['screenshots_committed'])}",
        f"can_claim_reference_pack -> {_format_bool(summary['can_claim_reference_pack'])}",
        f"can_claim_ocr_quality -> {_format_bool(summary['can_claim_ocr_quality'])}",
        f"can_claim_robust_pdf_extraction -> {_format_bool(summary['can_claim_robust_pdf_extraction'])}",
        "",
        "## Accepted Marker Anchors",
        "",
    ]
    for marker in summary["accepted_marker_anchors"]:
        lines.append(f"- {marker}")

    lines.extend(["", "## Normalization Rules", ""])
    for key, value in summary["normalization_rules"].items():
        lines.append(f"- {key} -> {_format_value(value)}")

    lines.extend(["", "## Supported Metric Classes", ""])
    for metric in summary["supported_metric_classes"]:
        lines.append(f"- {metric}")

    lines.extend(["", "## Blocked Metric Classes", ""])
    for metric in summary["blocked_metric_classes"]:
        lines.append(f"- {metric}")

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
            "This is a deterministic marker-anchor reference pack over the previous quality-eval plan.",
            "",
            "It supports only a future marker-presence proxy check.",
            "",
            "It does not contain a full page-level reference transcript and therefore cannot support CER or WER.",
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


def validate_source_policy_no_native_text_ocr_quality_reference_pack(
    payload: dict[str, Any],
) -> None:
    for field in _RAW_TEXT_FIELDS:
        if field in payload:
            raise ValueError(
                f"source-policy OCR reference pack must not commit {field}"
            )

    expected_values = {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "reference_pack_status": "marker_anchor_reference_pack",
        "target_fixture_id": TARGET_FIXTURE_ID,
        "publisher": TARGET_PUBLISHER,
        "source_url": TARGET_SOURCE_URL,
        "source_policy_url": TARGET_POLICY_URL,
        "source_sha256": TARGET_SHA256,
        "source_sha256_algorithm": "sha256",
        "quality_eval_plan_phase_marker": PREVIOUS_GATE,
        "quality_eval_plan_reference_pack_required": True,
        "quality_eval_plan_quality_eval_performed": False,
        "page_count": len(PAGE_MAPPING),
        "page_mapping_available": True,
        "page_mapping": PAGE_MAPPING,
        "reference_unit_type": "marker_anchor",
        "accepted_marker_anchors": ACCEPTED_MARKER_ANCHORS,
        "accepted_marker_anchor_count": len(ACCEPTED_MARKER_ANCHORS),
        "normalization_rules": NORMALIZATION_RULES,
        "full_reference_transcript_available": False,
        "supports_marker_proxy_eval": True,
        "supports_cer": False,
        "supports_wer": False,
        "supported_metric_classes": SUPPORTED_METRIC_CLASSES,
        "blocked_metric_classes": BLOCKED_METRIC_CLASSES,
        "quality_eval_performed": False,
        "raw_reference_text_committed": False,
        "raw_ocr_text_committed": False,
        "source_pdf_committed": False,
        "download_cache_committed": False,
        "page_images_committed": False,
        "screenshots_committed": False,
        "can_claim_reference_pack": True,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
        "recommended_next_gate": NEXT_GATE,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(f"source-policy OCR reference pack {field} must be {expected!r}")

    for field in ["warnings", "boundary_notes"]:
        value = payload.get(field)
        if not isinstance(value, list) or not value:
            raise ValueError(
                f"source-policy OCR reference pack {field} must be a non-empty list"
            )

    for note in BOUNDARY_NOTES:
        if note not in payload["boundary_notes"]:
            raise ValueError(
                f"source-policy OCR reference pack missing boundary note: {note}"
            )


def _validate_quality_eval_plan(payload: dict[str, Any]) -> None:
    expected_values = {
        "phase_marker": PREVIOUS_GATE,
        "target_fixture_id": TARGET_FIXTURE_ID,
        "publisher": TARGET_PUBLISHER,
        "source_url": TARGET_SOURCE_URL,
        "policy_source_url": TARGET_POLICY_URL,
        "source_sha256": TARGET_SHA256,
        "reference_pack_required": True,
        "quality_eval_performed": False,
        "raw_reference_text_committed": False,
        "raw_ocr_text_committed": False,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(f"quality eval plan {field} must be {expected!r}")


def _format_bool(value: object) -> str:
    return "true" if value is True else "false"


def _format_value(value: object) -> str:
    if isinstance(value, bool):
        return _format_bool(value)
    return str(value)
