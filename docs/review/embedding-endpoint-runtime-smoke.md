# Embedding Endpoint Runtime Smoke v0

Phase marker: embedding endpoint runtime smoke v0.

Status: verified local Docker DB plus live FastAPI HTTP.

## Environment

```text
Docker image: pgvector/pgvector:pg16
Docker container: noiseproof-agent-embedding-endpoint-db-64179
Database port: 55434
API port: 8011
API server: uv run uvicorn app.main:app --host 127.0.0.1 --port 8011
```

## Migration Evidence

Initial migration runner execution against a blank DB failed because the current runtime path requires the base schema before applying numbered migrations:

```text
psycopg.errors.UndefinedTable: relation "agent_runs" does not exist
```

The smoke then applied `db/init/001_schema.sql` and reran the migration runner.

Observed:

```text
Applied migrations: 0
Pending migrations: 14
applied 002_evidence_ledger_entries.sql
applied 003_noise_gate_records.sql
applied 004_report_records.sql
applied 005_workflow_trace_ids.sql
applied 006_child_agent_run_ids.sql
applied 007_workflow_runs.sql
applied 008_child_workflow_run_ids.sql
applied 009_stage_input_manifest.sql
applied 010_workflow_version_defaults.sql
applied 011_failure_case_workflow_run_id.sql
applied 012_uploaded_file_intake_manifests.sql
applied 013_document_chunks.sql
applied 014_evidence_ledger_retrieval_run_id.sql
applied 015_chunk_embeddings.sql
Applied migrations: 14
Pending migrations: 0
```

## Runtime Bug Found And Fixed

The first live HTTP attempt found a real pgvector serialization issue:

```text
ResponseValidationError
pgvector returned vector text: [0.1,0.2,0.3]
```

Fix applied:

```text
PostgresRepository normalizes returned chunk_embeddings.embedding values from pgvector text into list[float].
```

Regression coverage:

```text
uv run pytest tests/test_db.py -q -k "chunk_embedding or document_chunks"
uv run pytest tests/test_routes.py -q -k "chunk_embedding_endpoint"
```

Observed:

```text
3 passed, 3 deselected
2 passed, 98 deselected, 1 warning
```

## HTTP Smoke

Smoke path:

```text
GET /health -> 200
POST /documents -> 201
POST /documents/{document_id}/chunks -> 201
POST /chunks/{chunk_id}/embeddings -> 201
GET /chunks/{chunk_id}/embeddings -> 200
generated embedding claim -> 400
```

Observed response summary:

```json
{
  "health": "ok",
  "document_id": "e0743604-5203-47c7-93db-cfa874b60ac7",
  "chunk_id": "676669c2-4ea0-42a2-b3cf-ae860e3f748e",
  "embedding_id": "f2d0712b-7141-4865-b6ae-855beb50a6c5",
  "embedding": "0.1,0.2,0.3",
  "embedding_metadata_source": "caller_provided_vector",
  "embedding_boundary": "caller_provided_embedding_only_no_generation",
  "listed_count": 1,
  "listed_embedding_id": "f2d0712b-7141-4865-b6ae-855beb50a6c5",
  "listed_embedding": "0.1,0.2,0.3",
  "generated_claim_status": 400,
  "generated_claim_detail": "{\"detail\":\"Chunk embeddings currently accept only caller-provided vector input.\"}"
}
```

DB check:

```text
SELECT count(*) -> 1
metadata_json->>'embedding_source' -> caller_provided_vector
embedding::text -> [0.1,0.2,0.3]
```

## Boundaries

This is local runtime evidence only.

This is not embedding generation.

This is not semantic retrieval implementation.

This is not HNSW or IVFFlat index behavior.

This is not vector similarity search.

This is not Evidence Ledger generation.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation, Braincrew acceptance, or product-complete.

## Next Gate

```text
next product gate: embedding endpoint application refresh v0
```
