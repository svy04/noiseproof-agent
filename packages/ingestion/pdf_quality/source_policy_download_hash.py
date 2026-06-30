from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PHASE_MARKER = "real_world_pdf_fixture_source_policy_download_hash_v0"
PREVIOUS_GATE = "targeted_real_world_pdf_fixture_expansion_v0"
CLAIM_BOUNDARY = "source_policy_download_hash_metadata_only_not_runtime_pdf_extraction"
NEXT_GATE = "source_policy_pdf_parse_observation_v0"

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


def load_source_policy_download_hash_manifest(path: Path | str) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    _validate_manifest(payload)
    return payload


def build_source_policy_download_hash_summary(
    manifest: dict[str, Any],
) -> dict[str, Any]:
    _validate_manifest(manifest)
    downloaded = list(manifest["downloaded_fixtures"])
    blocked = list(manifest["blocked_fixtures"])
    external_routes = list(manifest["external_routes"])
    return {
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "source_plan": manifest["source_plan"],
        "observed_at_utc": manifest["observed_at_utc"],
        "download_hash_status": manifest["download_hash_status"],
        "candidate_count": len(downloaded) + len(blocked) + len(external_routes),
        "downloaded_fixture_count": len(downloaded),
        "blocked_fixture_count": len(blocked),
        "external_route_count": len(external_routes),
        "downloaded_fixture_ids": [item["fixture_id"] for item in downloaded],
        "blocked_fixture_ids": [item["fixture_id"] for item in blocked],
        "external_route_ids": [item["fixture_id"] for item in external_routes],
        "runtime_work_performed": True,
        "pdf_downloads_performed": True,
        "parser_calls_performed": False,
        "ocr_calls_performed": False,
        "table_extraction_calls_performed": False,
        "llm_calls_performed": False,
        "binary_files_committed": False,
        "download_cache_committed": False,
        "raw_text_committed": False,
        "can_claim_download_hash_metadata": True,
        "can_claim_robust_pdf_extraction": False,
        "downloaded_fixtures": downloaded,
        "blocked_fixtures": blocked,
        "external_routes": external_routes,
        "blocked_reasons": manifest["blocked_reasons"],
        "warnings": manifest["warnings"],
        "boundary_notes": manifest["boundary_notes"],
        "next_gate": NEXT_GATE,
    }


def build_source_policy_download_hash_report(summary: dict[str, Any]) -> str:
    lines = [
        "# Source-policy PDF Download and Hash",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report records temporary owner-runtime download/hash metadata for source-policy-reviewed PDF candidates.",
        "",
        "No external PDF binaries, download caches, raw text, page images, or screenshots are committed.",
        "",
        "It is not robust PDF extraction evidence.",
        "",
        "## Gate Result",
        "",
        f"download_hash_status -> {summary['download_hash_status']}",
        f"previous_gate -> {summary['previous_gate']}",
        f"candidate_count -> {summary['candidate_count']}",
        f"downloaded_fixture_count -> {summary['downloaded_fixture_count']}",
        f"blocked_fixture_count -> {summary['blocked_fixture_count']}",
        f"external_route_count -> {summary['external_route_count']}",
        f"runtime_work_performed -> {_format_bool(summary['runtime_work_performed'])}",
        f"pdf_downloads_performed -> {_format_bool(summary['pdf_downloads_performed'])}",
        f"parser_calls_performed -> {_format_bool(summary['parser_calls_performed'])}",
        f"ocr_calls_performed -> {_format_bool(summary['ocr_calls_performed'])}",
        f"table_extraction_calls_performed -> {_format_bool(summary['table_extraction_calls_performed'])}",
        f"llm_calls_performed -> {_format_bool(summary['llm_calls_performed'])}",
        f"binary_files_committed -> {_format_bool(summary['binary_files_committed'])}",
        f"download_cache_committed -> {_format_bool(summary['download_cache_committed'])}",
        f"raw_text_committed -> {_format_bool(summary['raw_text_committed'])}",
        f"can_claim_download_hash_metadata -> {_format_bool(summary['can_claim_download_hash_metadata'])}",
        f"can_claim_robust_pdf_extraction -> {_format_bool(summary['can_claim_robust_pdf_extraction'])}",
        "",
        "## Downloaded and Hashed Fixtures",
        "",
        "| Fixture | Missing cell | Publisher | HTTP | Content type | Bytes | SHA-256 |",
        "|---|---|---|---:|---|---:|---|",
    ]
    for item in summary["downloaded_fixtures"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    item["fixture_id"],
                    item["target_missing_cell"],
                    item["publisher"],
                    str(item["http_status"]),
                    item["content_type"],
                    str(item["byte_size"]),
                    item["sha256"],
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Blocked Download Candidates",
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

    lines.extend(["", "## External Routes", ""])
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
            "This is download/hash metadata only.",
            "",
            "It records source URLs, policy URLs, runtime HTTP status, byte size, SHA-256, PDF magic-header status, and binary non-commitment.",
            "",
            "It does not parse PDFs, run OCR, extract tables, call LLMs, chunk, retrieve, generate Evidence Ledger entries, run Noise Gate, or produce final reports from these PDFs.",
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


def _validate_manifest(payload: dict[str, Any]) -> None:
    _validate_forbidden_fields(payload)
    expected_values = {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "download_hash_status": "passed_with_blocked_candidates",
        "owner_approved": True,
        "can_claim_download_hash_metadata": True,
        "can_claim_robust_pdf_extraction": False,
        "runtime_work_performed": True,
        "pdf_downloads_performed": True,
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
            raise ValueError(f"source-policy download/hash {field} must be {expected!r}")

    downloaded = payload.get("downloaded_fixtures")
    blocked = payload.get("blocked_fixtures")
    external_routes = payload.get("external_routes")
    if not isinstance(downloaded, list) or len(downloaded) != 3:
        raise ValueError("source-policy download/hash must include 3 downloaded fixtures")
    if not isinstance(blocked, list) or len(blocked) != 2:
        raise ValueError("source-policy download/hash must include 2 blocked fixtures")
    if not isinstance(external_routes, list) or len(external_routes) != 1:
        raise ValueError("source-policy download/hash must include 1 external route")

    seen_ids: set[str] = set()
    for item in downloaded:
        fixture_id = _fixture_id(item, seen_ids)
        if item.get("download_status") != "downloaded_and_hashed":
            raise ValueError(f"downloaded fixture {fixture_id} has wrong status")
        if item.get("http_status") != 200:
            raise ValueError(f"downloaded fixture {fixture_id} must have HTTP 200")
        if not isinstance(item.get("byte_size"), int) or item["byte_size"] <= 0:
            raise ValueError(f"downloaded fixture {fixture_id} must record byte_size")
        sha256 = str(item.get("sha256") or "")
        if len(sha256) != 64:
            raise ValueError(f"downloaded fixture {fixture_id} must record sha256")
        if item.get("pdf_magic_header") is not True:
            raise ValueError(f"downloaded fixture {fixture_id} must record PDF magic")
        if item.get("raw_text_committed") is not False:
            raise ValueError(f"fixture {fixture_id} raw_text_committed must be false")
        _validate_no_binary_commit(item, fixture_id)

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
            raise ValueError(f"source-policy download/hash {field} must be non-empty")

    for note in [
        "download/hash metadata only",
        "source-policy reviewed candidates only",
        "no external PDF binaries committed",
        "no download cache committed",
        "no raw text committed",
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
            raise ValueError(f"source-policy download/hash missing boundary note: {note}")


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
                raise ValueError(f"source-policy download/hash must not commit {key}")
            _validate_forbidden_fields(nested)
    elif isinstance(value, list):
        for item in value:
            _validate_forbidden_fields(item)


def _format_bool(value: bool) -> str:
    return "true" if value else "false"
