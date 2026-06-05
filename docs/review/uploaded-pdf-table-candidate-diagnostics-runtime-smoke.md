# Uploaded PDF Table-candidate Diagnostics Runtime Smoke

Status: local runtime smoke evidence.

Phase marker: uploaded PDF table-candidate diagnostics runtime smoke v0.

This document records local Docker PostgreSQL plus live FastAPI HTTP evidence that `POST /documents/upload-preview` returns PyMuPDF table-candidate diagnostics for one uploaded digital PDF fixture.

It is a runtime smoke record for one small fixture, not a broad PDF parsing or table extraction claim.

## Environment

Observed runtime:

```text
Docker version 29.4.3, build 055a478
Docker Compose version v5.1.3
API image -> noiseproof-agent-api@sha256:ec7ffc44e2b71f649fb0fc970c9af356d41831a2dae1fbf1bdab98e864e8ea40
API started -> 2026-06-05T20:16:15.477344356Z
noiseproof-agent-db -> healthy
noiseproof-agent-api -> Up, 0.0.0.0:8000->8000/tcp
Applied migrations: 23
Pending migrations: 0
```

## Commands

Representative commands:

```powershell
docker compose --profile api up -d --build api
docker compose --profile api ps
$env:DATABASE_URL = "postgresql://noiseproof:noiseproof@localhost:55432/noiseproof"
uv run --project apps/api python -m app.migration_runner --status
```

HTTP checks used the live API:

```text
GET /health
POST /documents/upload-preview
GET /documents before and after the preview request
```

The PDF was generated in memory with PyMuPDF, using drawn grid lines and text labels to create one simple table-shaped candidate.

## Observed Results

```text
GET /health -> 200
health_status -> ok
POST /documents/upload-preview -> 200
parser -> pdf-pymupdf
digital_pdf_text_extraction -> true
robust_pdf_extraction -> false
table_candidate_diagnostics_available -> true
table_candidate_count -> 1
table_candidate_page_counts -> [1]
table_candidate_shapes -> page_index=0,row_count=2,col_count=2,cell_count=4
table_extraction_performed -> false
text_contains_segment -> true
text_contains_enterprise -> true
table_candidate_warning_present -> true
table_content_extraction_warning_present -> true
generic_table_extraction_warning_present -> true
before_document_count -> 1
after_document_count -> 1
document_count_delta -> 0
persistence_boundary -> preview_only_not_persisted
```

## Allowed Claim

`POST /documents/upload-preview` emitted table-candidate diagnostics for one uploaded digital PDF through local Docker/FastAPI runtime verification.

## Boundaries

This is local runtime evidence only.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not robust PDF extraction.

This is not OCR.

This is not table extraction.

This does not extract table contents.

This is not layout fidelity.

This is not raw file storage.

This is not parsed text persistence.

This is not retrieval quality evidence.

This is not Evidence Ledger generation.

This is not Noise Gate behavior.

This is not report generation.

This is not product-complete.

## Next Gate

Next recommended gate: downstream provenance runtime smoke for uploaded PDF table-candidate diagnostics if retrieval candidate proof is needed, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when `OPENAI_API_KEY` is configured by the owner, or another source-first product gate selected from `docs/GOAL.md`.
