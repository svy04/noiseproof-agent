from __future__ import annotations

import base64
from typing import Any

from packages.ingestion.pdf_quality.fixture import PdfExtractionQualityFixture
from packages.ingestion.parsers.pdf import PdfParser
from packages.ingestion.types import ParseInput, ParseResult


PHASE_MARKER = "ocr_layout_image_fixture_adapter_runtime_pack_v0"
CLAIM_BOUNDARY = "ocr_layout_image_adapter_runtime_pack_only_not_robust_pdf_extraction"
REQUIRED_ADAPTER_FIXTURE_IDS = [
    "scanned_image_pdf",
    "image_heavy_pdf",
    "multi_column_layout_pdf",
    "no_extractable_text_pdf",
]

_ONE_PIXEL_PNG = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+/p9sAAAAASUVORK5CYII="
)


def build_ocr_layout_image_adapter_runtime_pack() -> dict[str, Any]:
    observations = {
        "scanned_image_pdf": _scanned_image_observation(),
        "image_heavy_pdf": _image_heavy_observation(),
        "multi_column_layout_pdf": _multi_column_layout_observation(),
        "no_extractable_text_pdf": _no_extractable_text_observation(),
    }
    return {
        "packet": PHASE_MARKER,
        "claim_boundary": CLAIM_BOUNDARY,
        "robust_pdf_extraction_claimed": False,
        "observations": observations,
        "boundary_notes": _boundary_notes(),
    }


def build_ocr_layout_image_adapter_runtime_pack_summary(
    fixture: PdfExtractionQualityFixture,
    pack: dict[str, Any],
) -> dict[str, Any]:
    _validate_pack(pack)
    observations = pack["observations"]
    per_fixture = {
        fixture_id: _summary_row(fixture_id, observations[fixture_id])
        for fixture_id in REQUIRED_ADAPTER_FIXTURE_IDS
    }
    return {
        "phase_marker": PHASE_MARKER,
        "fixture": fixture.packet,
        "fixture_count": len(fixture.fixtures),
        "adapter_runtime_observed_count": len(observations),
        "adapter_runtime_fixture_ids": REQUIRED_ADAPTER_FIXTURE_IDS,
        "per_fixture": per_fixture,
        "quality_gate_status": "blocked",
        "robust_pdf_extraction_claimed": False,
        "can_claim_robust_pdf_extraction": False,
        "claim_boundary": CLAIM_BOUNDARY,
        "next_evidence_needed": [
            "committed OCR/layout/image binary fixture provenance before treating this as reusable fixture evidence",
            "explicit opt-in OCR adapter runtime smoke before scanned-image text coverage claims",
            "image/chart interpretation adapter evidence before image-heavy truth claims",
            "reading-order and layout diagnostics before layout fidelity claims",
        ],
        "boundary_notes": _boundary_notes(),
    }


def build_ocr_layout_image_adapter_runtime_pack_report(
    summary: dict[str, Any],
) -> str:
    lines = [
        "# OCR Layout Image Fixture Adapter Runtime Pack",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report records synthetic runtime adapter observations for OCR, image-heavy, layout, and empty-text PDF roles.",
        "",
        "It is not robust PDF extraction evidence.",
        "",
        "## Aggregate",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| fixture_count | {summary['fixture_count']} |",
        f"| adapter_runtime_observed_count | {summary['adapter_runtime_observed_count']} |",
        f"| robust_pdf_extraction_claimed | {_format_bool(summary['robust_pdf_extraction_claimed'])} |",
        f"| can_claim_robust_pdf_extraction | {_format_bool(summary['can_claim_robust_pdf_extraction'])} |",
        "",
        "## Adapter Runtime Roles",
        "",
        "| Fixture | Parser | Adapter boundary | Limitation codes | Failure candidate |",
        "|---|---|---|---|---|",
    ]
    for fixture_id in summary["adapter_runtime_fixture_ids"]:
        row = summary["per_fixture"][fixture_id]
        lines.append(
            "| "
            + " | ".join(
                [
                    fixture_id,
                    row["parser"],
                    row["adapter_boundary"],
                    _format_list(row["limitation_codes"]),
                    row["failure_case_candidate"] or "none",
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
            "This is a synthetic adapter runtime pack only.",
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


def _scanned_image_observation() -> dict[str, Any]:
    result = _parse_pdf_bytes(_build_image_only_pdf())
    return _observation_from_parse_result(
        "scanned_image_pdf",
        result,
        extra_warnings=[
            "OCR adapter is not implemented; OCR is required before scanned-image text coverage can be claimed.",
        ],
        extra_fields={
            "adapter_boundary": "ocr_adapter_not_implemented",
            "ocr_performed": False,
            "ocr_page_count": 0,
        },
    )


def _image_heavy_observation() -> dict[str, Any]:
    result = _parse_pdf_bytes(_build_image_heavy_pdf())
    image_block_count = _non_negative_int(result.metadata.get("image_block_count"))
    return _observation_from_parse_result(
        "image_heavy_pdf",
        result,
        extra_warnings=[
            "image/chart interpretation is not claimed; image blocks are diagnostics only.",
        ],
        extra_fields={
            "adapter_boundary": "image_diagnostics_only",
            "image_block_diagnostics_available": image_block_count > 0,
            "image_block_count": image_block_count,
            "image_chart_interpretation_claimed": False,
        },
    )


def _multi_column_layout_observation() -> dict[str, Any]:
    result = _parse_pdf_bytes(_build_multi_column_pdf())
    return _observation_from_parse_result(
        "multi_column_layout_pdf",
        result,
        extra_warnings=[
            "layout fidelity is not claimed; text block diagnostics do not prove reading order.",
        ],
        extra_fields={
            "adapter_boundary": "layout_diagnostics_only",
            "layout_block_diagnostics_available": bool(
                result.metadata.get("layout_block_diagnostics_available")
            ),
            "text_block_count": _non_negative_int(result.metadata.get("text_block_count")),
            "layout_fidelity_claimed": False,
        },
    )


def _no_extractable_text_observation() -> dict[str, Any]:
    result = _parse_pdf_bytes(_build_blank_pdf())
    return _observation_from_parse_result(
        "no_extractable_text_pdf",
        result,
        extra_warnings=["no digital text was extracted"],
        extra_fields={
            "adapter_boundary": "empty_text_failure_boundary",
        },
    )


def _observation_from_parse_result(
    fixture_id: str,
    result: ParseResult,
    *,
    extra_warnings: list[str],
    extra_fields: dict[str, Any],
) -> dict[str, Any]:
    failure = result.failure_case_candidate
    warnings = _dedupe([*result.warnings, *extra_warnings])
    metadata = result.metadata
    return {
        "adapter_runtime_observed": True,
        "observation_source": f"synthetic_{fixture_id}_pdf_parse_result",
        "truth_scope": "synthetic_adapter_runtime_boundary_observation",
        "parser": result.parser,
        "extracted_text": result.text,
        "warnings": warnings,
        "page_count": _positive_int(metadata.get("page_count")),
        "extracted_page_count": _non_negative_int(metadata.get("extracted_page_count")),
        "empty_page_count": _non_negative_int(metadata.get("empty_page_count")),
        "digital_pdf_text_extraction": bool(metadata.get("digital_pdf_text_extraction")),
        "robust_pdf_extraction": bool(metadata.get("robust_pdf_extraction")),
        "failure_case_candidate": failure.failure_type if failure else None,
        **extra_fields,
    }


def _parse_pdf_bytes(content: bytes) -> ParseResult:
    return PdfParser().parse(ParseInput(source_type="pdf", content_bytes=content))


def _build_blank_pdf() -> bytes:
    import pymupdf

    document = pymupdf.open()
    document.new_page(width=260, height=160)
    try:
        return document.tobytes()
    finally:
        document.close()


def _build_image_only_pdf() -> bytes:
    import pymupdf

    document = pymupdf.open()
    page = document.new_page(width=260, height=160)
    page.insert_image(pymupdf.Rect(70, 40, 190, 120), stream=_ONE_PIXEL_PNG)
    try:
        return document.tobytes()
    finally:
        document.close()


def _build_image_heavy_pdf() -> bytes:
    import pymupdf

    document = pymupdf.open()
    page = document.new_page(width=320, height=220)
    page.insert_text((40, 50), "chart title text")
    page.insert_image(pymupdf.Rect(40, 70, 180, 170), stream=_ONE_PIXEL_PNG)
    page.insert_text((40, 195), "caption text")
    try:
        return document.tobytes()
    finally:
        document.close()


def _build_multi_column_pdf() -> bytes:
    import pymupdf

    document = pymupdf.open()
    page = document.new_page(width=420, height=240)
    page.insert_textbox(
        pymupdf.Rect(40, 50, 190, 170),
        "left column claim\nmarket demand increased",
    )
    page.insert_textbox(
        pymupdf.Rect(230, 50, 380, 170),
        "right column limitation\nsample is synthetic",
    )
    try:
        return document.tobytes()
    finally:
        document.close()


def _validate_pack(pack: dict[str, Any]) -> None:
    if pack.get("packet") != PHASE_MARKER:
        raise ValueError("Unexpected OCR/layout/image adapter packet.")
    if pack.get("claim_boundary") != CLAIM_BOUNDARY:
        raise ValueError("OCR/layout/image adapter packet has wrong claim boundary.")
    if pack.get("robust_pdf_extraction_claimed") is not False:
        raise ValueError("OCR/layout/image adapter packet must not claim robust extraction.")
    observations = pack.get("observations")
    if not isinstance(observations, dict):
        raise ValueError("OCR/layout/image adapter observations must be an object.")
    if set(observations) != set(REQUIRED_ADAPTER_FIXTURE_IDS):
        raise ValueError("OCR/layout/image adapter packet must include exactly required roles.")


def _summary_row(fixture_id: str, observation: dict[str, Any]) -> dict[str, Any]:
    return {
        "fixture_id": fixture_id,
        "parser": str(observation["parser"]),
        "adapter_boundary": str(observation["adapter_boundary"]),
        "failure_case_candidate": observation.get("failure_case_candidate"),
        "limitation_codes": _limitation_codes(fixture_id, observation),
    }


def _limitation_codes(fixture_id: str, observation: dict[str, Any]) -> list[str]:
    by_fixture = {
        "scanned_image_pdf": ["ocr_adapter_not_implemented"],
        "image_heavy_pdf": ["image_chart_interpretation_not_claimed"],
        "multi_column_layout_pdf": ["layout_fidelity_not_claimed"],
        "no_extractable_text_pdf": ["empty_text_failure_boundary_only"],
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


def _dedupe(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result


def _format_bool(value: Any) -> str:
    return "true" if value else "false"


def _format_list(value: list[str]) -> str:
    return ", ".join(value) if value else "none"
