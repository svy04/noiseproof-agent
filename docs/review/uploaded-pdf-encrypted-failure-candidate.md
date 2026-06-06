# Uploaded PDF Encrypted Failure Candidate

Status: implemented.

Phase marker: uploaded PDF encrypted failure candidate v0.

## Purpose

Separate encrypted uploaded PDFs from generic no-text PDFs before any retrieval, Evidence Ledger, Noise Gate, or report step tries to use them.

This makes a common messy-input failure mode inspectable without claiming robust PDF extraction.

## Implemented Behavior

Route-level behavior:

```text
POST /documents/upload-preview
parser -> pdf-pymupdf
encrypted -> true
password_required -> true
digital_pdf_text_extraction -> false
robust_pdf_extraction -> false
extraction_scope -> encrypted_pdf_password_required
failure_case_candidate.failure_type -> pdf_encrypted_requires_password
```

When PyMuPDF opens an uploaded PDF and reports that a password is required, NoiseProof now returns an empty text result with a structured failure-case candidate instead of falling through to the text fallback parser.

## Why This Matters

Encrypted PDFs are a different failure mode from scanned or image-only PDFs.

The system should not treat a password boundary as ordinary extraction weakness, and it should not allow downstream stages to pretend that the missing text was inspected.

## Test Evidence

```text
uv run --project apps/api pytest -q apps/api/tests/test_routes.py::test_document_upload_preview_surfaces_encrypted_pdf_failure_candidate_without_robust_claim
```

Expected markers:

```text
parser -> pdf-pymupdf
metadata.encrypted -> true
metadata.password_required -> true
metadata.digital_pdf_text_extraction -> false
metadata.extraction_scope -> encrypted_pdf_password_required
failure_case_candidate.failure_type -> pdf_encrypted_requires_password
```

## Boundary

This does not claim robust PDF extraction.

It is not OCR.

It is not table extraction.

It is not layout fidelity.

It is not decryption.

It does not bypass password protection.

It does not store raw file bytes.

It does not persist parsed text.

It does not create a `failure_cases` row automatically.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not customer validation.

It is not Braincrew acceptance.

It is not product-complete.

## Next Gate

```text
local Docker/FastAPI runtime smoke for uploaded PDF encrypted failure candidate if runtime proof is needed, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
