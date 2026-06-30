from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]


def _read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_proof_gap_priority_matrix_is_linked_and_bounded():
    matrix = _read("docs/research/proof-gap-priority-matrix.md")
    spec = _read("docs/specs/2026-06-30-proof-gap-priority-matrix.md")
    review = _read("docs/review/proof-gap-priority-matrix.md")
    master = _read("docs/MASTER-SPEC.md")
    readme = _read("README.md")
    goal = _read("docs/GOAL.md")
    runbook = _read("docs/runbook.md")
    portfolio = _read("docs/application/portfolio-index.md")

    marker = "proof_gap_priority_matrix_v0"
    path = "docs/research/proof-gap-priority-matrix.md"
    review_path = "docs/review/proof-gap-priority-matrix.md"

    for surface in [matrix, spec, review, master, readme, goal, runbook, portfolio]:
        assert marker in surface
        assert path in surface

    for surface in [readme, goal, runbook, portfolio]:
        assert review_path in surface

    for gap_id in [
        "external_reviewer_feedback",
        "robust_pdf_extraction",
        "semantic_retrieval_quality",
        "actual_embedding_generation",
        "hosted_deployment",
        "hosted_observability",
        "distributed_tracing",
    ]:
        assert gap_id in matrix
        assert gap_id in review

    for source_marker in [
        "W3C PROV-DM",
        "SLSA Provenance",
        "OpenTelemetry",
        "RAGAS",
        "ALCE",
        "BEIR",
        "trec_eval",
        "Model Cards",
        "Datasheets for Datasets",
        "Diataxis",
        "Docling",
        "Unstructured",
        "US20260105079A1",
        "US10628389B2",
    ]:
        assert source_marker in matrix

    for boundary_marker in [
        "not new runtime evidence",
        "not robust PDF extraction evidence",
        "not semantic retrieval quality evidence",
        "not hosted deployment evidence",
        "not hosted observability evidence",
        "not external reviewer feedback",
        "not product-complete",
    ]:
        assert boundary_marker in matrix
        assert boundary_marker in review

    assert "external_reviewer_feedback_v0" in matrix
    assert "cannot be self-completed" in matrix
    assert "owner comments" in matrix
    assert "proof_gap_action_surface_current_state_refresh_v0" in matrix
    assert "No data model, API, or runtime behavior changes." in spec
