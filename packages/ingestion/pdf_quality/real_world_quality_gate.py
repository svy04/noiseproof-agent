from __future__ import annotations

from typing import Any


PHASE_MARKER = "robust_pdf_extraction_next_real_world_quality_gate_v0"
INPUT_MATRIX_PHASE = "multi_real_world_pdf_parse_observation_matrix_v0"
CLAIM_BOUNDARY = "real_world_quality_gate_blocks_robust_pdf_extraction_claim"
NEXT_GATE = "cross_publisher_real_world_pdf_fixture_gate_v0"


def build_real_world_quality_gate_summary(matrix: dict[str, Any]) -> dict[str, Any]:
    observations = list(matrix.get("observations") or [])
    if matrix.get("phase_marker") != INPUT_MATRIX_PHASE:
        raise ValueError("quality gate input must be multi real-world PDF matrix v0")
    if not observations:
        raise ValueError("quality gate requires at least one observation")

    observed_count = len(observations)
    parsed_count = sum(
        1 for item in observations if item.get("parse_status") == "parsed_digital_text"
    )
    publishers = sorted({str(item.get("publisher") or "") for item in observations})
    publishers = [publisher for publisher in publishers if publisher]

    has_table_extraction = bool(matrix.get("table_extraction_performed")) or any(
        bool(item.get("table_extraction_performed")) for item in observations
    )
    has_ocr = bool(matrix.get("ocr_calls_attempted")) or any(
        bool(item.get("ocr_calls_attempted")) for item in observations
    )
    has_layout_fidelity = any(
        bool(item.get("layout_fidelity_evidence")) for item in observations
    )
    has_cross_publisher = len(publishers) >= 2

    passed_checks = []
    if all(item.get("license_source_url") for item in observations):
        passed_checks.append("source_policy_visible")
    if all(len(str(item.get("source_sha256") or "")) == 64 for item in observations):
        passed_checks.append("sha256_visible")
    if parsed_count == observed_count:
        passed_checks.append("digital_text_observed_for_all_fixtures")
    if matrix.get("binary_files_committed") is False:
        passed_checks.append("external_binaries_not_committed")
    if matrix.get("raw_extracted_text_committed") is False:
        passed_checks.append("raw_extracted_text_not_committed")
    if all(item.get("warnings") for item in observations):
        passed_checks.append("warnings_visible")

    blocked_reasons = []
    if not has_cross_publisher:
        blocked_reasons.append("cross_publisher_coverage_missing")
    if not has_table_extraction:
        blocked_reasons.append("table_extraction_evidence_missing")
    if not has_ocr:
        blocked_reasons.append("ocr_evidence_missing")
    if not has_layout_fidelity:
        blocked_reasons.append("layout_fidelity_evidence_missing")

    can_claim_robust = not blocked_reasons
    return {
        "phase_marker": PHASE_MARKER,
        "input_matrix_phase": INPUT_MATRIX_PHASE,
        "claim_boundary": CLAIM_BOUNDARY,
        "quality_gate_status": "passed" if can_claim_robust else "blocked",
        "observed_fixture_count": observed_count,
        "parsed_fixture_count": parsed_count,
        "distinct_publisher_count": len(publishers),
        "publishers": publishers,
        "digital_text_coverage_ratio": parsed_count / observed_count,
        "has_cross_publisher_coverage": has_cross_publisher,
        "has_table_extraction_evidence": has_table_extraction,
        "has_ocr_evidence": has_ocr,
        "has_layout_fidelity_evidence": has_layout_fidelity,
        "can_claim_robust_pdf_extraction": can_claim_robust,
        "blocked_reasons": blocked_reasons,
        "passed_checks": passed_checks,
        "next_gate": NEXT_GATE,
        "boundary_notes": [
            "not robust PDF extraction evidence",
            "not arbitrary-market PDF parsing evidence",
            "not OCR evidence",
            "not table extraction evidence",
            "not layout fidelity evidence",
            "not hosted deployment evidence",
            "not external reviewer feedback",
            "not product-complete",
        ],
    }


def build_real_world_quality_gate_report(summary: dict[str, Any]) -> str:
    lines = [
        "# Robust PDF Real-world Quality Gate",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report scores the existing multi real-world PDF parse observation matrix against the next robust-PDF quality gate.",
        "",
        "It is not robust PDF extraction evidence.",
        "",
        "## Gate Result",
        "",
        f"quality_gate_status -> {summary['quality_gate_status']}",
        f"input_matrix_phase -> {summary['input_matrix_phase']}",
        f"observed_fixture_count -> {summary['observed_fixture_count']}",
        f"parsed_fixture_count -> {summary['parsed_fixture_count']}",
        f"distinct_publisher_count -> {summary['distinct_publisher_count']}",
        f"digital_text_coverage_ratio -> {summary['digital_text_coverage_ratio']:.4f}",
        f"has_cross_publisher_coverage -> {_format_bool(summary['has_cross_publisher_coverage'])}",
        f"has_table_extraction_evidence -> {_format_bool(summary['has_table_extraction_evidence'])}",
        f"has_ocr_evidence -> {_format_bool(summary['has_ocr_evidence'])}",
        f"has_layout_fidelity_evidence -> {_format_bool(summary['has_layout_fidelity_evidence'])}",
        f"can_claim_robust_pdf_extraction -> {_format_bool(summary['can_claim_robust_pdf_extraction'])}",
        "",
        "## Publishers",
        "",
    ]
    for publisher in summary["publishers"]:
        lines.append(f"- {publisher}")

    lines.extend(["", "## Passed Checks", ""])
    for check in summary["passed_checks"]:
        lines.append(f"- {check}")

    lines.extend(["", "## Blocked Reasons", ""])
    for reason in summary["blocked_reasons"]:
        lines.append(f"- {reason}")

    lines.extend(
        [
            "",
            "## Next Gate",
            "",
            f"- {summary['next_gate']}",
            "",
            "## Boundary Notes",
            "",
        ]
    )
    for note in summary["boundary_notes"]:
        lines.append(f"- {note}")

    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "This is a deterministic quality gate over existing sanitized real-world PDF observations.",
            "",
            "It does not download new PDFs, commit external binaries, commit raw extracted text, run OCR, extract tables, or prove layout fidelity.",
            "",
            "It does not prove robust PDF extraction or arbitrary-market PDF parsing reliability.",
            "",
            "This is not hosted deployment evidence.",
            "",
            "This is not external reviewer feedback.",
            "",
            "This is not product-complete.",
        ]
    )
    return "\n".join(lines) + "\n"


def _format_bool(value: bool) -> str:
    return "true" if value else "false"
