# Uploaded PDF Encrypted Failure Candidate Runtime Smoke

Status: verified.

Phase marker: uploaded PDF encrypted failure candidate runtime smoke v0.

## Purpose

Verify that the encrypted uploaded PDF failure candidate works through the live FastAPI upload route, not only through route-level tests.

This confirms that a password-protected uploaded PDF is separated from generic no-text PDFs before retrieval, Evidence Ledger, Noise Gate, or report stages can overread missing text.

## Runtime Setup

The existing Docker `api` container was already using port `8000`, so the current local source tree was verified with:

```text
uv run uvicorn app.main:app --host 127.0.0.1 --port 8001
```

The smoke generated a temporary encrypted PDF with PyMuPDF:

```text
runtime-encrypted-phase673.pdf
byte_count -> 1444
user_pw -> user
owner_pw -> owner
encryption -> PDF_ENCRYPT_AES_256
```

The temporary PDF was deleted after the smoke.

## HTTP Evidence

Command shape:

```text
curl.exe -s -F "file=@runtime-encrypted-phase673.pdf;type=application/pdf" -F "source_type=pdf" http://127.0.0.1:8001/documents/upload-preview
```

Observed route result:

```text
POST /documents/upload-preview -> 200
source_type -> pdf
parser -> pdf-pymupdf
text -> ""
metadata.robust_pdf_extraction -> false
metadata.text_only_fallback -> false
metadata.digital_pdf_text_extraction -> false
metadata.encrypted -> true
metadata.password_required -> true
metadata.page_count -> 1
metadata.page_diagnostics_available -> false
metadata.layout_block_diagnostics_available -> false
metadata.extraction_scope -> encrypted_pdf_password_required
metadata.extracted_page_count -> 0
metadata.empty_page_count -> 1
metadata.table_candidate_diagnostics_available -> false
metadata.table_extraction_performed -> false
failure_case_candidate.failure_type -> pdf_encrypted_requires_password
persistence_boundary -> preview_only_not_persisted
filename -> runtime-encrypted-phase673.pdf
content_type -> application/pdf
byte_count -> 1444
```

Observed warnings included:

```text
Upload preview is preview-only and does not create documents or persist parse records.
File upload preview does not claim robust PDF extraction.
PDF text extraction uses PyMuPDF for digital text only; OCR, table extraction, and layout fidelity are not claimed.
PDF is encrypted and requires a password; text extraction was not performed.
```

## Boundary

This is local FastAPI runtime evidence only.

It is not robust PDF extraction.

It is not OCR.

It is not table extraction.

It is not layout fidelity.

It is not decryption.

It does not bypass password protection.

It does not store raw file bytes.

It does not persist parsed text.

It does not create a `documents` row.

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
