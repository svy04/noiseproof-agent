from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]


def test_source_assimilation_registry_is_linked_and_bounded():
    registry = (
        REPO_ROOT / "docs/research/source-assimilation-registry.md"
    ).read_text(encoding="utf-8")
    spec = (
        REPO_ROOT / "docs/specs/2026-06-30-source-assimilation-registry.md"
    ).read_text(encoding="utf-8")
    review = (
        REPO_ROOT / "docs/review/source-assimilation-registry.md"
    ).read_text(encoding="utf-8")
    master = (REPO_ROOT / "docs/MASTER-SPEC.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (
        REPO_ROOT / "docs/application/portfolio-index.md"
    ).read_text(encoding="utf-8")

    marker = "source_assimilation_registry_v0"
    path = "docs/research/source-assimilation-registry.md"

    for surface in [registry, spec, review, master, readme, goal, runbook, portfolio]:
        assert marker in surface
        assert path in surface

    for card_marker in [
        "source:",
        "source_type:",
        "pattern_to_borrow:",
        "local_adaptation:",
        "boundary:",
        "rejection_condition:",
        "license_or_rights_note:",
    ]:
        assert card_marker in registry

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
        assert source_marker in registry
        assert source_marker in review

    for boundary_marker in [
        "not new runtime behavior",
        "not external reviewer feedback",
        "not benchmark evidence",
        "not patent implementation permission",
        "not product-complete",
    ]:
        assert boundary_marker in review

    assert "No data model, API, or runtime behavior changes." in spec
    assert "Future gates now have a documented source-card registry" in spec
