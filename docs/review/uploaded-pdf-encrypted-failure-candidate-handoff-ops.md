# Uploaded PDF Encrypted Failure Candidate Handoff Ops

Status: implemented.

Phase marker: uploaded PDF encrypted failure candidate handoff ops v0.

## Purpose

Make password-protected uploaded PDFs visible after the explicit chunk handoff path, not only in preview.

This keeps the downstream system from treating an encrypted PDF as an ordinary no-text PDF or silently hiding the password boundary from operations surfaces.

## Implemented Behavior

Route-level behavior:

```text
POST /documents/upload-chunks
parser -> pdf-pymupdf
chunks -> []
document.status -> chunk_handoff_no_chunks
failure_case_candidate.failure_type -> pdf_encrypted_requires_password
encrypted -> true
password_required -> true
digital_pdf_text_extraction -> false
robust_pdf_extraction -> false
extraction_scope -> encrypted_pdf_password_required
```

Operations behavior:

```text
GET /ops/summary
pdf_encrypted_failure_candidate_count -> count of persisted PDF documents whose profile_json failure candidate is pdf_encrypted_requires_password

GET /ops/dashboard
PDF Encrypted Failure Candidates -> displayed in the summary metric grid
```

The count is metadata-derived from persisted `documents.profile_json`.

## Why This Matters

Encrypted PDFs are not the same failure mode as scanned/image-only PDFs.

A password boundary should be visible to an operator before retrieval, Evidence Ledger, Noise Gate, or report stages make claims over missing text.

## Test Evidence

```text
uv run --project apps/api pytest -q apps/api/tests/test_routes.py::test_upload_chunks_ops_surface_encrypted_pdf_failure_candidate_counts
```

Expected markers:

```text
profile_json.failure_case_candidate.failure_type -> pdf_encrypted_requires_password
profile_json.encrypted -> true
profile_json.password_required -> true
profile_json.digital_pdf_text_extraction -> false
profile_json.extraction_scope -> encrypted_pdf_password_required
summary.pdf_encrypted_failure_candidate_count -> 1
dashboard -> PDF Encrypted Failure Candidates
```

## Boundary

This is local route and operations metadata behavior only.

It is not robust PDF extraction.

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
local Docker/FastAPI runtime smoke for uploaded PDF encrypted failure candidate handoff ops if runtime proof is needed, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
