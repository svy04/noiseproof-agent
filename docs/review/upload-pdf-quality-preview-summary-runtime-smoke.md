# Upload PDF Quality Preview Summary Runtime Smoke

Status: verified.

Phase marker: upload PDF quality preview summary runtime smoke v0.

## Purpose

Record local Docker PostgreSQL plus live FastAPI HTTP evidence that `POST /documents/upload-pdf-quality-preview` returns the new `quality_summary` field for born-digital and encrypted PDF uploads while preserving the preview-only and no-robust-PDF-extraction boundaries.

## Runtime Environment

```text
Docker version 29.4.3
Docker Compose version v5.1.3
Compose project: noiseproof-phase724
POSTGRES_PORT=55454
FastAPI URL: http://127.0.0.1:8115
```

## Migration State

Fresh DB migration runner output:

```text
Applied migrations: 0
Pending migrations: 23
Applied migrations: 23
Pending migrations: 0
```

## HTTP Smoke

```text
GET /health -> 200
phase724-born-digital.pdf_status=200
phase724-encrypted.pdf_status=200
document_count_before=0
document_count_after=0
document_count_delta=0
digital_quality_summary_present=True
digital_summary_boundary=summary_only_not_robust_pdf_extraction_evidence
digital_summary_page_count=1
digital_summary_extracted_page_count=1
digital_summary_digital_pdf_text_extraction=True
digital_summary_robust_pdf_extraction=False
digital_summary_table_extraction_performed=False
encrypted_quality_summary_present=True
encrypted_summary_boundary=summary_only_not_robust_pdf_extraction_evidence
encrypted_summary_password_required=True
encrypted_summary_robust_pdf_extraction=False
encrypted_summary_failure_case=pdf_encrypted_requires_password
```

Cleanup:

```text
uvicorn stopped
docker compose -p noiseproof-phase724 down -v -> completed
docker compose -p noiseproof-phase724 ps --format json -> no services
```

## Boundary

This is local runtime evidence only.

It is not hosted deployment evidence.
It is not external reviewer feedback.
It is not customer validation.
It is not Braincrew acceptance.
It is not extracted text storage.
It is not document persistence evidence for the preview route.
It is not retrieval behavior.
It is not Evidence Ledger generation.
It is not robust PDF extraction evidence.
It is not robust PDF extraction implementation.
It is not OCR implementation.
It is not table extraction implementation.
It is not decryption evidence.
It is not product-complete.

## Next Gate

Next gate: remote verification for this runtime-smoke proof after push, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when `OPENAI_API_KEY` is configured by the owner, or another source-first product gate selected from the current repository state.
