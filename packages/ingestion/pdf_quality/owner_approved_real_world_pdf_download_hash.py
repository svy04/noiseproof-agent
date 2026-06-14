from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PHASE_MARKER = "owner_approved_real_world_pdf_download_and_hash_v0"
CLAIM_BOUNDARY = (
    "owner_approved_real_world_pdf_download_hash_metadata_only_not_robust_pdf_extraction"
)
NEXT_GATE = "real_world_pdf_parse_observation_without_robust_claim_v0"


def load_owner_approved_real_world_pdf_download_hash_manifest(
    path: Path | str,
) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    _validate_manifest(payload)
    return payload


def build_owner_approved_real_world_pdf_download_hash_summary(
    manifest: dict[str, Any],
) -> dict[str, Any]:
    _validate_manifest(manifest)
    downloaded = list(manifest["downloaded_fixtures"])
    blocked = list(manifest["blocked_fixtures"])
    return {
        "phase_marker": PHASE_MARKER,
        "claim_boundary": CLAIM_BOUNDARY,
        "owner_approved": True,
        "source_manifest": manifest["source_manifest"],
        "observed_at_utc": manifest["observed_at_utc"],
        "downloaded_fixture_count": len(downloaded),
        "blocked_fixture_count": len(blocked),
        "downloaded_fixture_ids": [item["fixture_id"] for item in downloaded],
        "blocked_fixture_ids": [item["fixture_id"] for item in blocked],
        "binary_files_committed": False,
        "download_cache_committed": False,
        "parser_calls_attempted": False,
        "ocr_calls_attempted": False,
        "table_extraction_attempted": False,
        "robust_pdf_extraction_claimed": False,
        "can_claim_real_world_pdf_download_hash": True,
        "can_claim_robust_pdf_extraction": False,
        "downloaded_fixtures": downloaded,
        "blocked_fixtures": blocked,
        "boundary_notes": manifest["boundary_notes"],
        "recommended_next_gate": NEXT_GATE,
    }


def build_owner_approved_real_world_pdf_download_hash_report(
    summary: dict[str, Any],
) -> str:
    lines = [
        "# Owner-approved Real-world PDF Download and Hash",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report records owner-approved real-world PDF download/hash metadata.",
        "",
        "No external PDF binaries or download caches are committed in this gate.",
        "",
        "It is not robust PDF extraction evidence.",
        "",
        "## Aggregate",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| downloaded_fixture_count | {summary['downloaded_fixture_count']} |",
        f"| blocked_fixture_count | {summary['blocked_fixture_count']} |",
        f"| binary_files_committed | {_format_bool(summary['binary_files_committed'])} |",
        f"| download_cache_committed | {_format_bool(summary['download_cache_committed'])} |",
        f"| parser_calls_attempted | {_format_bool(summary['parser_calls_attempted'])} |",
        f"| ocr_calls_attempted | {_format_bool(summary['ocr_calls_attempted'])} |",
        f"| table_extraction_attempted | {_format_bool(summary['table_extraction_attempted'])} |",
        f"| can_claim_real_world_pdf_download_hash | {_format_bool(summary['can_claim_real_world_pdf_download_hash'])} |",
        f"| can_claim_robust_pdf_extraction | {_format_bool(summary['can_claim_robust_pdf_extraction'])} |",
        "",
        "## Downloaded and Hashed Fixtures",
        "",
        "| Fixture | Publisher | HTTP | Content type | Bytes | SHA-256 |",
        "|---|---|---:|---|---:|---|",
    ]
    for item in summary["downloaded_fixtures"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    item["fixture_id"],
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
            "## Blocked Runtime Attempts",
            "",
            "| Fixture | Publisher | HTTP | Download status | Boundary |",
            "|---|---|---:|---|---|",
        ]
    )
    for item in summary["blocked_fixtures"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    item["fixture_id"],
                    item["publisher"],
                    str(item["http_status"]),
                    item["download_status"],
                    item["boundary"],
                ]
            )
            + " |"
        )

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
            "This is download/hash metadata only.",
            "",
            "It records source URLs, runtime HTTP status, byte size, SHA-256, and binary non-commitment.",
            "",
            "It does not parse, OCR, chunk, retrieve, evaluate, or generate reports from these PDFs.",
            "",
            "This is not robust PDF extraction implementation.",
            "",
            "This is not arbitrary market PDF parsing evidence.",
            "",
            "This is not hosted deployment evidence.",
            "",
            "This is not product-complete.",
        ]
    )
    return "\n".join(lines) + "\n"


def _validate_manifest(payload: dict[str, Any]) -> None:
    expected_values = {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "claim_boundary": CLAIM_BOUNDARY,
        "owner_approved": True,
        "binary_files_committed": False,
        "download_cache_committed": False,
        "parser_calls_attempted": False,
        "ocr_calls_attempted": False,
        "table_extraction_attempted": False,
        "robust_pdf_extraction_claimed": False,
        "can_claim_robust_pdf_extraction": False,
        "recommended_next_gate": NEXT_GATE,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(f"download/hash manifest {field} must be {expected!r}")

    downloaded = payload.get("downloaded_fixtures")
    blocked = payload.get("blocked_fixtures")
    if not isinstance(downloaded, list) or not downloaded:
        raise ValueError("download/hash manifest must include downloaded fixtures")
    if not isinstance(blocked, list):
        raise ValueError("download/hash manifest blocked_fixtures must be a list")

    seen_ids: set[str] = set()
    for item in downloaded:
        fixture_id = _fixture_id(item, seen_ids)
        if item.get("download_status") != "downloaded_and_hashed":
            raise ValueError(f"downloaded fixture {fixture_id} has wrong status")
        if item.get("http_status") != 200:
            raise ValueError(f"downloaded fixture {fixture_id} must have HTTP 200")
        if item.get("content_type") != "application/pdf":
            raise ValueError(f"downloaded fixture {fixture_id} must be application/pdf")
        if not isinstance(item.get("byte_size"), int) or item["byte_size"] <= 0:
            raise ValueError(f"downloaded fixture {fixture_id} must record byte_size")
        sha256 = str(item.get("sha256") or "")
        if len(sha256) != 64:
            raise ValueError(f"downloaded fixture {fixture_id} must record sha256")
        if item.get("pdf_magic_header") is not True:
            raise ValueError(f"downloaded fixture {fixture_id} must record PDF magic")
        _validate_no_binary_commit(item, fixture_id)

    for item in blocked:
        fixture_id = _fixture_id(item, seen_ids)
        if item.get("download_status") != "blocked_403_in_owner_runtime":
            raise ValueError(f"blocked fixture {fixture_id} has wrong status")
        if item.get("http_status") != 403:
            raise ValueError(f"blocked fixture {fixture_id} must record HTTP 403")
        if item.get("sha256") is not None:
            raise ValueError(f"blocked fixture {fixture_id} must not record sha256")
        _validate_no_binary_commit(item, fixture_id)

    boundary_notes = payload.get("boundary_notes", [])
    for note in [
        "download/hash metadata only",
        "no external PDF binaries committed",
        "not robust PDF extraction evidence",
    ]:
        if note not in boundary_notes:
            raise ValueError(f"download/hash manifest missing boundary note: {note}")


def _fixture_id(item: dict[str, Any], seen_ids: set[str]) -> str:
    if not isinstance(item, dict):
        raise ValueError("fixture entries must be objects")
    fixture_id = str(item.get("fixture_id") or "")
    if not fixture_id:
        raise ValueError("fixture entry is missing fixture_id")
    if fixture_id in seen_ids:
        raise ValueError(f"duplicate fixture_id: {fixture_id}")
    seen_ids.add(fixture_id)
    for field in ["source_url", "license_source_url"]:
        value = str(item.get(field) or "")
        if not value.startswith("https://"):
            raise ValueError(f"fixture {fixture_id} {field} must be https")
    return fixture_id


def _validate_no_binary_commit(item: dict[str, Any], fixture_id: str) -> None:
    if item.get("binary_committed") is not False:
        raise ValueError(f"fixture {fixture_id} binary_committed must be false")
    if item.get("local_pdf_path") is not None:
        raise ValueError(f"fixture {fixture_id} must not record local_pdf_path")


def _format_bool(value: bool) -> str:
    return "true" if value else "false"
