from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]


def test_readme_has_proof_bounded_marketing_surface():
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")

    assert "## Current Proof Surface" in readme
    assert "Latest verified gate" in readme
    assert (
        "Latest verified gate | External Feedback Current-state Multi Real-world PDF Parse Observation Matrix Issue Verification Remote Verification v0"
        in readme
    )
    assert "Multi Real-world PDF Parse Observation Matrix v0" in readme
    assert "Owner-approved real-world PDF download/hash" in readme
    assert "Remote workflow verification" in readme
    assert "084e3fe9fd3bf65bef873a28d7cbf8a06f3405ea" in readme
    assert "27497284929" in readme
    assert "27497284920" in readme
    assert "candidate_count: 0" in readme
    assert "status: pending" in readme
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


def test_external_reader_phase_897_current_proof_packet_refresh_is_recorded():
    refresh_path = (
        REPO_ROOT
        / "docs/review/external-reader-phase-897-current-proof-packet-refresh.md"
    )
    assert refresh_path.is_file()

    refresh = refresh_path.read_text(encoding="utf-8")
    expected_markers = [
        "External-reader Phase 897 Current Proof Packet Refresh",
        "external reader phase 897 current proof packet refresh v0",
        "docs/review/external-review-issue-body-multi-real-world-pdf-parse-observation-matrix-route-refresh.md",
        "docs/review/external-feedback-current-state-multi-real-world-pdf-parse-observation-matrix-issue-verification.md",
        "docs/review/external-feedback-current-state-multi-real-world-pdf-parse-observation-matrix-issue-verification-remote-verification.md",
        "084e3fe9fd3bf65bef873a28d7cbf8a06f3405ea",
        "CI run `27497284929`: success",
        "External Feedback Screen run `27497284920`: success",
        "candidate_count: 0",
        "status: pending",
        "not external reviewer feedback",
        "not robust PDF extraction evidence",
        "not hosted deployment evidence",
        "not product-complete",
    ]
    for marker in expected_markers:
        assert marker in refresh

    for path in [
        "README.md",
        "docs/review/external-reader-proof-path.md",
        "docs/review/external-reviewer-outreach-packet.md",
        "docs/application/portfolio-index.md",
        "docs/review/application-ready-review.md",
        "docs/GOAL.md",
        "docs/runbook.md",
    ]:
        surface = (REPO_ROOT / path).read_text(encoding="utf-8")
        assert (
            "docs/review/external-reader-phase-897-current-proof-packet-refresh.md"
            in surface
        ), path


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
