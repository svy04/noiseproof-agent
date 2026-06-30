from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PHASE_MARKER = "source_policy_no_native_text_ocr_readiness_review_v0"
PREVIOUS_GATE = "source_policy_no_native_text_failure_route_v0"
CLAIM_BOUNDARY = (
    "source_policy_no_native_text_ocr_readiness_review_only_not_dependency_execution_or_quality_evidence"
)
NEXT_GATE = "source_policy_no_native_text_ocr_dependency_check_v0"

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
    "tessdata_path",
    "tesseract_path",
}


def load_source_policy_no_native_text_ocr_readiness_review(
    path: Path | str,
) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    _validate_review(payload)
    return payload


def build_source_policy_no_native_text_ocr_readiness_summary(
    review: dict[str, Any],
) -> dict[str, Any]:
    _validate_review(review)
    preserved_route = dict(review["preserved_failure_route"])
    return {
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "source_failure_route_manifest": review["source_failure_route_manifest"],
        "readiness_status": review["readiness_status"],
        "fixture_id": preserved_route["fixture_id"],
        "publisher": preserved_route["publisher"],
        "source_url": preserved_route["source_url"],
        "policy_source_url": preserved_route["policy_source_url"],
        "source_sha256": preserved_route["source_sha256"],
        "failure_type": preserved_route["failure_type"],
        "root_cause": preserved_route["root_cause"],
        "page_count": preserved_route["page_count"],
        "empty_page_count": preserved_route["empty_page_count"],
        "text_char_count": preserved_route["text_char_count"],
        "ocr_dependency_identified": True,
        "ocr_dependency_runtime_check_performed": False,
        "ocr_execution_performed": False,
        "ocr_quality_eval_performed": False,
        "runtime_work_performed": False,
        "pdf_downloads_performed": False,
        "parser_calls_performed": False,
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
        "local_paths_committed": False,
        "tessdata_paths_committed": False,
        "can_claim_ocr_readiness_review": True,
        "can_claim_ocr_dependency_available": False,
        "can_claim_ocr_execution": False,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
        "sources": review["sources"],
        "readiness_criteria": review["readiness_criteria"],
        "blocked_reasons": review["blocked_reasons"],
        "minimum_next_evidence": review["minimum_next_evidence"],
        "warnings": review["warnings"],
        "boundary_notes": review["boundary_notes"],
        "next_gate": NEXT_GATE,
    }


def build_source_policy_no_native_text_ocr_readiness_report(
    summary: dict[str, Any],
) -> str:
    lines = [
        "# Source-policy No-native-text OCR Readiness Review",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report reviews whether the preserved NARA no-native-text failure route is ready for a future OCR dependency check.",
        "",
        "It does not check local OCR dependencies.",
        "",
        "It does not run OCR.",
        "",
        "It is not OCR quality evidence.",
        "",
        "It is not robust PDF extraction evidence.",
        "",
        "## Gate Result",
        "",
        f"readiness_status -> {summary['readiness_status']}",
        f"previous_gate -> {summary['previous_gate']}",
        f"fixture_id -> {summary['fixture_id']}",
        f"publisher -> {summary['publisher']}",
        f"failure_type -> {summary['failure_type']}",
        f"root_cause -> {summary['root_cause']}",
        f"page_count -> {summary['page_count']}",
        f"empty_page_count -> {summary['empty_page_count']}",
        f"text_char_count -> {summary['text_char_count']}",
        f"ocr_dependency_identified -> {_format_bool(summary['ocr_dependency_identified'])}",
        f"ocr_dependency_runtime_check_performed -> {_format_bool(summary['ocr_dependency_runtime_check_performed'])}",
        f"ocr_execution_performed -> {_format_bool(summary['ocr_execution_performed'])}",
        f"ocr_quality_eval_performed -> {_format_bool(summary['ocr_quality_eval_performed'])}",
        f"runtime_work_performed -> {_format_bool(summary['runtime_work_performed'])}",
        f"pdf_downloads_performed -> {_format_bool(summary['pdf_downloads_performed'])}",
        f"parser_calls_performed -> {_format_bool(summary['parser_calls_performed'])}",
        f"table_extraction_calls_performed -> {_format_bool(summary['table_extraction_calls_performed'])}",
        f"llm_calls_performed -> {_format_bool(summary['llm_calls_performed'])}",
        f"binary_files_committed -> {_format_bool(summary['binary_files_committed'])}",
        f"download_cache_committed -> {_format_bool(summary['download_cache_committed'])}",
        f"raw_text_committed -> {_format_bool(summary['raw_text_committed'])}",
        f"raw_ocr_text_committed -> {_format_bool(summary['raw_ocr_text_committed'])}",
        f"local_paths_committed -> {_format_bool(summary['local_paths_committed'])}",
        f"tessdata_paths_committed -> {_format_bool(summary['tessdata_paths_committed'])}",
        f"can_claim_ocr_readiness_review -> {_format_bool(summary['can_claim_ocr_readiness_review'])}",
        f"can_claim_ocr_dependency_available -> {_format_bool(summary['can_claim_ocr_dependency_available'])}",
        f"can_claim_ocr_execution -> {_format_bool(summary['can_claim_ocr_execution'])}",
        f"can_claim_ocr_quality -> {_format_bool(summary['can_claim_ocr_quality'])}",
        f"can_claim_robust_pdf_extraction -> {_format_bool(summary['can_claim_robust_pdf_extraction'])}",
        "",
        "## Sources",
        "",
        "| Label | Type | URL | Pattern |",
        "|---|---|---|---|",
    ]
    for source in summary["sources"]:
        lines.append(
            f"| {source['label']} | {source['source_type']} | {source['url']} | {source['pattern']} |"
        )

    lines.extend(["", "## Readiness Criteria", "", "| Criterion | Status | Reason |", "|---|---|---|"])
    for criterion in summary["readiness_criteria"]:
        lines.append(
            f"| {criterion['criterion_id']} | {criterion['status']} | {criterion['reason']} |"
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
            "This is a deterministic OCR readiness review over a preserved source-policy no-native-text failure route.",
            "",
            "It does not install Tesseract, check tessdata, download PDFs, parse PDFs, run OCR, evaluate OCR output, extract tables, compare rendered pages, interpret images or charts, call LLMs, chunk, retrieve, generate Evidence Ledger entries, run Noise Gate, or build a dashboard.",
            "",
            "It does not commit external PDF binaries, download caches, raw text, raw OCR text, local paths, tessdata paths, page images, or screenshots.",
            "",
            "It does not prove OCR dependency availability, OCR execution, OCR quality, robust PDF extraction, arbitrary-market PDF parsing reliability, table extraction benchmark quality, layout fidelity, rendered visual fidelity, image/chart interpretation, or external validation.",
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
        "source_failure_route_manifest": "examples/pdf-extraction-quality/source-policy-no-native-text-failure-route.json",
        "readiness_status": "passed_with_conditions",
        "owner_approved": True,
        "ocr_dependency_identified": True,
        "ocr_dependency_runtime_check_performed": False,
        "ocr_execution_performed": False,
        "ocr_quality_eval_performed": False,
        "runtime_work_performed": False,
        "pdf_downloads_performed": False,
        "parser_calls_performed": False,
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
        "local_paths_committed": False,
        "tessdata_paths_committed": False,
        "can_claim_ocr_readiness_review": True,
        "can_claim_ocr_dependency_available": False,
        "can_claim_ocr_execution": False,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
        "recommended_next_gate": NEXT_GATE,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(
                f"source-policy no-native-text OCR readiness review {field} must be {expected!r}"
            )

    preserved_route = payload.get("preserved_failure_route")
    if not isinstance(preserved_route, dict):
        raise ValueError("OCR readiness review must include preserved_failure_route")
    _validate_preserved_route(preserved_route)

    for field in [
        "sources",
        "readiness_criteria",
        "blocked_reasons",
        "minimum_next_evidence",
        "warnings",
        "boundary_notes",
    ]:
        value = payload.get(field)
        if not isinstance(value, list) or not value:
            raise ValueError(
                f"source-policy no-native-text OCR readiness review {field} must be non-empty"
            )

    source_labels = {source.get("label") for source in payload["sources"]}
    for label in [
        "PyMuPDF OCR recipes",
        "PyMuPDF Page.get_textpage_ocr",
        "OCR-D evaluation",
        "Model Cards",
        "Datasheets for Datasets",
    ]:
        if label not in source_labels:
            raise ValueError(f"OCR readiness review missing source: {label}")

    criteria = {item.get("criterion_id"): item.get("status") for item in payload["readiness_criteria"]}
    expected_criteria = {
        "preserved_failure_route": "met",
        "source_policy_boundary": "met",
        "ocr_dependency_boundary": "planned_next_gate",
        "ocr_execution_boundary": "blocked_until_dependency_check",
        "ocr_quality_boundary": "blocked_until_ground_truth_eval",
        "raw_content_boundary": "met",
    }
    for criterion_id, expected_status in expected_criteria.items():
        if criteria.get(criterion_id) != expected_status:
            raise ValueError(
                f"OCR readiness criterion {criterion_id} must be {expected_status!r}"
            )

    for note in [
        "source-policy no-native-text OCR readiness review only",
        "not OCR dependency availability evidence",
        "not OCR execution evidence",
        "not OCR quality evidence",
        "not robust PDF extraction evidence",
        "not arbitrary-market PDF parsing evidence",
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
                f"source-policy no-native-text OCR readiness review missing boundary note: {note}"
            )


def _validate_preserved_route(route: dict[str, Any]) -> None:
    expected_values = {
        "fixture_id": "nara_911_mfr_00282_no_native_text_candidate",
        "publisher": "National Archives and Records Administration",
        "source_url": "https://nara-media-001.s3.amazonaws.com/arcmedia/9-11/MFR/t-0148-911MFR-00282.pdf",
        "policy_source_url": "https://www.archives.gov/global-pages/privacy.html",
        "source_sha256": "6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba",
        "failure_type": "no_native_text_observed",
        "root_cause": "image_or_scanned_pdf_without_native_text_layer",
        "page_count": 4,
        "empty_page_count": 4,
        "text_char_count": 0,
    }
    for field, expected in expected_values.items():
        if route.get(field) != expected:
            raise ValueError(f"preserved OCR readiness route {field} must be {expected!r}")


def _validate_forbidden_fields(value: Any) -> None:
    if isinstance(value, dict):
        for key, nested in value.items():
            if key in _FORBIDDEN_FIELDS:
                raise ValueError(
                    f"source-policy no-native-text OCR readiness review must not commit {key}"
                )
            _validate_forbidden_fields(nested)
    elif isinstance(value, list):
        for item in value:
            _validate_forbidden_fields(item)


def _format_bool(value: bool) -> str:
    return "true" if value else "false"
