from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PHASE_MARKER = "targeted_real_world_pdf_fixture_expansion_v0"
PREVIOUS_GATE = "multi_publisher_modality_stratified_pdf_eval_v0"
CLAIM_BOUNDARY = (
    "source_policy_reviewed_fixture_expansion_plan_only_not_runtime_pdf_evidence"
)
NEXT_GATE = "real_world_pdf_fixture_source_policy_download_hash_v0"

_REQUIRED_MISSING_CELLS = {
    "multi_publisher_reading_order",
    "multi_publisher_rendered_visual_fidelity",
    "multi_publisher_labeled_layout_ground_truth",
    "multi_publisher_image_chart_interpretation",
    "multi_publisher_no_extractable_text_failure",
    "external_reviewer_validation",
}

_ALLOWED_POLICY_STATUSES = {
    "source_policy_reviewed_metadata_only",
    "external_review_route_only",
}

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
}


def load_targeted_real_world_pdf_fixture_expansion_plan(
    path: Path | str,
) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    _validate_plan(payload)
    return payload


def build_targeted_real_world_pdf_fixture_expansion_summary(
    plan: dict[str, Any],
) -> dict[str, Any]:
    _validate_plan(plan)
    candidates = list(plan["candidates"])
    covered_missing_cells = sorted(
        {str(candidate["target_missing_cell"]) for candidate in candidates}
    )
    downloaded_candidates = [
        candidate
        for candidate in candidates
        if candidate.get("download_status") == "downloaded"
    ]
    candidate_by_cell: dict[str, list[str]] = {}
    for candidate in candidates:
        cell = str(candidate["target_missing_cell"])
        candidate_by_cell.setdefault(cell, []).append(str(candidate["fixture_id"]))

    return {
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "plan_status": plan["plan_status"],
        "coverage_status": plan["coverage_status"],
        "candidate_count": len(candidates),
        "missing_cell_count": len(plan["missing_cells"]),
        "covered_missing_cell_count": len(covered_missing_cells),
        "covered_missing_cells": covered_missing_cells,
        "source_policy_source_count": len(plan["source_policy_sources"]),
        "downloaded_candidate_count": len(downloaded_candidates),
        "runtime_work_performed": False,
        "pdf_downloads_performed": False,
        "parser_calls_performed": False,
        "ocr_calls_performed": False,
        "table_extraction_calls_performed": False,
        "llm_calls_performed": False,
        "binary_files_committed": False,
        "raw_text_committed": False,
        "can_claim_robust_pdf_extraction": False,
        "source_policy_sources": plan["source_policy_sources"],
        "candidates": candidates,
        "candidate_by_cell": candidate_by_cell,
        "minimum_next_evidence": plan["minimum_next_evidence"],
        "blocked_reasons": plan["blocked_reasons"],
        "warnings": plan["warnings"],
        "boundary_notes": plan["boundary_notes"],
        "next_gate": NEXT_GATE,
    }


def build_targeted_real_world_pdf_fixture_expansion_report(
    summary: dict[str, Any],
) -> str:
    lines = [
        "# Targeted Real-world PDF Fixture Expansion Plan",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report maps each missing PDF matrix cell to a source-policy-reviewed candidate fixture or reviewer route.",
        "",
        "It is a fixture expansion plan, not runtime PDF evidence.",
        "",
        "It does not add new runtime evidence.",
        "",
        "## Gate Result",
        "",
        f"plan_status -> {summary['plan_status']}",
        f"coverage_status -> {summary['coverage_status']}",
        f"previous_gate -> {summary['previous_gate']}",
        f"candidate_count -> {summary['candidate_count']}",
        f"missing_cell_count -> {summary['missing_cell_count']}",
        f"covered_missing_cell_count -> {summary['covered_missing_cell_count']}",
        f"source_policy_source_count -> {summary['source_policy_source_count']}",
        f"downloaded_candidate_count -> {summary['downloaded_candidate_count']}",
        f"runtime_work_performed -> {_format_bool(summary['runtime_work_performed'])}",
        f"pdf_downloads_performed -> {_format_bool(summary['pdf_downloads_performed'])}",
        f"parser_calls_performed -> {_format_bool(summary['parser_calls_performed'])}",
        f"ocr_calls_performed -> {_format_bool(summary['ocr_calls_performed'])}",
        f"table_extraction_calls_performed -> {_format_bool(summary['table_extraction_calls_performed'])}",
        f"llm_calls_performed -> {_format_bool(summary['llm_calls_performed'])}",
        f"binary_files_committed -> {_format_bool(summary['binary_files_committed'])}",
        f"raw_text_committed -> {_format_bool(summary['raw_text_committed'])}",
        f"can_claim_robust_pdf_extraction -> {_format_bool(summary['can_claim_robust_pdf_extraction'])}",
        "",
        "## Source Policy Sources",
        "",
    ]
    for source in summary["source_policy_sources"]:
        lines.append(f"- {source['publisher']} -> {source['url']}")

    lines.extend(["", "## Missing Cell Coverage", ""])
    for cell in summary["covered_missing_cells"]:
        fixture_ids = ", ".join(summary["candidate_by_cell"][cell])
        lines.append(f"- {cell}: {fixture_ids}")

    lines.extend(["", "## Candidate Plan", ""])
    lines.extend(
        [
            "| Candidate | Missing cell | Publisher | Policy status | Download status | Boundary |",
            "|---|---|---|---|---|---|",
        ]
    )
    for candidate in summary["candidates"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    candidate["fixture_id"],
                    candidate["target_missing_cell"],
                    candidate["publisher"],
                    candidate["policy_review_status"],
                    candidate["download_status"],
                    candidate["boundary"],
                ]
            )
            + " |"
        )

    lines.extend(["", "## Candidate Evaluation Intent", ""])
    for candidate in summary["candidates"]:
        lines.append(f"### {candidate['fixture_id']}")
        lines.append("")
        lines.append(f"- source_url: {candidate['source_url']}")
        lines.append(f"- policy_source_url: {candidate['policy_source_url']}")
        lines.append("- evaluation_intent:")
        for item in candidate["evaluation_intent"]:
            lines.append(f"  - {item}")
        lines.append("- acceptance_checks:")
        for item in candidate["acceptance_checks"]:
            lines.append(f"  - {item}")
        lines.append("- stop_conditions:")
        for item in candidate["stop_conditions"]:
            lines.append(f"  - {item}")
        lines.append("")

    lines.extend(["## Minimum Next Evidence", ""])
    for item in summary["minimum_next_evidence"]:
        lines.append(f"- {item}")

    lines.extend(["", "## Blocked Reasons", ""])
    for reason in summary["blocked_reasons"]:
        lines.append(f"- {reason}")

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
            "This is a source-policy-reviewed metadata plan only.",
            "",
            "It does not download PDFs, hash PDFs, parse PDFs, run OCR, extract tables, call LLMs, commit external binaries, commit raw extracted text, commit screenshots, or add new runtime evidence.",
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


def _validate_plan(payload: dict[str, Any]) -> None:
    _validate_forbidden_fields(payload)
    expected_values = {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "plan_status": "passed",
        "coverage_status": "planned",
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
            raise ValueError(f"targeted fixture expansion {field} must be {expected!r}")

    missing_cells = payload.get("missing_cells")
    if not isinstance(missing_cells, list) or set(missing_cells) != _REQUIRED_MISSING_CELLS:
        raise ValueError("targeted fixture expansion missing_cells must match required cells")

    sources = payload.get("source_policy_sources")
    if not isinstance(sources, list) or len(sources) < 5:
        raise ValueError("targeted fixture expansion requires source policy sources")
    for source in sources:
        _require_https(source, "url", "source_policy_source")
        if not source.get("publisher") or not source.get("use_in_plan"):
            raise ValueError("source policy sources require publisher and use_in_plan")

    candidates = payload.get("candidates")
    if not isinstance(candidates, list) or len(candidates) != 6:
        raise ValueError("targeted fixture expansion must include exactly 6 candidates")
    seen_ids: set[str] = set()
    covered_cells: set[str] = set()
    for candidate in candidates:
        covered_cells.add(_validate_candidate(candidate, seen_ids))
    if covered_cells != _REQUIRED_MISSING_CELLS:
        raise ValueError("targeted fixture expansion candidates must cover every missing cell")

    for field in ["minimum_next_evidence", "blocked_reasons", "warnings", "boundary_notes"]:
        value = payload.get(field)
        if not isinstance(value, list) or not value:
            raise ValueError(f"targeted fixture expansion {field} must be a non-empty list")

    for note in [
        "source_policy_reviewed_metadata_only",
        "does not add new runtime evidence",
        "not robust PDF extraction evidence",
        "not arbitrary-market PDF parsing evidence",
        "not OCR quality evidence",
        "not table extraction benchmark evidence",
        "not layout fidelity evidence",
        "not hosted deployment evidence",
        "not external reviewer feedback",
        "not product-complete",
    ]:
        if note not in payload["boundary_notes"]:
            raise ValueError(f"targeted fixture expansion missing boundary note: {note}")


def _validate_candidate(candidate: dict[str, Any], seen_ids: set[str]) -> str:
    if not isinstance(candidate, dict):
        raise ValueError("targeted fixture expansion candidates must be objects")
    fixture_id = str(candidate.get("fixture_id") or "")
    if not fixture_id:
        raise ValueError("targeted fixture expansion candidate missing fixture_id")
    if fixture_id in seen_ids:
        raise ValueError(f"duplicate targeted fixture expansion candidate: {fixture_id}")
    seen_ids.add(fixture_id)

    target_cell = str(candidate.get("target_missing_cell") or "")
    if target_cell not in _REQUIRED_MISSING_CELLS:
        raise ValueError(f"candidate {fixture_id} has invalid target_missing_cell")
    _require_https(candidate, "source_url", fixture_id)
    _require_https(candidate, "policy_source_url", fixture_id)
    if candidate.get("policy_review_status") not in _ALLOWED_POLICY_STATUSES:
        raise ValueError(f"candidate {fixture_id} has invalid policy_review_status")
    if candidate.get("download_status") != "not_downloaded":
        raise ValueError(f"candidate {fixture_id} must remain not_downloaded")
    if candidate.get("local_pdf_path") is not None:
        raise ValueError(f"candidate {fixture_id} must not include local_pdf_path")
    if candidate.get("sha256") is not None:
        raise ValueError(f"candidate {fixture_id} must not include sha256 before download")
    for field in ["evaluation_intent", "acceptance_checks", "stop_conditions"]:
        value = candidate.get(field)
        if not isinstance(value, list) or not value:
            raise ValueError(f"candidate {fixture_id} must include {field}")
    for field in ["publisher", "boundary"]:
        if not candidate.get(field):
            raise ValueError(f"candidate {fixture_id} missing {field}")
    return target_cell


def _validate_forbidden_fields(value: Any) -> None:
    if isinstance(value, dict):
        for key, nested in value.items():
            if key in _FORBIDDEN_FIELDS:
                raise ValueError(f"targeted fixture expansion must not commit {key}")
            _validate_forbidden_fields(nested)
    elif isinstance(value, list):
        for item in value:
            _validate_forbidden_fields(item)


def _require_https(item: dict[str, Any], field: str, fixture_id: str) -> None:
    value = str(item.get(field) or "")
    if not value.startswith("https://"):
        raise ValueError(f"{fixture_id} {field} must be https")


def _format_bool(value: bool) -> str:
    return "true" if value else "false"
