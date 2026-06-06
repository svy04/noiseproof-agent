# Uploaded PDF Table Adapter Metadata Provenance

Status: implemented.

Phase marker: uploaded PDF table adapter metadata provenance v0.

## Purpose

Preserve the default `PdfParser` table-adapter metadata across the explicit
uploaded-PDF handoff path.

Before this gate, `PdfParser` could expose bounded `table_adapter` metadata, but
`POST /documents/upload-chunks` only copied the older PDF diagnostic whitelist
into persisted document and chunk metadata. That meant reviewers could inspect
the adapter output at parse time, but the metadata could disappear before
retrieval provenance.

## Implemented

```text
apps/api/app/routes/documents.py
apps/api/app/services/document_chunk_retrieval.py
apps/api/tests/test_routes.py
apps/api/tests/test_docs.py
```

Route surfaces covered:

```text
POST /documents/upload-chunks
POST /documents/{document_id}/retrieval-runs
```

Regression test:

```text
test_uploaded_pdf_table_adapter_metadata_flows_into_chunk_and_retrieval_provenance
```

The route test proves these metadata fields survive the handoff:

```text
default_pdf_parser_table_adapter_metadata
table_adapter
table_adapter_boundary
table_adapter_extraction_performed
```

Observed deterministic fixture markers:

```text
document.profile_json.default_pdf_parser_table_adapter_metadata -> true
chunk.metadata_json.default_pdf_parser_table_adapter_metadata -> true
retrieval_run.metadata_json.default_pdf_parser_table_adapter_metadata -> true
retrieval results metadata.default_pdf_parser_table_adapter_metadata -> true
table_adapter.table_extraction_engine -> pymupdf-find_tables-extract
table_adapter.extracted_table_rows -> [[Segment, Growth], [Enterprise, 12%]]
table_adapter.robust_pdf_extraction -> false
table_extraction_performed remains false
source_provenance_boundary -> retrieval_run_candidate_chunk_metadata_only
```

## Boundary

This is metadata provenance for a deterministic uploaded PDF fixture.

It is not robust PDF extraction evidence.
It is not table extraction evidence for arbitrary market PDFs.
It is not OCR implementation.
It is not layout fidelity evidence.
It is not raw upload storage.
It is not Evidence Ledger generation.
It is not Noise Gate behavior.
It is not final report generation.
It is not hosted deployment evidence.
It is not external reviewer feedback.
It is not product-complete.

## Next Gate

Next gate: local runtime smoke for this uploaded-PDF table-adapter metadata
provenance path, remote verification after push, external reviewer feedback v0
if qualifying outside feedback exists, or another source-first product gate
selected from the current repository state.
