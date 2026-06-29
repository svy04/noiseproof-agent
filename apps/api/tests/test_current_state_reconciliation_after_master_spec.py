from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]


def test_current_state_reconciliation_after_master_spec_is_discoverable():
    spec = (
        REPO_ROOT
        / "docs/specs/2026-06-30-current-state-reconciliation-after-master-spec.md"
    ).read_text(encoding="utf-8")
    review = (
        REPO_ROOT / "docs/review/current-state-reconciliation-after-master-spec.md"
    ).read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (
        REPO_ROOT / "docs/application/portfolio-index.md"
    ).read_text(encoding="utf-8")

    marker = "current_state_reconciliation_after_master_spec_v0"

    for surface in [spec, review, readme, goal, runbook, portfolio]:
        assert marker in surface
        assert "docs/MASTER-SPEC.md" in surface
        assert "docs/GOAL.md" in surface

    for marker_text in [
        "docs/application/portfolio-index.md",
        "docs/review/external-reader-proof-path.md",
        "Diataxis",
        "SLSA Provenance",
        "not new runtime evidence",
        "not external reviewer feedback",
        "not product-complete",
    ]:
        assert marker_text in review

    assert "No data model, API, or runtime behavior changes." in spec
    assert "Future gate selection now has an explicit current-state reconciliation step" in spec
