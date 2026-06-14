from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from packages.ingestion.pdf_quality.fixture import PdfExtractionQualityFixture
from packages.ingestion.pdf_quality.multi_fixture import (
    build_multi_fixture_pdf_extraction_quality_matrix,
)


PHASE_MARKER = "missing_pdf_runtime_observation_pack_v0"
CLAIM_BOUNDARY = "missing_runtime_observation_pack_only_not_robust_pdf_extraction"
REQUIRED_MISSING_PDF_RUNTIME_FIXTURE_IDS = [
    "scanned_image_pdf",
    "image_heavy_pdf",
    "multi_column_layout_pdf",
    "no_extractable_text_pdf",
]


def load_missing_pdf_runtime_observation_pack(path: Path | str) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    _validate_pack(payload)
    return payload


def build_missing_pdf_runtime_observation_pack_summary(
    fixture: PdfExtractionQualityFixture,
    base_observations: dict[str, dict[str, Any]],
    pack: dict[str, Any],
) -> dict[str, Any]:
    _validate_pack(pack)
    pack_observations = {
        fixture_id: dict(observation)
        for fixture_id, observation in pack["observations"].items()
    }
    combined_observations = {**base_observations, **pack_observations}
    matrix = build_multi_fixture_pdf_extraction_quality_matrix(
        fixture,
        combined_observations,
    )
    per_fixture = {
        fixture_id: _summary_row(matrix["per_fixture"][fixture_id], pack_observations)
        for fixture_id in REQUIRED_MISSING_PDF_RUNTIME_FIXTURE_IDS
    }

    return {
        "phase_marker": PHASE_MARKER,
        "fixture": fixture.packet,
        "fixture_count": len(fixture.fixtures),
        "base_observed_fixture_count": len(base_observations),
        "pack_observed_fixture_count": len(pack_observations),
        "combined_observed_fixture_count": len(combined_observations),
        "runtime_observation_fixture_ids": REQUIRED_MISSING_PDF_RUNTIME_FIXTURE_IDS,
        "remaining_missing_runtime_observation_fixture_ids": matrix[
            "missing_runtime_observation_fixture_ids"
        ],
        "per_fixture": per_fixture,
        "quality_gate_status": "blocked",
        "robust_pdf_extraction_claimed": False,
        "can_claim_robust_pdf_extraction": False,
        "claim_boundary": CLAIM_BOUNDARY,
        "next_evidence_needed": [
            "real scanned-image binary fixture with explicit opt-in OCR adapter evidence",
            "image-heavy fixture with image/chart interpretation kept out of text claims",
            "multi-column fixture with reading-order diagnostics before layout fidelity claims",
            "separate adapter evidence before changing robust_pdf_extraction wording",
        ],
        "boundary_notes": [
            "not robust PDF extraction evidence",
            "not OCR evidence",
            "not image/chart interpretation evidence",
            "not layout fidelity evidence",
            "not hosted deployment evidence",
            "not product-complete",
        ],
    }


def build_missing_pdf_runtime_observation_pack_report(
    summary: dict[str, Any],
) -> str:
    lines = [
        "# Missing PDF Runtime Observation Pack",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report records the previously missing PDF fixture observation roles as a bounded pack.",
        "",
        "It is not robust PDF extraction evidence.",
        "",
        "## Aggregate",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| fixture_count | {summary['fixture_count']} |",
        f"| base_observed_fixture_count | {summary['base_observed_fixture_count']} |",
        f"| pack_observed_fixture_count | {summary['pack_observed_fixture_count']} |",
        f"| combined_observed_fixture_count | {summary['combined_observed_fixture_count']} |",
        f"| remaining_missing_runtime_observation_count | {len(summary['remaining_missing_runtime_observation_fixture_ids'])} |",
        f"| robust_pdf_extraction_claimed | {_format_bool(summary['robust_pdf_extraction_claimed'])} |",
        f"| can_claim_robust_pdf_extraction | {_format_bool(summary['can_claim_robust_pdf_extraction'])} |",
        "",
        "## Runtime Observation Roles",
        "",
        "| Fixture | Observation source | Limitation codes | Failure candidate |",
        "|---|---|---|---|",
    ]
    for fixture_id in summary["runtime_observation_fixture_ids"]:
        row = summary["per_fixture"][fixture_id]
        lines.append(
            "| "
            + " | ".join(
                [
                    fixture_id,
                    row["observation_source"],
                    _format_list(row["limitation_codes"]),
                    row["failure_case_candidate"] or "none",
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Remaining Missing Runtime Observations",
            "",
        ]
    )
    if summary["remaining_missing_runtime_observation_fixture_ids"]:
        for fixture_id in summary["remaining_missing_runtime_observation_fixture_ids"]:
            lines.append(f"- `{fixture_id}`")
    else:
        lines.append("- none")

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
            "This is a missing-runtime-observation pack only.",
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


def _validate_pack(payload: dict[str, Any]) -> None:
    if payload.get("packet") != PHASE_MARKER:
        raise ValueError("Unexpected missing PDF runtime observation packet.")
    if payload.get("claim_boundary") != CLAIM_BOUNDARY:
        raise ValueError("Missing PDF runtime pack has wrong claim boundary.")
    if payload.get("robust_pdf_extraction_claimed") is not False:
        raise ValueError("Missing PDF runtime pack must not claim robust extraction.")
    observations = payload.get("observations")
    if not isinstance(observations, dict):
        raise ValueError("Missing PDF runtime pack observations must be an object.")
    if set(observations) != set(REQUIRED_MISSING_PDF_RUNTIME_FIXTURE_IDS):
        raise ValueError("Missing PDF runtime pack must include exactly the required roles.")
    for fixture_id in REQUIRED_MISSING_PDF_RUNTIME_FIXTURE_IDS:
        _validate_observation(fixture_id, observations[fixture_id])


def _validate_observation(fixture_id: str, observation: Any) -> None:
    if not isinstance(observation, dict):
        raise ValueError(f"Observation for {fixture_id} must be an object.")
    if observation.get("runtime_observed") is not True:
        raise ValueError(f"Observation for {fixture_id} must be runtime_observed.")
    if observation.get("robust_pdf_extraction") is not False:
        raise ValueError(f"Observation for {fixture_id} must keep robust extraction false.")
    if not str(observation.get("observation_source") or ""):
        raise ValueError(f"Observation for {fixture_id} needs observation_source.")
    warnings = [str(warning) for warning in observation.get("warnings", [])]
    if fixture_id == "scanned_image_pdf":
        if observation.get("ocr_performed") is not False:
            raise ValueError("scanned_image_pdf must keep OCR disabled.")
        if not any("OCR is required" in warning for warning in warnings):
            raise ValueError("scanned_image_pdf must include OCR-required warning.")
        if not observation.get("failure_case_candidate"):
            raise ValueError("scanned_image_pdf must keep a failure candidate.")
    if fixture_id == "image_heavy_pdf":
        if observation.get("image_chart_interpretation_claimed") is not False:
            raise ValueError("image_heavy_pdf must not claim image/chart interpretation.")
    if fixture_id == "multi_column_layout_pdf":
        if observation.get("layout_fidelity_claimed") is not False:
            raise ValueError("multi_column_layout_pdf must not claim layout fidelity.")
    if fixture_id == "no_extractable_text_pdf":
        if observation.get("failure_case_candidate") != "pdf_no_extractable_text":
            raise ValueError("no_extractable_text_pdf must use pdf_no_extractable_text.")


def _summary_row(
    matrix_row: dict[str, Any],
    observations: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    observation = observations[matrix_row["fixture_id"]]
    return {
        **matrix_row,
        "observation_source": str(observation["observation_source"]),
        "failure_case_candidate": observation.get("failure_case_candidate"),
        "limitation_codes": sorted(
            set(matrix_row["limitation_codes"])
            | set(_role_limitation_codes(matrix_row["fixture_id"]))
        ),
    }


def _role_limitation_codes(fixture_id: str) -> list[str]:
    by_fixture = {
        "scanned_image_pdf": ["ocr_adapter_not_run"],
        "image_heavy_pdf": ["image_chart_interpretation_not_claimed"],
        "multi_column_layout_pdf": ["layout_fidelity_not_claimed"],
        "no_extractable_text_pdf": ["empty_text_failure_boundary_only"],
    }
    return by_fixture[fixture_id]


def _format_bool(value: Any) -> str:
    return "true" if value else "false"


def _format_list(value: list[str]) -> str:
    return ", ".join(value) if value else "none"
