# Ops Dashboard Semantic Retrieval Operational Counts Runtime Smoke

Status: implemented.

Phase marker: ops dashboard semantic retrieval operational counts runtime smoke v0.

## Purpose

Verify that the Phase 616 `/ops/dashboard` semantic retrieval operational count labels render in a local Docker-backed FastAPI runtime.

This smoke reuses the same shape as the Phase 615 summary count proof, then inspects the dashboard HTML.

## Runtime Setup

```text
compose project -> noiseproof-phase617
POSTGRES_PORT=55443
API port -> 8014
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
POST /chunks/{chunk_id}/embeddings -> 201
POST /chunks/{chunk_id}/embeddings -> 201
POST /documents/{document_id}/semantic-retrieval-runs -> 201
GET /ops/dashboard -> 200
```

## Observed Dashboard Markers

```text
DASHBOARD_HAS_RETRIEVAL_RUNS_RECORDED=True
DASHBOARD_HAS_SEMANTIC_RETRIEVAL_RUNS=True
DASHBOARD_HAS_CHUNK_EMBEDDING_ROWS=True
DASHBOARD_HAS_CALLER_PROVIDED_EMBEDDINGS=True
DASHBOARD_HAS_QUALITY_BOUNDARY=True
```

The first PowerShell `Invoke-WebRequest` dashboard fetch hit a local client-side `NullReferenceException`, while the API had already created the fixture rows. The same running API returned `GET /ops/dashboard -> 200` through `curl.exe`, and the HTML contained all expected markers.

## Cleanup

```text
docker compose -p noiseproof-phase617 down -v -> completed
docker ps --filter name=noiseproof-phase617 -> no remaining containers
```

## Boundary

This is local Docker/FastAPI runtime evidence for dashboard visibility only.

This is not a new retrieval algorithm.

This is not embedding generation.

This is not live OpenAI provider evidence.

This is not semantic retrieval quality evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not distributed tracing.

This is not free-form final report generation.

This is not product-complete.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
