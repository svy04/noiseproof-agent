from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PHASE_MARKER = "source_policy_no_native_text_ocr_marker_proxy_eval_v0"
PREVIOUS_GATE = "source_policy_no_native_text_ocr_quality_reference_pack_v0"
OCR_EXECUTION_SMOKE_GATE = "source_policy_no_native_text_ocr_execution_smoke_v0"
CLAIM_BOUNDARY = "source_policy_no_native_text_ocr_marker_proxy_eval_not_ocr_quality"
NEXT_GATE = "source_policy_no_native_text_ocr_transcript_reference_plan_v0"

TARGET_FIXTURE_ID = "nara_911_mfr_00282_no_native_text_candidate"
TARGET_PUBLISHER = "National Archives and Records Administration"
TARGET_SOURCE_URL = (
    "https://nara-media-001.s3.amazonaws.com/arcmedia/9-11/MFR/"
    "t-0148-911MFR-00282.pdf"
)
TARGET_POLICY_URL = "https://www.archives.gov/global-pages/privacy.html"
TARGET_SHA256 = "6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba"
ACCEPTED_MARKER_ANCHORS = ["commission", "mfr"]
MARKER_PROXY_THRESHOLD = 1.0
BOUNDARY_NOTES = [
    "source-policy no-native-text OCR marker proxy eval",
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
    "This is a marker-presence proxy eval only.",
    "It uses committed marker-hit booleans, not raw OCR text.",
    "It does not include a full reference transcript.",
    "It cannot support CER, WER, or OCR quality claims.",
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


def build_source_policy_no_native_text_ocr_marker_proxy_eval(
    reference_pack: dict[str, Any],
    execution_smoke: dict[str, Any],
) -> dict[str, Any]:
    _validate_reference_pack(reference_pack)
    _validate_execution_smoke(execution_smoke)
    anchors = list(reference_pack["accepted_marker_anchors"])
    observed_hits = {
        anchor: execution_smoke["expected_marker_hits"].get(anchor) is True
        for anchor in anchors
    }
    missing_anchors = [anchor for anchor in anchors if not observed_hits[anchor]]
    observed_hit_count = sum(1 for hit in observed_hits.values() if hit)
    hit_rate = observed_hit_count / len(anchors)
    return {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "eval_status": "marker_proxy_eval_completed",
        "target_fixture_id": reference_pack["target_fixture_id"],
        "publisher": reference_pack["publisher"],
        "source_url": reference_pack["source_url"],
        "source_policy_url": reference_pack["source_policy_url"],
        "source_sha256": reference_pack["source_sha256"],
        "source_sha256_algorithm": "sha256",
        "reference_pack_phase_marker": reference_pack["phase_marker"],
        "ocr_execution_smoke_phase_marker": execution_smoke["phase_marker"],
        "reference_unit_type": "marker_anchor",
        "expected_marker_anchors": anchors,
        "expected_marker_anchor_count": len(anchors),
        "observed_marker_hits": observed_hits,
        "observed_marker_hit_count": observed_hit_count,
        "missing_marker_anchors": missing_anchors,
        "missing_marker_anchor_count": len(missing_anchors),
        "marker_proxy_hit_rate": hit_rate,
        "marker_proxy_threshold": MARKER_PROXY_THRESHOLD,
        "marker_proxy_passed": hit_rate >= MARKER_PROXY_THRESHOLD,
        "quality_eval_performed": False,
        "cer_computed": False,
        "wer_computed": False,
        "raw_reference_text_committed": False,
        "raw_ocr_text_committed": False,
        "source_pdf_committed": False,
        "download_cache_committed": False,
        "page_images_committed": False,
        "screenshots_committed": False,
        "warnings": list(WARNING_MESSAGES),
        "boundary_notes": list(BOUNDARY_NOTES),
        "can_claim_marker_proxy_eval": True,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
        "recommended_next_gate": NEXT_GATE,
    }


def load_source_policy_no_native_text_ocr_marker_proxy_eval(
    path: Path | str,
) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    validate_source_policy_no_native_text_ocr_marker_proxy_eval(payload)
    return payload


def build_source_policy_no_native_text_ocr_marker_proxy_eval_summary(
    marker_eval: dict[str, Any],
) -> dict[str, Any]:
    validate_source_policy_no_native_text_ocr_marker_proxy_eval(marker_eval)
    return {
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "eval_status": marker_eval["eval_status"],
        "target_fixture_id": marker_eval["target_fixture_id"],
        "publisher": marker_eval["publisher"],
        "source_url": marker_eval["source_url"],
        "source_policy_url": marker_eval["source_policy_url"],
        "source_sha256": marker_eval["source_sha256"],
        "reference_pack_phase_marker": marker_eval["reference_pack_phase_marker"],
        "ocr_execution_smoke_phase_marker": marker_eval[
            "ocr_execution_smoke_phase_marker"
        ],
        "reference_unit_type": marker_eval["reference_unit_type"],
        "expected_marker_anchors": marker_eval["expected_marker_anchors"],
        "expected_marker_anchor_count": marker_eval[
            "expected_marker_anchor_count"
        ],
        "observed_marker_hits": marker_eval["observed_marker_hits"],
        "observed_marker_hit_count": marker_eval["observed_marker_hit_count"],
        "missing_marker_anchors": marker_eval["missing_marker_anchors"],
        "missing_marker_anchor_count": marker_eval["missing_marker_anchor_count"],
        "marker_proxy_hit_rate": marker_eval["marker_proxy_hit_rate"],
        "marker_proxy_threshold": marker_eval["marker_proxy_threshold"],
        "marker_proxy_passed": marker_eval["marker_proxy_passed"],
        "quality_eval_performed": marker_eval["quality_eval_performed"],
        "cer_computed": marker_eval["cer_computed"],
        "wer_computed": marker_eval["wer_computed"],
        "raw_reference_text_committed": marker_eval["raw_reference_text_committed"],
        "raw_ocr_text_committed": marker_eval["raw_ocr_text_committed"],
        "source_pdf_committed": marker_eval["source_pdf_committed"],
        "download_cache_committed": marker_eval["download_cache_committed"],
        "page_images_committed": marker_eval["page_images_committed"],
        "screenshots_committed": marker_eval["screenshots_committed"],
        "warnings": marker_eval["warnings"],
        "boundary_notes": marker_eval["boundary_notes"],
        "can_claim_marker_proxy_eval": marker_eval["can_claim_marker_proxy_eval"],
        "can_claim_ocr_quality": marker_eval["can_claim_ocr_quality"],
        "can_claim_robust_pdf_extraction": marker_eval[
            "can_claim_robust_pdf_extraction"
        ],
        "next_gate": marker_eval["recommended_next_gate"],
    }


def build_source_policy_no_native_text_ocr_marker_proxy_eval_report(
    summary: dict[str, Any],
) -> str:
    lines = [
        "# Source-policy No-native-text OCR Marker Proxy Eval",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report records a bounded marker-presence proxy evaluation for the preserved NARA no-native-text OCR route.",
        "",
        "It is not OCR quality evidence.",
        "",
        "It is not robust PDF extraction evidence.",
        "",
        "## Gate Result",
        "",
        f"eval_status -> {summary['eval_status']}",
        f"previous_gate -> {summary['previous_gate']}",
        f"target_fixture_id -> {summary['target_fixture_id']}",
        f"publisher -> {summary['publisher']}",
        f"source_sha256 -> {summary['source_sha256']}",
        f"source_policy_url -> {summary['source_policy_url']}",
        f"reference_pack_phase_marker -> {summary['reference_pack_phase_marker']}",
        f"ocr_execution_smoke_phase_marker -> {summary['ocr_execution_smoke_phase_marker']}",
        f"reference_unit_type -> {summary['reference_unit_type']}",
        f"expected_marker_anchor_count -> {summary['expected_marker_anchor_count']}",
        f"observed_marker_hit_count -> {summary['observed_marker_hit_count']}",
        f"missing_marker_anchor_count -> {summary['missing_marker_anchor_count']}",
        f"marker_proxy_hit_rate -> {_format_float(summary['marker_proxy_hit_rate'])}",
        f"marker_proxy_threshold -> {_format_float(summary['marker_proxy_threshold'])}",
        f"marker_proxy_passed -> {_format_bool(summary['marker_proxy_passed'])}",
        f"quality_eval_performed -> {_format_bool(summary['quality_eval_performed'])}",
        f"cer_computed -> {_format_bool(summary['cer_computed'])}",
        f"wer_computed -> {_format_bool(summary['wer_computed'])}",
        f"raw_reference_text_committed -> {_format_bool(summary['raw_reference_text_committed'])}",
        f"raw_ocr_text_committed -> {_format_bool(summary['raw_ocr_text_committed'])}",
        f"source_pdf_committed -> {_format_bool(summary['source_pdf_committed'])}",
        f"download_cache_committed -> {_format_bool(summary['download_cache_committed'])}",
        f"page_images_committed -> {_format_bool(summary['page_images_committed'])}",
        f"screenshots_committed -> {_format_bool(summary['screenshots_committed'])}",
        f"can_claim_marker_proxy_eval -> {_format_bool(summary['can_claim_marker_proxy_eval'])}",
        f"can_claim_ocr_quality -> {_format_bool(summary['can_claim_ocr_quality'])}",
        f"can_claim_robust_pdf_extraction -> {_format_bool(summary['can_claim_robust_pdf_extraction'])}",
        "",
        "## Observed Marker Hits",
        "",
        "| Marker | Hit |",
        "|---|---:|",
    ]
    for marker in summary["expected_marker_anchors"]:
        lines.append(
            f"| {marker} | {_format_bool(summary['observed_marker_hits'][marker])} |"
        )

    lines.extend(["", "## Missing Marker Anchors", ""])
    if summary["missing_marker_anchors"]:
        for marker in summary["missing_marker_anchors"]:
            lines.append(f"- {marker}")
    else:
        lines.append("- none")

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
            "This is a deterministic marker-presence proxy eval over committed marker-hit booleans.",
            "",
            "It does not inspect or commit raw OCR text.",
            "",
            "It does not contain a full page-level reference transcript and therefore cannot support CER or WER.",
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


def validate_source_policy_no_native_text_ocr_marker_proxy_eval(
    payload: dict[str, Any],
) -> None:
    for field in _RAW_TEXT_FIELDS:
        if field in payload:
            raise ValueError(f"source-policy OCR marker proxy eval must not commit {field}")

    expected_values = {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "eval_status": "marker_proxy_eval_completed",
        "target_fixture_id": TARGET_FIXTURE_ID,
        "publisher": TARGET_PUBLISHER,
        "source_url": TARGET_SOURCE_URL,
        "source_policy_url": TARGET_POLICY_URL,
        "source_sha256": TARGET_SHA256,
        "source_sha256_algorithm": "sha256",
        "reference_pack_phase_marker": PREVIOUS_GATE,
        "ocr_execution_smoke_phase_marker": OCR_EXECUTION_SMOKE_GATE,
        "reference_unit_type": "marker_anchor",
        "expected_marker_anchors": ACCEPTED_MARKER_ANCHORS,
        "expected_marker_anchor_count": len(ACCEPTED_MARKER_ANCHORS),
        "observed_marker_hits": {"commission": True, "mfr": True},
        "observed_marker_hit_count": len(ACCEPTED_MARKER_ANCHORS),
        "missing_marker_anchors": [],
        "missing_marker_anchor_count": 0,
        "marker_proxy_hit_rate": 1.0,
        "marker_proxy_threshold": MARKER_PROXY_THRESHOLD,
        "marker_proxy_passed": True,
        "quality_eval_performed": False,
        "cer_computed": False,
        "wer_computed": False,
        "raw_reference_text_committed": False,
        "raw_ocr_text_committed": False,
        "source_pdf_committed": False,
        "download_cache_committed": False,
        "page_images_committed": False,
        "screenshots_committed": False,
        "can_claim_marker_proxy_eval": True,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
        "recommended_next_gate": NEXT_GATE,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(
                f"source-policy OCR marker proxy eval {field} must be {expected!r}"
            )

    for field in ["warnings", "boundary_notes"]:
        value = payload.get(field)
        if not isinstance(value, list) or not value:
            raise ValueError(
                f"source-policy OCR marker proxy eval {field} must be a non-empty list"
            )

    for note in BOUNDARY_NOTES:
        if note not in payload["boundary_notes"]:
            raise ValueError(
                f"source-policy OCR marker proxy eval missing boundary note: {note}"
            )


def _validate_reference_pack(payload: dict[str, Any]) -> None:
    expected_values = {
        "phase_marker": PREVIOUS_GATE,
        "target_fixture_id": TARGET_FIXTURE_ID,
        "publisher": TARGET_PUBLISHER,
        "source_url": TARGET_SOURCE_URL,
        "source_policy_url": TARGET_POLICY_URL,
        "source_sha256": TARGET_SHA256,
        "reference_unit_type": "marker_anchor",
        "accepted_marker_anchors": ACCEPTED_MARKER_ANCHORS,
        "accepted_marker_anchor_count": len(ACCEPTED_MARKER_ANCHORS),
        "supports_marker_proxy_eval": True,
        "supports_cer": False,
        "supports_wer": False,
        "full_reference_transcript_available": False,
        "quality_eval_performed": False,
        "raw_reference_text_committed": False,
        "raw_ocr_text_committed": False,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(f"reference pack {field} must be {expected!r}")


def _validate_execution_smoke(payload: dict[str, Any]) -> None:
    expected_values = {
        "phase_marker": OCR_EXECUTION_SMOKE_GATE,
        "target_fixture_id": TARGET_FIXTURE_ID,
        "publisher": TARGET_PUBLISHER,
        "source_url": TARGET_SOURCE_URL,
        "policy_source_url": TARGET_POLICY_URL,
        "source_sha256": TARGET_SHA256,
        "expected_markers_checked": ACCEPTED_MARKER_ANCHORS,
        "expected_marker_hits": {"commission": True, "mfr": True},
        "expected_markers_found_count": len(ACCEPTED_MARKER_ANCHORS),
        "ocr_execution_performed": True,
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


def _format_float(value: float) -> str:
    return f"{value:.1f}"
