# External Review Issue Body Uploaded PDF Table Adapter Evidence Ledger Provenance Runtime Route Refresh

Status: implemented.

Phase marker: external review issue body uploaded PDF table adapter Evidence Ledger provenance runtime route refresh v0.

## Purpose

Record the owner-authored GitHub issue #1 body update that routes `Latest Proof To Inspect` to the uploaded PDF table-adapter Evidence Ledger provenance runtime proof chain.

Issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

## Observed Issue State

```text
updatedAt: 2026-06-06T23:33:08Z
comment_count: 1
starts_with_request: true
first_codepoint: 35
has_leading_bom: false
```

## Route Markers

```text
has_uploaded_pdf_table_adapter_evidence_ledger_provenance: true
has_uploaded_pdf_table_adapter_evidence_ledger_provenance_runtime_smoke: true
has_uploaded_pdf_table_adapter_evidence_ledger_provenance_runtime_smoke_remote_verification: true
has_external_reader_uploaded_pdf_table_adapter_evidence_ledger_provenance_runtime_route_refresh: true
has_external_reader_uploaded_pdf_table_adapter_evidence_ledger_provenance_runtime_route_refresh_remote_verification: true
old_uploaded_pdf_table_adapter_metadata_latest_label_present: false
POST /documents/upload-chunks
POST /documents/{document_id}/retrieval-runs
POST /retrieval-runs/{retrieval_run_id}/evidence-ledger
GET /evidence-ledgers?retrieval_run_id={retrieval_run_id}
default_pdf_parser_table_adapter_metadata
table_adapter.extracted_table_rows -> [['Segment', 'Growth'], ['Enterprise', '12%']]
table_extraction_performed remains false
source_provenance_boundary -> evidence_ledger_entry_metadata_from_retrieval_run_candidate_chunk
```

## Boundary

This is owner-authored issue body routing only.

It is not external reviewer feedback.
It is not new runtime evidence.
It is not hosted deployment evidence.
It is not robust PDF extraction evidence.
It is not robust PDF extraction implementation.
It is not OCR implementation.
It is not default PdfParser table extraction.
It is not table extraction evidence for arbitrary market PDFs.
It is not Evidence Ledger quality evidence.
It is not final truth adjudication.
It is not customer validation.
It is not Braincrew acceptance.
It is not product-complete.

## Next Gate

Next gate: external-feedback current-state verification for this issue route, remote verification for this issue-body refresh after push, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from the current repository state.
