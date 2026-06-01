# Uploaded File Intake Manifest Persistence Runtime Smoke

Phase marker: uploaded file intake manifest persistence runtime smoke v0.

## Purpose

Record local runtime evidence that the uploaded-file intake manifest persistence endpoint can write and read manifest metadata against a Docker PostgreSQL database.

This is local runtime evidence only, not hosted deployment evidence.

## Environment

```text
Docker version 29.4.3
Docker Compose version v5.1.3
DB image: pgvector/pgvector:pg16
Published DB port observed from docker compose config: 55432
API URL: http://127.0.0.1:8032
```

## Commands

```bash
docker compose config
docker compose up -d db
docker compose ps
uv run python -m app.migration_runner --status
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8032
curl http://127.0.0.1:8032/health
curl -X POST -F "source_type=markdown" -F "file=@examples/messy-market-data/sample-note.md;type=text/markdown" http://127.0.0.1:8032/documents/upload-intake-manifests
curl http://127.0.0.1:8032/documents/upload-intake-manifests
```

## Observed Migration State

Before applying the new manifest migration:

```text
Applied migrations: 10
Pending migrations: 1
pending 012_uploaded_file_intake_manifests.sql
```

After applying:

```text
Applied migrations: 11
Pending migrations: 0
```

## Observed HTTP Evidence

Health:

```json
{"status":"ok","service":"noiseproof-agent-api","workflow_version":"phase40-lineage-warning-code-dashboard"}
```

POST /documents/upload-intake-manifests returned a persisted manifest row with:

```text
filename = sample-note.md
source_type = markdown
content_type = text/markdown
size_bytes = 410
content_sha256 = 4e253da30538337b4fd8ceaaf24f1bdb6b1287a085b91d38c08b9b78eb4cd7a4
parser = markdown
storage_decision = do_not_persist_raw_upload_yet
replayable = false
persistence_boundary = manifest_only_no_raw_file_storage
```

GET /documents/upload-intake-manifests returned the same row.

Database counts observed after the POST:

```text
documents = 1
manifests = 1
latest manifest filename = sample-note.md
latest manifest persistence_boundary = manifest_only_no_raw_file_storage
latest manifest storage_decision = do_not_persist_raw_upload_yet
latest manifest replayable = false
```

The existing local database already had one document before the smoke. This smoke observed that the manifest count moved from 0 to 1 while the document count remained 1.

## Boundary

This smoke stores no raw uploaded bytes.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not customer validation.

It is not robust PDF extraction.

It is not parser output persistence, chunk persistence, retrieval persistence, Evidence Ledger persistence, Noise Gate persistence, report persistence, workflow persistence, LLM calls, embeddings, semantic retrieval, or automatic failure-case creation.

## Next Gate

```text
uploaded file intake manifest persistence application refresh v0
```
