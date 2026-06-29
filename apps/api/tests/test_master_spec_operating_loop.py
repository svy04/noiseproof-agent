from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]


def test_master_spec_operating_loop_is_documented():
    master_spec = (REPO_ROOT / "docs/MASTER-SPEC.md").read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (
        REPO_ROOT / "docs/application/portfolio-index.md"
    ).read_text(encoding="utf-8")
    spec_readme = (REPO_ROOT / "docs/specs/README.md").read_text(encoding="utf-8")
    gate_spec = (
        REPO_ROOT / "docs/specs/2026-06-30-master-spec-operating-loop.md"
    ).read_text(encoding="utf-8")
    review = (REPO_ROOT / "docs/review/master-spec-operating-loop.md").read_text(
        encoding="utf-8"
    )

    for marker in [
        "Source Assimilation Doctrine",
        "Reference Spine",
        "Gate Loop",
        "Stop Conditions",
        "master_spec_operating_loop_v0",
        "W3C PROV-DM",
        "SLSA Provenance",
        "OpenTelemetry",
        "RAGAS",
        "ALCE",
        "BEIR",
        "Model Cards",
        "Datasheets for Datasets",
        "US20260105079A1",
        "US10628389B2",
    ]:
        assert marker in master_spec

    for surface in [goal, readme, runbook, portfolio]:
        assert "docs/MASTER-SPEC.md" in surface
        assert "docs/specs/" in surface
        assert "master_spec_operating_loop_v0" in surface

    for marker in [
        "title:",
        "target_gate:",
        "sources_to_absorb:",
        "stop_conditions:",
        "claim_boundaries:",
    ]:
        assert marker in spec_readme

    assert "Master Spec Operating Loop v0" in gate_spec
    assert "No data model or API contract changes." in gate_spec
    assert "Cannot claim:" in gate_spec
    assert "Master Spec Operating Loop" in review
    assert "not new runtime behavior" in review
    assert "not product-complete" in review
