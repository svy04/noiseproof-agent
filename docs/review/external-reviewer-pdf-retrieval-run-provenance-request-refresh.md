# External Reviewer PDF Retrieval-run Provenance Request Refresh

Status: implemented.

Phase marker: external reviewer PDF retrieval-run provenance request refresh v0.

Label: External reviewer PDF retrieval-run provenance request refresh.

## Goal

Point reviewer-facing request surfaces to the uploaded PDF retrieval-run provenance runtime proof without claiming external feedback or editing the live public issue body.

## What Changed

- `CONTRIBUTING.md` now links reviewers to the uploaded PDF retrieval-run provenance runtime proof.
- `.github/ISSUE_TEMPLATE/external-review-feedback.md` now includes the same proof link in fast links.
- `docs/review/external-review-request.md` now includes the proof in the request packet.
- `docs/review/external-reviewer-brief.md` now includes the proof in the 2-minute path.
- `docs/review/external-reviewer-link-map.md` now includes the proof in the direct link map.
- `docs/review/external-reader-proof-path.md` now names the runtime proof and this request refresh.
- `README.md`, `docs/runbook.md`, `docs/GOAL.md`, and `docs/application/portfolio-index.md` now record this phase.

## Follow-up

The live issue body refresh is recorded here:

```text
docs/review/external-review-issue-body-pdf-retrieval-run-provenance-refresh.md
```

## Proof Link

uploaded PDF retrieval-run provenance runtime proof:

```text
docs/review/uploaded-pdf-retrieval-run-provenance-runtime-smoke.md
```

## Evidence Markers

```text
POST /documents/upload-chunks
POST /documents/{document_id}/retrieval-runs
GET /retrieval-runs
candidate_parsers -> pdf-pymupdf
source_provenance_boundary -> retrieval_run_candidate_chunk_metadata_only
```

## Boundary

This is request infrastructure only.

It does not edit the live public issue body.

It is not external reviewer feedback.

It is not hosted deployment evidence.

It is not customer validation.

It is not Braincrew acceptance.

It is not robust PDF extraction.

It is not OCR.

It is not table extraction.

It is not layout fidelity.

It is not raw file storage.

It is not full parsed text persistence.

It is not Evidence Ledger generation.

It is not Noise Gate behavior.

It is not report generation.

It is not production readiness.

## Next Gate

```text
external reviewer feedback v0 remains pending, external feedback current-state PDF retrieval-run provenance issue verification v0, or select the next source-first product gate
```
