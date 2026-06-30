from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PHASE_MARKER = "robust_pdf_extraction_generalization_gap_review_v0"
PREVIOUS_GATE = "real_world_layout_fidelity_evidence_gate_v0"
CLAIM_BOUNDARY = "generalization_gap_review_blocks_robust_pdf_extraction_claim"
NEXT_GATE = "multi_publisher_modality_stratified_pdf_eval_v0"

_COVERED_STATUS = "covered_limited"
_MISSING_STATUS = "missing"

_REQUIRED_COVERED_CAPABILITIES = {
    "digital_text_parse_observation",
    "cross_publisher_fixture_coverage",
    "table_extraction_observation",
    "ocr_observation",
    "layout_metadata_sanity_observation",
}

_REQUIRED_MISSING_CAPABILITIES = {
    "labeled_layout_ground_truth",
    "natural_reading_order_benchmark",
    "rendered_visual_fidelity_comparison",
    "image_chart_interpretation_evidence",
    "arbitrary_market_pdf_coverage",
    "external_reviewer_validation",
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
    "local_pdf_path",
}


def load_robust_pdf_generalization_gap_review(path: Path | str) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    _validate_review(payload)
    return payload


def build_robust_pdf_generalization_gap_review_summary(
    review: dict[str, Any],
) -> dict[str, Any]:
    _validate_review(review)

    capability_reviews = list(review["capability_reviews"])
    covered_capabilities = [
        item["capability"]
        for item in capability_reviews
        if item["status"] == _COVERED_STATUS
    ]
    missing_capabilities = [
        item["capability"]
        for item in capability_reviews
        if item["status"] == _MISSING_STATUS
    ]
    evidence_chain = list(review["evidence_chain"])
    max_fixture_count = max(item["fixture_count"] for item in evidence_chain)
    max_publisher_count = max(item["publisher_count"] for item in evidence_chain)

    passed_checks = [
        "evidence_chain_reviewed",
        "capability_matrix_reviewed",
        "robust_claim_blocked",
        "runtime_work_not_performed",
        "external_binaries_not_committed",
        "raw_text_not_committed",
    ]

    return {
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "review_status": review["review_status"],
        "generalization_gap_status": review["generalization_gap_status"],
        "evidence_chain_count": len(evidence_chain),
        "covered_capability_count": len(covered_capabilities),
        "missing_capability_count": len(missing_capabilities),
        "covered_capabilities": covered_capabilities,
        "missing_capabilities": missing_capabilities,
        "source_patterns": review["source_patterns"],
        "max_fixture_count": max_fixture_count,
        "max_publisher_count": max_publisher_count,
        "can_claim_robust_pdf_extraction": False,
        "blocked_reasons": review["blocked_reasons"],
        "minimum_next_evidence": review["minimum_next_evidence"],
        "passed_checks": passed_checks,
        "evidence_chain": evidence_chain,
        "capability_reviews": capability_reviews,
        "warnings": review["warnings"],
        "boundary_notes": review["boundary_notes"],
        "next_gate": NEXT_GATE,
    }


def build_robust_pdf_generalization_gap_review_report(
    summary: dict[str, Any],
) -> str:
    lines = [
        "# Robust PDF Extraction Generalization Gap Review",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report reviews the current real-world PDF evidence chain before any robust PDF extraction wording is allowed.",
        "",
        "It is a generalization gap review, not robust PDF extraction evidence.",
        "",
        "It does not add new runtime evidence.",
        "",
        "## Gate Result",
        "",
        f"review_status -> {summary['review_status']}",
        f"generalization_gap_status -> {summary['generalization_gap_status']}",
        f"previous_gate -> {summary['previous_gate']}",
        f"evidence_chain_count -> {summary['evidence_chain_count']}",
        f"covered_capability_count -> {summary['covered_capability_count']}",
        f"missing_capability_count -> {summary['missing_capability_count']}",
        f"max_fixture_count -> {summary['max_fixture_count']}",
        f"max_publisher_count -> {summary['max_publisher_count']}",
        f"can_claim_robust_pdf_extraction -> {_format_bool(summary['can_claim_robust_pdf_extraction'])}",
        "",
        "## Source Patterns",
        "",
    ]
    for source_pattern in summary["source_patterns"]:
        lines.append(f"- {source_pattern}")

    lines.extend(["", "## Evidence Chain Reviewed", ""])
    lines.extend(
        [
            "| Gate | Fixtures | Publishers | Capabilities | Boundary |",
            "|---|---:|---:|---|---|",
        ]
    )
    for item in summary["evidence_chain"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    item["gate"],
                    str(item["fixture_count"]),
                    str(item["publisher_count"]),
                    ", ".join(item["capabilities"]),
                    item["boundary"],
                ]
            )
            + " |"
        )

    lines.extend(["", "## Capability Review", ""])
    lines.extend(
        [
            "| Capability | Status | Current evidence | Required next evidence |",
            "|---|---|---|---|",
        ]
    )
    for item in summary["capability_reviews"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    item["capability"],
                    item["status"],
                    item["current_evidence"],
                    item["required_next_evidence"],
                ]
            )
            + " |"
        )

    lines.extend(["", "## Missing Capabilities", ""])
    for capability in summary["missing_capabilities"]:
        lines.append(f"- {capability}")

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
            "This is a deterministic review over existing sanitized PDF proof packets.",
            "",
            "It does not download PDFs, parse PDFs, run OCR, extract tables, call LLMs, commit external binaries, commit raw extracted text, or add new runtime evidence.",
            "",
            "It does not prove robust PDF extraction, arbitrary-market PDF parsing reliability, natural reading order correctness, rendered visual fidelity, image/chart interpretation, or benchmark performance.",
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
        "review_status": "passed",
        "generalization_gap_status": "open",
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
            raise ValueError(
                f"robust PDF generalization gap review {field} must be {expected!r}"
            )

    source_patterns = payload.get("source_patterns")
    if not isinstance(source_patterns, list) or len(source_patterns) < 5:
        raise ValueError("review must include at least five source patterns")

    evidence_chain = payload.get("evidence_chain")
    if not isinstance(evidence_chain, list) or len(evidence_chain) != 5:
        raise ValueError("review must include exactly five evidence chain entries")
    for item in evidence_chain:
        _validate_evidence_chain_entry(item)

    capability_reviews = payload.get("capability_reviews")
    if not isinstance(capability_reviews, list):
        raise ValueError("review must include capability reviews")
    capabilities = {str(item.get("capability") or "") for item in capability_reviews}
    if not _REQUIRED_COVERED_CAPABILITIES.issubset(capabilities):
        raise ValueError("review missing required covered capability")
    if not _REQUIRED_MISSING_CAPABILITIES.issubset(capabilities):
        raise ValueError("review missing required missing capability")
    for item in capability_reviews:
        _validate_capability_review(item)

    blocked_reasons = payload.get("blocked_reasons")
    if not isinstance(blocked_reasons, list):
        raise ValueError("review blocked_reasons must be a list")
    for capability in _REQUIRED_MISSING_CAPABILITIES:
        reason = f"{capability}_missing"
        if reason not in blocked_reasons:
            raise ValueError(f"review missing blocked reason: {reason}")

    for field in ["minimum_next_evidence", "warnings", "boundary_notes"]:
        value = payload.get(field)
        if not isinstance(value, list) or not value:
            raise ValueError(f"review {field} must be a non-empty list")

    for note in [
        "generalization gap review only",
        "does not add new runtime evidence",
        "not robust PDF extraction evidence",
        "not arbitrary-market PDF parsing evidence",
        "not natural reading order correctness evidence",
        "not rendered visual fidelity evidence",
        "not hosted deployment evidence",
        "not external reviewer feedback",
        "not product-complete",
    ]:
        if note not in payload["boundary_notes"]:
            raise ValueError(f"review missing boundary note: {note}")


def _validate_evidence_chain_entry(item: dict[str, Any]) -> None:
    if not isinstance(item, dict):
        raise ValueError("evidence chain entries must be objects")
    for field in ["gate", "route", "boundary"]:
        if not item.get(field):
            raise ValueError(f"evidence chain entry missing {field}")
    for field in ["fixture_count", "publisher_count"]:
        value = item.get(field)
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"evidence chain entry {field} must be positive")
    capabilities = item.get("capabilities")
    if not isinstance(capabilities, list) or not capabilities:
        raise ValueError("evidence chain entry capabilities must be non-empty")
    if item.get("can_claim_robust_pdf_extraction") is not False:
        raise ValueError("evidence chain entries must keep robust claim false")


def _validate_capability_review(item: dict[str, Any]) -> None:
    if not isinstance(item, dict):
        raise ValueError("capability reviews must be objects")
    capability = str(item.get("capability") or "")
    if not capability:
        raise ValueError("capability review missing capability")
    status = item.get("status")
    if capability in _REQUIRED_COVERED_CAPABILITIES and status != _COVERED_STATUS:
        raise ValueError(f"{capability} must be covered_limited")
    if capability in _REQUIRED_MISSING_CAPABILITIES and status != _MISSING_STATUS:
        raise ValueError(f"{capability} must be missing")
    if not item.get("current_evidence") or not item.get("required_next_evidence"):
        raise ValueError(f"{capability} must include evidence and next evidence")


def _validate_forbidden_fields(value: Any) -> None:
    if isinstance(value, dict):
        for key, nested in value.items():
            if key in _FORBIDDEN_FIELDS:
                raise ValueError(f"review must not commit {key}")
            _validate_forbidden_fields(nested)
    elif isinstance(value, list):
        for item in value:
            _validate_forbidden_fields(item)


def _format_bool(value: bool) -> str:
    return "true" if value else "false"
