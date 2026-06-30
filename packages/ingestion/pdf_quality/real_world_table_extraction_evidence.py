from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PHASE_MARKER = "real_world_table_extraction_evidence_gate_v0"
PREVIOUS_GATE = "cross_publisher_real_world_pdf_fixture_gate_v0"
CLAIM_BOUNDARY = "real_world_table_extraction_evidence_not_robust_pdf_extraction"
TABLE_ENGINE = "pymupdf-find_tables-extract"
NEXT_GATE = "real_world_ocr_evidence_gate_v0"


def load_real_world_table_extraction_evidence(path: Path | str) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    _validate_evidence(payload)
    return payload


def build_real_world_table_extraction_evidence_summary(
    evidence: dict[str, Any],
) -> dict[str, Any]:
    _validate_evidence(evidence)
    observations = list(evidence["observations"])
    publishers = sorted({str(item.get("publisher") or "") for item in observations})
    publishers = [publisher for publisher in publishers if publisher]
    observed_count = len(observations)
    table_observed = [
        item for item in observations if item.get("table_extraction_performed") is True
    ]
    has_cross_publisher = len(publishers) >= 2
    has_table_evidence = len(table_observed) == observed_count
    has_ocr = bool(evidence.get("ocr_calls_attempted"))
    has_layout_fidelity = bool(evidence.get("layout_fidelity_evidence"))

    passed_checks = []
    if has_table_evidence:
        passed_checks.append("real_world_table_extraction_observed")
    if has_cross_publisher:
        passed_checks.append("cross_publisher_coverage_visible")
    if all(item.get("license_source_url") for item in observations):
        passed_checks.append("source_policy_visible")
    if all(len(str(item.get("source_sha256") or "")) == 64 for item in observations):
        passed_checks.append("sha256_visible")
    if evidence.get("binary_files_committed") is False:
        passed_checks.append("external_binaries_not_committed")
    if evidence.get("raw_extracted_text_committed") is False:
        passed_checks.append("raw_extracted_text_not_committed")
    if evidence.get("raw_table_rows_committed") is False:
        passed_checks.append("raw_table_rows_not_committed")

    blocked_reasons = []
    if not has_cross_publisher:
        blocked_reasons.append("cross_publisher_coverage_missing")
    if not has_table_evidence:
        blocked_reasons.append("table_extraction_evidence_missing")
    if not has_ocr:
        blocked_reasons.append("ocr_evidence_missing")
    if not has_layout_fidelity:
        blocked_reasons.append("layout_fidelity_evidence_missing")

    return {
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "table_extraction_gate_status": "passed" if has_table_evidence else "blocked",
        "observed_fixture_count": observed_count,
        "table_extraction_observed_fixture_count": len(table_observed),
        "distinct_publisher_count": len(publishers),
        "publishers": publishers,
        "total_page_count": sum(item["page_count"] for item in observations),
        "total_table_count": sum(item["table_count"] for item in observations),
        "total_table_rows_extracted": sum(
            item["table_rows_extracted"] for item in observations
        ),
        "total_table_cell_count": sum(item["table_cell_count"] for item in observations),
        "has_cross_publisher_coverage": has_cross_publisher,
        "has_table_extraction_evidence": has_table_evidence,
        "has_ocr_evidence": has_ocr,
        "has_layout_fidelity_evidence": has_layout_fidelity,
        "can_claim_real_world_table_extraction_evidence": has_table_evidence,
        "can_claim_robust_pdf_extraction": False,
        "blocked_reasons": blocked_reasons,
        "passed_checks": passed_checks,
        "observations": observations,
        "warnings": evidence["warnings"],
        "boundary_notes": evidence["boundary_notes"],
        "next_gate": NEXT_GATE,
    }


def build_real_world_table_extraction_evidence_report(summary: dict[str, Any]) -> str:
    lines = [
        "# Real-world Table Extraction Evidence Gate",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report records sanitized PyMuPDF table extraction observations for temporary owner-runtime real-world PDF downloads.",
        "",
        "It is real-world table extraction evidence, not robust PDF extraction evidence.",
        "",
        "## Gate Result",
        "",
        f"table_extraction_gate_status -> {summary['table_extraction_gate_status']}",
        f"previous_gate -> {summary['previous_gate']}",
        f"observed_fixture_count -> {summary['observed_fixture_count']}",
        f"table_extraction_observed_fixture_count -> {summary['table_extraction_observed_fixture_count']}",
        f"distinct_publisher_count -> {summary['distinct_publisher_count']}",
        f"total_page_count -> {summary['total_page_count']}",
        f"total_table_count -> {summary['total_table_count']}",
        f"total_table_rows_extracted -> {summary['total_table_rows_extracted']}",
        f"total_table_cell_count -> {summary['total_table_cell_count']}",
        f"has_cross_publisher_coverage -> {_format_bool(summary['has_cross_publisher_coverage'])}",
        f"has_table_extraction_evidence -> {_format_bool(summary['has_table_extraction_evidence'])}",
        f"has_ocr_evidence -> {_format_bool(summary['has_ocr_evidence'])}",
        f"has_layout_fidelity_evidence -> {_format_bool(summary['has_layout_fidelity_evidence'])}",
        f"can_claim_real_world_table_extraction_evidence -> {_format_bool(summary['can_claim_real_world_table_extraction_evidence'])}",
        f"can_claim_robust_pdf_extraction -> {_format_bool(summary['can_claim_robust_pdf_extraction'])}",
        "",
        "## Publishers",
        "",
    ]
    for publisher in summary["publishers"]:
        lines.append(f"- {publisher}")

    lines.extend(
        [
            "",
            "## Fixtures",
            "",
            "| Fixture | Publisher | Pages | Tables | Rows | Cells | SHA-256 |",
            "|---|---|---:|---:|---:|---:|---|",
        ]
    )
    for item in summary["observations"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    item["fixture_id"],
                    item["publisher"],
                    str(item["page_count"]),
                    str(item["table_count"]),
                    str(item["table_rows_extracted"]),
                    str(item["table_cell_count"]),
                    item["source_sha256"],
                ]
            )
            + " |"
        )

    lines.extend(["", "## Passed Checks", ""])
    for check in summary["passed_checks"]:
        lines.append(f"- {check}")

    lines.extend(["", "## Remaining Blocked Reasons", ""])
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
            "This is a deterministic report over sanitized owner-runtime table observations.",
            "",
            "It does not commit external PDF binaries, download caches, raw extracted text, or raw table rows.",
            "",
            "It does not run OCR, prove layout fidelity, prove arbitrary-market PDF parsing reliability, or prove robust PDF extraction.",
            "",
            "This is not hosted deployment evidence.",
            "",
            "This is not external reviewer feedback.",
            "",
            "This is not product-complete.",
        ]
    )
    return "\n".join(lines) + "\n"


def _validate_evidence(payload: dict[str, Any]) -> None:
    expected_values = {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "table_extraction_engine": TABLE_ENGINE,
        "table_extraction_performed": True,
        "ocr_calls_attempted": False,
        "layout_fidelity_evidence": False,
        "robust_pdf_extraction_claimed": False,
        "can_claim_robust_pdf_extraction": False,
        "binary_files_committed": False,
        "download_cache_committed": False,
        "raw_extracted_text_committed": False,
        "raw_table_rows_committed": False,
        "recommended_next_gate": NEXT_GATE,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(
                f"real-world table extraction evidence {field} must be {expected!r}"
            )

    observations = payload.get("observations")
    if not isinstance(observations, list) or len(observations) != 3:
        raise ValueError("real-world table extraction evidence must include 3 observations")

    seen_ids: set[str] = set()
    for item in observations:
        _validate_observation(item, seen_ids)

    for field in ["warnings", "boundary_notes"]:
        value = payload.get(field)
        if not isinstance(value, list) or not value:
            raise ValueError(
                f"real-world table extraction evidence {field} must be a non-empty list"
            )

    for note in [
        "real-world table extraction evidence",
        "no external PDF binaries committed",
        "no raw table rows committed",
        "not robust PDF extraction evidence",
        "not OCR evidence",
        "not layout fidelity evidence",
    ]:
        if note not in payload["boundary_notes"]:
            raise ValueError(f"real-world table extraction evidence missing note: {note}")


def _validate_observation(item: dict[str, Any], seen_ids: set[str]) -> None:
    if not isinstance(item, dict):
        raise ValueError("table extraction observations must be objects")
    fixture_id = str(item.get("fixture_id") or "")
    if not fixture_id:
        raise ValueError("table extraction observation missing fixture_id")
    if fixture_id in seen_ids:
        raise ValueError(f"duplicate fixture_id: {fixture_id}")
    seen_ids.add(fixture_id)

    expected_values = {
        "source_sha256_algorithm": "sha256",
        "pdf_magic_header": True,
        "parser": "pdf-pymupdf",
        "table_extraction_engine": TABLE_ENGINE,
        "table_extraction_performed": True,
        "failure_case_candidate": None,
        "binary_committed": False,
        "raw_table_rows_committed": False,
    }
    for field, expected in expected_values.items():
        if item.get(field) != expected:
            raise ValueError(f"observation {fixture_id} {field} must be {expected!r}")

    for field in [
        "byte_size",
        "page_count",
        "table_count",
        "table_rows_extracted",
        "table_cell_count",
    ]:
        value = item.get(field)
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"observation {fixture_id} {field} must be positive")

    if len(str(item.get("source_sha256") or "")) != 64:
        raise ValueError(f"observation {fixture_id} must include a SHA-256 digest")
    if not item.get("license_source_url"):
        raise ValueError(f"observation {fixture_id} must include a source policy URL")
    if "extracted_table_rows" in item or "tables" in item:
        raise ValueError(
            f"observation {fixture_id} must not commit raw extracted table rows"
        )

    shapes = item.get("table_shapes_sample")
    if not isinstance(shapes, list) or not shapes:
        raise ValueError(f"observation {fixture_id} must include table shape samples")
    for shape in shapes:
        if not isinstance(shape, dict):
            raise ValueError(f"observation {fixture_id} table shape must be an object")
        for field in ["page_index", "table_index", "row_count", "col_count", "cell_count"]:
            value = shape.get(field)
            if not isinstance(value, int):
                raise ValueError(
                    f"observation {fixture_id} table shape {field} must be an integer"
                )
        if shape["page_index"] < 0 or shape["table_index"] < 0:
            raise ValueError(f"observation {fixture_id} table shape index must be non-negative")
        if shape["row_count"] <= 0 or shape["col_count"] <= 0 or shape["cell_count"] <= 0:
            raise ValueError(f"observation {fixture_id} table shape dimensions must be positive")

    if not item.get("warnings"):
        raise ValueError(f"observation {fixture_id} must include warnings")


def _format_bool(value: bool) -> str:
    return "true" if value else "false"
