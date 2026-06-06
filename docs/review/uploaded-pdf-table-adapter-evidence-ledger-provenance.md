# Uploaded PDF Table Adapter Evidence Ledger Provenance

Status: implemented.

Phase marker: uploaded PDF table adapter Evidence Ledger provenance v0.

## Purpose

Prove that bounded default `PdfParser` table-adapter metadata can survive one
more handoff: from uploaded PDF chunk persistence, through document-chunk
retrieval, into persisted Evidence Ledger entry metadata.

This gate exists because the previous uploaded-PDF table-adapter provenance
proof stopped at persisted retrieval-run metadata. Reviewers could inspect that
the metadata reached retrieval candidates, but not that it reached persisted
Evidence Ledger rows.

## Implemented

```text
apps/api/app/services/retrieval_run_evidence.py
apps/api/tests/test_routes.py
apps/api/tests/test_docs.py
docs/review/uploaded-pdf-table-adapter-evidence-ledger-provenance.md
```

Route surfaces covered:

```text
POST /documents/upload-chunks
POST /documents/{document_id}/retrieval-runs
POST /retrieval-runs/{retrieval_run_id}/evidence-ledger
GET /evidence-ledgers?retrieval_run_id={retrieval_run_id}
```

Regression test:

```text
test_uploaded_pdf_table_adapter_metadata_flows_into_evidence_ledger_provenance
```

The route test proves these metadata fields survive into the stored Evidence
Ledger entry:

```text
default_pdf_parser_table_adapter_metadata
table_adapter
table_adapter_boundary
table_adapter_extraction_performed
```

Observed deterministic fixture markers:

```text
evidence_ledger_entry.metadata_json.default_pdf_parser_table_adapter_metadata -> true
evidence_ledger_entry.metadata_json.table_adapter_extraction_performed -> true
table_adapter.table_extraction_engine -> pymupdf-find_tables-extract
table_adapter.extracted_table_rows -> [[Segment, Growth], [Enterprise, 12%]]
table_adapter.robust_pdf_extraction -> false
table_extraction_performed remains false
source_provenance_boundary -> evidence_ledger_entry_metadata_from_retrieval_run_candidate_chunk
persistence_boundary -> retrieval_run_linked_evidence_ledger_no_llm_no_embeddings
```

The response warning now also exposes the boundary:

```text
Uploaded PDF table-adapter metadata is preserved in Evidence Ledger entry metadata as provenance only
```

## Boundary

This is deterministic metadata provenance for one synthetic uploaded PDF table
fixture.

It is not robust PDF extraction evidence.
It is not table extraction evidence for arbitrary market PDFs.
It is not OCR implementation.
It is not layout fidelity evidence.
It is not Evidence Ledger quality evidence.
It is not final truth adjudication.
It is not Noise Gate behavior.
It is not final report generation.
It is not hosted deployment evidence.
It is not external reviewer feedback.
It is not product-complete.

## Next Gate

Next gate: local runtime smoke for this uploaded-PDF table-adapter Evidence
Ledger provenance path, remote verification after push, external reviewer
feedback v0 if qualifying outside feedback exists, or another source-first
product gate selected from the current repository state.
