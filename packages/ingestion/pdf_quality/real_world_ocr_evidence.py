from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PHASE_MARKER = "real_world_ocr_evidence_gate_v0"
PREVIOUS_GATE = "real_world_table_extraction_evidence_gate_v0"
CLAIM_BOUNDARY = "real_world_ocr_evidence_not_robust_pdf_extraction"
OCR_ENGINE = "pymupdf_get_textpage_ocr"
NEXT_GATE = "real_world_layout_fidelity_evidence_gate_v0"

_RAW_TEXT_FIELDS = {
    "recognized_text",
    "ocr_sample",
    "raw_text",
    "raw_extracted_text",
    "raw_ocr_text",
}


def load_real_world_ocr_evidence(path: Path | str) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    _validate_evidence(payload)
    return payload


def build_real_world_ocr_evidence_summary(evidence: dict[str, Any]) -> dict[str, Any]:
    _validate_evidence(evidence)
    observations = list(evidence["observations"])
    publishers = sorted({str(item.get("publisher") or "") for item in observations})
    publishers = [publisher for publisher in publishers if publisher]
    fixture_ids = [str(item["fixture_id"]) for item in observations]
    ocr_observed = [item for item in observations if item.get("ocr_performed") is True]
    has_real_world_ocr = len(ocr_observed) == len(observations)
    has_layout_fidelity = bool(evidence.get("layout_fidelity_evidence"))

    passed_checks = []
    if has_real_world_ocr:
        passed_checks.append("real_world_ocr_observed")
    if all(item.get("collection_page_url") for item in observations):
        passed_checks.append("collection_page_visible")
    if all(item.get("rights_source_url") for item in observations):
        passed_checks.append("source_policy_visible")
    if all(len(str(item.get("source_sha256") or "")) == 64 for item in observations):
        passed_checks.append("sha256_visible")
    if evidence.get("binary_files_committed") is False:
        passed_checks.append("external_binaries_not_committed")
    if evidence.get("raw_ocr_text_committed") is False:
        passed_checks.append("raw_ocr_text_not_committed")
    if evidence.get("tessdata_path_committed_to_repo") is False:
        passed_checks.append("tessdata_path_not_committed")

    blocked_reasons = []
    if not has_real_world_ocr:
        blocked_reasons.append("ocr_evidence_missing")
    if not has_layout_fidelity:
        blocked_reasons.append("layout_fidelity_evidence_missing")

    total_page_count = sum(item["page_count"] for item in observations)
    total_ocr_pages = sum(item["ocr_pages_attempted"] for item in observations)

    return {
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "ocr_gate_status": "passed" if has_real_world_ocr else "blocked",
        "observed_fixture_count": len(observations),
        "ocr_observed_fixture_count": len(ocr_observed),
        "fixture_ids": fixture_ids,
        "publishers": publishers,
        "total_page_count": total_page_count,
        "total_ocr_pages_attempted": total_ocr_pages,
        "total_native_text_char_count": sum(
            item["native_text_char_count"] for item in observations
        ),
        "total_ocr_text_char_count": sum(
            item["ocr_text_char_count"] for item in observations
        ),
        "ocr_page_coverage_ratio": total_ocr_pages / total_page_count,
        "expected_terms_found_count": sum(
            item["expected_terms_found_count"] for item in observations
        ),
        "has_real_world_ocr_evidence": has_real_world_ocr,
        "has_layout_fidelity_evidence": has_layout_fidelity,
        "can_claim_real_world_ocr_evidence": has_real_world_ocr,
        "can_claim_robust_pdf_extraction": False,
        "blocked_reasons": blocked_reasons,
        "passed_checks": passed_checks,
        "observations": observations,
        "warnings": evidence["warnings"],
        "boundary_notes": evidence["boundary_notes"],
        "next_gate": NEXT_GATE,
    }


def build_real_world_ocr_evidence_report(summary: dict[str, Any]) -> str:
    lines = [
        "# Real-world OCR Evidence Gate",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report records a sanitized PyMuPDF OCR observation for a temporary owner-runtime NARA PDF download.",
        "",
        "It is real-world OCR evidence, not robust PDF extraction evidence.",
        "",
        "raw OCR text is not committed.",
        "",
        "## Gate Result",
        "",
        f"ocr_gate_status -> {summary['ocr_gate_status']}",
        f"previous_gate -> {summary['previous_gate']}",
        f"observed_fixture_count -> {summary['observed_fixture_count']}",
        f"ocr_observed_fixture_count -> {summary['ocr_observed_fixture_count']}",
        f"total_page_count -> {summary['total_page_count']}",
        f"total_ocr_pages_attempted -> {summary['total_ocr_pages_attempted']}",
        f"total_native_text_char_count -> {summary['total_native_text_char_count']}",
        f"total_ocr_text_char_count -> {summary['total_ocr_text_char_count']}",
        f"ocr_page_coverage_ratio -> {summary['ocr_page_coverage_ratio']:.2f}",
        f"expected_terms_found_count -> {summary['expected_terms_found_count']}",
        f"has_real_world_ocr_evidence -> {_format_bool(summary['has_real_world_ocr_evidence'])}",
        f"has_layout_fidelity_evidence -> {_format_bool(summary['has_layout_fidelity_evidence'])}",
        f"can_claim_real_world_ocr_evidence -> {_format_bool(summary['can_claim_real_world_ocr_evidence'])}",
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
            "| Fixture | Publisher | Pages | OCR pages | Native chars | OCR chars | Expected terms | SHA-256 |",
            "|---|---|---:|---:|---:|---:|---:|---|",
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
                    str(item["ocr_pages_attempted"]),
                    str(item["native_text_char_count"]),
                    str(item["ocr_text_char_count"]),
                    str(item["expected_terms_found_count"]),
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
            "This is a deterministic report over one sanitized owner-runtime OCR observation.",
            "",
            "It does not commit external PDF binaries, download caches, local paths, tessdata paths, raw extracted text, or raw OCR text.",
            "",
            "It does not prove layout fidelity, arbitrary-market PDF OCR reliability, arbitrary-market PDF parsing reliability, or robust PDF extraction.",
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
        "ocr_engine": OCR_ENGINE,
        "ocr_performed": True,
        "ocr_calls_attempted": True,
        "layout_fidelity_evidence": False,
        "robust_pdf_extraction_claimed": False,
        "can_claim_robust_pdf_extraction": False,
        "binary_files_committed": False,
        "download_cache_committed": False,
        "raw_extracted_text_committed": False,
        "raw_ocr_text_committed": False,
        "tessdata_path_printed": False,
        "tessdata_path_committed_to_repo": False,
        "recommended_next_gate": NEXT_GATE,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(f"real-world OCR evidence {field} must be {expected!r}")

    observations = payload.get("observations")
    if not isinstance(observations, list) or len(observations) != 1:
        raise ValueError("real-world OCR evidence must include exactly 1 observation")

    seen_ids: set[str] = set()
    for item in observations:
        _validate_observation(item, seen_ids)

    for field in ["warnings", "boundary_notes"]:
        value = payload.get(field)
        if not isinstance(value, list) or not value:
            raise ValueError(f"real-world OCR evidence {field} must be a non-empty list")

    for note in [
        "real-world OCR evidence",
        "no external PDF binaries committed",
        "no raw OCR text committed",
        "not robust PDF extraction evidence",
        "not arbitrary-market PDF OCR evidence",
        "not layout fidelity evidence",
    ]:
        if note not in payload["boundary_notes"]:
            raise ValueError(f"real-world OCR evidence missing note: {note}")


def _validate_observation(item: dict[str, Any], seen_ids: set[str]) -> None:
    if not isinstance(item, dict):
        raise ValueError("OCR observations must be objects")
    fixture_id = str(item.get("fixture_id") or "")
    if not fixture_id:
        raise ValueError("OCR observation missing fixture_id")
    if fixture_id in seen_ids:
        raise ValueError(f"duplicate fixture_id: {fixture_id}")
    seen_ids.add(fixture_id)

    for field in _RAW_TEXT_FIELDS:
        if field in item:
            raise ValueError(f"observation {fixture_id} must not commit {field}")

    expected_values = {
        "source_sha256_algorithm": "sha256",
        "pdf_magic_header": True,
        "parser": "pdf-pymupdf",
        "ocr_engine": OCR_ENGINE,
        "ocr_performed": True,
        "ocr_calls_attempted": True,
        "recognized_text_committed": False,
        "raw_ocr_text_committed": False,
        "binary_committed": False,
        "local_pdf_path": None,
        "tessdata_path_printed": False,
        "tessdata_path_committed_to_repo": False,
        "failure_case_candidate": None,
    }
    for field, expected in expected_values.items():
        if item.get(field) != expected:
            raise ValueError(f"observation {fixture_id} {field} must be {expected!r}")

    for field in [
        "http_status",
        "byte_size",
        "page_count",
        "ocr_pages_attempted",
        "ocr_text_char_count",
        "expected_terms_found_count",
    ]:
        value = item.get(field)
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"observation {fixture_id} {field} must be positive")

    native_count = item.get("native_text_char_count")
    if not isinstance(native_count, int) or native_count < 0:
        raise ValueError(f"observation {fixture_id} native_text_char_count must be non-negative")
    if item["ocr_pages_attempted"] > item["page_count"]:
        raise ValueError(
            f"observation {fixture_id} ocr_pages_attempted cannot exceed page_count"
        )
    expected_ratio = item["ocr_pages_attempted"] / item["page_count"]
    if item.get("ocr_page_coverage_ratio") != expected_ratio:
        raise ValueError(
            f"observation {fixture_id} ocr_page_coverage_ratio must match page coverage"
        )

    if len(str(item.get("source_sha256") or "")) != 64:
        raise ValueError(f"observation {fixture_id} must include a SHA-256 digest")
    for field in ["source_url", "collection_page_url", "rights_source_url"]:
        if not item.get(field):
            raise ValueError(f"observation {fixture_id} must include {field}")

    terms = item.get("expected_terms_checked")
    hits = item.get("expected_term_hits")
    if not isinstance(terms, list) or not terms:
        raise ValueError(f"observation {fixture_id} must include expected terms")
    if not isinstance(hits, dict):
        raise ValueError(f"observation {fixture_id} must include expected term hits")
    if set(terms) != set(hits):
        raise ValueError(f"observation {fixture_id} expected term hits must match terms")
    found_count = sum(1 for term in terms if hits.get(term) is True)
    if item["expected_terms_found_count"] != found_count:
        raise ValueError(
            f"observation {fixture_id} expected_terms_found_count must match hits"
        )

    if not item.get("warnings"):
        raise ValueError(f"observation {fixture_id} must include warnings")


def _format_bool(value: bool) -> str:
    return "true" if value else "false"
