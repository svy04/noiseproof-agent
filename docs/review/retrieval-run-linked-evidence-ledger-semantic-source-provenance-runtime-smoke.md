# Retrieval-run-linked Evidence Ledger Semantic Source Provenance Runtime Smoke

Status: implemented.

Phase marker: retrieval-run-linked Evidence Ledger semantic source provenance runtime smoke v0.

## Purpose

Verify that the Phase 624 semantic source-provenance handoff works against a local Docker-backed PostgreSQL database and live FastAPI HTTP server.

This smoke proves the source retrieval provenance fields survive a real HTTP flow through persisted rows, not only the in-memory route test repository.

## Runtime Setup

```text
compose project -> noiseproof-phase625
POSTGRES_PORT=55445
API port -> 8016
database image -> pgvector/pgvector:pg16
docker compose ps -> db healthy
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
POST /retrieval-runs/{retrieval_run_id}/evidence-ledger -> 201
GET /evidence-ledgers?retrieval_run_id={retrieval_run_id} -> 200
GET /agent-runs -> 200
```

## Observed API Markers

```text
GET_HEALTH_STATUS=ok
POST_DOCUMENTS_CREATED=True
POST_CHUNKS_CREATED=3
POST_EMBEDDINGS_CREATED=2
POST_SEMANTIC_RETRIEVAL_RUN_RESULT_COUNT=2
POST_LEDGER_STORED_ENTRY_COUNT=2
LEDGER_WARNING_HAS_SOURCE_MODE=True
LEDGER_WARNING_HAS_QUERY_VECTOR_SOURCE=True
ENTRY_SOURCE_RETRIEVAL_MODE=semantic_persisted
ENTRY_SOURCE_QUERY_VECTOR_SOURCE=caller_provided_vector
ENTRY_SOURCE_IS_SEMANTIC=True
ENTRY_SOURCE_RETRIEVAL_PERSISTENCE_BOUNDARY=semantic_retrieval_run_only_no_evidence_ledger
ENTRY_PERSISTENCE_BOUNDARY=retrieval_run_linked_evidence_ledger_no_llm_no_embeddings
LISTED_ENTRY_SOURCE_RETRIEVAL_MODE contains semantic_persisted
TRACE_SOURCE_RETRIEVAL_MODE=semantic_persisted
TRACE_SOURCE_QUERY_VECTOR_SOURCE=caller_provided_vector
TRACE_SOURCE_IS_SEMANTIC=True
TRACE_HANDOFF_PERFORMS_SEMANTIC_RETRIEVAL=False
TRACE_NO_EMBEDDINGS=True
TRACE_NO_LLM=True
```

## Cleanup

```text
Stop-Process -Id 81568 -> completed
docker compose -p noiseproof-phase625 down -v -> completed
docker ps -a --filter name=noiseproof-phase625 -> no remaining containers
GET http://127.0.0.1:8016/health -> API_STOPPED=True
```

## Boundary

This is local Docker/FastAPI runtime evidence for semantic source-provenance preservation through the Evidence Ledger handoff.

This is not semantic retrieval quality evidence.

This is not embedding generation.

This is not a live OpenAI provider call.

This is not Evidence Ledger quality evidence.

This is not final truth adjudication.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.

## Next Gate

```text
remote verification for this runtime-smoke proof after push, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
