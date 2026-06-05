# Uploaded PDF No-text Ops Summary Dashboard

Status: implemented.

Phase marker: uploaded PDF no-text ops summary dashboard v0.

## Purpose

This gate makes uploaded PDF no-text failure candidates visible in the local operations surfaces after they are persisted as document metadata.

It does not add parsing capability.

It does not create failure cases automatically.

It does not judge whether a PDF should have extractable text.

## Runtime Surface

Routes:

```text
POST /documents/upload-chunks
GET /ops/summary
GET /ops/dashboard
```

New `GET /ops/summary` fields:

```text
chunk_handoff_no_chunks_count
pdf_no_text_failure_candidate_count
```

New `GET /ops/dashboard` metrics:

```text
No-text PDF Handoffs
PDF No-text Failure Candidates
```

The count is metadata-derived from document profile_json:

```text
document.status -> chunk_handoff_no_chunks
document.source_type -> pdf
document.profile_json.failure_case_candidate.failure_type -> pdf_no_extractable_text
```

## Test Evidence

Route test:

```text
apps/api/tests/test_routes.py::test_ops_summary_and_dashboard_surface_no_text_pdf_failure_candidate_counts
```

The test posts a valid blank uploaded PDF through:

```text
POST /documents/upload-chunks
```

Then verifies:

```text
document_count -> 1
chunk_handoff_no_chunks_count -> 1
pdf_no_text_failure_candidate_count -> 1
No-text PDF Handoffs
PDF No-text Failure Candidates
This is metadata-derived from document profile_json
```

## Allowed Claim

An operator can now see that at least one uploaded PDF produced a no-text handoff/failure-candidate state without manually inspecting the document row.

## Boundary

This is local metadata-count surfacing only.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not robust PDF extraction.

This is not OCR.

This is not table extraction.

This is not layout fidelity evidence.

This is not raw file storage.

This is not parsed text persistence.

This is not full parsed text persistence.

This is not automatic failure-case creation.

This is not Evidence Ledger generation.

This is not Noise Gate behavior.

This is not report generation.

This is not product-complete.

## Next Gate

External reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when `OPENAI_API_KEY` is configured by the owner, or another source-first product gate selected from `docs/GOAL.md`.
