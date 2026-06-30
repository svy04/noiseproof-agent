from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PHASE_MARKER = "real_world_layout_fidelity_evidence_gate_v0"
PREVIOUS_GATE = "real_world_ocr_evidence_gate_v0"
CLAIM_BOUNDARY = "real_world_layout_fidelity_evidence_not_robust_pdf_extraction"
LAYOUT_ADAPTER = "pymupdf_get_text_blocks_dict_sort"
NEXT_GATE = "robust_pdf_extraction_generalization_gap_review_v0"

_FORBIDDEN_FIELDS = {
    "text_sample",
    "raw_text",
    "raw_extracted_text",
    "raw_block_text",
    "page_image",
    "screenshot",
    "rendered_page_image",
}


def load_real_world_layout_fidelity_evidence(path: Path | str) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    _validate_evidence(payload)
    return payload


def build_real_world_layout_fidelity_evidence_summary(
    evidence: dict[str, Any],
) -> dict[str, Any]:
    _validate_evidence(evidence)
    observations = list(evidence["observations"])
    publishers = sorted({str(item.get("publisher") or "") for item in observations})
    publishers = [publisher for publisher in publishers if publisher]
    fixture_ids = [str(item["fixture_id"]) for item in observations]
    layout_observed = [
        item for item in observations if item.get("layout_metadata_observed") is True
    ]
    has_layout_evidence = len(layout_observed) == len(observations)

    passed_checks = []
    if has_layout_evidence:
        passed_checks.append("real_world_layout_metadata_observed")
    if all(
        item["text_blocks_with_bbox_in_page_bounds"] == item["text_block_count"]
        for item in observations
    ):
        passed_checks.append("bbox_page_bounds_sanity_observed")
    if all(item.get("expected_marker_order_observed") is True for item in observations):
        passed_checks.append("expected_marker_order_sanity_observed")
    if all(item.get("license_source_url") for item in observations):
        passed_checks.append("source_policy_visible")
    if all(len(str(item.get("source_sha256") or "")) == 64 for item in observations):
        passed_checks.append("sha256_visible")
    if evidence.get("raw_block_text_committed") is False:
        passed_checks.append("raw_block_text_not_committed")
    if evidence.get("page_image_committed") is False:
        passed_checks.append("page_images_not_committed")

    blocked_reasons = []
    if not has_layout_evidence:
        blocked_reasons.append("layout_fidelity_evidence_missing")
    blocked_reasons.extend(
        [
            "robust_pdf_generalization_missing",
            "arbitrary_market_pdf_coverage_missing",
        ]
    )

    return {
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "layout_gate_status": "passed" if has_layout_evidence else "blocked",
        "observed_fixture_count": len(observations),
        "layout_observed_fixture_count": len(layout_observed),
        "fixture_ids": fixture_ids,
        "publishers": publishers,
        "total_page_count": sum(item["page_count"] for item in observations),
        "observed_page_count": sum(item["observed_page_count"] for item in observations),
        "total_block_count": sum(item["block_count"] for item in observations),
        "total_text_block_count": sum(item["text_block_count"] for item in observations),
        "total_image_block_count": sum(item["image_block_count"] for item in observations),
        "total_text_blocks_with_bbox_in_page_bounds": sum(
            item["text_blocks_with_bbox_in_page_bounds"] for item in observations
        ),
        "expected_markers_found_count": sum(
            item["expected_markers_found_count"] for item in observations
        ),
        "expected_marker_order_observed": all(
            item["expected_marker_order_observed"] for item in observations
        ),
        "has_real_world_layout_fidelity_evidence": has_layout_evidence,
        "can_claim_real_world_layout_fidelity_evidence": has_layout_evidence,
        "can_claim_robust_pdf_extraction": False,
        "blocked_reasons": blocked_reasons,
        "passed_checks": passed_checks,
        "observations": observations,
        "warnings": evidence["warnings"],
        "boundary_notes": evidence["boundary_notes"],
        "next_gate": NEXT_GATE,
    }


def build_real_world_layout_fidelity_evidence_report(
    summary: dict[str, Any],
) -> str:
    lines = [
        "# Real-world Layout Fidelity Evidence Gate",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report records sanitized PyMuPDF block and bbox metadata for one temporary owner-runtime BEA PDF download.",
        "",
        "It is real-world layout metadata sanity evidence, not robust PDF extraction evidence.",
        "",
        "raw text is not committed.",
        "",
        "## Gate Result",
        "",
        f"layout_gate_status -> {summary['layout_gate_status']}",
        f"previous_gate -> {summary['previous_gate']}",
        f"observed_fixture_count -> {summary['observed_fixture_count']}",
        f"layout_observed_fixture_count -> {summary['layout_observed_fixture_count']}",
        f"total_page_count -> {summary['total_page_count']}",
        f"observed_page_count -> {summary['observed_page_count']}",
        f"total_block_count -> {summary['total_block_count']}",
        f"total_text_block_count -> {summary['total_text_block_count']}",
        f"total_image_block_count -> {summary['total_image_block_count']}",
        f"total_text_blocks_with_bbox_in_page_bounds -> {summary['total_text_blocks_with_bbox_in_page_bounds']}",
        f"expected_markers_found_count -> {summary['expected_markers_found_count']}",
        f"expected_marker_order_observed -> {_format_bool(summary['expected_marker_order_observed'])}",
        f"has_real_world_layout_fidelity_evidence -> {_format_bool(summary['has_real_world_layout_fidelity_evidence'])}",
        f"can_claim_real_world_layout_fidelity_evidence -> {_format_bool(summary['can_claim_real_world_layout_fidelity_evidence'])}",
        f"can_claim_robust_pdf_extraction -> {_format_bool(summary['can_claim_robust_pdf_extraction'])}",
        "",
        "## Publishers",
        "",
    ]
    for publisher in summary["publishers"]:
        lines.append(f"- {publisher}")

    lines.extend(
        [
            "",
            "## Fixtures",
            "",
            "| Fixture | Publisher | Pages | Observed pages | Blocks | Text blocks | BBox-in-bounds | Marker hits | SHA-256 |",
            "|---|---|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for item in summary["observations"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    item["fixture_id"],
                    item["publisher"],
                    str(item["page_count"]),
                    str(item["observed_page_count"]),
                    str(item["block_count"]),
                    str(item["text_block_count"]),
                    str(item["text_blocks_with_bbox_in_page_bounds"]),
                    str(item["expected_markers_found_count"]),
                    item["source_sha256"],
                ]
            )
            + " |"
        )

    lines.extend(["", "## Passed Checks", ""])
    for check in summary["passed_checks"]:
        lines.append(f"- {check}")

    lines.extend(["", "## Remaining Blocked Reasons", ""])
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
            "This is a deterministic report over one sanitized owner-runtime layout metadata observation.",
            "",
            "It does not commit external PDF binaries, download caches, local paths, raw extracted text, raw block text, screenshots, or rendered page images.",
            "",
            "It does not prove robust PDF extraction, arbitrary-market PDF parsing reliability, arbitrary-market layout fidelity, natural reading order correctness, or rendered visual fidelity.",
            "",
            "This is not hosted deployment evidence.",
            "",
            "This is not external reviewer feedback.",
            "",
            "This is not product-complete.",
        ]
    )
    return "\n".join(lines) + "\n"


def _validate_evidence(payload: dict[str, Any]) -> None:
    expected_values = {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "layout_adapter": LAYOUT_ADAPTER,
        "layout_metadata_observed": True,
        "layout_fidelity_evidence": True,
        "robust_pdf_extraction_claimed": False,
        "can_claim_robust_pdf_extraction": False,
        "binary_files_committed": False,
        "download_cache_committed": False,
        "raw_extracted_text_committed": False,
        "raw_block_text_committed": False,
        "page_image_committed": False,
        "screenshot_committed": False,
        "local_pdf_path_committed": False,
        "recommended_next_gate": NEXT_GATE,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(
                f"real-world layout fidelity evidence {field} must be {expected!r}"
            )

    observations = payload.get("observations")
    if not isinstance(observations, list) or len(observations) != 1:
        raise ValueError(
            "real-world layout fidelity evidence must include exactly 1 observation"
        )

    seen_ids: set[str] = set()
    for item in observations:
        _validate_observation(item, seen_ids)

    for field in ["warnings", "boundary_notes"]:
        value = payload.get(field)
        if not isinstance(value, list) or not value:
            raise ValueError(
                f"real-world layout fidelity evidence {field} must be a non-empty list"
            )

    for note in [
        "real-world layout fidelity evidence",
        "no external PDF binaries committed",
        "no raw block text committed",
        "not robust PDF extraction evidence",
        "not arbitrary-market layout fidelity evidence",
        "not natural reading order correctness evidence",
    ]:
        if note not in payload["boundary_notes"]:
            raise ValueError(
                f"real-world layout fidelity evidence missing note: {note}"
            )


def _validate_observation(item: dict[str, Any], seen_ids: set[str]) -> None:
    if not isinstance(item, dict):
        raise ValueError("layout observations must be objects")
    fixture_id = str(item.get("fixture_id") or "")
    if not fixture_id:
        raise ValueError("layout observation missing fixture_id")
    if fixture_id in seen_ids:
        raise ValueError(f"duplicate fixture_id: {fixture_id}")
    seen_ids.add(fixture_id)

    for field in _FORBIDDEN_FIELDS:
        if field in item:
            raise ValueError(f"observation {fixture_id} must not commit {field}")

    expected_values = {
        "source_sha256_algorithm": "sha256",
        "pdf_magic_header": True,
        "parser": "pdf-pymupdf",
        "layout_adapter": LAYOUT_ADAPTER,
        "layout_metadata_observed": True,
        "layout_fidelity_evidence": True,
        "raw_text_committed": False,
        "raw_extracted_text_committed": False,
        "raw_block_text_committed": False,
        "page_image_committed": False,
        "screenshot_committed": False,
        "binary_committed": False,
        "local_pdf_path": None,
        "failure_case_candidate": None,
    }
    for field, expected in expected_values.items():
        if item.get(field) != expected:
            raise ValueError(f"observation {fixture_id} {field} must be {expected!r}")

    for field in [
        "http_status",
        "byte_size",
        "page_count",
        "observed_page_count",
        "block_count",
        "dict_block_count",
        "text_block_count",
        "text_blocks_with_bbox_in_page_bounds",
        "expected_markers_found_count",
        "sorted_text_char_count",
        "unsorted_text_char_count",
    ]:
        value = item.get(field)
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"observation {fixture_id} {field} must be positive")

    for field in ["observed_page_index", "image_block_count"]:
        value = item.get(field)
        if not isinstance(value, int) or value < 0:
            raise ValueError(f"observation {fixture_id} {field} must be non-negative")

    if item["observed_page_count"] > item["page_count"]:
        raise ValueError(
            f"observation {fixture_id} observed_page_count cannot exceed page_count"
        )
    if item["text_blocks_with_bbox_in_page_bounds"] != item["text_block_count"]:
        raise ValueError(
            f"observation {fixture_id} all text block bboxes must be inside page bounds"
        )

    for field in ["page_width", "page_height"]:
        value = item.get(field)
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f"observation {fixture_id} {field} must be positive")

    if len(str(item.get("source_sha256") or "")) != 64:
        raise ValueError(f"observation {fixture_id} must include a SHA-256 digest")
    for field in ["source_url", "license_source_url"]:
        if not item.get(field):
            raise ValueError(f"observation {fixture_id} must include {field}")

    terms = item.get("expected_layout_markers_checked")
    hits = item.get("expected_marker_hits")
    if not isinstance(terms, list) or not terms:
        raise ValueError(f"observation {fixture_id} must include expected markers")
    if not isinstance(hits, dict):
        raise ValueError(f"observation {fixture_id} must include expected marker hits")
    if set(terms) != set(hits):
        raise ValueError(f"observation {fixture_id} expected marker hits must match terms")
    found_count = sum(1 for term in terms if hits.get(term) is True)
    if item["expected_markers_found_count"] != found_count:
        raise ValueError(
            f"observation {fixture_id} expected_markers_found_count must match hits"
        )
    if item.get("expected_marker_order_observed") is not True:
        raise ValueError(
            f"observation {fixture_id} expected_marker_order_observed must be true"
        )

    bboxes = item.get("sample_text_block_bboxes")
    if not isinstance(bboxes, list) or not bboxes:
        raise ValueError(f"observation {fixture_id} must include bbox samples")
    for bbox in bboxes:
        _validate_bbox_sample(fixture_id, bbox, item["page_width"], item["page_height"])

    if not item.get("warnings"):
        raise ValueError(f"observation {fixture_id} must include warnings")


def _validate_bbox_sample(
    fixture_id: str,
    bbox: dict[str, Any],
    page_width: float,
    page_height: float,
) -> None:
    if not isinstance(bbox, dict):
        raise ValueError(f"observation {fixture_id} bbox sample must be an object")
    block_index = bbox.get("block_index")
    if not isinstance(block_index, int) or block_index < 0:
        raise ValueError(f"observation {fixture_id} bbox block_index must be non-negative")
    for field in ["x0", "y0", "x1", "y1"]:
        value = bbox.get(field)
        if not isinstance(value, (int, float)):
            raise ValueError(f"observation {fixture_id} bbox {field} must be numeric")
    if not (0 <= bbox["x0"] <= bbox["x1"] <= page_width):
        raise ValueError(f"observation {fixture_id} bbox x coordinates out of bounds")
    if not (0 <= bbox["y0"] <= bbox["y1"] <= page_height):
        raise ValueError(f"observation {fixture_id} bbox y coordinates out of bounds")
    if bbox.get("in_page_bounds") is not True:
        raise ValueError(f"observation {fixture_id} bbox must be in page bounds")


def _format_bool(value: bool) -> str:
    return "true" if value else "false"
