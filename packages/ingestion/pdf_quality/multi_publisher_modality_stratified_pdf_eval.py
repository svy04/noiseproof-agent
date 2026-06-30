from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PHASE_MARKER = "multi_publisher_modality_stratified_pdf_eval_v0"
PREVIOUS_GATE = "robust_pdf_extraction_generalization_gap_review_v0"
CLAIM_BOUNDARY = "stratified_pdf_eval_matrix_blocks_robust_pdf_extraction_claim"
NEXT_GATE = "targeted_real_world_pdf_fixture_expansion_v0"

_COVERED_LIMITED = "covered_limited"
_MISSING = "missing"

_FORBIDDEN_FIELDS = {
    "raw_text",
    "raw_extracted_text",
    "raw_ocr_text",
    "raw_table_rows",
    "text_sample",
    "page_image",
    "screenshot",
    "rendered_page_image",
    "local_pdf_path",
}

_REQUIRED_AXES = {
    "publisher",
    "modality",
    "failure_class",
    "evidence_role",
    "rights_boundary",
}

_REQUIRED_MISSING_REASONS = {
    "reading_order_ground_truth_missing",
    "rendered_visual_fidelity_missing",
    "labeled_layout_ground_truth_missing",
    "image_chart_interpretation_missing",
    "real_world_no_extractable_text_failure_missing",
    "external_reviewer_validation_missing",
}


def load_multi_publisher_modality_stratified_pdf_eval(
    path: Path | str,
) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    _validate_matrix(payload)
    return payload


def build_multi_publisher_modality_stratified_pdf_eval_summary(
    matrix: dict[str, Any],
) -> dict[str, Any]:
    _validate_matrix(matrix)
    cells = list(matrix["matrix_cells"])
    covered_cells = [
        cell for cell in cells if cell["evidence_status"] == _COVERED_LIMITED
    ]
    missing_cells = [cell for cell in cells if cell["evidence_status"] == _MISSING]

    return {
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "matrix_status": matrix["matrix_status"],
        "coverage_status": matrix["coverage_status"],
        "robust_pdf_eval_status": matrix["robust_pdf_eval_status"],
        "publisher_stratum_count": len(matrix["publisher_strata"]),
        "modality_stratum_count": len(matrix["modality_strata"]),
        "matrix_cell_count": len(cells),
        "covered_limited_cell_count": len(covered_cells),
        "missing_cell_count": len(missing_cells),
        "publishers": matrix["publisher_strata"],
        "modality_strata": matrix["modality_strata"],
        "stratification_axes": matrix["stratification_axes"],
        "source_patterns": matrix["source_patterns"],
        "can_claim_robust_pdf_extraction": False,
        "matrix_cells": cells,
        "covered_cells": covered_cells,
        "missing_cells": missing_cells,
        "minimum_next_evidence": matrix["minimum_next_evidence"],
        "blocked_reasons": matrix["blocked_reasons"],
        "warnings": matrix["warnings"],
        "boundary_notes": matrix["boundary_notes"],
        "passed_checks": [
            "publisher_strata_visible",
            "modality_strata_visible",
            "matrix_cells_visible",
            "covered_and_missing_cells_separated",
            "robust_claim_blocked",
            "runtime_work_not_performed",
            "external_binaries_not_committed",
            "raw_text_not_committed",
        ],
        "next_gate": NEXT_GATE,
    }


def build_multi_publisher_modality_stratified_pdf_eval_report(
    summary: dict[str, Any],
) -> str:
    lines = [
        "# Multi-publisher Modality-stratified PDF Eval",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report turns the robust-PDF generalization gap review into a publisher/modality/failure-class matrix.",
        "",
        "It is a stratified evaluation matrix, not robust PDF extraction evidence.",
        "",
        "It does not add new runtime evidence.",
        "",
        "## Gate Result",
        "",
        f"matrix_status -> {summary['matrix_status']}",
        f"coverage_status -> {summary['coverage_status']}",
        f"robust_pdf_eval_status -> {summary['robust_pdf_eval_status']}",
        f"previous_gate -> {summary['previous_gate']}",
        f"publisher_stratum_count -> {summary['publisher_stratum_count']}",
        f"modality_stratum_count -> {summary['modality_stratum_count']}",
        f"matrix_cell_count -> {summary['matrix_cell_count']}",
        f"covered_limited_cell_count -> {summary['covered_limited_cell_count']}",
        f"missing_cell_count -> {summary['missing_cell_count']}",
        f"can_claim_robust_pdf_extraction -> {_format_bool(summary['can_claim_robust_pdf_extraction'])}",
        "",
        "## Stratification Axes",
        "",
    ]
    for axis in summary["stratification_axes"]:
        lines.append(f"- {axis}")

    lines.extend(["", "## Publishers", ""])
    for publisher in summary["publishers"]:
        lines.append(f"- {publisher}")

    lines.extend(["", "## Modalities", ""])
    for modality in summary["modality_strata"]:
        lines.append(f"- {modality}")

    lines.extend(["", "## Source Patterns", ""])
    for source_pattern in summary["source_patterns"]:
        lines.append(f"- {source_pattern}")

    lines.extend(["", "## Matrix Cells", ""])
    lines.extend(
        [
            "| Cell | Publisher | Modality | Failure class | Role | Status | Route | Missing evidence |",
            "|---|---|---|---|---|---|---|---|",
        ]
    )
    for cell in summary["matrix_cells"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    cell["cell_id"],
                    cell["publisher"],
                    cell["modality"],
                    cell["failure_class"],
                    cell["evidence_role"],
                    cell["evidence_status"],
                    cell["source_route"],
                    cell["missing_evidence"],
                ]
            )
            + " |"
        )

    lines.extend(["", "## Missing Cells", ""])
    for cell in summary["missing_cells"]:
        lines.append(f"- {cell['cell_id']} -> {cell['missing_evidence']}")

    lines.extend(["", "## Blocked Reasons", ""])
    for reason in summary["blocked_reasons"]:
        lines.append(f"- {reason}")

    lines.extend(["", "## Minimum Next Evidence", ""])
    for item in summary["minimum_next_evidence"]:
        lines.append(f"- {item}")

    lines.extend(["", "## Passed Checks", ""])
    for check in summary["passed_checks"]:
        lines.append(f"- {check}")

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
            "This is a deterministic matrix over existing sanitized PDF proof packets.",
            "",
            "It does not download PDFs, parse PDFs, run OCR, extract tables, call LLMs, commit external binaries, commit raw extracted text, commit screenshots, or add new runtime evidence.",
            "",
            "It does not prove robust PDF extraction, arbitrary-market PDF parsing reliability, table extraction benchmark quality, OCR quality benchmark performance, natural reading order correctness, rendered visual fidelity, image/chart interpretation, or external validation.",
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
        "matrix_status": "passed",
        "coverage_status": "partial",
        "robust_pdf_eval_status": "blocked",
        "can_claim_robust_pdf_extraction": False,
        "runtime_work_performed": False,
        "pdf_downloads_performed": False,
        "parser_calls_performed": False,
        "ocr_calls_performed": False,
        "table_extraction_calls_performed": False,
        "llm_calls_performed": False,
        "binary_files_committed": False,
        "download_cache_committed": False,
        "raw_extracted_text_committed": False,
        "raw_ocr_text_committed": False,
        "raw_table_rows_committed": False,
        "page_images_committed": False,
        "screenshots_committed": False,
        "recommended_next_gate": NEXT_GATE,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(f"stratified PDF eval {field} must be {expected!r}")

    axes = payload.get("stratification_axes")
    if not isinstance(axes, list) or set(axes) != _REQUIRED_AXES:
        raise ValueError("stratified PDF eval axes must match the required axes")

    for field, expected_count in [
        ("publisher_strata", 3),
        ("modality_strata", 9),
        ("source_patterns", 7),
    ]:
        value = payload.get(field)
        if not isinstance(value, list) or len(value) != expected_count:
            raise ValueError(f"stratified PDF eval {field} count mismatch")

    cells = payload.get("matrix_cells")
    if not isinstance(cells, list) or len(cells) != 12:
        raise ValueError("stratified PDF eval must include exactly 12 matrix cells")
    seen_ids: set[str] = set()
    covered_count = 0
    missing_count = 0
    for cell in cells:
        status = _validate_cell(cell, seen_ids)
        if status == _COVERED_LIMITED:
            covered_count += 1
        if status == _MISSING:
            missing_count += 1
    if covered_count != 6 or missing_count != 6:
        raise ValueError("stratified PDF eval must have 6 covered and 6 missing cells")

    blocked_reasons = payload.get("blocked_reasons")
    if not isinstance(blocked_reasons, list):
        raise ValueError("stratified PDF eval blocked_reasons must be a list")
    if set(blocked_reasons) != _REQUIRED_MISSING_REASONS:
        raise ValueError("stratified PDF eval blocked reasons must match missing cells")

    for field in ["minimum_next_evidence", "warnings", "boundary_notes"]:
        value = payload.get(field)
        if not isinstance(value, list) or not value:
            raise ValueError(f"stratified PDF eval {field} must be a non-empty list")

    for note in [
        "stratified PDF evaluation matrix only",
        "does not add new runtime evidence",
        "not robust PDF extraction evidence",
        "not arbitrary-market PDF parsing evidence",
        "not table extraction benchmark evidence",
        "not OCR quality benchmark evidence",
        "not hosted deployment evidence",
        "not external reviewer feedback",
        "not product-complete",
    ]:
        if note not in payload["boundary_notes"]:
            raise ValueError(f"stratified PDF eval missing boundary note: {note}")


def _validate_cell(cell: dict[str, Any], seen_ids: set[str]) -> str:
    if not isinstance(cell, dict):
        raise ValueError("stratified PDF eval matrix cells must be objects")
    cell_id = str(cell.get("cell_id") or "")
    if not cell_id:
        raise ValueError("stratified PDF eval matrix cell missing cell_id")
    if cell_id in seen_ids:
        raise ValueError(f"duplicate matrix cell: {cell_id}")
    seen_ids.add(cell_id)
    for field in [
        "publisher",
        "modality",
        "failure_class",
        "evidence_role",
        "source_route",
        "current_evidence",
        "missing_evidence",
        "boundary",
    ]:
        if not cell.get(field):
            raise ValueError(f"matrix cell {cell_id} missing {field}")
    status = cell.get("evidence_status")
    if status not in {_COVERED_LIMITED, _MISSING}:
        raise ValueError(f"matrix cell {cell_id} has invalid evidence_status")
    return str(status)


def _validate_forbidden_fields(value: Any) -> None:
    if isinstance(value, dict):
        for key, nested in value.items():
            if key in _FORBIDDEN_FIELDS:
                raise ValueError(f"stratified PDF eval must not commit {key}")
            _validate_forbidden_fields(nested)
    elif isinstance(value, list):
        for item in value:
            _validate_forbidden_fields(item)


def _format_bool(value: bool) -> str:
    return "true" if value else "false"
