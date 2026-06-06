# External-reader Proof Path Upload PDF Quality Preview Route Refresh

Status: implemented.

Phase marker: external-reader proof path upload PDF quality preview route refresh v0.

## Purpose

Surface the upload PDF quality preview proof chain in the repository-native reviewer path without claiming robust PDF extraction.

This is a focused intake proof route. It helps an external reviewer inspect whether born-digital and password-protected PDFs produce explicit quality observations through `POST /documents/upload-pdf-quality-preview` while staying preview-only and non-persistent.

## Routed Proof Artifacts

```text
docs/review/upload-pdf-quality-preview-api.md
docs/review/upload-pdf-quality-preview-runtime-smoke.md
docs/review/upload-pdf-quality-preview-runtime-smoke-remote-verification.md
```

## Route Markers

```text
POST /documents/upload-pdf-quality-preview
quality_boundary=pdf_quality_observation_preview_only_no_robust_extraction_claim
persistence_boundary=preview_only_not_persisted
document_count_delta=0
pdf_encrypted_requires_password
```

## Surfaces Refreshed

```text
docs/review/external-reader-proof-path.md
docs/review/external-reviewer-link-map.md
README.md
docs/GOAL.md
docs/runbook.md
docs/application/portfolio-index.md
apps/api/tests/test_docs.py
```

## Boundary

This is reader-route alignment only.

It is not new runtime evidence.

It is not a live issue body edit.

It is not external reviewer feedback.

It is not hosted deployment evidence.

It is not document persistence evidence for this preview route.

It is not retrieval behavior.

It is not Evidence Ledger generation.

It is not robust PDF extraction evidence.

It is not robust PDF extraction implementation.

It is not OCR implementation.

It is not table extraction implementation.

It is not decryption evidence.

It is not password bypass.

It is not product-complete.

The route points to preview-only quality observations and a password-required failure candidate. It does not prove encrypted PDFs can be decrypted, chunked, or used for trustworthy downstream retrieval.

## Next Gate

Remote verification for this route refresh after push, issue-body refresh if the public feedback issue should also route reviewers to this focused proof, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when `OPENAI_API_KEY` is configured by the owner, or another source-first product gate selected from current repository state.
