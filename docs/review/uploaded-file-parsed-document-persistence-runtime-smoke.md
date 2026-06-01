# Uploaded File Parsed Document Persistence Runtime Smoke

Phase marker: uploaded file parsed document persistence runtime smoke v0.

This smoke records local runtime evidence for `POST /documents/upload-parsed-documents` against Docker PostgreSQL and a live FastAPI process.

## Commands Run

```text
docker compose config
docker compose up -d db
docker compose ps
uv run python -m app.migration_runner --status
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8033
GET /health
POST /documents/upload-parsed-documents
GET /documents
docker compose down
```

The shell needed an explicit runtime value:

```text
DATABASE_URL=postgresql://noiseproof:noiseproof@localhost:55432/noiseproof
```

Without that environment variable, the migration runner correctly failed with `DATABASE_URL is required`.

## Observed Runtime Result

Database:

```text
db_health=healthy
Applied migrations: 11
Pending migrations: 0
```

HTTP:

```text
GET /health -> 200
POST /documents/upload-parsed-documents -> 201
GET /documents -> 200
```

Persisted document observation:

```text
source_type -> markdown
source_uri -> upload://sample-note.md
filename -> sample-note.md
title -> Runtime uploaded market note
status -> parsed_metadata_only
extraction_quality -> high
persistence_boundary -> document_metadata_and_profile_only_no_raw_file_storage
raw_file_storage -> false
parsed_text_storage -> false
parser -> markdown
upload.byte_count -> 410
profile.recommended_strategy -> heading-aware
```

The persisted row id observed in this local volume was:

```text
56e5f36c-8dad-420f-bc92-9fae04071317
```

The `GET /documents` response also included an older local fixture row already present in the Docker volume. That older row is not part of this proof; the proof claim is limited to the newly persisted `upload://sample-note.md` row above.

## Boundaries

This is local runtime evidence, not hosted deployment evidence.

It is not external reviewer feedback, customer validation, Braincrew acceptance, robust PDF extraction, raw uploaded byte storage, parsed text persistence, persisted chunks, retrieval-run creation, Evidence Ledger generation, Noise Gate generation, report generation, LLM calls, embeddings, semantic retrieval, automatic failure-case creation, or a product-complete claim.

External reviewer feedback v0 remains open.
