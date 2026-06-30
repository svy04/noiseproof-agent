from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PHASE_MARKER = "cross_publisher_real_world_pdf_fixture_gate_v0"
BASE_MATRIX_PHASE = "multi_real_world_pdf_parse_observation_matrix_v0"
CLAIM_BOUNDARY = "cross_publisher_real_world_pdf_fixture_coverage_not_robust_pdf_extraction"
NEXT_GATE = "real_world_table_extraction_evidence_gate_v0"


def load_cross_publisher_observation(path: Path | str) -> dict[str, Any]:
    observation = json.loads(Path(path).read_text(encoding="utf-8"))
    if observation.get("phase_marker") != PHASE_MARKER:
        raise ValueError("cross-publisher observation must use gate v0 phase marker")
    if observation.get("binary_committed") is not False:
        raise ValueError("cross-publisher observation must not commit external PDFs")
    if observation.get("raw_extracted_text_committed") is not False:
        raise ValueError("cross-publisher observation must not commit raw extracted text")
    return observation


def build_cross_publisher_fixture_gate_summary(
    base_matrix: dict[str, Any], observation: dict[str, Any]
) -> dict[str, Any]:
    if base_matrix.get("phase_marker") != BASE_MATRIX_PHASE:
        raise ValueError("base matrix must be multi real-world PDF matrix v0")
    base_observations = list(base_matrix.get("observations") or [])
    if not base_observations:
        raise ValueError("base matrix requires at least one observation")
    if observation.get("parse_status") != "parsed_digital_text":
        raise ValueError("cross-publisher observation must be parsed digital text")

    all_observations = [*base_observations, observation]
    publishers = sorted({str(item.get("publisher") or "") for item in all_observations})
    publishers = [publisher for publisher in publishers if publisher]
    has_cross_publisher = len(publishers) >= 2

    has_table_extraction = bool(base_matrix.get("table_extraction_performed")) or any(
        bool(item.get("table_extraction_performed")) for item in all_observations
    )
    has_ocr = bool(base_matrix.get("ocr_calls_attempted")) or any(
        bool(item.get("ocr_calls_attempted")) for item in all_observations
    )
    has_layout_fidelity = any(
        bool(item.get("layout_fidelity_evidence")) for item in all_observations
    )

    passed_checks = []
    if has_cross_publisher:
        passed_checks.append("cross_publisher_coverage_visible")
    if all(item.get("license_source_url") for item in all_observations):
        passed_checks.append("source_policy_visible")
    if all(len(str(item.get("source_sha256") or "")) == 64 for item in all_observations):
        passed_checks.append("sha256_visible")
    if observation.get("binary_committed") is False:
        passed_checks.append("external_binary_not_committed_for_added_fixture")
    if observation.get("download_cache_committed") is False:
        passed_checks.append("download_cache_not_committed_for_added_fixture")
    if observation.get("raw_extracted_text_committed") is False:
        passed_checks.append("raw_extracted_text_not_committed_for_added_fixture")

    blocked_reasons = []
    if not has_cross_publisher:
        blocked_reasons.append("cross_publisher_coverage_missing")
    if not has_table_extraction:
        blocked_reasons.append("table_extraction_evidence_missing")
    if not has_ocr:
        blocked_reasons.append("ocr_evidence_missing")
    if not has_layout_fidelity:
        blocked_reasons.append("layout_fidelity_evidence_missing")

    return {
        "phase_marker": PHASE_MARKER,
        "base_matrix_phase": BASE_MATRIX_PHASE,
        "claim_boundary": CLAIM_BOUNDARY,
        "cross_publisher_gate_status": "passed" if has_cross_publisher else "blocked",
        "base_observed_fixture_count": len(base_observations),
        "added_observed_fixture_count": 1,
        "combined_observed_fixture_count": len(all_observations),
        "distinct_publisher_count": len(publishers),
        "publishers": publishers,
        "added_fixture_id": observation["fixture_id"],
        "added_fixture_title": observation["title"],
        "added_fixture_publisher": observation["publisher"],
        "added_fixture_source_url": observation["source_url"],
        "added_fixture_license_source_url": observation["license_source_url"],
        "added_fixture_page_count": observation["page_count"],
        "added_fixture_text_char_count": observation["text_char_count"],
        "added_fixture_table_candidate_count": observation["table_candidate_count"],
        "has_cross_publisher_coverage": has_cross_publisher,
        "has_table_extraction_evidence": has_table_extraction,
        "has_ocr_evidence": has_ocr,
        "has_layout_fidelity_evidence": has_layout_fidelity,
        "can_claim_cross_publisher_real_world_pdf_fixture_coverage": has_cross_publisher,
        "can_claim_robust_pdf_extraction": False,
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


def build_cross_publisher_fixture_gate_report(summary: dict[str, Any]) -> str:
    lines = [
        "# Cross-publisher Real-world PDF Fixture Gate",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report adds one EIA Short-Term Energy Outlook owner-runtime observation to the existing BEA real-world PDF matrix.",
        "",
        "It is cross-publisher fixture coverage, not robust PDF extraction evidence.",
        "",
        "## Gate Result",
        "",
        f"cross_publisher_gate_status -> {summary['cross_publisher_gate_status']}",
        f"base_matrix_phase -> {summary['base_matrix_phase']}",
        f"base_observed_fixture_count -> {summary['base_observed_fixture_count']}",
        f"added_observed_fixture_count -> {summary['added_observed_fixture_count']}",
        f"combined_observed_fixture_count -> {summary['combined_observed_fixture_count']}",
        f"distinct_publisher_count -> {summary['distinct_publisher_count']}",
        f"has_cross_publisher_coverage -> {_format_bool(summary['has_cross_publisher_coverage'])}",
        f"has_table_extraction_evidence -> {_format_bool(summary['has_table_extraction_evidence'])}",
        f"has_ocr_evidence -> {_format_bool(summary['has_ocr_evidence'])}",
        f"has_layout_fidelity_evidence -> {_format_bool(summary['has_layout_fidelity_evidence'])}",
        f"can_claim_cross_publisher_real_world_pdf_fixture_coverage -> {_format_bool(summary['can_claim_cross_publisher_real_world_pdf_fixture_coverage'])}",
        f"can_claim_robust_pdf_extraction -> {_format_bool(summary['can_claim_robust_pdf_extraction'])}",
        "",
        "## Added Fixture",
        "",
        f"- fixture_id: {summary['added_fixture_id']}",
        f"- title: {summary['added_fixture_title']}",
        f"- publisher: {summary['added_fixture_publisher']}",
        f"- source_url: {summary['added_fixture_source_url']}",
        f"- license_source_url: {summary['added_fixture_license_source_url']}",
        f"- page_count: {summary['added_fixture_page_count']}",
        f"- text_char_count: {summary['added_fixture_text_char_count']}",
        f"- table_candidate_count: {summary['added_fixture_table_candidate_count']}",
        "",
        "## Publishers",
        "",
    ]
    for publisher in summary["publishers"]:
        lines.append(f"- {publisher}")

    lines.extend(["", "## Passed Checks", ""])
    for check in summary["passed_checks"]:
        lines.append(f"- {check}")

    lines.extend(["", "## Remaining Blocked Reasons", ""])
    for reason in summary["blocked_reasons"]:
        lines.append(f"- {reason}")

    lines.extend(["", "## Next Gate", "", f"- {summary['next_gate']}", ""])
    lines.extend(["## Boundary Notes", ""])
    for note in summary["boundary_notes"]:
        lines.append(f"- {note}")

    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "This is a deterministic report over sanitized owner-runtime observations.",
            "",
            "It does not commit external PDF binaries, download caches, or raw extracted text.",
            "",
            "It does not run OCR, extract tables, prove layout fidelity, or prove arbitrary-market PDF parsing reliability.",
            "",
            "It does not prove robust PDF extraction.",
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

