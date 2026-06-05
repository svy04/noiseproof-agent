# Retrieval Run Semantic Provenance Runtime Smoke

Status: implemented.

Phase marker: retrieval run semantic provenance runtime smoke v0.

## Purpose

Verify that the Phase 618 retrieval-run semantic provenance read fields render through a local Docker-backed PostgreSQL database and live FastAPI HTTP server.

This smoke proves the read surface works against persisted `retrieval_runs` rows, not only the in-memory route test repository.

## Runtime Setup

```text
compose project -> noiseproof-phase619
POSTGRES_PORT=55444
API port -> 8015
database image -> pgvector/pgvector:pg16
pg_isready -> accepting connections
migration apply -> applied 002 through 024
migration status -> Pending migrations: 0
```

## HTTP Flow

```text
GET /health -> 200
POST /documents -> 201
POST /documents/{document_id}/chunks -> 201
POST /documents/{document_id}/chunks -> 201
POST /documents/{document_id}/chunks -> 201
POST /chunks/{chunk_id}/embeddings -> 201
POST /chunks/{chunk_id}/embeddings -> 201
POST /documents/{document_id}/semantic-retrieval-runs -> 201
GET /retrieval-runs -> 200
GET /ops/dashboard -> 200
```

## Observed API Markers

```text
RETRIEVAL_RUNS_COUNT=1
RETRIEVAL_RUN_HAS_IS_SEMANTIC=True
RETRIEVAL_RUN_RETRIEVAL_MODE=semantic_persisted
RETRIEVAL_RUN_QUERY_VECTOR_SOURCE=caller_provided_vector
RETRIEVAL_RUN_PERSISTENCE_BOUNDARY=semantic_retrieval_run_only_no_evidence_ledger
```

## Observed Dashboard Markers

```text
DASHBOARD_HAS_RETRIEVAL_MODE=True
DASHBOARD_HAS_QUERY_VECTOR_SOURCE=True
DASHBOARD_HAS_PERSISTENCE_BOUNDARY=True
DASHBOARD_HAS_SEMANTIC_PERSISTED=True
DASHBOARD_HAS_CALLER_VECTOR=True
```

## Cleanup

```text
Stop-Process -Id 72264 -> completed
docker compose -p noiseproof-phase619 down -v -> completed
docker ps -a --filter name=noiseproof-phase619 -> no remaining containers
GET http://127.0.0.1:8015/health -> api stopped
```

## Boundary

This is local Docker/FastAPI runtime evidence for read-surface inspectability only.

This is not a new retrieval algorithm.

This is not embedding generation.

This is not live OpenAI provider evidence.

This is not semantic retrieval quality evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not distributed tracing.

This is not Evidence Ledger generation.

This is not free-form final report generation.

This is not product-complete.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
