from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PHASE_MARKER = "multi_real_world_pdf_parse_observation_matrix_v0"
CLAIM_BOUNDARY = (
    "multi_real_world_pdf_parse_observation_matrix_not_robust_pdf_extraction"
)
NEXT_GATE = "multi_real_world_pdf_parse_observation_matrix_remote_verification_v0"
EXPECTED_FIXTURE_IDS = {
    "bea_nipa_glossary_2019",
    "bea_nipa_chapter_04_2024",
    "bea_open_source_software_innovation_wp_2022_10",
}


def load_multi_real_world_pdf_parse_observation_matrix(
    path: Path | str,
) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    _validate_matrix(payload)
    return payload


def build_multi_real_world_pdf_parse_observation_summary(
    matrix: dict[str, Any],
) -> dict[str, Any]:
    _validate_matrix(matrix)
    observations = list(matrix["observations"])
    parsed = [
        item for item in observations if item["parse_status"] == "parsed_digital_text"
    ]
    return {
        "phase_marker": PHASE_MARKER,
        "claim_boundary": CLAIM_BOUNDARY,
        "source_download_hash_gate": matrix["source_download_hash_gate"],
        "fixture_count": len(observations),
        "observed_fixture_count": len(observations),
        "parsed_fixture_count": len(parsed),
        "fixture_ids": sorted(item["fixture_id"] for item in observations),
        "total_page_count": sum(item["page_count"] for item in observations),
        "total_extracted_page_count": sum(
            item["extracted_page_count"] for item in observations
        ),
        "total_empty_page_count": sum(item["empty_page_count"] for item in observations),
        "total_text_char_count": sum(item["text_char_count"] for item in observations),
        "total_text_block_count": sum(item["text_block_count"] for item in observations),
        "total_image_block_count": sum(
            item["image_block_count"] for item in observations
        ),
        "total_table_candidate_count": sum(
            item["table_candidate_count"] for item in observations
        ),
        "table_extraction_performed": False,
        "ocr_calls_attempted": False,
        "binary_files_committed": False,
        "download_cache_committed": False,
        "raw_extracted_text_committed": False,
        "can_claim_multi_real_world_pdf_parse_observation": True,
        "can_claim_robust_pdf_extraction": False,
        "observations": observations,
        "warnings": matrix["warnings"],
        "boundary_notes": matrix["boundary_notes"],
        "recommended_next_gate": NEXT_GATE,
    }


def build_multi_real_world_pdf_parse_observation_report(
    summary: dict[str, Any],
) -> str:
    lines = [
        "# Multi Real-world PDF Parse Observation Matrix",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report records PyMuPDF digital-text observations for multiple real-world BEA PDFs.",
        "",
        "It is not robust PDF extraction evidence.",
        "",
        "## Aggregate",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| observed_fixture_count | {summary['observed_fixture_count']} |",
        f"| parsed_fixture_count | {summary['parsed_fixture_count']} |",
        f"| total_page_count | {summary['total_page_count']} |",
        f"| total_extracted_page_count | {summary['total_extracted_page_count']} |",
        f"| total_empty_page_count | {summary['total_empty_page_count']} |",
        f"| total_text_char_count | {summary['total_text_char_count']} |",
        f"| total_text_block_count | {summary['total_text_block_count']} |",
        f"| total_image_block_count | {summary['total_image_block_count']} |",
        f"| total_table_candidate_count | {summary['total_table_candidate_count']} |",
        f"| table_extraction_performed | {_format_bool(summary['table_extraction_performed'])} |",
        f"| ocr_calls_attempted | {_format_bool(summary['ocr_calls_attempted'])} |",
        f"| binary_files_committed | {_format_bool(summary['binary_files_committed'])} |",
        f"| download_cache_committed | {_format_bool(summary['download_cache_committed'])} |",
        f"| raw_extracted_text_committed | {_format_bool(summary['raw_extracted_text_committed'])} |",
        f"| can_claim_multi_real_world_pdf_parse_observation | {_format_bool(summary['can_claim_multi_real_world_pdf_parse_observation'])} |",
        f"| can_claim_robust_pdf_extraction | {_format_bool(summary['can_claim_robust_pdf_extraction'])} |",
        "",
        "## Fixtures",
        "",
        "| Fixture | Pages | Text chars | Text blocks | Image blocks | Table candidates | SHA-256 |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]
    for item in summary["observations"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    item["fixture_id"],
                    str(item["page_count"]),
                    str(item["text_char_count"]),
                    str(item["text_block_count"]),
                    str(item["image_block_count"]),
                    str(item["table_candidate_count"]),
                    item["source_sha256"],
                ]
            )
            + " |"
        )

    lines.extend(["", "## Warnings", ""])
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
            "This is a multi-fixture real-world PDF parse observation matrix only.",
            "",
            "It records sanitized metadata, byte hashes, and PyMuPDF digital-text diagnostics for three BEA PDFs.",
            "",
            "It does not commit external PDF binaries, download caches, or raw extracted text.",
            "",
            "It does not prove table extraction, OCR, layout fidelity, arbitrary market PDF reliability, or robust PDF extraction.",
            "",
            "This is not hosted deployment evidence.",
            "",
            "This is not product-complete.",
        ]
    )
    return "\n".join(lines) + "\n"


def _validate_matrix(payload: dict[str, Any]) -> None:
    expected_values = {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "claim_boundary": CLAIM_BOUNDARY,
        "source_download_hash_gate": "owner_approved_real_world_pdf_download_and_hash_v0",
        "fixture_count": 3,
        "observed_fixture_count": 3,
        "table_extraction_performed": False,
        "ocr_calls_attempted": False,
        "robust_pdf_extraction_claimed": False,
        "can_claim_robust_pdf_extraction": False,
        "binary_files_committed": False,
        "download_cache_committed": False,
        "raw_extracted_text_committed": False,
        "recommended_next_gate": NEXT_GATE,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(
                f"multi real-world parse observation {field} must be {expected!r}"
            )

    observations = payload.get("observations")
    if not isinstance(observations, list) or len(observations) != 3:
        raise ValueError("multi real-world parse observation must include 3 observations")

    seen_ids: set[str] = set()
    for item in observations:
        _validate_observation(item, seen_ids)
    if seen_ids != EXPECTED_FIXTURE_IDS:
        raise ValueError("multi real-world parse observation fixture set changed")

    for field in ["warnings", "boundary_notes"]:
        value = payload.get(field)
        if not isinstance(value, list) or not value:
            raise ValueError(
                f"multi real-world parse observation {field} must be a non-empty list"
            )

    for note in [
        "multiple real-world PDF parse observations",
        "not robust PDF extraction evidence",
        "no external PDF binaries committed",
        "no raw extracted text committed",
    ]:
        if note not in payload["boundary_notes"]:
            raise ValueError(f"multi real-world parse observation missing note: {note}")


def _validate_observation(item: dict[str, Any], seen_ids: set[str]) -> None:
    if not isinstance(item, dict):
        raise ValueError("multi real-world parse observation entries must be objects")
    fixture_id = str(item.get("fixture_id") or "")
    if not fixture_id:
        raise ValueError("multi real-world parse observation entry missing fixture_id")
    if fixture_id in seen_ids:
        raise ValueError(f"duplicate fixture_id: {fixture_id}")
    seen_ids.add(fixture_id)

    expected_values = {
        "publisher": "U.S. Bureau of Economic Analysis",
        "license_source_url": "https://www.bea.gov/help/faq/147",
        "redistribution_status": "public_domain_unless_stated_otherwise",
        "download_status": "downloaded_and_hashed_for_owner_runtime_observation",
        "http_status": 200,
        "content_type": "application/pdf",
        "source_sha256_algorithm": "sha256",
        "pdf_magic_header": True,
        "parser": "pdf-pymupdf",
        "parse_status": "parsed_digital_text",
        "table_extraction_performed": False,
        "ocr_calls_attempted": False,
        "robust_pdf_extraction_claimed": False,
        "can_claim_robust_pdf_extraction": False,
        "binary_committed": False,
        "local_pdf_path": None,
        "failure_case_candidate": None,
    }
    for field, expected in expected_values.items():
        if item.get(field) != expected:
            raise ValueError(f"observation {fixture_id} {field} must be {expected!r}")

    for field in [
        "byte_size",
        "page_count",
        "extracted_page_count",
        "text_char_count",
        "text_block_count",
    ]:
        value = item.get(field)
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"observation {fixture_id} {field} must be positive")

    for field in ["empty_page_count", "image_block_count", "table_candidate_count"]:
        value = item.get(field)
        if not isinstance(value, int) or value < 0:
            raise ValueError(f"observation {fixture_id} {field} must be non-negative")

    sha256 = str(item.get("source_sha256") or "")
    if len(sha256) != 64:
        raise ValueError(f"observation {fixture_id} must include a SHA-256 digest")
    if not str(item.get("source_url") or "").startswith("https://www.bea.gov/"):
        raise ValueError(f"observation {fixture_id} source_url must be a BEA URL")
    if len(str(item.get("text_sample") or "")) > 240:
        raise ValueError(f"observation {fixture_id} text_sample must stay short")
    if not item.get("warnings"):
        raise ValueError(f"observation {fixture_id} must include warnings")


def _format_bool(value: bool) -> str:
    return "true" if value else "false"
