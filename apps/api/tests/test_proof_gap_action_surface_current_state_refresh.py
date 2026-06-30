from pathlib import Path

from app.main import app
from fastapi.testclient import TestClient


REPO_ROOT = Path(__file__).resolve().parents[3]


def _read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_proof_gap_action_surface_advances_after_table_extraction_evidence_gate():
    client = TestClient(app)

    response = client.get("/ops/proof-gaps")

    assert response.status_code == 200
    body = response.json()
    robust_gap = next(
        gap for gap in body["gaps"] if gap["gap_id"] == "robust_pdf_extraction"
    )
    assert body["surface_boundary"] == (
        "action_surface_only_not_new_proof_or_gap_closure"
    )
    assert robust_gap["recommended_next_gate"] == (
        "robust_pdf_extraction_generalization_gap_review_v0"
    )
    assert robust_gap["next_evidence_needed"] == (
        "robust_pdf_extraction_generalization_gap_review_v0"
    )
    assert (
        "multi_real_world_pdf_parse_observation_matrix_remote_verification_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "robust_pdf_extraction_next_real_world_quality_gate_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "cross_publisher_real_world_pdf_fixture_gate_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "real_world_table_extraction_evidence_gate_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "real_world_ocr_evidence_gate_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "real_world_layout_fidelity_evidence_gate_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "docs/review/multi-real-world-pdf-parse-observation-remote-verification.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/review/robust-pdf-extraction-next-real-world-quality-gate.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/evaluation/robust-pdf-real-world-quality-gate-report.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/review/cross-publisher-real-world-pdf-fixture-gate.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/evaluation/cross-publisher-real-world-pdf-fixture-gate-report.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/review/real-world-table-extraction-evidence-gate.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/evaluation/real-world-table-extraction-evidence-gate-report.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/review/real-world-ocr-evidence-gate.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/evaluation/real-world-ocr-evidence-gate-report.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/review/real-world-layout-fidelity-evidence-gate.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/evaluation/real-world-layout-fidelity-evidence-gate-report.md"
        in robust_gap["proof_routes"]
    )
    assert "robust PDF extraction is implemented" in robust_gap["blocked_claims"]


def test_proof_gap_action_refresh_docs_are_linked_and_bounded():
    marker = "proof_gap_action_surface_current_state_refresh_v0"
    review_path = "docs/review/proof-gap-action-surface-current-state-refresh.md"
    spec_path = "docs/specs/2026-06-30-proof-gap-action-surface-current-state-refresh.md"

    surfaces = [
        _read("README.md"),
        _read("docs/GOAL.md"),
        _read("docs/runbook.md"),
        _read("docs/application/portfolio-index.md"),
        _read("docs/review/proof-gap-action-surface.md"),
        _read(review_path),
        _read(spec_path),
    ]

    for surface in surfaces:
        assert marker in surface
        assert "robust_pdf_extraction_next_real_world_quality_gate_v0" in surface

    for surface in [
        _read("README.md"),
        _read("docs/GOAL.md"),
        _read("docs/runbook.md"),
        _read("docs/application/portfolio-index.md"),
    ]:
        assert review_path in surface

    review = _read(review_path)
    for boundary in [
        "not new runtime evidence",
        "not robust PDF extraction evidence",
        "not semantic retrieval quality evidence",
        "not hosted deployment evidence",
        "not hosted observability evidence",
        "not external reviewer feedback",
        "not product-complete",
    ]:
        assert boundary in review
