# Uploaded PDF Encrypted Failure Candidate Handoff Ops Runtime Smoke

Status: verified.

Phase marker: uploaded PDF encrypted failure candidate handoff ops runtime smoke v0.

## Purpose

Verify that the explicit encrypted PDF chunk handoff and operations count work through live FastAPI plus local PostgreSQL, not only route-level tests.

## Runtime Setup

The existing Docker `api` container was already using port `8000`, so the current local source tree was verified with:

```text
uv run uvicorn app.main:app --host 127.0.0.1 --port 8001
```

The smoke generated a temporary encrypted PDF with PyMuPDF:

```text
runtime-encrypted-handoff-phase675.pdf
byte_count -> 1460
user_pw -> user
owner_pw -> owner
encryption -> PDF_ENCRYPT_AES_256
```

The temporary PDF was deleted after the smoke.

## HTTP Evidence

Observed values:

```text
pre_pdf_encrypted_failure_candidate_count -> 0
POST /documents/upload-chunks -> 201
upload_status -> chunk_handoff_no_chunks
upload_failure_type -> pdf_encrypted_requires_password
upload_encrypted -> True
upload_password_required -> True
upload_extraction_scope -> encrypted_pdf_password_required
post_pdf_encrypted_failure_candidate_count -> 1
post_chunk_handoff_no_chunks_count -> 7
GET /ops/dashboard -> 200
dashboard -> PDF Encrypted Failure Candidates
dashboard -> does not prove decryption
```

The dashboard HTML contained:

```text
PDF Encrypted Failure Candidates
Encrypted PDF failure candidate counts are metadata-derived from document profile_json and does not prove decryption, password bypass, robust PDF extraction, OCR, table extraction, or layout fidelity.
```

## Boundary

This is local Docker PostgreSQL plus live FastAPI runtime evidence only.

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
external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
