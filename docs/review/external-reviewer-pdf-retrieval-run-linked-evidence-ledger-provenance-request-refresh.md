# External Reviewer PDF Retrieval-run-linked Evidence Ledger Provenance Request Refresh

Status: implemented.

Phase marker: external reviewer PDF retrieval-run-linked Evidence Ledger provenance request refresh v0.

Label: External reviewer PDF retrieval-run-linked Evidence Ledger provenance request refresh.

## Goal

Point reviewer-facing request surfaces to the uploaded PDF retrieval-run-linked Evidence Ledger provenance runtime proof without claiming external feedback or editing the live public issue body.

## What Changed

- `CONTRIBUTING.md` now links reviewers to the uploaded PDF retrieval-run-linked Evidence Ledger provenance runtime proof.
- `.github/ISSUE_TEMPLATE/external-review-feedback.md` now includes the same proof link in fast links.
- `docs/review/external-review-request.md` now includes the proof in the request packet.
- `docs/review/external-reviewer-brief.md` now includes the proof in the 2-minute path.
- `docs/review/external-reviewer-link-map.md` now includes the proof in the direct link map.
- `docs/review/external-reader-proof-path.md` now names the runtime proof and this request refresh.
- `README.md`, `docs/runbook.md`, `docs/GOAL.md`, and `docs/application/portfolio-index.md` now record this phase.

## Proof Link

uploaded PDF retrieval-run-linked Evidence Ledger provenance runtime proof:

```text
docs/review/uploaded-pdf-retrieval-run-linked-evidence-ledger-provenance-runtime-smoke.md
```

## Follow-up

The live issue body refresh is recorded here:

```text
docs/review/external-review-issue-body-pdf-retrieval-run-linked-evidence-ledger-provenance-refresh.md
```

## Evidence Markers

```text
POST /documents/upload-chunks
POST /documents/{document_id}/retrieval-runs
POST /retrieval-runs/{retrieval_run_id}/evidence-ledger
GET /evidence-ledgers?retrieval_run_id=
metadata_json.parser -> pdf-pymupdf
metadata_json.source_provenance_boundary -> evidence_ledger_entry_metadata_from_retrieval_run_candidate_chunk
ledger_retrieval_run_id_matches -> true
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

It is not Noise Gate behavior.

It is not report generation.

It is not production readiness.

## Next Gate

```text
external reviewer feedback v0 remains pending, external reviewer PDF retrieval-run-linked Evidence Ledger provenance issue-body refresh v0, or select the next source-first product gate
```
