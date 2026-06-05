# Uploaded PDF Page Diagnostics Runtime Smoke

Status: local runtime smoke evidence.

Phase marker: uploaded PDF page diagnostics runtime smoke v0.

This document records local Docker plus live FastAPI HTTP evidence that `POST /documents/upload-preview` returns uploaded digital PDF page diagnostics. It is a runtime smoke record for one small fixture, not a broad PDF parsing claim.

## Environment

Observed runtime:

```text
Docker version 29.4.3, build 055a478
Docker Compose version v5.1.3
API image -> sha256:fd6184cf0cf27afc0ffa664a13b3f72f49f693d65d7447d6d76b15a45f212523
API started -> 2026-06-05T10:44:19.556179505Z
noiseproof-agent-db -> healthy
noiseproof-agent-api -> Up, 0.0.0.0:8000->8000/tcp
Applied migrations: 23
Pending migrations: 0
```

## Commands

Representative commands:

```powershell
docker compose config
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

## Observed Results

```text
docker compose config -> exit 0
docker compose --profile api up -d --build api -> exit 0
docker compose --profile api ps -> db healthy, api up, api port 8000 published
GET /health -> 200
POST /documents/upload-preview -> 200
health_status -> ok
workflow_version -> phase40-lineage-warning-code-dashboard
parser -> pdf-pymupdf
digital_pdf_text_extraction -> true
robust_pdf_extraction -> false
page_diagnostics_available -> true
layout_block_diagnostics_available -> true
extraction_scope -> digital_text_page_diagnostics
page_count -> 1
page_text_char_counts -> [39]
extracted_page_count -> 1
empty_page_count -> 0
text_block_count -> 1
image_block_count -> 0
text_contains_pdf_text -> true
ocr_warning_present -> true
table_warning_present -> true
layout_warning_present -> true
before_document_count -> 16
after_document_count -> 16
document_count_delta -> 0
persistence_boundary -> preview_only_not_persisted
```

## Allowed Claim

`POST /documents/upload-preview` emitted page-level diagnostics for one uploaded digital-text PDF through local Docker/FastAPI runtime verification.

## Boundaries

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not robust PDF extraction.

This is not OCR.

This is not table extraction.

This is not layout fidelity.

This is not raw file storage.

This is not parsed text persistence.

This is not retrieval quality evidence.

This is not Evidence Ledger generation.

This is not Noise Gate behavior.

This is not report generation.

This is not product-complete.

## Next Gate

Next recommended gate: external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when `OPENAI_API_KEY` is configured by the owner, or another source-first product gate selected from `docs/GOAL.md`.
