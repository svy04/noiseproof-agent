# External Review Issue Body PDF Retrieval-run Provenance Refresh

Status: implemented.

Phase marker: external reviewer PDF retrieval-run provenance issue-body refresh v0.

Label: External reviewer PDF retrieval-run provenance issue-body refresh.

## Goal

Update the live public external review issue body so reviewers can reach the uploaded PDF retrieval-run provenance runtime proof.

## Live Issue

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

## Updated Links

uploaded PDF retrieval-run provenance runtime proof:

```text
docs/review/uploaded-pdf-retrieval-run-provenance-runtime-smoke.md
```

external reviewer PDF retrieval-run provenance request refresh:

```text
docs/review/external-reviewer-pdf-retrieval-run-provenance-request-refresh.md
```

## Evidence Markers

```text
POST /documents/upload-chunks
POST /documents/{document_id}/retrieval-runs
GET /retrieval-runs
candidate_parsers -> pdf-pymupdf
source_provenance_boundary -> retrieval_run_candidate_chunk_metadata_only
```

## Observed Live Issue Markers

```text
updatedAt: 2026-06-04T06:48:07Z
starts_with_request: true
first_codepoint: 35
has_pdf_retrieval_run_provenance_runtime_proof: true
has_pdf_retrieval_run_provenance_runtime_link: true
has_pdf_retrieval_run_provenance_request_refresh: true
has_candidate_parsers_marker: true
has_source_provenance_boundary_marker: true
has_external_feedback_boundary: true
comment_count: 1
```

## Boundary

This is an owner-authored issue body edit.

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
