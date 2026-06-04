# Uploaded PDF Text Extraction

Status: bounded product parser improvement.

Phase marker: uploaded PDF text extraction v0.

## Purpose

This gate adds a small, inspectable PDF text extraction path for uploaded digital PDFs.

Before this gate, PDF handling was a text-only fallback: callers had to provide already-extracted text, and binary-looking PDF input produced a warning/failure candidate.

After this gate, `POST /documents/upload-preview` can pass uploaded PDF bytes to the parser and extract digital text with PyMuPDF.

## Primary Reference

PyMuPDF documents the basic text extraction path as opening a document and calling page text extraction methods.

```text
https://pymupdf.readthedocs.io/en/latest/the-basics.html
```

## Implemented

```text
apps/api/pyproject.toml adds pymupdf
apps/api/uv.lock records pymupdf
packages/ingestion/types.py adds ParseInput.content_bytes
packages/ingestion/selector.py preserves content_bytes during parser selection
packages/ingestion/parsers/pdf.py adds pdf-pymupdf extraction for uploaded bytes
apps/api/app/services/upload_preview.py passes uploaded bytes into parse_document
apps/api/tests/test_routes.py covers upload-preview PDF extraction
```

API boundary:

```text
POST /documents/upload-preview
```

Observed behavior in test:

```text
parser: pdf-pymupdf
digital_pdf_text_extraction: true
robust_pdf_extraction: false
page_count: 1
persistence_boundary: preview_only_not_persisted
```

## Boundary

This is digital PDF text only.

OCR, table extraction, and layout fidelity are not claimed.

This is not robust PDF extraction.

This is not raw file storage.

This is not parsed text persistence.

This is not retrieval, Evidence Ledger generation, Noise Gate behavior, or report generation.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation, Braincrew acceptance, production readiness, embedding generation, semantic retrieval quality evidence, LLM output, automatic failure-case creation, or product-complete.

## Tests

```text
uv run pytest -q tests/test_routes.py -k "pdf_text or pdf_is_text_only"
uv run pytest -q tests/test_docs.py -k "uploaded_pdf_text"
```

## Next Gate

```text
external reviewer feedback v0 remains pending, or select the next source-first product gate
```
