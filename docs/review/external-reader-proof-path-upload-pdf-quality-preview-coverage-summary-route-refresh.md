# External-reader Proof Path Upload PDF Quality Preview Coverage Summary Route Refresh

Status: implemented.

Phase marker: external-reader proof path upload PDF quality preview coverage summary route refresh v0.

Purpose: route first-pass external reviewers to the current `quality_summary` coverage proof chain for `POST /documents/upload-pdf-quality-preview`.

This refresh makes page-level PDF coverage signals visible before reviewers inspect older summary-only or full observation payloads.

## Route

The external-reader proof path and external reviewer link map now surface this chain:

```text
docs/review/upload-pdf-quality-preview-api.md
docs/review/upload-pdf-quality-preview-summary.md
docs/review/upload-pdf-quality-preview-coverage-summary.md
docs/review/upload-pdf-quality-preview-coverage-summary-remote-verification.md
docs/review/upload-pdf-quality-preview-coverage-summary-runtime-smoke.md
docs/review/upload-pdf-quality-preview-coverage-summary-runtime-smoke-remote-verification.md
```

## Markers

```text
POST /documents/upload-pdf-quality-preview
quality_summary.page_coverage_ratio
quality_summary.extraction_status
full_text
partial_text
no_text
password_required
partial_page_coverage_ratio=0.5
partial_extraction_status=partial_text
partial_warning_present=True
no_text_extraction_status=no_text
encrypted_extraction_status=password_required
summary_only_not_robust_pdf_extraction_evidence
document_count_delta=0
pdf_encrypted_requires_password
```

## Boundary

This is reader-route alignment only.

It is not new runtime evidence, not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not customer validation, not Braincrew acceptance, not extracted text storage, not document persistence evidence for this preview route, not retrieval behavior, not Evidence Ledger generation, not robust PDF extraction evidence, not robust PDF extraction implementation, not OCR implementation, not table extraction implementation, not decryption evidence, and not product-complete.

Next gate: remote verification for this route refresh after push, live issue-body refresh only if the owner wants issue #1 to route to the coverage-summary proof chain, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from the current repository state.
