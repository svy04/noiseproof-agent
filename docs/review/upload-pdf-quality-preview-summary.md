# Upload PDF Quality Preview Summary

Phase marker: upload PDF quality preview summary v0.

Status: implemented.

## Purpose

Add a compact `quality_summary` field to `POST /documents/upload-pdf-quality-preview` so reviewers can inspect the most important PDF quality boundary signals without reading the full `quality_observation.extracted_text` payload.

The summary is derived from the existing parser observation. It does not run a new parser, does not persist records, and does not claim better PDF extraction quality.

## Endpoint

```text
POST /documents/upload-pdf-quality-preview
```

## Implemented Code

```text
apps/api/app/schemas.py
apps/api/app/services/upload_pdf_quality_preview.py
apps/api/tests/test_routes.py
apps/api/tests/test_docs.py
```

## Response Field

```text
quality_summary
```

Summary markers:

```text
page_count
extracted_page_count
empty_page_count
digital_pdf_text_extraction
robust_pdf_extraction
encrypted
password_required
table_candidate_count
table_extraction_performed
failure_case_candidate
reviewer_boundary -> summary_only_not_robust_pdf_extraction_evidence
```

## Source-first Notes

The current parser path uses PyMuPDF for digital text and page-level diagnostics. PyMuPDF documents expose document-level metadata such as page counts and encryption/password state, while page APIs expose text extraction and table-candidate inspection surfaces.

Primary references:

```text
https://pymupdf.readthedocs.io/en/latest/document.html
https://pymupdf.readthedocs.io/en/latest/page.html
```

## Behavior

- Born-digital PDF preview returns `quality_summary.digital_pdf_text_extraction -> true`.
- Encrypted PDF preview returns `quality_summary.password_required -> true`.
- `quality_summary.robust_pdf_extraction` stays `false`.
- `quality_summary.table_extraction_performed` stays `false`.
- `quality_summary.reviewer_boundary` is always `summary_only_not_robust_pdf_extraction_evidence`.

## Boundary

This is response-shape inspectability only.

This is not extracted text storage.
This is not document persistence.
This is not retrieval behavior.
This is not Evidence Ledger generation.
This is not robust PDF extraction evidence.
This is not robust PDF extraction implementation.
This is not OCR implementation.
This is not table extraction implementation.
This is not decryption evidence.
This is not hosted deployment evidence.
This is not external reviewer feedback.
This is not customer validation.
This is not Braincrew acceptance.
This is not product-complete.

## Next Gate

Next gate: local test and remote workflow verification for this summary field after push, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when `OPENAI_API_KEY` is configured by the owner, or another source-first product gate selected from the current repository state.
