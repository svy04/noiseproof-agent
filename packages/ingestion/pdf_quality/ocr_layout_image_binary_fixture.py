from __future__ import annotations

import contextlib
import hashlib
import io
import json
from pathlib import Path
from typing import Any

from packages.ingestion.parsers.pdf import PdfParser
from packages.ingestion.types import ParseInput


PHASE_MARKER = "committed_ocr_layout_image_binary_fixture_provenance_v0"
CLAIM_BOUNDARY = (
    "committed_ocr_layout_image_binary_fixture_provenance_only_not_robust_pdf_extraction"
)
PACKET_FILENAME = "ocr-layout-image-provenance.json"
REQUIRED_OCR_LAYOUT_IMAGE_BINARY_FIXTURE_IDS = [
    "scanned_image_pdf",
    "image_heavy_pdf",
    "multi_column_layout_pdf",
    "no_extractable_text_pdf",
]


def load_ocr_layout_image_binary_fixture_provenance(
    path: Path | str,
) -> dict[str, Any]:
    root = Path(path)
    payload = json.loads((root / PACKET_FILENAME).read_text(encoding="utf-8"))
    _validate_packet(root, payload)
    return payload


def build_committed_ocr_layout_image_binary_fixture_provenance_summary(
    root: Path | str,
    packet: dict[str, Any],
) -> dict[str, Any]:
    fixture_root = Path(root)
    _validate_packet(fixture_root, packet)
    per_fixture = {
        str(item["fixture_id"]): _observe_fixture(fixture_root, item)
        for item in packet["fixtures"]
    }
    return {
        "phase_marker": PHASE_MARKER,
        "packet": packet["packet"],
        "committed_fixture_count": len(packet["fixtures"]),
        "parser_observed_fixture_count": len(per_fixture),
        "committed_fixture_ids": REQUIRED_OCR_LAYOUT_IMAGE_BINARY_FIXTURE_IDS,
        "per_fixture": per_fixture,
        "quality_gate_status": "blocked",
        "robust_pdf_extraction_claimed": False,
        "can_claim_robust_pdf_extraction": False,
        "claim_boundary": CLAIM_BOUNDARY,
        "next_evidence_needed": [
            "explicit opt-in OCR adapter runtime smoke before scanned-image text coverage claims",
            "image/chart interpretation adapter evidence before image-heavy truth claims",
            "reading-order and layout diagnostics before layout fidelity claims",
            "real-world PDF fixture license and redistribution review before external PDF evidence",
        ],
        "boundary_notes": _boundary_notes(),
    }


def build_committed_ocr_layout_image_binary_fixture_provenance_report(
    summary: dict[str, Any],
) -> str:
    lines = [
        "# Committed OCR Layout Image Binary Fixture Provenance",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report records committed synthetic binary PDF fixtures for OCR, image-heavy, layout, and empty-text roles.",
        "",
        "It is not robust PDF extraction evidence.",
        "",
        "## Aggregate",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| committed_fixture_count | {summary['committed_fixture_count']} |",
        f"| parser_observed_fixture_count | {summary['parser_observed_fixture_count']} |",
        f"| robust_pdf_extraction_claimed | {_format_bool(summary['robust_pdf_extraction_claimed'])} |",
        f"| can_claim_robust_pdf_extraction | {_format_bool(summary['can_claim_robust_pdf_extraction'])} |",
        "",
        "## Per-fixture Provenance",
        "",
        "| Fixture | Path | Parser | Boundary | Failure candidate | Expected spans found |",
        "|---|---|---|---|---|---:|",
    ]
    for fixture_id in summary["committed_fixture_ids"]:
        row = summary["per_fixture"][fixture_id]
        lines.append(
            "| "
            + " | ".join(
                [
                    fixture_id,
                    row["path"],
                    row["parser"],
                    row["adapter_boundary"],
                    row["failure_case_candidate"] or "none",
                    _format_bool(row["expected_spans_found"]),
                ]
            )
            + " |"
        )

    lines.extend(["", "## Next Evidence Needed", ""])
    for item in summary["next_evidence_needed"]:
        lines.append(f"- {item}")

    lines.extend(["", "## Boundary Notes", ""])
    for note in summary["boundary_notes"]:
        lines.append(f"- {note}")

    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "This is committed synthetic binary fixture provenance only.",
            "",
            "This is not robust PDF extraction implementation.",
            "",
            "This is not OCR implementation.",
            "",
            "This is not image/chart interpretation evidence.",
            "",
            "This is not layout fidelity evidence.",
            "",
            "This is not hosted deployment evidence.",
            "",
            "This is not product-complete.",
        ]
    )
    return "\n".join(lines) + "\n"


def _observe_fixture(root: Path, item: dict[str, Any]) -> dict[str, Any]:
    fixture_id = str(item["fixture_id"])
    content = (root / str(item["path"])).read_bytes()
    with contextlib.redirect_stdout(io.StringIO()):
        parse_result = PdfParser().parse(
            ParseInput(
                source_type="pdf",
                content_bytes=content,
                filename=str(item["path"]),
            )
        )
    metadata = parse_result.metadata
    failure = parse_result.failure_case_candidate
    failure_type = failure.failure_type if failure else None
    expected_failure = item.get("expected_failure_case")
    expected_spans = [str(span) for span in item.get("expected_spans", [])]
    expected_spans_found = _expected_spans_found(parse_result.text, expected_spans)
    expected_failure_case_observed = (
        True if not expected_failure else failure_type == expected_failure
    )
    image_block_count = _non_negative_int(metadata.get("image_block_count"))
    text_block_count = _non_negative_int(metadata.get("text_block_count"))
    return {
        "fixture_id": fixture_id,
        "path": str(item["path"]),
        "sha256": str(item["sha256"]),
        "size_bytes": int(item["size_bytes"]),
        "parser": parse_result.parser,
        "extracted_text": parse_result.text,
        "digital_pdf_text_extraction": bool(metadata.get("digital_pdf_text_extraction")),
        "robust_pdf_extraction": bool(metadata.get("robust_pdf_extraction")),
        "page_count": _positive_int(metadata.get("page_count")),
        "extracted_page_count": _non_negative_int(metadata.get("extracted_page_count")),
        "empty_page_count": _non_negative_int(metadata.get("empty_page_count")),
        "image_block_count": image_block_count,
        "text_block_count": text_block_count,
        "ocr_performed": False,
        "image_chart_interpretation_claimed": False,
        "layout_fidelity_claimed": False,
        "adapter_boundary": _adapter_boundary(fixture_id),
        "expected_spans_found": expected_spans_found,
        "expected_failure_case_observed": expected_failure_case_observed,
        "failure_case_candidate": failure_type,
        "warnings": list(parse_result.warnings),
        "passed_boundary_check": (
            bool(metadata.get("robust_pdf_extraction")) is False
            and expected_spans_found
            and expected_failure_case_observed
            and image_block_count >= _non_negative_int(item.get("expected_min_image_blocks"))
            and text_block_count >= _non_negative_int(item.get("expected_min_text_blocks"))
        ),
    }


def _validate_packet(root: Path, payload: dict[str, Any]) -> None:
    if payload.get("packet") != PHASE_MARKER:
        raise ValueError("Unexpected OCR/layout/image binary fixture packet.")
    if payload.get("claim_boundary") != CLAIM_BOUNDARY:
        raise ValueError("OCR/layout/image binary fixture packet has wrong boundary.")
    if payload.get("binary_pdf_fixtures_included") is not True:
        raise ValueError("OCR/layout/image binary fixture packet must include binaries.")
    if payload.get("robust_pdf_extraction_claimed") is not False:
        raise ValueError("OCR/layout/image binary fixture packet must not claim robust extraction.")
    fixtures = payload.get("fixtures")
    if not isinstance(fixtures, list):
        raise ValueError("OCR/layout/image binary fixture packet fixtures must be a list.")
    if [item.get("fixture_id") for item in fixtures] != REQUIRED_OCR_LAYOUT_IMAGE_BINARY_FIXTURE_IDS:
        raise ValueError("OCR/layout/image binary fixture packet has wrong fixture order.")
    for item in fixtures:
        _validate_fixture_entry(root, item)
    for note in _boundary_notes():
        if note not in payload.get("boundary_notes", []):
            raise ValueError(f"OCR/layout/image binary fixture packet missing boundary note: {note}")


def _validate_fixture_entry(root: Path, item: Any) -> None:
    if not isinstance(item, dict):
        raise ValueError("OCR/layout/image binary fixture entries must be objects.")
    fixture_id = str(item.get("fixture_id") or "")
    if item.get("source_kind") != "synthetic_generated":
        raise ValueError(f"Fixture {fixture_id} must be synthetic_generated.")
    if item.get("redistribution_allowed") is not True:
        raise ValueError(f"Fixture {fixture_id} must be redistributable in repo.")
    if item.get("robust_pdf_extraction_claimed") is not False:
        raise ValueError(f"Fixture {fixture_id} must not claim robust extraction.")
    relative_path = Path(str(item.get("path") or ""))
    if relative_path.is_absolute() or ".." in relative_path.parts:
        raise ValueError(f"Fixture {fixture_id} has unsafe path.")
    if not str(relative_path).lower().endswith(".pdf"):
        raise ValueError(f"Fixture {fixture_id} must point to a PDF.")
    content = (root / relative_path).read_bytes()
    if hashlib.sha256(content).hexdigest() != item.get("sha256"):
        raise ValueError(f"Fixture {fixture_id} sha256 mismatch.")
    if len(content) != item.get("size_bytes"):
        raise ValueError(f"Fixture {fixture_id} size_bytes mismatch.")


def _adapter_boundary(fixture_id: str) -> str:
    by_fixture = {
        "scanned_image_pdf": "ocr_adapter_not_implemented",
        "image_heavy_pdf": "image_diagnostics_only",
        "multi_column_layout_pdf": "layout_diagnostics_only",
        "no_extractable_text_pdf": "empty_text_failure_boundary",
    }
    return by_fixture[fixture_id]


def _boundary_notes() -> list[str]:
    return [
        "not robust PDF extraction evidence",
        "not OCR evidence",
        "not image/chart interpretation evidence",
        "not layout fidelity evidence",
        "not hosted deployment evidence",
        "not product-complete",
    ]


def _expected_spans_found(text: str, expected_spans: list[str]) -> bool:
    if not expected_spans:
        return True
    normalized = _normalize_text(text)
    return all(_normalize_text(span) in normalized for span in expected_spans)


def _normalize_text(value: object) -> str:
    return " ".join(str(value).lower().split())


def _positive_int(value: Any) -> int:
    if isinstance(value, bool):
        return 1
    if isinstance(value, int) and value > 0:
        return value
    return 1


def _non_negative_int(value: Any) -> int:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return max(value, 0)
    return 0


def _format_bool(value: Any) -> str:
    return "true" if value else "false"
