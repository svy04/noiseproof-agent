# Uploaded File Chunk Persistence Handoff Runtime Smoke

Status: local runtime smoke evidence.

Phase marker: uploaded file chunk persistence handoff runtime smoke v0.

Label: Uploaded file chunk persistence handoff runtime smoke.

This artifact records local Docker PostgreSQL plus live FastAPI HTTP evidence for the explicit upload-to-chunks handoff endpoint.

## Commands

```powershell
docker compose config
docker compose up -d db
docker compose ps
cd apps/api
$env:DATABASE_URL="postgresql://noiseproof:noiseproof@localhost:55432/noiseproof"
uv run python -m app.migration_runner --status
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8034
```

HTTP smoke:

```text
GET /health
POST /documents/upload-chunks
GET /documents
GET /documents/{document_id}/chunks
```

## Observed

```text
docker compose config -> exit 0
docker compose up -d db -> db healthy
Applied migrations: 12
Pending migrations: 0
GET /health -> 200
POST /documents/upload-chunks -> 201
GET /documents -> 200
GET /documents/{document_id}/chunks -> 200
document_id -> 04d2fdab-dfcf-4ae1-a6ed-d7d10277e729
upload_chunk_count -> 4
listed_chunk_count -> 4
chunk_count_for_created_document -> 4
document_count_after_upload_chunks -> 4
chunk_count_after_upload_chunks -> 5
explicit_upload_to_chunks_no_raw_file_storage
chunk_text_only_no_raw_file_storage
raw_file_storage -> false
parsed_text_storage -> false
```

`document_count_after_upload_chunks` and `chunk_count_after_upload_chunks` are cumulative for the existing local Docker database volume. The created document's own chunk count was verified separately as `4`.

## Allowed Claim

NoiseProof has local runtime evidence that `POST /documents/upload-chunks` can create a document metadata row and derived chunk rows against the local Docker PostgreSQL database through live FastAPI HTTP.

## Boundary / Non-claims

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not raw uploaded byte storage.

This has no raw uploaded byte storage.

This is not full parsed text persistence.

This has no full parsed text persistence.

This adds no embeddings.

This adds no retrieval persistence.

This adds no Evidence Ledger persistence.

This adds no Noise Gate persistence.

This adds no report persistence.

This is not robust PDF extraction.

This is not semantic retrieval.

This is not product-complete.

## Next Gate

The next external evidence gate remains:

```text
external reviewer feedback v0
```
