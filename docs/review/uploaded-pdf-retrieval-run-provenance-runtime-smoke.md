# Uploaded PDF Retrieval-run Provenance Runtime Smoke

Status: local runtime smoke evidence.

Phase marker: uploaded PDF retrieval-run provenance runtime smoke v0.

This smoke records local Docker PostgreSQL plus live FastAPI HTTP evidence that the Phase 347 uploaded PDF retrieval-run provenance path works against a running service.

It rebuilds the API container so the runtime includes the latest upload chunk metadata and document retrieval-run provenance code.

## Environment

```text
Docker version 29.4.3, build 055a478
Docker Compose version v5.1.3
API image -> sha256:d8b351ba139af10c61e11e47bc5b29816c1286eca7a0097fab4b2d435fdb1842
API started -> 2026-06-04T06:28:04.33069529Z
```

## Commands

```powershell
$env:POSTGRES_PORT='55432'
$env:API_PORT='8000'
docker compose config
docker compose --profile api up -d --build api
docker compose --profile api ps
cd apps/api
$env:DATABASE_URL='postgresql://noiseproof:noiseproof@localhost:55432/noiseproof'
uv run python -m app.migration_runner --status
```

HTTP smoke:

```text
GET /health
POST /documents/upload-chunks
POST /documents/{document_id}/retrieval-runs
GET /retrieval-runs
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
POST /documents/upload-chunks -> 201
POST /documents/{document_id}/retrieval-runs -> 201
GET /retrieval-runs -> 200
health_status -> ok
parser -> pdf-pymupdf
chunk_metadata_parser -> pdf-pymupdf
chunk_metadata_digital_pdf_text_extraction -> true
chunk_metadata_robust_pdf_extraction -> false
document_id -> 6d010f08-3b11-4bcc-b000-b357f5f2fede
chunk_count -> 1
retrieval_id -> 31cc3c61-a6d0-485b-b3e0-2ce9eb03fda2
retrieval_status -> completed
retrieval_result_count -> 1
retrieval_candidate_source_types -> pdf
retrieval_candidate_parsers -> pdf-pymupdf
retrieval_digital_pdf_text_extraction -> true
retrieval_robust_pdf_extraction -> false
source_provenance_boundary -> retrieval_run_candidate_chunk_metadata_only
latest_listed_id_matches -> true
listed_candidate_parsers -> pdf-pymupdf
first_candidate_parser -> pdf-pymupdf
first_candidate_text_contains_pdf_text -> true
raw_file_storage -> false
parsed_text_storage -> false
all_required_markers_passed -> true
```

## Allowed Claim

NoiseProof has local runtime evidence that uploaded digital PDF bytes can pass through PyMuPDF extraction into persisted chunk rows, and that a persisted document retrieval run can preserve PDF parser provenance in candidate metadata.

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

This is not Evidence Ledger generation.

This adds no Noise Gate behavior.

This adds no report generation.

This is not production readiness.

This is not product-complete.

## Next Gate

The next external evidence gate remains:

```text
external reviewer feedback v0
```
