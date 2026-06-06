# Upload PDF Quality Preview Table Adapter Runtime Smoke

Status: verified.

Phase marker: upload PDF quality preview table adapter runtime smoke v0.

## Purpose

Record local Docker PostgreSQL plus live FastAPI HTTP evidence that `POST /documents/upload-pdf-quality-preview` returns the preview-only `quality_table_adapter` block for a deterministic born-digital PDF with a simple 2x2 table.

This verifies the adapter response path through the live local service. It does not promote table extraction into the default `PdfParser` behavior and does not expand the robust PDF extraction claim.

## Runtime Environment

```text
Docker version 29.4.3
Docker Compose version v5.1.3
Compose project: noiseproof-phase774
POSTGRES_PORT=55456
FastAPI URL: http://127.0.0.1:8117
```

## Migration State

Migration runner output for the runtime DB:

```text
Applied migrations: 23
Pending migrations: 0
Applied migrations: 23
Pending migrations: 0
Applied migrations: 23
Pending migrations: 0
```

## HTTP Smoke

```text
GET /health -> 200
table_adapter_upload_status=200
document_count_before=0
document_count_after=0
document_count_delta=0
quality_table_adapter_present=True
quality_table_adapter.table_extraction_engine=pymupdf-find_tables-extract
quality_table_adapter.table_rows_extracted=2
quality_table_adapter.table_cell_count=4
quality_table_adapter.rows=[['Segment', 'Growth'], ['Enterprise', '12%']]
quality_table_adapter.robust_pdf_extraction=False
quality_observation.table_extraction_performed=False
quality_summary.table_extraction_performed=False
persistence_boundary=preview_only_not_persisted
quality_boundary=pdf_quality_observation_preview_only_no_robust_extraction_claim
```

Cleanup:

```text
uvicorn stopped
docker compose -p noiseproof-phase774 down -v -> completed
docker compose -p noiseproof-phase774 ps -> no services
Get-NetTCPConnection -LocalPort 8117 -> no listening process
```

## Boundary

This is local runtime evidence only.

It is not default PdfParser table extraction.
It is not table extraction evidence for arbitrary market PDFs.
It is not robust PDF extraction evidence.
It is not robust PDF extraction implementation.
It is not OCR implementation.
It is not layout fidelity evidence.
It is not extracted text storage.
It is not document persistence evidence for the preview route.
It is not retrieval behavior.
It is not Evidence Ledger generation.
It is not hosted deployment evidence.
It is not external reviewer feedback.
It is not customer validation.
It is not Braincrew acceptance.
It is not product-complete.

## Next Gate

Next gate: remote verification for this runtime-smoke proof after push, a quality fixture/report update that evaluates the deterministic table fixture, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when `OPENAI_API_KEY` is configured by the owner, or another source-first product gate selected from the current repository state.
