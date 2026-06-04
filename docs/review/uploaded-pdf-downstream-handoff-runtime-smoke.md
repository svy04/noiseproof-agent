# Uploaded PDF Downstream Handoff Runtime Smoke

Status: local runtime smoke evidence.

Phase marker: uploaded PDF downstream handoff runtime smoke v0.

This smoke records local Docker PostgreSQL plus live FastAPI HTTP evidence that the Phase 341 uploaded PDF downstream handoff works against a running service.

It rebuilds the profiled API container so the runtime includes the latest `pymupdf` dependency and upload handoff code.

## Environment

```text
Docker version 29.4.3, build 055a478
Docker Compose version v5.1.3
API image -> sha256:15e2bdcc09724315d1f17a23e0bc163b9401f2e688de6787e668b25bf0bbf05b
API started -> 2026-06-04T05:11:38.835285408Z
```

## Commands

```powershell
docker compose config
docker compose --profile api up -d --build api
docker compose --profile api ps
cd apps/api
$env:DATABASE_URL="postgresql://noiseproof:noiseproof@localhost:55432/noiseproof"
uv run python -m app.migration_runner --status
```

HTTP smoke:

```text
GET /health
POST /documents/upload-preview
POST /documents/upload-chunk-preview
POST /documents/upload-chunks
GET /documents/{document_id}/chunks
POST /documents/upload-retrieval-preview
```

The PDF was generated in memory with PyMuPDF and uploaded as multipart `application/pdf`.

## Observed

```text
docker compose config -> exit 0
docker compose --profile api up -d --build api -> exit 0
docker compose --profile api ps -> db healthy, api up, api port 8000 published
Applied migrations: 16
Pending migrations: 0
GET /health -> 200
POST /documents/upload-preview -> 200
POST /documents/upload-chunk-preview -> 200
POST /documents/upload-chunks -> 201
GET /documents/{document_id}/chunks -> 200
POST /documents/upload-retrieval-preview -> 200
health_status -> ok
parser -> pdf-pymupdf
digital_pdf_text_extraction -> true
robust_pdf_extraction -> false
chunk_text_contains_pdf_text -> true
retrieval_text_contains_pdf_text -> true
replacement_decode_warning_present -> false
ocr_warning_present -> true
digital_text_warning_present -> true
document_id -> 2c743649-abdb-430f-a741-43fe92c2c794
upload_chunks_chunk_count -> 1
listed_chunk_count -> 1
upload_retrieval_preview_status -> completed
upload_retrieval_preview_result_count -> 1
explicit_upload_to_chunks_no_raw_file_storage
chunk_text_only_no_raw_file_storage
raw_file_storage -> false
parsed_text_storage -> false
all_required_markers_passed -> true
```

## Allowed Claim

NoiseProof has local runtime evidence that uploaded digital PDF bytes can pass through PyMuPDF extraction and then feed upload chunk preview, explicit upload-to-chunks persistence, listed chunk lookup, and upload retrieval preview through live FastAPI HTTP.

## Boundary / Non-claims

This is local runtime evidence only.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not robust PDF extraction.

This is digital PDF text only.

OCR, table extraction, and layout fidelity are not claimed.

This is not raw file storage.

This has no raw uploaded byte storage.

This is not full parsed text persistence.

This has no full parsed text persistence.

This adds no embeddings.

This adds no semantic retrieval quality evidence.

This adds no Evidence Ledger generation.

This adds no Noise Gate behavior.

This adds no report generation.

This is not production readiness.

This is not product-complete.

## Next Gate

The next external evidence gate remains:

```text
external reviewer feedback v0
```
