from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PHASE_MARKER = "source_policy_pdf_quality_gap_review_v0"
PREVIOUS_GATE = "source_policy_pdf_parse_quality_matrix_v0"
CLAIM_BOUNDARY = "source_policy_pdf_quality_gap_review_only_not_pdf_quality_evidence"
NEXT_GATE = "source_policy_no_native_text_failure_route_v0"

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

_REQUIRED_GAPS = {
    "multi_publisher_rendered_visual_fidelity",
    "multi_publisher_labeled_layout_ground_truth",
    "multi_publisher_no_extractable_text_failure",
    "multi_publisher_reading_order",
    "multi_publisher_image_chart_interpretation",
    "external_reviewer_validation",
}


def load_source_policy_pdf_quality_gap_review(path: Path | str) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    _validate_review(payload)
    return payload


def build_source_policy_pdf_quality_gap_review_summary(
    review: dict[str, Any],
) -> dict[str, Any]:
    _validate_review(review)
    gaps = list(review["reviewed_gaps"])
    self_completable = [
        gap for gap in gaps if gap["self_completable_without_new_download"] is True
    ]
    quality_ready = [gap for gap in gaps if gap["quality_claim_ready"] is True]
    selected = [gap for gap in gaps if gap["selected_for_next_gate"] is True]
    selected_gap = selected[0]
    return {
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "source_quality_matrix_manifest": review["source_quality_matrix_manifest"],
        "review_status": review["review_status"],
        "quality_gap_status": review["quality_gap_status"],
        "reviewed_gap_count": len(gaps),
        "quality_claim_ready_cell_count": len(quality_ready),
        "quality_blocked_cell_count": len(gaps) - len(quality_ready),
        "self_completable_without_new_download_count": len(self_completable),
        "selected_next_gap": selected_gap["target_missing_cell"],
        "selected_next_gate": review["selected_next_gate"],
        "can_claim_source_policy_pdf_quality_gap_review": True,
        "can_claim_robust_pdf_extraction": False,
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
        "reviewed_gaps": gaps,
        "decision_rules": review["decision_rules"],
        "blocked_reasons": review["blocked_reasons"],
        "minimum_next_evidence": review["minimum_next_evidence"],
        "warnings": review["warnings"],
        "boundary_notes": review["boundary_notes"],
        "next_gate": NEXT_GATE,
    }


def build_source_policy_pdf_quality_gap_review_report(
    summary: dict[str, Any],
) -> str:
    lines = [
        "# Source-policy PDF Quality Gap Review",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report reviews source-policy PDF quality blockers and selects the smallest inspectable next gate.",
        "",
        "It does not add new runtime evidence.",
        "",
        "It is not robust PDF extraction evidence.",
        "",
        "## Gate Result",
        "",
        f"review_status -> {summary['review_status']}",
        f"quality_gap_status -> {summary['quality_gap_status']}",
        f"previous_gate -> {summary['previous_gate']}",
        f"reviewed_gap_count -> {summary['reviewed_gap_count']}",
        f"quality_claim_ready_cell_count -> {summary['quality_claim_ready_cell_count']}",
        f"quality_blocked_cell_count -> {summary['quality_blocked_cell_count']}",
        f"self_completable_without_new_download_count -> {summary['self_completable_without_new_download_count']}",
        f"selected_next_gap -> {summary['selected_next_gap']}",
        f"selected_next_gate -> {summary['selected_next_gate']}",
        f"runtime_work_performed -> {_format_bool(summary['runtime_work_performed'])}",
        f"pdf_downloads_performed -> {_format_bool(summary['pdf_downloads_performed'])}",
        f"parser_calls_performed -> {_format_bool(summary['parser_calls_performed'])}",
        f"ocr_calls_performed -> {_format_bool(summary['ocr_calls_performed'])}",
        f"table_extraction_calls_performed -> {_format_bool(summary['table_extraction_calls_performed'])}",
        f"llm_calls_performed -> {_format_bool(summary['llm_calls_performed'])}",
        f"binary_files_committed -> {_format_bool(summary['binary_files_committed'])}",
        f"download_cache_committed -> {_format_bool(summary['download_cache_committed'])}",
        f"raw_text_committed -> {_format_bool(summary['raw_text_committed'])}",
        f"can_claim_source_policy_pdf_quality_gap_review -> {_format_bool(summary['can_claim_source_policy_pdf_quality_gap_review'])}",
        f"can_claim_robust_pdf_extraction -> {_format_bool(summary['can_claim_robust_pdf_extraction'])}",
        f"can_claim_ocr_quality -> {_format_bool(summary['can_claim_ocr_quality'])}",
        f"can_claim_external_validation -> {_format_bool(summary['can_claim_external_validation'])}",
        "",
        "## Decision Rules",
        "",
    ]
    for rule in summary["decision_rules"]:
        lines.append(f"- {rule}")

    lines.extend(
        [
            "",
            "## Reviewed Gaps",
            "",
            "| Gap | Status | External dependency | Requires new download | Requires OCR | Selected | Recommended gate | Decision reason |",
            "|---|---|---|---|---|---|---|---|",
        ]
    )
    for gap in summary["reviewed_gaps"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    gap["target_missing_cell"],
                    gap["cell_status"],
                    gap["external_dependency"],
                    _format_bool(gap["requires_new_download"]),
                    _format_bool(gap["requires_ocr"]),
                    _format_bool(gap["selected_for_next_gate"]),
                    gap["recommended_gate"],
                    gap["decision_reason"],
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
            "This is a deterministic review over the source-policy PDF parse quality matrix.",
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


def _validate_review(payload: dict[str, Any]) -> None:
    _validate_forbidden_fields(payload)
    expected_values = {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "source_quality_matrix_manifest": "examples/pdf-extraction-quality/source-policy-pdf-parse-quality-matrix.json",
        "review_status": "passed",
        "quality_gap_status": "open",
        "selected_next_gate": NEXT_GATE,
        "owner_approved": True,
        "can_claim_source_policy_pdf_quality_gap_review": True,
        "can_claim_robust_pdf_extraction": False,
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
                f"source-policy PDF quality gap review {field} must be {expected!r}"
            )

    rules = payload.get("decision_rules")
    if not isinstance(rules, list) or len(rules) != 5:
        raise ValueError("source-policy PDF quality gap review must include 5 rules")

    reviewed_gaps = payload.get("reviewed_gaps")
    if not isinstance(reviewed_gaps, list) or len(reviewed_gaps) != 6:
        raise ValueError("source-policy PDF quality gap review must include 6 gaps")
    seen_gaps: set[str] = set()
    selected_count = 0
    for gap in reviewed_gaps:
        selected = _validate_gap(gap, seen_gaps)
        if selected:
            selected_count += 1
    if seen_gaps != _REQUIRED_GAPS:
        raise ValueError("source-policy PDF quality gap review gaps are incomplete")
    if selected_count != 1:
        raise ValueError("source-policy PDF quality gap review must select one gate")

    for field in ["blocked_reasons", "minimum_next_evidence", "warnings", "boundary_notes"]:
        value = payload.get(field)
        if not isinstance(value, list) or not value:
            raise ValueError(f"source-policy PDF quality gap review {field} must be non-empty")

    for note in [
        "source-policy PDF quality gap review only",
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
                f"source-policy PDF quality gap review missing boundary note: {note}"
            )


def _validate_gap(gap: dict[str, Any], seen_gaps: set[str]) -> bool:
    if not isinstance(gap, dict):
        raise ValueError("reviewed gaps must be objects")
    target = str(gap.get("target_missing_cell") or "")
    if target not in _REQUIRED_GAPS:
        raise ValueError("reviewed gap has unsupported target_missing_cell")
    if target in seen_gaps:
        raise ValueError(f"duplicate reviewed gap: {target}")
    seen_gaps.add(target)
    for field in [
        "cell_id",
        "cell_status",
        "current_evidence",
        "missing_quality_evidence",
        "external_dependency",
        "recommended_gate",
        "decision_reason",
        "boundary",
    ]:
        if not gap.get(field):
            raise ValueError(f"reviewed gap {target} missing {field}")
    for field in [
        "requires_new_download",
        "requires_ocr",
        "quality_claim_ready",
        "self_completable_without_new_download",
        "selected_for_next_gate",
    ]:
        if not isinstance(gap.get(field), bool):
            raise ValueError(f"reviewed gap {target} {field} must be boolean")
    if gap["quality_claim_ready"] is not False:
        raise ValueError(f"reviewed gap {target} must keep quality_claim_ready false")
    if "not robust PDF extraction evidence" not in gap["boundary"]:
        raise ValueError(f"reviewed gap {target} boundary must block robust PDF claim")
    if gap["selected_for_next_gate"] is True:
        if target != "multi_publisher_no_extractable_text_failure":
            raise ValueError("selected next gate must be no-native-text failure")
        if gap["recommended_gate"] != NEXT_GATE:
            raise ValueError("selected reviewed gap must recommend the next gate")
        if gap["requires_new_download"] is not False or gap["requires_ocr"] is not False:
            raise ValueError("selected reviewed gap must not require download or OCR")
        if gap["external_dependency"] != "none":
            raise ValueError("selected reviewed gap must not require external dependency")
    return bool(gap["selected_for_next_gate"])


def _validate_forbidden_fields(value: Any) -> None:
    if isinstance(value, dict):
        for key, nested in value.items():
            if key in _FORBIDDEN_FIELDS:
                raise ValueError(
                    f"source-policy PDF quality gap review must not commit {key}"
                )
            _validate_forbidden_fields(nested)
    elif isinstance(value, list):
        for item in value:
            _validate_forbidden_fields(item)


def _format_bool(value: bool) -> str:
    return "true" if value else "false"
