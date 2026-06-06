# External Reviewer Request Brief Outreach Uploaded PDF Table Adapter Metadata Provenance Runtime Refresh

Status: implemented.

Phase marker: external reviewer request brief outreach uploaded PDF table adapter metadata provenance runtime refresh v0.

## Purpose

Make `docs/review/external-review-request.md`, `docs/review/external-reviewer-brief.md`, and `docs/review/external-reviewer-outreach-packet.md` point reviewers to the current uploaded-PDF table-adapter metadata provenance runtime proof chain.

This is a reviewer-request surface refresh only. It does not claim that any reviewer has responded.

## Updated Surfaces

```text
docs/review/external-review-request.md
docs/review/external-reviewer-brief.md
docs/review/external-reviewer-outreach-packet.md
```

## Route Markers

```text
Uploaded PDF table adapter metadata provenance runtime proof
docs/review/uploaded-pdf-table-adapter-metadata-provenance.md
docs/review/uploaded-pdf-table-adapter-metadata-provenance-runtime-smoke.md
docs/review/uploaded-pdf-table-adapter-metadata-provenance-runtime-smoke-remote-verification.md
docs/review/external-reader-proof-path-uploaded-pdf-table-adapter-metadata-provenance-runtime-route-refresh.md
docs/review/external-reader-proof-path-uploaded-pdf-table-adapter-metadata-provenance-runtime-route-refresh-remote-verification.md
POST /documents/upload-chunks
POST /documents/{document_id}/retrieval-runs
GET /retrieval-runs
default_pdf_parser_table_adapter_metadata
table_adapter.extracted_table_rows -> [[Segment, Growth], [Enterprise, 12%]]
table_extraction_performed remains false
source_provenance_boundary -> retrieval_run_candidate_chunk_metadata_only
```

## Boundary

This is reviewer navigation only.

It is not new runtime evidence.
It is not a live issue body edit.
It is not external reviewer feedback.
It is not hosted deployment evidence.
It is not customer validation.
It is not Braincrew acceptance.
It is not robust PDF extraction evidence.
It is not table extraction evidence for arbitrary market PDFs.
It is not Evidence Ledger generation.
It is not product-complete.

## Next Gate

Next gate: remote verification for this request/brief/outreach refresh after push, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from the current repository state.
