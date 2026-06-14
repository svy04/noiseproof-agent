from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]


def test_readme_has_proof_bounded_marketing_surface():
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")

    assert "## Current Proof Surface" in readme
    assert "Latest verified gate" in readme
    assert "Owner-approved Real-world PDF Download and Hash v0" in readme
    assert "Remote workflow verification" in readme
    assert "6d638fca11b02e03581a8296bb95bc9a5da3894c" in readme
    assert "27495693041" in readme
    assert "27495693049" in readme
    assert "## What This Proves Now" in readme
    assert "## What This Does Not Prove Yet" in readme
    assert "robust PDF extraction" in readme
    assert "hosted deployment" in readme
    assert "external reviewer feedback" in readme
    assert "## Source-first Patterns Borrowed" in readme
    assert "RAGAS" in readme
    assert "Self-RAG" in readme
    assert "Corrective RAG" in readme
    assert "ALCE" in readme
    assert "BEIR" in readme
    assert "trec_eval" in readme
    assert "W3C PROV-DM" in readme
    assert "Docling" in readme
    assert "Unstructured" in readme
    assert "OCR-D" in readme
    assert "PyMuPDF" in readme
    assert "OCRmyPDF" in readme
    assert "BLS public domain" in readme
    assert "## 90-second Reviewer Path" in readme
    assert "Do not read this as a product-complete claim" in readme


def test_readme_marketing_surface_review_doc_exists():
    review = (
        REPO_ROOT / "docs/review/readme-proof-bounded-marketing-surface.md"
    ).read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (
        REPO_ROOT / "docs/application/portfolio-index.md"
    ).read_text(encoding="utf-8")
    application_ready = (
        REPO_ROOT / "docs/review/application-ready-review.md"
    ).read_text(encoding="utf-8")

    assert "README Proof-bounded Marketing Surface" in review
    assert "source-first patterns borrowed" in review
    assert "ALCE" in review
    assert "BEIR" in review
    assert "W3C PROV-DM" in review
    assert "not product-complete" in review
    assert "not robust PDF extraction evidence" in review
    assert "Phase 886 - README Proof-bounded Marketing Surface v0" in goal
    assert "Phase 886 adds README proof-bounded marketing surface v0" in runbook
    assert "docs/review/readme-proof-bounded-marketing-surface.md" in portfolio
    assert "README Proof-bounded Marketing Surface" in application_ready
