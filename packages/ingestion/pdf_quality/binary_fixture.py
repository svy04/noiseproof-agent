import hashlib
import json
from pathlib import Path
from typing import Any


PDF_BINARY_FIXTURE_CLAIM_BOUNDARY = (
    "synthetic_binary_fixture_provenance_only_not_robust_pdf_extraction"
)


def load_pdf_binary_fixture_provenance(path: Path | str) -> dict[str, Any]:
    root = Path(path)
    packet_path = root / "provenance.json"
    payload = json.loads(packet_path.read_text(encoding="utf-8"))
    _validate_packet(root, payload)
    return payload


def _validate_packet(root: Path, payload: dict[str, Any]) -> None:
    if payload.get("packet") != "pdf_binary_fixture_provenance_packet_v0":
        raise ValueError("Unexpected PDF binary fixture provenance packet.")
    if payload.get("claim_boundary") != PDF_BINARY_FIXTURE_CLAIM_BOUNDARY:
        raise ValueError("PDF binary fixture provenance packet has wrong boundary.")
    if payload.get("robust_pdf_extraction_claimed") is not False:
        raise ValueError("Binary fixture packet must not claim robust PDF extraction.")
    if payload.get("binary_pdf_fixtures_included") is not True:
        raise ValueError("Binary fixture packet must declare included binary fixtures.")

    fixtures = payload.get("fixtures")
    if not isinstance(fixtures, list) or not fixtures:
        raise ValueError("Binary fixture packet must include fixtures.")

    fixture_ids: set[str] = set()
    for item in fixtures:
        if not isinstance(item, dict):
            raise ValueError("Binary fixture entries must be objects.")
        fixture_id = str(item.get("fixture_id") or "")
        if not fixture_id:
            raise ValueError("Binary fixture entry is missing fixture_id.")
        if fixture_id in fixture_ids:
            raise ValueError(f"Duplicate binary fixture id: {fixture_id}")
        fixture_ids.add(fixture_id)

        if item.get("source_kind") != "synthetic_generated":
            raise ValueError(f"Binary fixture {fixture_id} must be synthetic_generated.")
        if item.get("redistribution_allowed") is not True:
            raise ValueError(
                f"Binary fixture {fixture_id} must be redistributable in-repo."
            )
        if item.get("robust_pdf_extraction_claimed") is not False:
            raise ValueError(
                f"Binary fixture {fixture_id} must not claim robust PDF extraction."
            )

        relative_path = Path(str(item.get("path") or ""))
        if relative_path.is_absolute() or ".." in relative_path.parts:
            raise ValueError(f"Binary fixture {fixture_id} has unsafe path.")
        file_path = root / relative_path
        if not file_path.is_file():
            raise ValueError(f"Binary fixture file is missing: {relative_path}")

        content = file_path.read_bytes()
        sha256 = hashlib.sha256(content).hexdigest()
        if item.get("sha256") != sha256:
            raise ValueError(f"Binary fixture {fixture_id} sha256 mismatch.")
        if item.get("size_bytes") != len(content):
            raise ValueError(f"Binary fixture {fixture_id} size_bytes mismatch.")
        if not str(relative_path).lower().endswith(".pdf"):
            raise ValueError(f"Binary fixture {fixture_id} must point to a PDF.")

    boundary_notes = payload.get("boundary_notes", [])
    if "not robust PDF extraction evidence" not in boundary_notes:
        raise ValueError("Binary fixture packet must preserve robust-extraction boundary.")
