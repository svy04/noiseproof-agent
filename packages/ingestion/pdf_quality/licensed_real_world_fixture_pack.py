from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PHASE_MARKER = "licensed_real_world_pdf_fixture_pack_v0"
CLAIM_BOUNDARY = (
    "licensed_real_world_pdf_fixture_pack_metadata_only_not_robust_pdf_extraction"
)
NEXT_GATE = "owner_approved_real_world_pdf_download_and_hash_v0"
ALLOWED_REDISTRIBUTION_STATUSES = {
    "public_domain_with_citation_requested",
    "public_domain_unless_stated_otherwise",
}


def load_licensed_real_world_fixture_pack(path: Path | str) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    _validate_pack(payload)
    return payload


def build_licensed_real_world_fixture_pack_summary(
    pack: dict[str, Any],
) -> dict[str, Any]:
    _validate_pack(pack)
    candidates = list(pack["candidates"])
    downloaded = [
        item for item in candidates if item.get("download_status") == "downloaded"
    ]
    role_counts: dict[str, int] = {}
    publisher_counts: dict[str, int] = {}
    for item in candidates:
        role = str(item["fixture_role"])
        publisher = str(item["publisher"])
        role_counts[role] = role_counts.get(role, 0) + 1
        publisher_counts[publisher] = publisher_counts.get(publisher, 0) + 1

    return {
        "phase_marker": PHASE_MARKER,
        "claim_boundary": CLAIM_BOUNDARY,
        "candidate_count": len(candidates),
        "downloaded_candidate_count": len(downloaded),
        "binary_files_committed": False,
        "robust_pdf_extraction_claimed": False,
        "can_claim_robust_pdf_extraction": False,
        "license_review_status": "candidate_metadata_only",
        "candidate_ids": [str(item["fixture_id"]) for item in candidates],
        "role_counts": role_counts,
        "publisher_counts": publisher_counts,
        "license_policy_source_count": len(pack["license_policy_sources"]),
        "source_checked_date": pack["source_checked_date"],
        "candidates": candidates,
        "boundary_notes": pack["boundary_notes"],
        "recommended_next_gate": NEXT_GATE,
    }


def build_licensed_real_world_fixture_pack_report(summary: dict[str, Any]) -> str:
    lines = [
        "# Licensed Real-world PDF Fixture Pack",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report records a metadata-only, source-first candidate pack for future real-world PDF fixture downloads.",
        "",
        "No external PDF binaries are committed in this gate.",
        "",
        "It is not robust PDF extraction evidence.",
        "",
        "## Aggregate",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| candidate_count | {summary['candidate_count']} |",
        f"| downloaded_candidate_count | {summary['downloaded_candidate_count']} |",
        f"| binary_files_committed | {_format_bool(summary['binary_files_committed'])} |",
        f"| robust_pdf_extraction_claimed | {_format_bool(summary['robust_pdf_extraction_claimed'])} |",
        f"| can_claim_robust_pdf_extraction | {_format_bool(summary['can_claim_robust_pdf_extraction'])} |",
        f"| license_policy_source_count | {summary['license_policy_source_count']} |",
        "",
        "## Candidate Sources",
        "",
        "| Candidate | Role | Publisher | Redistribution status | Download status |",
        "|---|---|---|---|---|",
    ]
    for item in summary["candidates"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    item["fixture_id"],
                    item["fixture_role"],
                    item["publisher"],
                    item["redistribution_status"],
                    item["download_status"],
                ]
            )
            + " |"
        )

    lines.extend(["", "## Role Coverage", ""])
    for role, count in sorted(summary["role_counts"].items()):
        lines.append(f"- {role}: {count}")

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
            "This is a licensed real-world PDF fixture candidate pack only.",
            "",
            "It records candidate URLs, publisher/license sources, expected signals, and known risks.",
            "",
            "It does not download, hash, commit, parse, OCR, or evaluate real-world PDF binaries.",
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


def _validate_pack(payload: dict[str, Any]) -> None:
    expected_values = {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "claim_boundary": CLAIM_BOUNDARY,
        "download_status": "candidate_metadata_only",
        "binary_files_committed": False,
        "robust_pdf_extraction_claimed": False,
        "can_claim_robust_pdf_extraction": False,
        "recommended_next_gate": NEXT_GATE,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(f"licensed real-world fixture pack {field} must be {expected!r}")

    candidates = payload.get("candidates")
    if not isinstance(candidates, list) or not candidates:
        raise ValueError("licensed real-world fixture pack must include candidates")
    policy_sources = payload.get("license_policy_sources")
    if not isinstance(policy_sources, list) or not policy_sources:
        raise ValueError("licensed real-world fixture pack must include license policy sources")

    seen_ids: set[str] = set()
    for item in candidates:
        if not isinstance(item, dict):
            raise ValueError("candidate entries must be objects")
        fixture_id = str(item.get("fixture_id") or "")
        if not fixture_id:
            raise ValueError("candidate entry is missing fixture_id")
        if fixture_id in seen_ids:
            raise ValueError(f"duplicate candidate fixture_id: {fixture_id}")
        seen_ids.add(fixture_id)

        _require_https(item, "source_url", fixture_id)
        _require_https(item, "license_source_url", fixture_id)
        if item.get("redistribution_status") not in ALLOWED_REDISTRIBUTION_STATUSES:
            raise ValueError(f"candidate {fixture_id} has unsupported redistribution status")
        if item.get("download_status") != "not_downloaded":
            raise ValueError(f"candidate {fixture_id} must remain not_downloaded in this gate")
        if item.get("local_pdf_path") is not None:
            raise ValueError(f"candidate {fixture_id} must not include a local PDF path")
        if item.get("sha256") is not None:
            raise ValueError(f"candidate {fixture_id} must not include sha256 before download")
        if not item.get("expected_signals"):
            raise ValueError(f"candidate {fixture_id} must include expected_signals")
        if not item.get("known_risks"):
            raise ValueError(f"candidate {fixture_id} must include known_risks")

    boundary_notes = payload.get("boundary_notes", [])
    for note in [
        "candidate metadata only",
        "no external PDF binaries committed",
        "not robust PDF extraction evidence",
    ]:
        if note not in boundary_notes:
            raise ValueError(f"licensed real-world fixture pack missing boundary note: {note}")


def _require_https(item: dict[str, Any], field: str, fixture_id: str) -> None:
    value = str(item.get(field) or "")
    if not value.startswith("https://"):
        raise ValueError(f"candidate {fixture_id} {field} must be https")


def _format_bool(value: bool) -> str:
    return "true" if value else "false"
