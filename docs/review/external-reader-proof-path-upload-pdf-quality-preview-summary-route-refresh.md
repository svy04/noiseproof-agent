# External-reader Proof Path Upload PDF Quality Preview Summary Route Refresh

Status: implemented.

Phase marker: external-reader proof path upload PDF quality preview summary route refresh v0.

Purpose: route first-pass external reviewers to the compact `quality_summary` proof chain for `POST /documents/upload-pdf-quality-preview` before they inspect the full extracted-text quality observation payload.

## Route

The external-reader proof path and external reviewer link map now surface this chain:

```text
docs/review/upload-pdf-quality-preview-api.md
docs/review/upload-pdf-quality-preview-summary.md
docs/review/upload-pdf-quality-preview-summary-remote-verification.md
docs/review/upload-pdf-quality-preview-summary-runtime-smoke.md
docs/review/upload-pdf-quality-preview-summary-runtime-smoke-remote-verification.md
```

## Markers

```text
POST /documents/upload-pdf-quality-preview
quality_summary
summary_only_not_robust_pdf_extraction_evidence
digital_quality_summary_present=True
encrypted_quality_summary_present=True
digital_summary_robust_pdf_extraction=False
encrypted_summary_failure_case=pdf_encrypted_requires_password
document_count_delta=0
pdf_encrypted_requires_password
```

## Boundary

This is reader-route alignment only.

It is not new runtime evidence, not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not customer validation, not Braincrew acceptance, not extracted text storage, not document persistence evidence for this preview route, not retrieval behavior, not Evidence Ledger generation, not robust PDF extraction evidence, not robust PDF extraction implementation, not OCR implementation, not table extraction implementation, not decryption evidence, and not product-complete.

Next gate: remote verification for this route refresh after push, live issue-body refresh only if the owner wants issue #1 to route to the summary proof chain, or external reviewer feedback v0 if qualifying outside feedback exists.
