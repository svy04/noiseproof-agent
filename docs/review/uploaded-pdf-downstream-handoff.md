# Uploaded PDF Downstream Handoff

Status: bounded product handoff improvement.

Phase marker: uploaded PDF downstream handoff v0.

## Purpose

This gate reuses the Phase 340 uploaded digital PDF text extraction path in downstream upload handoffs.

Before this gate, `POST /documents/upload-preview` could extract digital PDF text with PyMuPDF, but upload chunk preview, explicit upload-to-chunks persistence, and upload retrieval preview still passed decoded PDF bytes into the parser path.

After this gate, the downstream upload handoffs share the same byte-aware parser helper and can carry `parser: pdf-pymupdf` output into chunking and lexical retrieval preview.

## Implemented

```text
apps/api/app/services/upload_preview.py exposes parse_uploaded_content
apps/api/app/services/upload_chunk_preview.py uses parse_uploaded_content
apps/api/app/services/upload_retrieval_preview.py uses parse_uploaded_content
packages/ingestion/types.py allows RetrievalSource.content_bytes
packages/ingestion/retrieval/lexical.py preserves content_bytes during parser selection
apps/api/tests/test_routes.py covers uploaded PDF chunk preview, upload-to-chunks handoff, and upload retrieval preview
```

API boundaries:

```text
POST /documents/upload-chunk-preview
POST /documents/upload-chunks
POST /documents/upload-retrieval-preview
```

Observed local test markers:

```text
parser: pdf-pymupdf
digital_pdf_text_extraction: true
robust_pdf_extraction: false
chunk text contains extracted digital PDF text
retrieval result text contains extracted digital PDF text
persistence_boundary: preview_only_not_persisted for preview routes
handoff_boundary: explicit_upload_to_chunks_no_raw_file_storage for POST /documents/upload-chunks
```

## Boundary

This is digital PDF text only.

OCR, table extraction, and layout fidelity are not claimed.

This is not robust PDF extraction.

This is not raw file storage.

This is not full parsed text persistence.

This is not embedding generation, semantic retrieval quality evidence, Evidence Ledger generation, Noise Gate behavior, or report generation.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation, Braincrew acceptance, production readiness, LLM output, automatic failure-case creation, or product-complete.

## Tests

```text
uv run pytest -q tests/test_routes.py -k "pdf_text_extraction_for_uploaded_pdf or chunks_from_uploaded_pdf"
uv run pytest -q tests/test_docs.py -k "uploaded_pdf_downstream_handoff"
```

## Next Gate

```text
external reviewer feedback v0 remains pending, or select the next source-first product gate
```
