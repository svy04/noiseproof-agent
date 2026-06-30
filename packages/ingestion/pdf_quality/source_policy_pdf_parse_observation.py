from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PHASE_MARKER = "source_policy_pdf_parse_observation_v0"
PREVIOUS_GATE = "real_world_pdf_fixture_source_policy_download_hash_v0"
CLAIM_BOUNDARY = (
    "source_policy_parse_observation_metadata_only_not_robust_pdf_extraction"
)
NEXT_GATE = "source_policy_pdf_parse_quality_matrix_v0"

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


def load_source_policy_pdf_parse_observation(path: Path | str) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    _validate_observation(payload)
    return payload


def build_source_policy_pdf_parse_observation_summary(
    observation: dict[str, Any],
) -> dict[str, Any]:
    _validate_observation(observation)
    observed = list(observation["observed_fixtures"])
    blocked = list(observation["blocked_fixtures"])
    external_routes = list(observation["external_routes"])
    native_text = [
        item for item in observed if item["parse_status"] == "metadata_observed"
    ]
    no_native_text = [
        item
        for item in observed
        if item["parse_status"] == "no_native_text_observed"
    ]
    failure_candidates = [
        item for item in observed if item.get("failure_case_candidate") is not None
    ]
    return {
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "source_download_hash_manifest": observation[
            "source_download_hash_manifest"
        ],
        "observed_at_utc": observation["observed_at_utc"],
        "parse_observation_status": observation["parse_observation_status"],
        "candidate_count": len(observed) + len(blocked) + len(external_routes),
        "observed_fixture_count": len(observed),
        "native_text_fixture_count": len(native_text),
        "no_native_text_fixture_count": len(no_native_text),
        "blocked_fixture_count": len(blocked),
        "external_route_count": len(external_routes),
        "failure_case_candidate_count": len(failure_candidates),
        "observed_fixture_ids": [item["fixture_id"] for item in observed],
        "blocked_fixture_ids": [item["fixture_id"] for item in blocked],
        "external_route_ids": [item["fixture_id"] for item in external_routes],
        "total_page_count": sum(item["page_count"] for item in observed),
        "total_extracted_page_count": sum(
            item["extracted_page_count"] for item in observed
        ),
        "total_empty_page_count": sum(item["empty_page_count"] for item in observed),
        "total_text_char_count": sum(item["text_char_count"] for item in observed),
        "total_text_block_count": sum(item["text_block_count"] for item in observed),
        "total_image_block_count": sum(
            item["image_block_count"] for item in observed
        ),
        "runtime_work_performed": True,
        "pdf_downloads_performed": True,
        "parser_calls_performed": True,
        "ocr_calls_performed": False,
        "table_extraction_calls_performed": False,
        "llm_calls_performed": False,
        "binary_files_committed": False,
        "download_cache_committed": False,
        "raw_text_committed": False,
        "can_claim_source_policy_pdf_parse_observation": True,
        "can_claim_robust_pdf_extraction": False,
        "observed_fixtures": observed,
        "blocked_fixtures": blocked,
        "external_routes": external_routes,
        "blocked_reasons": observation["blocked_reasons"],
        "warnings": observation["warnings"],
        "boundary_notes": observation["boundary_notes"],
        "next_gate": NEXT_GATE,
    }


def build_source_policy_pdf_parse_observation_report(
    summary: dict[str, Any],
) -> str:
    lines = [
        "# Source-policy PDF Parse Observation",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report records temporary owner-runtime PyMuPDF text/block metadata observations for source-policy-reviewed PDF candidates.",
        "",
        "No external PDF binaries, download caches, raw text, page images, or screenshots are committed.",
        "",
        "It is not robust PDF extraction evidence.",
        "",
        "## Gate Result",
        "",
        f"parse_observation_status -> {summary['parse_observation_status']}",
        f"previous_gate -> {summary['previous_gate']}",
        f"candidate_count -> {summary['candidate_count']}",
        f"observed_fixture_count -> {summary['observed_fixture_count']}",
        f"native_text_fixture_count -> {summary['native_text_fixture_count']}",
        f"no_native_text_fixture_count -> {summary['no_native_text_fixture_count']}",
        f"blocked_fixture_count -> {summary['blocked_fixture_count']}",
        f"external_route_count -> {summary['external_route_count']}",
        f"failure_case_candidate_count -> {summary['failure_case_candidate_count']}",
        f"total_page_count -> {summary['total_page_count']}",
        f"total_extracted_page_count -> {summary['total_extracted_page_count']}",
        f"total_empty_page_count -> {summary['total_empty_page_count']}",
        f"total_text_char_count -> {summary['total_text_char_count']}",
        f"total_text_block_count -> {summary['total_text_block_count']}",
        f"total_image_block_count -> {summary['total_image_block_count']}",
        f"runtime_work_performed -> {_format_bool(summary['runtime_work_performed'])}",
        f"pdf_downloads_performed -> {_format_bool(summary['pdf_downloads_performed'])}",
        f"parser_calls_performed -> {_format_bool(summary['parser_calls_performed'])}",
        f"ocr_calls_performed -> {_format_bool(summary['ocr_calls_performed'])}",
        f"table_extraction_calls_performed -> {_format_bool(summary['table_extraction_calls_performed'])}",
        f"llm_calls_performed -> {_format_bool(summary['llm_calls_performed'])}",
        f"binary_files_committed -> {_format_bool(summary['binary_files_committed'])}",
        f"download_cache_committed -> {_format_bool(summary['download_cache_committed'])}",
        f"raw_text_committed -> {_format_bool(summary['raw_text_committed'])}",
        f"can_claim_source_policy_pdf_parse_observation -> {_format_bool(summary['can_claim_source_policy_pdf_parse_observation'])}",
        f"can_claim_robust_pdf_extraction -> {_format_bool(summary['can_claim_robust_pdf_extraction'])}",
        "",
        "## Observed Fixtures",
        "",
        "| Fixture | Missing cell | Publisher | Status | Pages | Extracted pages | Empty pages | Text chars | Text blocks | Image blocks | Failure candidate |",
        "|---|---|---|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for item in summary["observed_fixtures"]:
        failure = item.get("failure_case_candidate") or {}
        failure_label = failure.get("failure_type", "")
        lines.append(
            "| "
            + " | ".join(
                [
                    item["fixture_id"],
                    item["target_missing_cell"],
                    item["publisher"],
                    item["parse_status"],
                    str(item["page_count"]),
                    str(item["extracted_page_count"]),
                    str(item["empty_page_count"]),
                    str(item["text_char_count"]),
                    str(item["text_block_count"]),
                    str(item["image_block_count"]),
                    failure_label,
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Blocked Download Candidates Preserved",
            "",
            "| Fixture | Missing cell | Publisher | HTTP | Status | Boundary |",
            "|---|---|---|---:|---|---|",
        ]
    )
    for item in summary["blocked_fixtures"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    item["fixture_id"],
                    item["target_missing_cell"],
                    item["publisher"],
                    str(item["http_status"]),
                    item["download_status"],
                    item["boundary"],
                ]
            )
            + " |"
        )

    lines.extend(["", "## External Routes Preserved", ""])
    for item in summary["external_routes"]:
        lines.append(f"- {item['fixture_id']} -> {item['source_url']}")

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
            "This is source-policy PDF parse observation metadata only.",
            "",
            "It records source URLs, policy URLs, SHA-256 provenance, PyMuPDF text/block metadata, no-native-text failure candidacy, and binary non-commitment.",
            "",
            "It does not commit raw text, run OCR, extract tables, compare rendered pages, interpret images or charts, call LLMs, chunk, retrieve, generate Evidence Ledger entries, run Noise Gate, or produce final reports from these PDFs.",
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


def _validate_observation(payload: dict[str, Any]) -> None:
    _validate_forbidden_fields(payload)
    expected_values = {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "source_download_hash_manifest": "examples/pdf-extraction-quality/source-policy-download-hash-observations.json",
        "parse_observation_status": "passed_with_no_native_text_candidate",
        "owner_approved": True,
        "parser": "pymupdf",
        "can_claim_source_policy_pdf_parse_observation": True,
        "can_claim_robust_pdf_extraction": False,
        "runtime_work_performed": True,
        "pdf_downloads_performed": True,
        "parser_calls_performed": True,
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
                f"source-policy parse observation {field} must be {expected!r}"
            )

    observed = payload.get("observed_fixtures")
    blocked = payload.get("blocked_fixtures")
    external_routes = payload.get("external_routes")
    if not isinstance(observed, list) or len(observed) != 3:
        raise ValueError("source-policy parse observation must include 3 observed fixtures")
    if not isinstance(blocked, list) or len(blocked) != 2:
        raise ValueError("source-policy parse observation must include 2 blocked fixtures")
    if not isinstance(external_routes, list) or len(external_routes) != 1:
        raise ValueError("source-policy parse observation must include 1 external route")

    seen_ids: set[str] = set()
    no_native_text_count = 0
    for item in observed:
        fixture_id = _fixture_id(item, seen_ids)
        if item.get("http_status") != 200:
            raise ValueError(f"observed fixture {fixture_id} must have HTTP 200")
        if not isinstance(item.get("byte_size"), int) or item["byte_size"] <= 0:
            raise ValueError(f"observed fixture {fixture_id} must record byte_size")
        sha256 = str(item.get("source_sha256") or "")
        if len(sha256) != 64:
            raise ValueError(f"observed fixture {fixture_id} must record source_sha256")
        if item.get("parser") != "pymupdf":
            raise ValueError(f"observed fixture {fixture_id} must use pymupdf")
        if item.get("table_extraction_performed") is not False:
            raise ValueError(f"observed fixture {fixture_id} must not extract tables")
        if item.get("ocr_calls_attempted") is not False:
            raise ValueError(f"observed fixture {fixture_id} must not run OCR")
        if item.get("raw_text_committed") is not False:
            raise ValueError(f"observed fixture {fixture_id} raw text must not be committed")
        _validate_no_binary_commit(item, fixture_id)
        for field in [
            "page_count",
            "extracted_page_count",
            "empty_page_count",
            "pages_with_text",
            "pages_with_images",
            "text_char_count",
            "text_block_count",
            "image_block_count",
        ]:
            value = item.get(field)
            if not isinstance(value, int) or value < 0:
                raise ValueError(f"observed fixture {fixture_id} {field} must be non-negative")
        if item["page_count"] <= 0:
            raise ValueError(f"observed fixture {fixture_id} page_count must be positive")
        if item["extracted_page_count"] + item["empty_page_count"] != item["page_count"]:
            raise ValueError(f"observed fixture {fixture_id} page counts do not add up")
        status = item.get("parse_status")
        failure = item.get("failure_case_candidate")
        if status == "metadata_observed":
            if item["text_char_count"] <= 0 or failure is not None:
                raise ValueError(f"observed fixture {fixture_id} metadata status is inconsistent")
        elif status == "no_native_text_observed":
            no_native_text_count += 1
            if item["text_char_count"] != 0:
                raise ValueError(f"observed fixture {fixture_id} no-native text has characters")
            if not isinstance(failure, dict) or failure.get("failure_type") != "no_native_text_observed":
                raise ValueError(f"observed fixture {fixture_id} missing no-native-text failure candidate")
        else:
            raise ValueError(f"observed fixture {fixture_id} has unsupported parse status")

    if no_native_text_count != 1:
        raise ValueError("source-policy parse observation must include one no-native-text candidate")

    for item in blocked:
        fixture_id = _fixture_id(item, seen_ids)
        if item.get("download_status") != "blocked_http_403":
            raise ValueError(f"blocked fixture {fixture_id} has wrong status")
        if item.get("http_status") != 403:
            raise ValueError(f"blocked fixture {fixture_id} must record HTTP 403")
        _validate_no_hash(item, fixture_id)
        _validate_no_binary_commit(item, fixture_id)

    for item in external_routes:
        fixture_id = _fixture_id(item, seen_ids)
        if item.get("download_status") != "not_applicable_external_review_route":
            raise ValueError(f"external route {fixture_id} has wrong status")
        if item.get("http_status") is not None:
            raise ValueError(f"external route {fixture_id} must not record HTTP status")
        _validate_no_hash(item, fixture_id)
        _validate_no_binary_commit(item, fixture_id)

    for field in ["blocked_reasons", "warnings", "boundary_notes"]:
        value = payload.get(field)
        if not isinstance(value, list) or not value:
            raise ValueError(f"source-policy parse observation {field} must be non-empty")

    for note in [
        "source-policy PDF parse observation metadata only",
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
            raise ValueError(f"source-policy parse observation missing boundary note: {note}")


def _fixture_id(item: dict[str, Any], seen_ids: set[str]) -> str:
    if not isinstance(item, dict):
        raise ValueError("fixture entries must be objects")
    fixture_id = str(item.get("fixture_id") or "")
    if not fixture_id:
        raise ValueError("fixture entry is missing fixture_id")
    if fixture_id in seen_ids:
        raise ValueError(f"duplicate fixture_id: {fixture_id}")
    seen_ids.add(fixture_id)
    for field in ["source_url", "policy_source_url"]:
        value = str(item.get(field) or "")
        if not value.startswith("https://"):
            raise ValueError(f"fixture {fixture_id} {field} must be https")
    if not item.get("target_missing_cell") or not item.get("publisher"):
        raise ValueError(f"fixture {fixture_id} missing target_missing_cell or publisher")
    return fixture_id


def _validate_no_binary_commit(item: dict[str, Any], fixture_id: str) -> None:
    if item.get("binary_committed") is not False:
        raise ValueError(f"fixture {fixture_id} binary_committed must be false")
    if item.get("local_pdf_path") is not None:
        raise ValueError(f"fixture {fixture_id} must not record local_pdf_path")


def _validate_no_hash(item: dict[str, Any], fixture_id: str) -> None:
    if item.get("sha256") is not None:
        raise ValueError(f"fixture {fixture_id} must not record sha256")
    if item.get("byte_size") is not None:
        raise ValueError(f"fixture {fixture_id} must not record byte_size")
    if item.get("pdf_magic_header") is not None:
        raise ValueError(f"fixture {fixture_id} must not record PDF magic")


def _validate_forbidden_fields(value: Any) -> None:
    if isinstance(value, dict):
        for key, nested in value.items():
            if key in _FORBIDDEN_FIELDS:
                raise ValueError(f"source-policy parse observation must not commit {key}")
            _validate_forbidden_fields(nested)
    elif isinstance(value, list):
        for item in value:
            _validate_forbidden_fields(item)


def _format_bool(value: bool) -> str:
    return "true" if value else "false"
