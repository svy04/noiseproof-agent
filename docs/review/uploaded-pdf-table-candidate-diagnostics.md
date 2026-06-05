# Uploaded PDF Table-candidate Diagnostics

Status: bounded product parser improvement.

Phase marker: uploaded PDF table-candidate diagnostics v0.

## Purpose

Add table-candidate diagnostics to the existing uploaded digital PDF preview path.

This makes a PDF easier to inspect before chunking, retrieval, or Evidence Ledger handoff by showing whether PyMuPDF sees table-shaped candidates on the page.

It does not extract table contents.

It does not make PDF extraction robust.

## Primary Reference

PyMuPDF documents `Page.find_tables()` as the page-level API for locating tables. This phase uses that API only for candidate diagnostics.

```text
https://pymupdf.readthedocs.io/en/latest/the-basics.html#extracting-tables-from-a-page
https://pymupdf.readthedocs.io/en/latest/page.html
```

## Implemented

```text
packages/ingestion/parsers/pdf.py records table-candidate diagnostics for uploaded PDF bytes
POST /documents/upload-preview returns candidate diagnostics in metadata
apps/api/app/routes/documents.py allows the same metadata into explicit upload-to-chunks handoff
apps/api/app/services/document_chunk_retrieval.py allows the same metadata into retrieval candidate provenance
apps/api/tests/test_routes.py covers uploaded PDF table-candidate diagnostics
apps/api/tests/test_docs.py covers the proof surface
```

Returned metadata:

```text
table_candidate_diagnostics_available
table_candidate_count
table_candidate_page_counts
table_candidate_shapes
table_extraction_performed: false
```

Observed fixture behavior:

```text
parser: pdf-pymupdf
digital_pdf_text_extraction: true
robust_pdf_extraction: false
table_candidate_diagnostics_available: true
table_candidate_count: 1
table_candidate_page_counts: [1]
table_candidate_shapes:
  - page_index: 0
    row_count: 2
    col_count: 2
    cell_count: 4
table_extraction_performed: false
```

Warning boundary:

```text
PyMuPDF table candidate diagnostics found potential tables but does not extract table contents.
```

## Boundary

This is table-candidate diagnostics only.

It is not table extraction.

It does not extract table contents.

It is not OCR.

It is not layout fidelity.

It is not robust PDF extraction.

It is not raw file storage.

It is not parsed text persistence.

It is not retrieval quality evidence.

It is not Evidence Ledger generation.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, embedding generation, semantic retrieval quality evidence, LLM output, automatic failure-case creation, or product-complete.

## Tests

```text
uv run pytest -q tests/test_routes.py::test_document_upload_preview_exposes_pdf_table_candidate_diagnostics_without_table_extraction_claim
uv run pytest -q tests/test_docs.py::test_uploaded_pdf_table_candidate_diagnostics_is_documented_without_table_extraction_claim
```

## Next Gate

```text
local Docker/FastAPI runtime smoke for uploaded PDF table-candidate diagnostics if runtime proof is needed, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
