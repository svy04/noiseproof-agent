# Ops Summary Semantic Retrieval Operational Counts Runtime Smoke

Status: implemented.

Phase marker: ops summary semantic retrieval operational counts runtime smoke v0.

## Purpose

Verify that the Phase 614 `/ops/summary` semantic retrieval operational counts work in a local Docker-backed FastAPI runtime.

This smoke creates real local PostgreSQL rows for one document, two chunks, two caller-provided embedding rows, and one semantic retrieval run.

## Runtime Setup

```text
compose project -> noiseproof-phase615
POSTGRES_PORT=55442
API port -> 8013
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
GET /ops/summary -> 200
```

## Observed Runtime Values

```text
document_id -> edf23670-8ceb-4085-944f-d263242bfe17
demand_chunk_id -> a1850930-9003-4038-837d-265d2f4555c4
noise_chunk_id -> ae4d1c85-460a-4f4a-856a-094ba164ba9d
retrieval_status -> completed
retrieval_result_count -> 2
retrieval_run_count -> 1
semantic_retrieval_run_count -> 1
chunk_embedding_count -> 2
caller_provided_embedding_count -> 2
note_has_operational_count -> true
note_has_quality_boundary -> true
```

Observed `/ops/summary` note fragment:

```text
Semantic retrieval runs recorded: 1; caller-provided embedding row(s): 2. These are operational counts, not semantic retrieval quality evidence.
```

## Cleanup

```text
docker compose -p noiseproof-phase615 down -v -> completed
docker ps --filter name=noiseproof-phase615 -> no remaining containers
```

## Boundary

This is local Docker/FastAPI runtime evidence for operational count surfacing only.

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
