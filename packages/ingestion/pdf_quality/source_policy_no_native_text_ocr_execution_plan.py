from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PHASE_MARKER = "source_policy_no_native_text_ocr_execution_plan_v0"
PREVIOUS_GATE = "source_policy_no_native_text_ocr_dependency_resolution_v0"
CLAIM_BOUNDARY = (
    "source_policy_no_native_text_ocr_execution_plan_only_not_execution_or_quality_evidence"
)
NEXT_GATE = "source_policy_no_native_text_ocr_execution_smoke_v0"

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
    "tessdata_path",
    "tesseract_path",
    "tesseract_executable_path",
}


def load_source_policy_no_native_text_ocr_execution_plan(
    path: Path | str,
) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    _validate_plan(payload)
    return payload


def build_source_policy_no_native_text_ocr_execution_plan_summary(
    plan: dict[str, Any],
) -> dict[str, Any]:
    _validate_plan(plan)
    preserved_route = dict(plan["preserved_failure_route"])
    return {
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "source_dependency_resolution_manifest": plan[
            "source_dependency_resolution_manifest"
        ],
        "plan_status": plan["plan_status"],
        "execution_adapter": plan["execution_adapter"],
        "execution_mode": plan["execution_mode"],
        "target_fixture_id": preserved_route["fixture_id"],
        "publisher": preserved_route["publisher"],
        "failure_type": preserved_route["failure_type"],
        "target_page_count": preserved_route["page_count"],
        "target_empty_page_count": preserved_route["empty_page_count"],
        "target_text_char_count": preserved_route["text_char_count"],
        "dependency_available": plan["dependency_available"],
        "path_refresh_required": plan["path_refresh_required"],
        "opt_in_required": plan["opt_in_required"],
        "planned_ocr_language": plan["planned_ocr_language"],
        "planned_dpi": plan["planned_dpi"],
        "planned_full_page_ocr": plan["planned_full_page_ocr"],
        "planned_pages": plan["planned_pages"],
        "planned_output_policy": plan["planned_output_policy"],
        "ocr_execution_performed": plan["ocr_execution_performed"],
        "ocr_quality_eval_performed": plan["ocr_quality_eval_performed"],
        "pdf_downloads_performed": False,
        "parser_calls_performed": False,
        "table_extraction_calls_performed": False,
        "llm_calls_performed": False,
        "binary_files_committed": False,
        "download_cache_committed": False,
        "raw_text_committed": False,
        "raw_ocr_text_committed": False,
        "page_images_committed": False,
        "screenshots_committed": False,
        "can_claim_ocr_execution_plan": True,
        "can_claim_ocr_execution": False,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
        "sources": plan["sources"],
        "planned_execution_steps": plan["planned_execution_steps"],
        "stop_conditions": plan["stop_conditions"],
        "minimum_next_evidence": plan["minimum_next_evidence"],
        "warnings": plan["warnings"],
        "boundary_notes": plan["boundary_notes"],
        "next_gate": NEXT_GATE,
    }


def build_source_policy_no_native_text_ocr_execution_plan_report(
    summary: dict[str, Any],
) -> str:
    lines = [
        "# Source-policy No-native-text OCR Execution Plan",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report records a bounded OCR execution plan for the preserved NARA no-native-text route.",
        "",
        "It plans a future PyMuPDF/Tesseract OCR smoke only.",
        "",
        "It does not run OCR.",
        "",
        "It is not OCR quality evidence.",
        "",
        "It is not robust PDF extraction evidence.",
        "",
        "## Gate Result",
        "",
        f"plan_status -> {summary['plan_status']}",
        f"previous_gate -> {summary['previous_gate']}",
        f"execution_adapter -> {summary['execution_adapter']}",
        f"execution_mode -> {summary['execution_mode']}",
        f"target_fixture_id -> {summary['target_fixture_id']}",
        f"publisher -> {summary['publisher']}",
        f"failure_type -> {summary['failure_type']}",
        f"target_page_count -> {summary['target_page_count']}",
        f"target_empty_page_count -> {summary['target_empty_page_count']}",
        f"target_text_char_count -> {summary['target_text_char_count']}",
        f"dependency_available -> {_format_bool(summary['dependency_available'])}",
        f"path_refresh_required -> {_format_bool(summary['path_refresh_required'])}",
        f"opt_in_required -> {_format_bool(summary['opt_in_required'])}",
        f"planned_ocr_language -> {summary['planned_ocr_language']}",
        f"planned_dpi -> {summary['planned_dpi']}",
        f"planned_full_page_ocr -> {_format_bool(summary['planned_full_page_ocr'])}",
        f"planned_pages -> {', '.join(str(page) for page in summary['planned_pages'])}",
        f"planned_output_policy -> {summary['planned_output_policy']}",
        f"ocr_execution_performed -> {_format_bool(summary['ocr_execution_performed'])}",
        f"ocr_quality_eval_performed -> {_format_bool(summary['ocr_quality_eval_performed'])}",
        f"pdf_downloads_performed -> {_format_bool(summary['pdf_downloads_performed'])}",
        f"parser_calls_performed -> {_format_bool(summary['parser_calls_performed'])}",
        f"table_extraction_calls_performed -> {_format_bool(summary['table_extraction_calls_performed'])}",
        f"llm_calls_performed -> {_format_bool(summary['llm_calls_performed'])}",
        f"binary_files_committed -> {_format_bool(summary['binary_files_committed'])}",
        f"download_cache_committed -> {_format_bool(summary['download_cache_committed'])}",
        f"raw_text_committed -> {_format_bool(summary['raw_text_committed'])}",
        f"raw_ocr_text_committed -> {_format_bool(summary['raw_ocr_text_committed'])}",
        f"page_images_committed -> {_format_bool(summary['page_images_committed'])}",
        f"screenshots_committed -> {_format_bool(summary['screenshots_committed'])}",
        f"can_claim_ocr_execution_plan -> {_format_bool(summary['can_claim_ocr_execution_plan'])}",
        f"can_claim_ocr_execution -> {_format_bool(summary['can_claim_ocr_execution'])}",
        f"can_claim_ocr_quality -> {_format_bool(summary['can_claim_ocr_quality'])}",
        f"can_claim_robust_pdf_extraction -> {_format_bool(summary['can_claim_robust_pdf_extraction'])}",
        "",
        "## Sources",
        "",
        "| Label | Type | URL | Pattern |",
        "|---|---|---|---|",
    ]
    for source in summary["sources"]:
        lines.append(
            f"| {source['label']} | {source['source_type']} | {source['url']} | {source['pattern']} |"
        )

    lines.extend(["", "## Planned Execution Steps", ""])
    for step in summary["planned_execution_steps"]:
        lines.append(f"- {step}")

    lines.extend(["", "## Stop Conditions", ""])
    for condition in summary["stop_conditions"]:
        lines.append(f"- {condition}")

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
            "This is a deterministic OCR execution-plan packet over the current source-policy no-native-text route.",
            "",
            "It does not download PDFs, parse PDFs, run OCR, evaluate OCR output, extract tables, compare rendered pages, interpret images or charts, call LLMs, chunk, retrieve, generate Evidence Ledger entries, run Noise Gate, or build a dashboard.",
            "",
            "It does not commit local executable paths, tessdata paths, external PDF binaries, download caches, raw text, raw OCR text, page images, or screenshots.",
            "",
            "It does not prove OCR execution, OCR quality, robust PDF extraction, arbitrary-market PDF parsing reliability, table extraction benchmark quality, layout fidelity, rendered visual fidelity, image/chart interpretation, or external validation.",
            "",
            "This is not hosted deployment evidence.",
            "",
            "This is not external reviewer feedback.",
            "",
            "This is not product-complete.",
        ]
    )
    return "\n".join(lines) + "\n"


def _validate_plan(payload: dict[str, Any]) -> None:
    _validate_forbidden_fields(payload)
    expected_values = {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "source_dependency_resolution_manifest": "examples/pdf-extraction-quality/source-policy-no-native-text-ocr-dependency-resolution.json",
        "plan_status": "planned_execution_contract",
        "execution_adapter": "pymupdf_page_get_textpage_ocr",
        "execution_mode": "owner_runtime_opt_in_smoke",
        "dependency_available": True,
        "path_refresh_required": True,
        "opt_in_required": True,
        "planned_ocr_language": "eng",
        "planned_dpi": 300,
        "planned_full_page_ocr": True,
        "planned_output_policy": "sanitized_counts_and_expected_marker_hits_only",
        "ocr_execution_performed": False,
        "ocr_quality_eval_performed": False,
        "pdf_downloads_performed": False,
        "parser_calls_performed": False,
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
        "can_claim_ocr_execution_plan": True,
        "can_claim_ocr_execution": False,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
        "recommended_next_gate": NEXT_GATE,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(
                f"source-policy no-native-text OCR execution plan {field} must be {expected!r}"
            )

    preserved_route = payload.get("preserved_failure_route")
    if not isinstance(preserved_route, dict):
        raise ValueError("OCR execution plan must include preserved_failure_route")
    _validate_preserved_route(preserved_route)

    planned_pages = payload.get("planned_pages")
    if planned_pages != [1, 2, 3, 4]:
        raise ValueError("source-policy no-native-text OCR execution plan planned_pages must be [1, 2, 3, 4]")

    for field in [
        "sources",
        "planned_execution_steps",
        "stop_conditions",
        "minimum_next_evidence",
        "warnings",
        "boundary_notes",
    ]:
        value = payload.get(field)
        if not isinstance(value, list) or not value:
            raise ValueError(
                f"source-policy no-native-text OCR execution plan {field} must be non-empty"
            )

    source_labels = {source.get("label") for source in payload["sources"]}
    for label in [
        "PyMuPDF OCR recipes",
        "PyMuPDF Page.get_textpage_ocr",
        "Tesseract command line usage",
        "OCR-D evaluation",
    ]:
        if label not in source_labels:
            raise ValueError(f"OCR execution plan missing source: {label}")

    for note in [
        "source-policy no-native-text OCR execution plan only",
        "not OCR execution evidence",
        "not OCR quality evidence",
        "not robust PDF extraction evidence",
        "not arbitrary-market PDF parsing evidence",
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
                f"source-policy no-native-text OCR execution plan missing boundary note: {note}"
            )


def _validate_preserved_route(route: dict[str, Any]) -> None:
    expected_values = {
        "fixture_id": "nara_911_mfr_00282_no_native_text_candidate",
        "publisher": "National Archives and Records Administration",
        "failure_type": "no_native_text_observed",
        "page_count": 4,
        "empty_page_count": 4,
        "text_char_count": 0,
    }
    for field, expected in expected_values.items():
        if route.get(field) != expected:
            raise ValueError(f"preserved OCR execution plan route {field} must be {expected!r}")


def _validate_forbidden_fields(value: Any) -> None:
    if isinstance(value, dict):
        for key, nested in value.items():
            if key in _FORBIDDEN_FIELDS:
                raise ValueError(
                    f"source-policy no-native-text OCR execution plan must not commit {key}"
                )
            _validate_forbidden_fields(nested)
    elif isinstance(value, list):
        for item in value:
            _validate_forbidden_fields(item)


def _format_bool(value: bool) -> str:
    return "true" if value else "false"
