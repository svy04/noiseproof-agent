# Uploaded PDF Page Diagnostics

Status: bounded product parser improvement.

Phase marker: uploaded PDF page diagnostics v0.

## Purpose

Add page-level diagnostics to the existing uploaded digital PDF text extraction path.

This makes PDF extraction easier to inspect before chunking, retrieval, or Evidence Ledger handoff.

It does not make PDF extraction robust.

## Primary Reference

PyMuPDF exposes text extraction through page-level `get_text()` calls and structured text dictionaries.

```text
https://pymupdf.readthedocs.io/en/latest/app1.html
```

## Implemented

```text
packages/ingestion/parsers/pdf.py records page diagnostics for uploaded PDF bytes
POST /documents/upload-preview returns diagnostics in metadata
apps/api/tests/test_routes.py covers PDF page diagnostics
apps/api/tests/test_docs.py covers the proof surface
```

Returned metadata:

```text
page_diagnostics_available
layout_block_diagnostics_available
extraction_scope: digital_text_page_diagnostics
page_text_char_counts
extracted_page_count
empty_page_count
text_block_count
image_block_count
```

Observed fixture behavior:

```text
parser: pdf-pymupdf
digital_pdf_text_extraction: true
robust_pdf_extraction: false
page_count: 1
page_text_char_counts: [39]
extracted_page_count: 1
empty_page_count: 0
text_block_count: 1
image_block_count: 0
```

## Boundary

This is digital PDF page diagnostics only.

It is not robust PDF extraction.

It is not OCR.

It is not table extraction.

It is not layout fidelity.

It is not raw file storage.

It is not parsed text persistence.

It is not retrieval quality evidence.

It is not Evidence Ledger generation.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, embedding generation, semantic retrieval quality evidence, LLM output, automatic failure-case creation, or product-complete.

## Tests

```text
uv run pytest -q tests/test_routes.py -k "pdf_page_diagnostics"
uv run pytest -q tests/test_docs.py -k "uploaded_pdf_page_diagnostics"
```

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, robust PDF extraction only after OCR/table/layout fidelity are explicitly tested, or another source-first product gate selected from docs/GOAL.md
```
