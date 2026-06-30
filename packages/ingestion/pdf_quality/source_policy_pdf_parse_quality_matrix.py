from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PHASE_MARKER = "source_policy_pdf_parse_quality_matrix_v0"
PREVIOUS_GATE = "source_policy_pdf_parse_observation_v0"
CLAIM_BOUNDARY = "source_policy_parse_quality_matrix_only_not_pdf_quality_evidence"
NEXT_GATE = "source_policy_pdf_quality_gap_review_v0"

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

_REQUIRED_MISSING_CELLS = {
    "multi_publisher_rendered_visual_fidelity",
    "multi_publisher_labeled_layout_ground_truth",
    "multi_publisher_no_extractable_text_failure",
    "multi_publisher_reading_order",
    "multi_publisher_image_chart_interpretation",
    "external_reviewer_validation",
}

_CELL_STATUSES = {
    "metadata_observed_quality_unproven",
    "no_native_text_failure_candidate",
    "blocked_download",
    "external_review_pending",
}


def load_source_policy_pdf_parse_quality_matrix(path: Path | str) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    _validate_matrix(payload)
    return payload


def build_source_policy_pdf_parse_quality_matrix_summary(
    matrix: dict[str, Any],
) -> dict[str, Any]:
    _validate_matrix(matrix)
    cells = list(matrix["matrix_cells"])
    native_text = [
        cell
        for cell in cells
        if cell["cell_status"] == "metadata_observed_quality_unproven"
    ]
    no_native_text = [
        cell
        for cell in cells
        if cell["cell_status"] == "no_native_text_failure_candidate"
    ]
    blocked_downloads = [
        cell for cell in cells if cell["cell_status"] == "blocked_download"
    ]
    external_routes = [
        cell for cell in cells if cell["cell_status"] == "external_review_pending"
    ]
    quality_ready = [cell for cell in cells if cell["quality_claim_ready"] is True]
    return {
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "source_parse_observation_manifest": matrix[
            "source_parse_observation_manifest"
        ],
        "matrix_status": matrix["matrix_status"],
        "quality_status": matrix["quality_status"],
        "matrix_cell_count": len(cells),
        "observed_fixture_cell_count": len(native_text) + len(no_native_text),
        "native_text_observed_cell_count": len(native_text),
        "no_native_text_failure_cell_count": len(no_native_text),
        "blocked_download_cell_count": len(blocked_downloads),
        "external_route_cell_count": len(external_routes),
        "quality_claim_ready_cell_count": len(quality_ready),
        "quality_blocked_cell_count": len(cells) - len(quality_ready),
        "can_claim_source_policy_pdf_parse_quality_matrix": True,
        "can_claim_robust_pdf_extraction": False,
        "can_claim_rendered_visual_fidelity": False,
        "can_claim_labeled_layout_ground_truth": False,
        "can_claim_reading_order": False,
        "can_claim_image_chart_interpretation": False,
        "can_claim_ocr_quality": False,
        "can_claim_external_validation": False,
        "runtime_work_performed": False,
        "pdf_downloads_performed": False,
        "parser_calls_performed": False,
        "ocr_calls_performed": False,
        "table_extraction_calls_performed": False,
        "llm_calls_performed": False,
        "binary_files_committed": False,
        "download_cache_committed": False,
        "raw_text_committed": False,
        "matrix_cells": cells,
        "blocked_reasons": matrix["blocked_reasons"],
        "minimum_next_evidence": matrix["minimum_next_evidence"],
        "warnings": matrix["warnings"],
        "boundary_notes": matrix["boundary_notes"],
        "next_gate": NEXT_GATE,
    }


def build_source_policy_pdf_parse_quality_matrix_report(
    summary: dict[str, Any],
) -> str:
    lines = [
        "# Source-policy PDF Parse Quality Matrix",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report turns source-policy PDF parse observations into a quality-claim blocker matrix.",
        "",
        "It does not add new runtime evidence.",
        "",
        "It is not robust PDF extraction evidence.",
        "",
        "## Gate Result",
        "",
        f"matrix_status -> {summary['matrix_status']}",
        f"quality_status -> {summary['quality_status']}",
        f"previous_gate -> {summary['previous_gate']}",
        f"matrix_cell_count -> {summary['matrix_cell_count']}",
        f"observed_fixture_cell_count -> {summary['observed_fixture_cell_count']}",
        f"native_text_observed_cell_count -> {summary['native_text_observed_cell_count']}",
        f"no_native_text_failure_cell_count -> {summary['no_native_text_failure_cell_count']}",
        f"blocked_download_cell_count -> {summary['blocked_download_cell_count']}",
        f"external_route_cell_count -> {summary['external_route_cell_count']}",
        f"quality_claim_ready_cell_count -> {summary['quality_claim_ready_cell_count']}",
        f"quality_blocked_cell_count -> {summary['quality_blocked_cell_count']}",
        f"runtime_work_performed -> {_format_bool(summary['runtime_work_performed'])}",
        f"pdf_downloads_performed -> {_format_bool(summary['pdf_downloads_performed'])}",
        f"parser_calls_performed -> {_format_bool(summary['parser_calls_performed'])}",
        f"ocr_calls_performed -> {_format_bool(summary['ocr_calls_performed'])}",
        f"table_extraction_calls_performed -> {_format_bool(summary['table_extraction_calls_performed'])}",
        f"llm_calls_performed -> {_format_bool(summary['llm_calls_performed'])}",
        f"binary_files_committed -> {_format_bool(summary['binary_files_committed'])}",
        f"download_cache_committed -> {_format_bool(summary['download_cache_committed'])}",
        f"raw_text_committed -> {_format_bool(summary['raw_text_committed'])}",
        f"can_claim_source_policy_pdf_parse_quality_matrix -> {_format_bool(summary['can_claim_source_policy_pdf_parse_quality_matrix'])}",
        f"can_claim_robust_pdf_extraction -> {_format_bool(summary['can_claim_robust_pdf_extraction'])}",
        f"can_claim_rendered_visual_fidelity -> {_format_bool(summary['can_claim_rendered_visual_fidelity'])}",
        f"can_claim_labeled_layout_ground_truth -> {_format_bool(summary['can_claim_labeled_layout_ground_truth'])}",
        f"can_claim_reading_order -> {_format_bool(summary['can_claim_reading_order'])}",
        f"can_claim_image_chart_interpretation -> {_format_bool(summary['can_claim_image_chart_interpretation'])}",
        f"can_claim_ocr_quality -> {_format_bool(summary['can_claim_ocr_quality'])}",
        f"can_claim_external_validation -> {_format_bool(summary['can_claim_external_validation'])}",
        "",
        "## Matrix Cells",
        "",
        "| Cell | Missing cell | Publisher | Status | Quality ready | Missing quality evidence | Boundary |",
        "|---|---|---|---|---|---|---|",
    ]
    for cell in summary["matrix_cells"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    cell["cell_id"],
                    cell["target_missing_cell"],
                    cell["publisher"],
                    cell["cell_status"],
                    _format_bool(cell["quality_claim_ready"]),
                    cell["missing_quality_evidence"],
                    cell["boundary"],
                ]
            )
            + " |"
        )

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
            "This is a deterministic quality-claim blocker matrix over the existing source-policy PDF parse observation packet.",
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


def _validate_matrix(payload: dict[str, Any]) -> None:
    _validate_forbidden_fields(payload)
    expected_values = {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "source_parse_observation_manifest": "examples/pdf-extraction-quality/source-policy-pdf-parse-observations.json",
        "matrix_status": "passed",
        "quality_status": "blocked",
        "owner_approved": True,
        "can_claim_source_policy_pdf_parse_quality_matrix": True,
        "can_claim_robust_pdf_extraction": False,
        "can_claim_rendered_visual_fidelity": False,
        "can_claim_labeled_layout_ground_truth": False,
        "can_claim_reading_order": False,
        "can_claim_image_chart_interpretation": False,
        "can_claim_ocr_quality": False,
        "can_claim_external_validation": False,
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
                f"source-policy parse quality matrix {field} must be {expected!r}"
            )

    cells = payload.get("matrix_cells")
    if not isinstance(cells, list) or len(cells) != 6:
        raise ValueError("source-policy parse quality matrix must include 6 cells")
    seen_ids: set[str] = set()
    seen_roles: set[str] = set()
    quality_ready_count = 0
    status_counts = {status: 0 for status in _CELL_STATUSES}
    for cell in cells:
        status = _validate_cell(cell, seen_ids)
        seen_roles.add(cell["target_missing_cell"])
        status_counts[status] += 1
        if cell["quality_claim_ready"] is True:
            quality_ready_count += 1
    if seen_roles != _REQUIRED_MISSING_CELLS:
        raise ValueError("source-policy parse quality matrix roles are incomplete")
    if quality_ready_count != 0:
        raise ValueError("source-policy parse quality matrix must not mark quality ready")
    expected_status_counts = {
        "metadata_observed_quality_unproven": 2,
        "no_native_text_failure_candidate": 1,
        "blocked_download": 2,
        "external_review_pending": 1,
    }
    if status_counts != expected_status_counts:
        raise ValueError("source-policy parse quality matrix status counts mismatch")

    for field in ["blocked_reasons", "minimum_next_evidence", "warnings", "boundary_notes"]:
        value = payload.get(field)
        if not isinstance(value, list) or not value:
            raise ValueError(f"source-policy parse quality matrix {field} must be non-empty")

    for note in [
        "source-policy PDF parse quality matrix only",
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
                f"source-policy parse quality matrix missing boundary note: {note}"
            )


def _validate_cell(cell: dict[str, Any], seen_ids: set[str]) -> str:
    if not isinstance(cell, dict):
        raise ValueError("source-policy parse quality matrix cells must be objects")
    cell_id = str(cell.get("cell_id") or "")
    if not cell_id:
        raise ValueError("source-policy parse quality matrix cell missing cell_id")
    if cell_id in seen_ids:
        raise ValueError(f"duplicate source-policy parse quality matrix cell: {cell_id}")
    seen_ids.add(cell_id)
    for field in [
        "target_missing_cell",
        "publisher",
        "fixture_id",
        "source_url",
        "policy_source_url",
        "input_status",
        "current_evidence",
        "missing_quality_evidence",
        "boundary",
    ]:
        if not cell.get(field):
            raise ValueError(f"matrix cell {cell_id} missing {field}")
    for field in ["source_url", "policy_source_url"]:
        if not str(cell[field]).startswith("https://"):
            raise ValueError(f"matrix cell {cell_id} {field} must be https")
    target_missing_cell = cell["target_missing_cell"]
    if target_missing_cell not in _REQUIRED_MISSING_CELLS:
        raise ValueError(f"matrix cell {cell_id} has unsupported target_missing_cell")
    status = str(cell.get("cell_status") or "")
    if status not in _CELL_STATUSES:
        raise ValueError(f"matrix cell {cell_id} has unsupported cell_status")
    if cell.get("quality_claim_ready") is not False:
        raise ValueError(f"matrix cell {cell_id} must keep quality_claim_ready false")
    if "not robust PDF extraction evidence" not in cell["boundary"]:
        raise ValueError(f"matrix cell {cell_id} boundary must block robust PDF claim")
    if status == "no_native_text_failure_candidate":
        failure = cell.get("failure_case_candidate")
        if not isinstance(failure, dict) or failure.get("failure_type") != "no_native_text_observed":
            raise ValueError(f"matrix cell {cell_id} must preserve no-native-text failure")
    return status


def _validate_forbidden_fields(value: Any) -> None:
    if isinstance(value, dict):
        for key, nested in value.items():
            if key in _FORBIDDEN_FIELDS:
                raise ValueError(
                    f"source-policy parse quality matrix must not commit {key}"
                )
            _validate_forbidden_fields(nested)
    elif isinstance(value, list):
        for item in value:
            _validate_forbidden_fields(item)


def _format_bool(value: bool) -> str:
    return "true" if value else "false"
