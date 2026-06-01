# Uploaded File Intake Manifest Runtime Smoke

Phase marker: uploaded file intake manifest runtime smoke v0.

## Purpose

This packet records local HTTP evidence for the uploaded file intake manifest preview endpoint.

It verifies the endpoint can run against a live local FastAPI server while keeping uploaded content preview-only and not persisted.

## Runtime context

Date: 2026-06-01

Local-only runtime:

- Docker DB service: `noiseproof-agent-db`
- PostgreSQL image: `pgvector/pgvector:pg16`
- DB port: `55432 -> 5432`
- FastAPI URL: `http://127.0.0.1:8031`
- Uploaded fixture: `examples/messy-market-data/sample-note.md`

Commands used:

```powershell
docker compose up -d db
docker compose ps
cd apps/api
uv run python -m app.migration_runner --database-url postgresql://noiseproof:noiseproof@localhost:55432/noiseproof --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8031
```

Migration runner status before HTTP smoke:

```text
Applied migrations: 10
Pending migrations: 0
```

## HTTP smoke path

The local server was called with:

```powershell
curl.exe -s http://127.0.0.1:8031/health

curl.exe -s -X POST http://127.0.0.1:8031/documents/upload-intake-manifest-preview `
  -F "source_type=markdown" `
  -F "file=@examples/messy-market-data/sample-note.md;type=text/markdown"
```

## Observed result

```text
GET /health -> 200
health.status -> ok

POST /documents/upload-intake-manifest-preview -> 200
filename -> sample-note.md
source_type -> markdown
parser -> markdown
byte_count -> 410
content_sha256 -> 4e253da30538337b4fd8ceaaf24f1bdb6b1287a085b91d38c08b9b78eb4cd7a4
storage_decision -> do_not_persist_raw_upload_yet
replayable -> false
persistence_boundary -> preview_only_not_persisted
manifest.source_uri -> upload://sample-note.md
manifest.future_persistence_candidate -> uploaded_file_intake
manifest.profile.extraction_quality -> high
```

## What this proves

The new endpoint can produce an uploaded-file intake manifest over live local HTTP.

The manifest includes `content_sha256`, parser/profile summary, a future persistence candidate name, and an explicit no-raw-storage decision.

## What this does not prove

This is not hosted deployment evidence.

It is not external reviewer feedback.

It is not raw file storage.

It is not customer validation, Braincrew acceptance, production readiness, document row creation, chunk persistence, retrieval persistence, Evidence Ledger persistence, Noise Gate persistence, report persistence, workflow persistence, robust PDF extraction, semantic retrieval, embeddings, LLM output, or automatic failure-case creation.

The endpoint still returns `preview_only_not_persisted`.

## Next gate

The next bounded product gate should remain conservative:

```text
uploaded file intake manifest application refresh v0
```

That gate should only surface this new runtime packet in application-facing materials. It should not add persistence or storage.
