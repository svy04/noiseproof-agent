from __future__ import annotations

from typing import Any

from packages.ingestion.pdf_quality.evaluator import evaluate_pdf_extraction_quality
from packages.ingestion.pdf_quality.fixture import PdfExtractionQualityFixture


PHASE_MARKER = "multi_fixture_pdf_extraction_quality_eval_v0"


def build_multi_fixture_pdf_extraction_quality_matrix(
    fixture: PdfExtractionQualityFixture,
    observations: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    evaluation = evaluate_pdf_extraction_quality(fixture, observations)
    per_fixture: dict[str, dict[str, Any]] = {}

    for item in fixture.fixtures:
        metrics = evaluation["per_fixture"][item.fixture_id]
        observation = observations.get(item.fixture_id)
        per_fixture[item.fixture_id] = {
            "fixture_id": item.fixture_id,
            "role": item.role,
            "source_shape": item.source_shape,
            "fixture_eval_state": _fixture_eval_state(
                item.fixture_id,
                metrics,
                observation,
            ),
            "limitation_codes": _limitation_codes(
                item.fixture_id,
                metrics,
                observation,
            ),
            "expected_span_recall": metrics["expected_span_recall"],
            "table_cell_recall": metrics["table_cell_recall"],
            "warning_correctness": metrics["warning_correctness"],
            "failure_case_candidate_correctness": (
                metrics["failure_case_candidate_correctness"]
            ),
        }

    observed_fixture_ids = [
        item.fixture_id for item in fixture.fixtures if item.fixture_id in observations
    ]
    missing_runtime_observation_fixture_ids = [
        item.fixture_id
        for item in fixture.fixtures
        if item.fixture_id not in observations
    ]

    return {
        "phase_marker": PHASE_MARKER,
        "fixture": fixture.packet,
        "fixture_count": len(fixture.fixtures),
        "observed_fixture_count": len(observed_fixture_ids),
        "gap_fixture_count": len(missing_runtime_observation_fixture_ids),
        "observed_fixture_ids": observed_fixture_ids,
        "missing_runtime_observation_fixture_ids": (
            missing_runtime_observation_fixture_ids
        ),
        "per_fixture": per_fixture,
        "aggregate": evaluation["aggregate"],
        "quality_gate_status": "blocked",
        "robust_pdf_extraction_claimed": False,
        "can_claim_robust_pdf_extraction": False,
        "claim_boundary": "multi_fixture_matrix_only_not_robust_pdf_extraction",
        "next_evidence_needed": [
            "runtime observations for missing PDF fixture roles",
            "OCR adapter evidence before scanned-image text coverage",
            "layout-order diagnostics before multi-column fidelity claims",
            "image/chart interpretation boundary before image-heavy claims",
        ],
        "boundary_notes": [
            "not robust PDF extraction evidence",
            "not OCR evidence",
            "not table extraction evidence for arbitrary market PDFs",
            "not layout fidelity evidence",
            "not hosted deployment evidence",
            "not product-complete",
        ],
    }


def build_multi_fixture_pdf_extraction_quality_report(
    matrix: dict[str, Any],
) -> str:
    lines = [
        "# Multi-fixture PDF Extraction Quality Eval",
        "",
        f"Phase marker: {matrix['phase_marker']}.",
        "",
        "This report maps every PDF extraction quality fixture role to its current observation state.",
        "",
        "It is not robust PDF extraction evidence.",
        "",
        "## Aggregate",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| fixture_count | {matrix['fixture_count']} |",
        f"| observed_fixture_count | {matrix['observed_fixture_count']} |",
        f"| gap_fixture_count | {matrix['gap_fixture_count']} |",
        f"| robust_pdf_extraction_claimed | {_format_bool(matrix['robust_pdf_extraction_claimed'])} |",
        f"| can_claim_robust_pdf_extraction | {_format_bool(matrix['can_claim_robust_pdf_extraction'])} |",
        "",
        "## Per-fixture Matrix",
        "",
        "| Fixture | State | Limitation codes | expected_span_recall | table_cell_recall | warning_correctness | failure_case_candidate_correctness |",
        "|---|---|---|---:|---:|---:|---:|",
    ]
    for fixture_id, row in matrix["per_fixture"].items():
        lines.append(
            "| "
            + " | ".join(
                [
                    fixture_id,
                    row["fixture_eval_state"],
                    _format_list(row["limitation_codes"]),
                    _format_metric(row["expected_span_recall"]),
                    _format_metric(row["table_cell_recall"]),
                    _format_metric(row["warning_correctness"]),
                    _format_metric(row["failure_case_candidate_correctness"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Missing Runtime Observations",
            "",
        ]
    )
    for fixture_id in matrix["missing_runtime_observation_fixture_ids"]:
        lines.append(f"- `{fixture_id}`")

    lines.extend(
        [
            "",
            "## Next Evidence Needed",
            "",
        ]
    )
    for item in matrix["next_evidence_needed"]:
        lines.append(f"- {item}")

    lines.extend(
        [
            "",
            "## Boundary Notes",
            "",
        ]
    )
    for note in matrix["boundary_notes"]:
        lines.append(f"- {note}")

    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "This is a multi-fixture observation matrix only.",
            "",
            "This is not robust PDF extraction implementation.",
            "",
            "This is not OCR implementation.",
            "",
            "This is not layout fidelity evidence.",
            "",
            "This is not hosted deployment evidence.",
            "",
            "This is not product-complete.",
        ]
    )
    return "\n".join(lines) + "\n"


def _fixture_eval_state(
    fixture_id: str,
    metrics: dict[str, Any],
    observation: dict[str, Any] | None,
) -> str:
    if observation is None:
        return "missing_runtime_observation"
    if fixture_id == "encrypted_pdf" and metrics["failure_case_candidate_correctness"] == 1.0:
        return "expected_failure_observed"
    if fixture_id == "deterministic_table_adapter_pdf":
        return "adapter_contract_observed"
    if _limitation_codes(fixture_id, metrics, observation):
        return "observed_with_gaps"
    return "observed_passed"


def _limitation_codes(
    fixture_id: str,
    metrics: dict[str, Any],
    observation: dict[str, Any] | None,
) -> list[str]:
    if observation is None:
        return _missing_observation_limitations(fixture_id)
    limitations: list[str] = []
    if fixture_id == "table_heavy_report" and metrics["table_cell_recall"] < 1.0:
        limitations.append("table_rows_not_extracted")
    if fixture_id == "deterministic_table_adapter_pdf":
        limitations.append("adapter_contract_not_arbitrary_pdf_evidence")
    return limitations


def _missing_observation_limitations(fixture_id: str) -> list[str]:
    by_fixture = {
        "scanned_image_pdf": [
            "ocr_adapter_not_run",
            "no_runtime_scan_fixture_observation",
        ],
        "image_heavy_pdf": [
            "image_chart_interpretation_not_claimed",
            "no_runtime_image_heavy_observation",
        ],
        "multi_column_layout_pdf": [
            "layout_fidelity_not_claimed",
            "reading_order_not_evaluated",
        ],
        "no_extractable_text_pdf": [
            "failure_candidate_runtime_observation_missing",
            "no_runtime_empty_text_observation",
        ],
    }
    return by_fixture.get(fixture_id, ["runtime_observation_missing"])


def _format_metric(value: Any) -> str:
    if isinstance(value, float):
        text = f"{value:.4f}".rstrip("0").rstrip(".")
        return text or "0"
    return str(value)


def _format_bool(value: Any) -> str:
    return "true" if value else "false"


def _format_list(value: list[str]) -> str:
    return ", ".join(value) if value else "none"
