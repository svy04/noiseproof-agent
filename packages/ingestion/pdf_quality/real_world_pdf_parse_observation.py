from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PHASE_MARKER = "real_world_pdf_parse_observation_without_robust_claim_v0"
CLAIM_BOUNDARY = (
    "single_real_world_pdf_parse_observation_not_robust_pdf_extraction"
)
NEXT_GATE = "multi_real_world_pdf_parse_observation_matrix_v0"


def load_real_world_pdf_parse_observation(path: Path | str) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    _validate_observation(payload)
    return payload


def build_real_world_pdf_parse_observation_summary(
    observation: dict[str, Any],
) -> dict[str, Any]:
    _validate_observation(observation)
    return {
        "phase_marker": PHASE_MARKER,
        "claim_boundary": CLAIM_BOUNDARY,
        "source_download_hash_gate": observation["source_download_hash_gate"],
        "observed_fixture_count": 1,
        "parsed_fixture_count": 1 if observation["parse_status"] == "parsed_digital_text" else 0,
        "fixture_id": observation["fixture_id"],
        "publisher": observation["publisher"],
        "parser": observation["parser"],
        "page_count": observation["page_count"],
        "extracted_page_count": observation["extracted_page_count"],
        "empty_page_count": observation["empty_page_count"],
        "text_char_count": observation["text_char_count"],
        "text_block_count": observation["text_block_count"],
        "image_block_count": observation["image_block_count"],
        "table_candidate_count": observation["table_candidate_count"],
        "table_extraction_performed": False,
        "ocr_calls_attempted": False,
        "binary_files_committed": False,
        "download_cache_committed": False,
        "can_claim_real_world_pdf_parse_observation": True,
        "can_claim_robust_pdf_extraction": False,
        "warnings": observation["warnings"],
        "boundary_notes": observation["boundary_notes"],
        "recommended_next_gate": NEXT_GATE,
    }


def build_real_world_pdf_parse_observation_report(summary: dict[str, Any]) -> str:
    lines = [
        "# Real-world PDF Parse Observation",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report records one owner-runtime PyMuPDF digital-text parse observation for a real-world BEA PDF.",
        "",
        "It is not robust PDF extraction evidence.",
        "",
        "## Aggregate",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| observed_fixture_count | {summary['observed_fixture_count']} |",
        f"| parsed_fixture_count | {summary['parsed_fixture_count']} |",
        f"| page_count | {summary['page_count']} |",
        f"| extracted_page_count | {summary['extracted_page_count']} |",
        f"| empty_page_count | {summary['empty_page_count']} |",
        f"| text_char_count | {summary['text_char_count']} |",
        f"| text_block_count | {summary['text_block_count']} |",
        f"| image_block_count | {summary['image_block_count']} |",
        f"| table_candidate_count | {summary['table_candidate_count']} |",
        f"| table_extraction_performed | {_format_bool(summary['table_extraction_performed'])} |",
        f"| ocr_calls_attempted | {_format_bool(summary['ocr_calls_attempted'])} |",
        f"| binary_files_committed | {_format_bool(summary['binary_files_committed'])} |",
        f"| download_cache_committed | {_format_bool(summary['download_cache_committed'])} |",
        f"| can_claim_real_world_pdf_parse_observation | {_format_bool(summary['can_claim_real_world_pdf_parse_observation'])} |",
        f"| can_claim_robust_pdf_extraction | {_format_bool(summary['can_claim_robust_pdf_extraction'])} |",
        "",
        "## Fixture",
        "",
        f"- fixture_id: `{summary['fixture_id']}`",
        f"- publisher: {summary['publisher']}",
        f"- parser: `{summary['parser']}`",
        f"- source download/hash gate: `{summary['source_download_hash_gate']}`",
        "",
        "## Warnings",
        "",
    ]
    for warning in summary["warnings"]:
        lines.append(f"- {warning}")

    lines.extend(["", "## Next Gate", ""])
    lines.append(f"- {summary['recommended_next_gate']}")

    lines.extend(["", "## Boundary Notes", ""])
    for note in summary["boundary_notes"]:
        lines.append(f"- {note}")

    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "This is a single real-world PDF parse observation only.",
            "",
            "It records PyMuPDF digital-text parser metadata for one BEA PDF.",
            "",
            "It does not prove table extraction, OCR, layout fidelity, arbitrary market PDF reliability, or robust PDF extraction.",
            "",
            "This is not hosted deployment evidence.",
            "",
            "This is not product-complete.",
        ]
    )
    return "\n".join(lines) + "\n"


def _validate_observation(payload: dict[str, Any]) -> None:
    expected_values = {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "claim_boundary": CLAIM_BOUNDARY,
        "source_download_hash_gate": "owner_approved_real_world_pdf_download_and_hash_v0",
        "parser": "pdf-pymupdf",
        "parse_status": "parsed_digital_text",
        "table_extraction_performed": False,
        "ocr_calls_attempted": False,
        "robust_pdf_extraction_claimed": False,
        "can_claim_robust_pdf_extraction": False,
        "binary_files_committed": False,
        "download_cache_committed": False,
        "recommended_next_gate": NEXT_GATE,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(f"real-world parse observation {field} must be {expected!r}")

    for field in [
        "page_count",
        "extracted_page_count",
        "text_char_count",
        "text_block_count",
        "table_candidate_count",
    ]:
        value = payload.get(field)
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"real-world parse observation {field} must be positive")

    if payload.get("failure_case_candidate") is not None:
        raise ValueError("successful parse observation must not include failure candidate")
    if not payload.get("warnings"):
        raise ValueError("real-world parse observation must include warnings")
    if not payload.get("text_sample"):
        raise ValueError("real-world parse observation must include a text sample")

    boundary_notes = payload.get("boundary_notes", [])
    for note in [
        "single real-world PDF parse observation only",
        "not robust PDF extraction evidence",
        "not table extraction evidence",
    ]:
        if note not in boundary_notes:
            raise ValueError(f"real-world parse observation missing boundary note: {note}")


def _format_bool(value: bool) -> str:
    return "true" if value else "false"
