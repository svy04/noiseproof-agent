# External-reader Proof Path Uploaded PDF Table Adapter Metadata Provenance Runtime Route Refresh

Status: implemented.

Phase marker: external-reader proof path uploaded PDF table adapter metadata provenance runtime route refresh v0.

## Purpose

Route first-pass external reviewers to the Phase 795/796/797/798 uploaded PDF table-adapter metadata provenance proof chain without making any new runtime, extraction, or Evidence Ledger claim.

This refresh makes the latest uploaded-PDF persistence and retrieval-candidate provenance path easier to inspect from the compact proof path, link map, and 90-second shortlist.

## Updated Artifacts

```text
docs/review/external-reader-proof-path.md
docs/review/external-reviewer-link-map.md
docs/review/external-reviewer-shortlist.md
README.md
docs/GOAL.md
docs/runbook.md
docs/application/portfolio-index.md
apps/api/tests/test_docs.py
```

## Routed Proof Chain

```text
docs/review/uploaded-pdf-table-adapter-metadata-provenance.md
docs/review/uploaded-pdf-table-adapter-metadata-provenance-remote-verification.md
docs/review/uploaded-pdf-table-adapter-metadata-provenance-runtime-smoke.md
docs/review/uploaded-pdf-table-adapter-metadata-provenance-runtime-smoke-remote-verification.md
POST /documents/upload-chunks
POST /documents/{document_id}/retrieval-runs
GET /retrieval-runs
apps/api/app/routes/documents.py
apps/api/app/services/document_chunk_retrieval.py
```

## Route Markers

```text
POST /documents/upload-chunks
POST /documents/{document_id}/retrieval-runs
GET /retrieval-runs
default_pdf_parser_table_adapter_metadata
table_adapter_boundary
table_adapter.extracted_table_rows -> [[Segment, Growth], [Enterprise, 12%]]
table_extraction_performed remains false
source_provenance_boundary -> retrieval_run_candidate_chunk_metadata_only
document_profile_default_pdf_parser_table_adapter_metadata -> true
chunk_metadata_default_pdf_parser_table_adapter_metadata -> true
retrieval_metadata_default_pdf_parser_table_adapter_metadata -> true
retrieval_candidate_default_pdf_parser_table_adapter_metadata -> true
CI run `27075457410`
External Feedback Screen run `27075457400`
remote verification follow-up CI run `27075534491`
remote verification follow-up External Feedback Screen run `27075534480`
```

## Boundary

This is reviewer route hygiene only.

It is not new runtime evidence.
It is not the runtime smoke itself.
It is not robust PDF extraction evidence.
It is not robust PDF extraction implementation.
It is not OCR implementation.
It is not default PdfParser table extraction.
It is not table extraction evidence for arbitrary market PDFs.
It is not Evidence Ledger generation.
It is not final truth adjudication.
It is not hosted deployment evidence.
It is not external reviewer feedback.
It is not customer validation.
It is not Braincrew acceptance.
It is not product-complete.

## Next Gate

Next gate: remote verification for this reader-route refresh after push, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from the current repository state.
