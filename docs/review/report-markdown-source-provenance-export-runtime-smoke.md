# Report Markdown Source Provenance Export Runtime Smoke

Status: implemented.

Phase marker: report markdown source provenance export runtime smoke v0.

## Purpose

Record local Docker PostgreSQL plus live FastAPI HTTP evidence that persisted Report markdown export renders source retrieval provenance.

This is the runtime proof for `docs/review/report-markdown-source-provenance-export.md`.

## Environment

```text
Docker version 29.4.3
Docker Compose version v5.1.3
Compose project: noiseproof-phase642
POSTGRES_PORT=55445
DB container: noiseproof-phase642-db-1
DB health: healthy
pg_isready: accepting connections
```

## Migration State

```text
Applied migrations: 23
Pending migrations: 0
```

## API Runtime

```text
uvicorn on 127.0.0.1:8042
GET /health -> ok
```

## Runtime Flow

```text
POST /documents -> 201
POST /documents/{document_id}/chunks -> 201
POST /chunks/{chunk_id}/embeddings -> 201
POST /documents/{document_id}/semantic-retrieval-runs -> completed
retrieval_mode=semantic_persisted
query_vector_source=caller_provided_vector
missing_embedding_chunk_ids_count=1
POST /retrieval-runs/{retrieval_run_id}/evidence-ledger -> stored_entry_count=2
POST /retrieval-runs/{retrieval_run_id}/noise-gate -> blocked
gate_source_retrieval_mode=semantic_persisted
gate_handoff_performs_semantic_retrieval=False
POST /retrieval-runs/{retrieval_run_id}/report -> blocked
report_source_retrieval_mode=semantic_persisted
report_handoff_performs_semantic_retrieval=False
GET /reports/{report_record_id}/markdown -> HTTP/1.1 200 OK
content-type: text/markdown; charset=utf-8
```

## Markdown Markers

```text
markdown_contains_source_provenance=True
markdown_contains_semantic_persisted=True
markdown_contains_caller_vector=True
markdown_contains_semantic_flag=True
markdown_contains_persistence_boundary=True
markdown_contains_handoff_false=True
markdown_boundary_present=True
```

## Runtime Note

PowerShell `Invoke-WebRequest` raised a client-side NullReferenceException while fetching the markdown endpoint after the report record was created.

The same endpoint was then rechecked with `curl.exe`, which verified the endpoint returned `HTTP/1.1 200 OK`, `text/markdown; charset=utf-8`, and all expected markdown markers.

## Cleanup

```text
Stop-Process -Id 79612 -Force
docker compose -p noiseproof-phase642 down -v
cleanup_done=true
```

## Boundary

This is local Docker/FastAPI runtime evidence only.

This is not hosted deployment evidence.

This is not customer validation.

This is not Braincrew acceptance.

This is not semantic retrieval quality evidence.

This is not embedding generation.

This is not Evidence Ledger quality evidence.

This is not Noise Gate quality evidence.

This is not report quality evidence.

This is not a new report-generation path.

This is not free-form report generation.

This is not an LLM call.

This is not product-complete.

## Next Gate

```text
remote verification for this runtime-smoke proof after push, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
