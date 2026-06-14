from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from packages.ingestion.pdf_quality.fixture import PdfExtractionQualityFixture


PHASE_MARKER = "multi_fixture_ocr_adapter_eval_v0"
OWNER_OCR_OBSERVATION_PACKET = "sanitized_owner_runtime_ocr_smoke_observation_v0"
CLAIM_BOUNDARY = "multi_fixture_ocr_adapter_eval_only_not_robust_pdf_extraction"
NEXT_GATE = "licensed_real_world_pdf_fixture_pack_v0"


def load_owner_runtime_ocr_smoke_observation(path: Path | str) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    _validate_owner_ocr_observation(payload)
    return payload


def build_multi_fixture_ocr_adapter_eval_summary(
    *,
    fixture: PdfExtractionQualityFixture,
    base_observations_path: Path | str,
    missing_pack: dict[str, Any],
    owner_ocr_observation: dict[str, Any],
) -> dict[str, Any]:
    _validate_owner_ocr_observation(owner_ocr_observation)
    base_observations = _read_observations(Path(base_observations_path))
    missing_observations = _read_missing_pack_observations(missing_pack)
    combined_observations = {**base_observations, **missing_observations}
    fixture_ids = [item.fixture_id for item in fixture.fixtures]
    base_observed_fixture_ids = [
        fixture_id for fixture_id in fixture_ids if fixture_id in combined_observations
    ]

    per_signal = {
        fixture_id: _base_signal_row(fixture_id, combined_observations.get(fixture_id))
        for fixture_id in fixture_ids
    }
    ocr_fixture_id = str(owner_ocr_observation["fixture_id"])
    per_signal[ocr_fixture_id] = _owner_ocr_signal_row(owner_ocr_observation)

    return {
        "phase_marker": PHASE_MARKER,
        "base_fixture": fixture.packet,
        "base_fixture_count": len(fixture_ids),
        "base_observed_fixture_count": len(base_observed_fixture_ids),
        "owner_runtime_ocr_smoke_count": 1,
        "combined_fixture_signal_count": len(base_observed_fixture_ids) + 1,
        "owner_runtime_ocr_fixture_ids": [ocr_fixture_id],
        "owner_runtime_ocr_expected_spans_found": bool(
            owner_ocr_observation["expected_spans_found"]
        ),
        "ocr_evidence_scope": "single_synthetic_owner_runtime_fixture",
        "per_signal": per_signal,
        "quality_gate_status": "blocked",
        "robust_pdf_extraction_claimed": False,
        "can_claim_robust_pdf_extraction": False,
        "claim_boundary": CLAIM_BOUNDARY,
        "next_evidence_needed": [
            "licensed real-world PDF fixture pack before arbitrary-market-PDF claims",
            "OCR text-span fixture expansion before scanned-image coverage claims",
            "image/chart interpretation adapter evidence before image-heavy truth claims",
            "reading-order diagnostics before layout fidelity claims",
            "table extraction evaluation beyond deterministic adapter contracts",
        ],
        "recommended_next_gate": NEXT_GATE,
        "boundary_notes": _boundary_notes(),
    }


def build_multi_fixture_ocr_adapter_eval_report(summary: dict[str, Any]) -> str:
    lines = [
        "# Multi-fixture OCR Adapter Eval",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report combines the existing 8-role PDF fixture matrix with one sanitized owner-runtime OCR smoke observation.",
        "",
        "It is not robust PDF extraction evidence.",
        "",
        "## Aggregate",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| base_fixture_count | {summary['base_fixture_count']} |",
        f"| base_observed_fixture_count | {summary['base_observed_fixture_count']} |",
        f"| owner_runtime_ocr_smoke_count | {summary['owner_runtime_ocr_smoke_count']} |",
        f"| combined_fixture_signal_count | {summary['combined_fixture_signal_count']} |",
        f"| owner_runtime_ocr_expected_spans_found | {_format_bool(summary['owner_runtime_ocr_expected_spans_found'])} |",
        f"| robust_pdf_extraction_claimed | {_format_bool(summary['robust_pdf_extraction_claimed'])} |",
        f"| can_claim_robust_pdf_extraction | {_format_bool(summary['can_claim_robust_pdf_extraction'])} |",
        "",
        "## Signal Matrix",
        "",
        "| Signal | Status | Evidence scope | Limitation codes |",
        "|---|---|---|---|",
    ]
    for signal_id, row in summary["per_signal"].items():
        lines.append(
            "| "
            + " | ".join(
                [
                    signal_id,
                    row["signal_status"],
                    row["evidence_scope"],
                    _format_list(row["limitation_codes"]),
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
            "This is a multi-fixture OCR adapter evaluation surface only.",
            "",
            "The OCR evidence is limited to one synthetic owner-runtime fixture.",
            "",
            "This is not robust PDF extraction implementation.",
            "",
            "This is not arbitrary market PDF OCR evidence.",
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


def _validate_owner_ocr_observation(payload: dict[str, Any]) -> None:
    expected_values = {
        "packet": OWNER_OCR_OBSERVATION_PACKET,
        "phase_marker": "opt_in_ocr_adapter_runtime_smoke_v0",
        "run_source": "owner_runtime_pymupdf_ocr_smoke",
        "fixture_id": "ocr_smoke_text_image_pdf",
        "ocr_performed": True,
        "ocr_calls_attempted": True,
        "expected_spans_found": True,
        "accepted_owner_runtime_smoke": True,
        "tessdata_path_printed": False,
        "tessdata_path_committed_to_repo": False,
        "robust_pdf_extraction_claimed": False,
        "can_claim_robust_pdf_extraction": False,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(f"owner OCR observation {field} must be {expected!r}")
    if not str(payload.get("recognized_text") or "").strip():
        raise ValueError("owner OCR observation recognized_text must be non-empty")
    for forbidden in ["tessdata_path", "report_path", "local_report_path"]:
        if forbidden in payload:
            raise ValueError(f"owner OCR observation must not include {forbidden}")
    for note in [
        "not robust PDF extraction evidence",
        "not arbitrary market PDF OCR evidence",
    ]:
        if note not in payload.get("boundary_notes", []):
            raise ValueError(f"owner OCR observation missing boundary note: {note}")


def _read_observations(path: Path) -> dict[str, dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("base observations must be a JSON object")
    return {str(key): dict(value) for key, value in payload.items()}


def _read_missing_pack_observations(pack: dict[str, Any]) -> dict[str, dict[str, Any]]:
    if pack.get("packet") != "missing_pdf_runtime_observation_pack_v0":
        raise ValueError("missing pack has unexpected packet marker")
    observations = pack.get("observations")
    if not isinstance(observations, dict):
        raise ValueError("missing pack observations must be an object")
    return {str(key): dict(value) for key, value in observations.items()}


def _base_signal_row(
    fixture_id: str,
    observation: dict[str, Any] | None,
) -> dict[str, Any]:
    if observation is None:
        return {
            "signal_status": "missing_runtime_observation",
            "evidence_scope": "missing",
            "limitation_codes": ["runtime_observation_missing"],
        }
    statuses = {
        "born_digital_text": "digital_text_observed",
        "table_heavy_report": "table_candidate_gap_visible",
        "deterministic_table_adapter_pdf": "deterministic_table_adapter_contract",
        "encrypted_pdf": "expected_failure_observed",
        "scanned_image_pdf": "base_scanned_role_still_boundary_only",
        "image_heavy_pdf": "image_diagnostics_only",
        "multi_column_layout_pdf": "layout_diagnostics_only",
        "no_extractable_text_pdf": "empty_text_failure_boundary_only",
    }
    limitation_codes = _base_limitation_codes(fixture_id, observation)
    return {
        "signal_status": statuses.get(fixture_id, "observed_with_boundary"),
        "evidence_scope": "base_pdf_quality_fixture",
        "limitation_codes": limitation_codes,
    }


def _owner_ocr_signal_row(owner_ocr_observation: dict[str, Any]) -> dict[str, Any]:
    return {
        "signal_status": "owner_runtime_ocr_smoke_passed",
        "evidence_scope": "single_synthetic_owner_runtime_fixture",
        "expected_spans_found": bool(owner_ocr_observation["expected_spans_found"]),
        "limitation_codes": [
            "single_synthetic_fixture_only",
            "not_arbitrary_market_pdf_ocr",
            "not_robust_pdf_extraction",
        ],
    }


def _base_limitation_codes(
    fixture_id: str,
    observation: dict[str, Any],
) -> list[str]:
    by_fixture = {
        "born_digital_text": ["digital_text_only"],
        "table_heavy_report": ["table_rows_not_extracted"],
        "deterministic_table_adapter_pdf": [
            "deterministic_adapter_contract_not_arbitrary_pdf_evidence"
        ],
        "encrypted_pdf": ["expected_failure_boundary"],
        "scanned_image_pdf": [
            "ocr_smoke_is_adjacent_not_same_fixture",
            "base_fixture_text_still_not_extracted",
        ],
        "image_heavy_pdf": ["image_chart_interpretation_not_claimed"],
        "multi_column_layout_pdf": ["layout_fidelity_not_claimed"],
        "no_extractable_text_pdf": ["empty_text_failure_boundary_only"],
    }
    codes = list(by_fixture.get(fixture_id, []))
    if observation.get("robust_pdf_extraction") is not False:
        codes.append("robust_pdf_extraction_not_explicitly_false")
    return codes


def _boundary_notes() -> list[str]:
    return [
        "one owner-runtime OCR smoke over one synthetic fixture only",
        "not robust PDF extraction evidence",
        "not arbitrary market PDF OCR evidence",
        "not image/chart interpretation evidence",
        "not layout fidelity evidence",
        "not hosted deployment evidence",
        "not external reviewer feedback",
        "not product-complete",
    ]


def _format_bool(value: Any) -> str:
    return "true" if value else "false"


def _format_list(value: list[str]) -> str:
    return ", ".join(value) if value else "none"
