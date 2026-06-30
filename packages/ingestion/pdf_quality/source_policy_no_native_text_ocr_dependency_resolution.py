from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PHASE_MARKER = "source_policy_no_native_text_ocr_dependency_resolution_v0"
PREVIOUS_GATE = "source_policy_no_native_text_ocr_dependency_check_v0"
CLAIM_BOUNDARY = (
    "source_policy_no_native_text_ocr_dependency_resolution_only_not_execution_or_quality_evidence"
)
NEXT_GATE = "source_policy_no_native_text_ocr_execution_plan_v0"

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


def load_source_policy_no_native_text_ocr_dependency_resolution(
    path: Path | str,
) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    _validate_resolution(payload)
    return payload


def build_source_policy_no_native_text_ocr_dependency_resolution_summary(
    resolution: dict[str, Any],
) -> dict[str, Any]:
    _validate_resolution(resolution)
    preserved_route = dict(resolution["preserved_failure_route"])
    return {
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "source_dependency_check_manifest": resolution[
            "source_dependency_check_manifest"
        ],
        "dependency_resolution_status": resolution[
            "dependency_resolution_status"
        ],
        "observation_source": resolution["observation_source"],
        "installation_method": resolution["installation_method"],
        "installation_package_id": resolution["installation_package_id"],
        "installed_package_version": resolution["installed_package_version"],
        "codex_parent_path_inheritance_mismatch": resolution[
            "codex_parent_path_inheritance_mismatch"
        ],
        "owner_runtime_path_refresh_performed": resolution[
            "owner_runtime_path_refresh_performed"
        ],
        "fixture_id": preserved_route["fixture_id"],
        "publisher": preserved_route["publisher"],
        "failure_type": preserved_route["failure_type"],
        "page_count": preserved_route["page_count"],
        "empty_page_count": preserved_route["empty_page_count"],
        "text_char_count": preserved_route["text_char_count"],
        "tesseract_command_present": resolution["tesseract_command_present"],
        "version_check_performed": resolution["version_check_performed"],
        "language_list_check_performed": resolution[
            "language_list_check_performed"
        ],
        "tesseract_version_reported": resolution[
            "tesseract_version_reported"
        ],
        "tesseract_version": resolution["tesseract_version"],
        "detected_language_count": resolution["detected_language_count"],
        "eng_language_available": resolution["eng_language_available"],
        "local_path_discovery_performed": resolution[
            "local_path_discovery_performed"
        ],
        "local_paths_committed": resolution["local_paths_committed"],
        "tesseract_path_committed": resolution["tesseract_path_committed"],
        "tessdata_path_committed": resolution["tessdata_path_committed"],
        "runtime_work_performed": resolution["runtime_work_performed"],
        "pdf_downloads_performed": False,
        "parser_calls_performed": False,
        "ocr_execution_performed": False,
        "ocr_quality_eval_performed": False,
        "table_extraction_calls_performed": False,
        "llm_calls_performed": False,
        "binary_files_committed": False,
        "download_cache_committed": False,
        "raw_text_committed": False,
        "raw_ocr_text_committed": False,
        "can_claim_ocr_dependency_available": True,
        "can_claim_ocr_execution": False,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
        "sources": resolution["sources"],
        "resolved_evidence": resolution["resolved_evidence"],
        "remaining_blockers": resolution["remaining_blockers"],
        "minimum_next_evidence": resolution["minimum_next_evidence"],
        "warnings": resolution["warnings"],
        "boundary_notes": resolution["boundary_notes"],
        "next_gate": NEXT_GATE,
    }


def build_source_policy_no_native_text_ocr_dependency_resolution_report(
    summary: dict[str, Any],
) -> str:
    lines = [
        "# Source-policy No-native-text OCR Dependency Resolution",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report records a sanitized owner-runtime dependency resolution observation for the preserved NARA no-native-text route.",
        "",
        "It records command and English language-data availability only.",
        "",
        "It does not commit local executable or tessdata paths.",
        "",
        "It does not run OCR.",
        "",
        "It is not OCR quality evidence.",
        "",
        "It is not robust PDF extraction evidence.",
        "",
        "## Gate Result",
        "",
        f"dependency_resolution_status -> {summary['dependency_resolution_status']}",
        f"previous_gate -> {summary['previous_gate']}",
        f"observation_source -> {summary['observation_source']}",
        f"installation_method -> {summary['installation_method']}",
        f"installation_package_id -> {summary['installation_package_id']}",
        f"installed_package_version -> {summary['installed_package_version']}",
        f"codex_parent_path_inheritance_mismatch -> {_format_bool(summary['codex_parent_path_inheritance_mismatch'])}",
        f"owner_runtime_path_refresh_performed -> {_format_bool(summary['owner_runtime_path_refresh_performed'])}",
        f"fixture_id -> {summary['fixture_id']}",
        f"publisher -> {summary['publisher']}",
        f"failure_type -> {summary['failure_type']}",
        f"page_count -> {summary['page_count']}",
        f"empty_page_count -> {summary['empty_page_count']}",
        f"text_char_count -> {summary['text_char_count']}",
        f"tesseract_command_present -> {_format_bool(summary['tesseract_command_present'])}",
        f"version_check_performed -> {_format_bool(summary['version_check_performed'])}",
        f"language_list_check_performed -> {_format_bool(summary['language_list_check_performed'])}",
        f"tesseract_version_reported -> {_format_bool(summary['tesseract_version_reported'])}",
        f"tesseract_version -> {summary['tesseract_version']}",
        f"detected_language_count -> {summary['detected_language_count']}",
        f"eng_language_available -> {_format_bool(summary['eng_language_available'])}",
        f"local_path_discovery_performed -> {_format_bool(summary['local_path_discovery_performed'])}",
        f"local_paths_committed -> {_format_bool(summary['local_paths_committed'])}",
        f"tesseract_path_committed -> {_format_bool(summary['tesseract_path_committed'])}",
        f"tessdata_path_committed -> {_format_bool(summary['tessdata_path_committed'])}",
        f"runtime_work_performed -> {_format_bool(summary['runtime_work_performed'])}",
        f"pdf_downloads_performed -> {_format_bool(summary['pdf_downloads_performed'])}",
        f"parser_calls_performed -> {_format_bool(summary['parser_calls_performed'])}",
        f"ocr_execution_performed -> {_format_bool(summary['ocr_execution_performed'])}",
        f"ocr_quality_eval_performed -> {_format_bool(summary['ocr_quality_eval_performed'])}",
        f"table_extraction_calls_performed -> {_format_bool(summary['table_extraction_calls_performed'])}",
        f"llm_calls_performed -> {_format_bool(summary['llm_calls_performed'])}",
        f"binary_files_committed -> {_format_bool(summary['binary_files_committed'])}",
        f"download_cache_committed -> {_format_bool(summary['download_cache_committed'])}",
        f"raw_text_committed -> {_format_bool(summary['raw_text_committed'])}",
        f"raw_ocr_text_committed -> {_format_bool(summary['raw_ocr_text_committed'])}",
        f"can_claim_ocr_dependency_available -> {_format_bool(summary['can_claim_ocr_dependency_available'])}",
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

    lines.extend(["", "## Resolved Evidence", ""])
    for item in summary["resolved_evidence"]:
        lines.append(f"- {item}")

    lines.extend(["", "## Remaining Blockers", ""])
    for item in summary["remaining_blockers"]:
        lines.append(f"- {item}")

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
            "This is a deterministic dependency-resolution packet over the current owner-runtime OCR dependency state.",
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


def _validate_resolution(payload: dict[str, Any]) -> None:
    _validate_forbidden_fields(payload)
    expected_values = {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "source_dependency_check_manifest": "examples/pdf-extraction-quality/source-policy-no-native-text-ocr-dependency-check.json",
        "dependency_resolution_status": "resolved_dependency_available",
        "observation_source": "owner_runtime_path_refresh_after_winget_install_2026_06_30",
        "owner_approved": True,
        "installation_method": "winget",
        "installation_package_id": "tesseract-ocr.tesseract",
        "installed_package_version": "5.5.0.20241111",
        "codex_parent_path_inheritance_mismatch": True,
        "owner_runtime_path_refresh_performed": True,
        "tesseract_command_present": True,
        "version_check_performed": True,
        "language_list_check_performed": True,
        "tesseract_version_reported": True,
        "tesseract_version": "5.5.0.20241111",
        "detected_language_count": 2,
        "eng_language_available": True,
        "local_path_discovery_performed": True,
        "local_paths_committed": False,
        "tesseract_path_committed": False,
        "tessdata_path_committed": False,
        "runtime_work_performed": True,
        "pdf_downloads_performed": False,
        "parser_calls_performed": False,
        "ocr_execution_performed": False,
        "ocr_quality_eval_performed": False,
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
        "can_claim_ocr_dependency_available": True,
        "can_claim_ocr_execution": False,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
        "recommended_next_gate": NEXT_GATE,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(
                f"source-policy no-native-text OCR dependency resolution {field} must be {expected!r}"
            )

    preserved_route = payload.get("preserved_failure_route")
    if not isinstance(preserved_route, dict):
        raise ValueError("OCR dependency resolution must include preserved_failure_route")
    _validate_preserved_route(preserved_route)

    for field in [
        "sources",
        "resolved_evidence",
        "remaining_blockers",
        "minimum_next_evidence",
        "warnings",
        "boundary_notes",
    ]:
        value = payload.get(field)
        if not isinstance(value, list) or not value:
            raise ValueError(
                f"source-policy no-native-text OCR dependency resolution {field} must be non-empty"
            )

    source_labels = {source.get("label") for source in payload["sources"]}
    for label in [
        "Tesseract command line usage",
        "Tesseract installation",
        "PyMuPDF OCR recipes",
        "OCR-D evaluation",
        "Windows Package Manager",
    ]:
        if label not in source_labels:
            raise ValueError(f"OCR dependency resolution missing source: {label}")

    for note in [
        "source-policy no-native-text OCR dependency resolution only",
        "OCR dependency availability evidence only",
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
                f"source-policy no-native-text OCR dependency resolution missing boundary note: {note}"
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
            raise ValueError(f"preserved dependency route {field} must be {expected!r}")


def _validate_forbidden_fields(value: Any) -> None:
    if isinstance(value, dict):
        for key, nested in value.items():
            if key in _FORBIDDEN_FIELDS:
                raise ValueError(
                    f"source-policy no-native-text OCR dependency resolution must not commit {key}"
                )
            _validate_forbidden_fields(nested)
    elif isinstance(value, list):
        for item in value:
            _validate_forbidden_fields(item)


def _format_bool(value: bool) -> str:
    return "true" if value else "false"
