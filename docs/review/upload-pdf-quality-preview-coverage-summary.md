# Upload PDF Quality Preview Coverage Summary

Phase marker: upload PDF quality preview coverage summary v0.

Status: implemented.

## Purpose

Add page-level coverage signals to the compact `quality_summary` returned by `POST /documents/upload-pdf-quality-preview`.

This makes partial digital-text extraction visible before reviewers read the full `quality_observation` payload. A PDF with text on only some pages now surfaces that boundary as coverage metadata instead of looking like a fully extracted PDF.

## Endpoint

```text
POST /documents/upload-pdf-quality-preview
```

## Implemented Code

```text
apps/api/app/services/upload_pdf_quality_preview.py
apps/api/tests/test_routes.py
apps/api/tests/test_docs.py
docs/review/upload-pdf-quality-preview-summary.md
```

## Response Fields

```text
quality_summary.page_coverage_ratio
quality_summary.extraction_status
```

Status values:

```text
full_text
partial_text
no_text
password_required
unknown
```

## Behavior

- `quality_summary.page_coverage_ratio` is calculated from extracted text pages divided by total pages.
- `quality_summary.extraction_status -> full_text` means every counted page produced digital text.
- `quality_summary.extraction_status -> partial_text` means at least one counted page produced no digital text.
- `quality_summary.extraction_status -> no_text` means no counted page produced digital text or the parser reported `pdf_no_extractable_text`.
- `quality_summary.extraction_status -> password_required` means the PDF requires a password and is not decrypted by this preview.
- Partial extraction adds a warning containing `partial PDF text extraction`.
- `quality_summary.reviewer_boundary` remains `summary_only_not_robust_pdf_extraction_evidence`.

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

Next gate: remote verification for this coverage summary after push, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when `OPENAI_API_KEY` is configured by the owner, or another source-first product gate selected from the current repository state.
