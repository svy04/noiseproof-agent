from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PHASE_MARKER = "source_policy_no_native_text_failure_route_v0"
PREVIOUS_GATE = "source_policy_pdf_quality_gap_review_v0"
CLAIM_BOUNDARY = (
    "source_policy_no_native_text_failure_route_only_not_ocr_quality_evidence"
)
NEXT_GATE = "source_policy_no_native_text_ocr_readiness_review_v0"

_FORBIDDEN_FIELDS = {
    "raw_text",
    "raw_extracted_text",
    "raw_ocr_text",
    "raw_table_rows",
    "text_sample",
    "page_image",
    "screenshot",
    "rendered_page_image",
    "local_path",
    "local_pdf_path",
}


def load_source_policy_no_native_text_failure_route(
    path: Path | str,
) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    _validate_route(payload)
    return payload


def build_source_policy_no_native_text_failure_route_summary(
    route: dict[str, Any],
) -> dict[str, Any]:
    _validate_route(route)
    failure_route = dict(route["failure_route"])
    return {
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "source_parse_observation_manifest": route["source_parse_observation_manifest"],
        "source_quality_matrix_manifest": route["source_quality_matrix_manifest"],
        "source_quality_gap_review_manifest": route[
            "source_quality_gap_review_manifest"
        ],
        "route_status": route["route_status"],
        "failure_route_count": 1,
        "selected_failure_route": failure_route["target_missing_cell"],
        "fixture_id": failure_route["fixture_id"],
        "publisher": failure_route["publisher"],
        "failure_type": failure_route["failure_type"],
        "root_cause": failure_route["root_cause"],
        "fix_status": failure_route["fix_status"],
        "page_count": failure_route["page_count"],
        "empty_page_count": failure_route["empty_page_count"],
        "text_char_count": failure_route["text_char_count"],
        "runtime_work_performed": False,
        "pdf_downloads_performed": False,
        "parser_calls_performed": False,
        "ocr_calls_performed": False,
        "table_extraction_calls_performed": False,
        "llm_calls_performed": False,
        "binary_files_committed": False,
        "download_cache_committed": False,
        "raw_text_committed": False,
        "can_claim_source_policy_no_native_text_failure_route": True,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
        "failure_route": failure_route,
        "blocked_reasons": route["blocked_reasons"],
        "minimum_next_evidence": route["minimum_next_evidence"],
        "warnings": route["warnings"],
        "boundary_notes": route["boundary_notes"],
        "next_gate": NEXT_GATE,
    }


def build_source_policy_no_native_text_failure_route_report(
    summary: dict[str, Any],
) -> str:
    failure_route = summary["failure_route"]
    lines = [
        "# Source-policy No-native-text Failure Route",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report preserves the NARA no-native-text observation as an explicit source-policy failure route.",
        "",
        "It does not add new runtime evidence.",
        "",
        "It is not OCR quality evidence.",
        "",
        "It is not robust PDF extraction evidence.",
        "",
        "## Gate Result",
        "",
        f"route_status -> {summary['route_status']}",
        f"previous_gate -> {summary['previous_gate']}",
        f"failure_route_count -> {summary['failure_route_count']}",
        f"selected_failure_route -> {summary['selected_failure_route']}",
        f"fixture_id -> {summary['fixture_id']}",
        f"publisher -> {summary['publisher']}",
        f"failure_type -> {summary['failure_type']}",
        f"root_cause -> {summary['root_cause']}",
        f"fix_status -> {summary['fix_status']}",
        f"page_count -> {summary['page_count']}",
        f"empty_page_count -> {summary['empty_page_count']}",
        f"text_char_count -> {summary['text_char_count']}",
        f"runtime_work_performed -> {_format_bool(summary['runtime_work_performed'])}",
        f"pdf_downloads_performed -> {_format_bool(summary['pdf_downloads_performed'])}",
        f"parser_calls_performed -> {_format_bool(summary['parser_calls_performed'])}",
        f"ocr_calls_performed -> {_format_bool(summary['ocr_calls_performed'])}",
        f"table_extraction_calls_performed -> {_format_bool(summary['table_extraction_calls_performed'])}",
        f"llm_calls_performed -> {_format_bool(summary['llm_calls_performed'])}",
        f"binary_files_committed -> {_format_bool(summary['binary_files_committed'])}",
        f"download_cache_committed -> {_format_bool(summary['download_cache_committed'])}",
        f"raw_text_committed -> {_format_bool(summary['raw_text_committed'])}",
        f"can_claim_source_policy_no_native_text_failure_route -> {_format_bool(summary['can_claim_source_policy_no_native_text_failure_route'])}",
        f"can_claim_ocr_quality -> {_format_bool(summary['can_claim_ocr_quality'])}",
        f"can_claim_robust_pdf_extraction -> {_format_bool(summary['can_claim_robust_pdf_extraction'])}",
        "",
        "## Preserved Failure Route",
        "",
        "| Field | Value |",
        "|---|---|",
    ]
    for field in [
        "fixture_id",
        "target_missing_cell",
        "publisher",
        "source_url",
        "policy_source_url",
        "source_sha256",
        "input_status",
        "failure_type",
        "root_cause",
        "fix_status",
        "page_count",
        "empty_page_count",
        "text_char_count",
        "quality_claim_ready",
        "boundary",
    ]:
        value = failure_route[field]
        if isinstance(value, bool):
            value = _format_bool(value)
        lines.append(f"| {field} | {value} |")

    lines.extend(["", "## Blocked Reasons", ""])
    for reason in summary["blocked_reasons"]:
        lines.append(f"- {reason}")

    lines.extend(["", "## Minimum Next Evidence", ""])
    for item in summary["minimum_next_evidence"]:
        lines.append(f"- {item}")

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
            "This is a deterministic failure-route packet over existing source-policy PDF observations.",
            "",
            "It does not download PDFs, parse PDFs, run OCR, extract tables, compare rendered pages, interpret images or charts, call LLMs, chunk, retrieve, generate Evidence Ledger entries, run Noise Gate, or build a dashboard.",
            "",
            "It does not commit external PDF binaries, download caches, raw text, page images, or screenshots.",
            "",
            "It does not prove robust PDF extraction, arbitrary-market PDF parsing reliability, OCR quality, table extraction benchmark quality, layout fidelity, rendered visual fidelity, image/chart interpretation, or external validation.",
            "",
            "This is not hosted deployment evidence.",
            "",
            "This is not external reviewer feedback.",
            "",
            "This is not product-complete.",
        ]
    )
    return "\n".join(lines) + "\n"


def _validate_route(payload: dict[str, Any]) -> None:
    _validate_forbidden_fields(payload)
    expected_values = {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "source_parse_observation_manifest": "examples/pdf-extraction-quality/source-policy-pdf-parse-observations.json",
        "source_quality_matrix_manifest": "examples/pdf-extraction-quality/source-policy-pdf-parse-quality-matrix.json",
        "source_quality_gap_review_manifest": "examples/pdf-extraction-quality/source-policy-pdf-quality-gap-review.json",
        "route_status": "passed_failure_route_preserved",
        "owner_approved": True,
        "can_claim_source_policy_no_native_text_failure_route": True,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
        "runtime_work_performed": False,
        "pdf_downloads_performed": False,
        "parser_calls_performed": False,
        "ocr_calls_performed": False,
        "table_extraction_calls_performed": False,
        "llm_calls_performed": False,
        "binary_files_committed": False,
        "download_cache_committed": False,
        "raw_text_committed": False,
        "raw_extracted_text_committed": False,
        "raw_ocr_text_committed": False,
        "raw_table_rows_committed": False,
        "page_images_committed": False,
        "screenshots_committed": False,
        "recommended_next_gate": NEXT_GATE,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(
                f"source-policy no-native-text failure route {field} must be {expected!r}"
            )

    failure_route = payload.get("failure_route")
    if not isinstance(failure_route, dict):
        raise ValueError("source-policy no-native-text failure route must include failure_route")
    _validate_failure_route(failure_route)

    for field in ["blocked_reasons", "minimum_next_evidence", "warnings", "boundary_notes"]:
        value = payload.get(field)
        if not isinstance(value, list) or not value:
            raise ValueError(
                f"source-policy no-native-text failure route {field} must be non-empty"
            )

    for note in [
        "source-policy no-native-text failure route only",
        "does not add new runtime evidence",
        "source-policy reviewed candidates only",
        "no external PDF binaries committed",
        "no download cache committed",
        "no raw text committed",
        "not robust PDF extraction evidence",
        "not arbitrary-market PDF parsing evidence",
        "not OCR quality evidence",
        "not table extraction benchmark evidence",
        "not layout fidelity evidence",
        "not rendered visual fidelity evidence",
        "not image/chart interpretation evidence",
        "not hosted deployment evidence",
        "not external reviewer feedback",
        "not product-complete",
    ]:
        if note not in payload["boundary_notes"]:
            raise ValueError(
                f"source-policy no-native-text failure route missing boundary note: {note}"
            )


def _validate_failure_route(route: dict[str, Any]) -> None:
    expected_values = {
        "fixture_id": "nara_911_mfr_00282_no_native_text_candidate",
        "target_missing_cell": "multi_publisher_no_extractable_text_failure",
        "publisher": "National Archives and Records Administration",
        "source_url": "https://nara-media-001.s3.amazonaws.com/arcmedia/9-11/MFR/t-0148-911MFR-00282.pdf",
        "policy_source_url": "https://www.archives.gov/global-pages/privacy.html",
        "source_sha256": "6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba",
        "input_status": "no_native_text_observed",
        "failure_type": "no_native_text_observed",
        "root_cause": "image_or_scanned_pdf_without_native_text_layer",
        "fix_status": "planned_not_implemented",
        "page_count": 4,
        "empty_page_count": 4,
        "text_char_count": 0,
        "binary_committed": False,
        "raw_text_committed": False,
        "quality_claim_ready": False,
    }
    for field, expected in expected_values.items():
        if route.get(field) != expected:
            raise ValueError(f"failure route {field} must be {expected!r}")
    warnings = route.get("warnings")
    if not isinstance(warnings, list) or not warnings:
        raise ValueError("failure route warnings must be non-empty")
    if "OCR was not attempted" not in warnings[0]:
        raise ValueError("failure route must disclose that OCR was not attempted")
    if "not robust PDF extraction evidence" not in str(route.get("boundary") or ""):
        raise ValueError("failure route boundary must block robust PDF claim")


def _validate_forbidden_fields(value: Any) -> None:
    if isinstance(value, dict):
        for key, nested in value.items():
            if key in _FORBIDDEN_FIELDS:
                raise ValueError(
                    f"source-policy no-native-text failure route must not commit {key}"
                )
            _validate_forbidden_fields(nested)
    elif isinstance(value, list):
        for item in value:
            _validate_forbidden_fields(item)


def _format_bool(value: bool) -> str:
    return "true" if value else "false"
