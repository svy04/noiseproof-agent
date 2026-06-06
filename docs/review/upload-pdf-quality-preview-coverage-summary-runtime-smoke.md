# Upload PDF Quality Preview Coverage Summary Runtime Smoke

Status: verified.

Phase marker: upload PDF quality preview coverage summary runtime smoke v0.

## Purpose

Record local Docker PostgreSQL plus live FastAPI HTTP evidence that `POST /documents/upload-pdf-quality-preview` returns coverage-summary fields for born-digital, partial-text, no-text, and encrypted PDF uploads.

This verifies the `quality_summary.page_coverage_ratio` and `quality_summary.extraction_status` response contract through a live local service path. It does not expand PDF parsing capability.

## Runtime Environment

```text
Docker version 29.4.3
Docker Compose version v5.1.3
Compose project: noiseproof-phase745
POSTGRES_PORT=55455
FastAPI URL: http://127.0.0.1:8116
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
phase745-born-digital.pdf_status=200
phase745-partial.pdf_status=200
phase745-no-text.pdf_status=200
phase745-encrypted.pdf_status=200
document_count_before=0
document_count_after=0
document_count_delta=0
born_digital_page_coverage_ratio=1.0
born_digital_extraction_status=full_text
born_digital_robust_pdf_extraction=False
born_digital_reviewer_boundary=summary_only_not_robust_pdf_extraction_evidence
partial_page_coverage_ratio=0.5
partial_extraction_status=partial_text
partial_warning_present=True
partial_robust_pdf_extraction=False
no_text_page_coverage_ratio=0.0
no_text_extraction_status=no_text
no_text_failure_case=pdf_no_extractable_text
no_text_robust_pdf_extraction=False
encrypted_page_coverage_ratio=0.0
encrypted_extraction_status=password_required
encrypted_failure_case=pdf_encrypted_requires_password
encrypted_password_required=True
encrypted_robust_pdf_extraction=False
summary_boundary=summary_only_not_robust_pdf_extraction_evidence
persistence_boundary=preview_only_not_persisted
```

Cleanup:

```text
uvicorn stopped
docker compose -p noiseproof-phase745 down -v -> completed
docker compose -p noiseproof-phase745 ps --format json -> no services
GET-NetTCPConnection -LocalPort 8116 -> no listening process
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
