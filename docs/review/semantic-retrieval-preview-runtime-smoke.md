# Semantic Retrieval Preview Runtime Smoke

Phase marker: semantic retrieval preview runtime smoke v0.

Status: implemented.

## Purpose

Verify the semantic retrieval preview endpoint against a live local Docker PostgreSQL/pgvector database and a live FastAPI process.

This smoke test proves the endpoint can rank existing persisted chunk embeddings at runtime. It does not prove vector search quality, hosted deployment, semantic retrieval persistence, or final answer quality.

## Runtime Environment

Commit:

```text
39510fffce17fd91239a45dc3d08ab39afe52e53
```

Docker:

```text
Docker version 29.4.3, build 055a478
Docker Compose version v5.1.3
```

Compose service:

```text
noiseproof-agent-db
pgvector/pgvector:pg16
0.0.0.0:55432->5432/tcp
status: healthy
```

## Migration Verification

Initial status:

```text
Applied migrations: 13
Pending migrations: 1
pending 015_chunk_embeddings.sql
```

Apply:

```text
Applied migrations: 13
Pending migrations: 1
applied 015_chunk_embeddings.sql
```

Final status:

```text
Applied migrations: 14
Pending migrations: 0
```

One command-level issue was observed:

```text
uv run python -m app.migration_runner
MigrationError: DATABASE_URL is required
```

Root cause:

```text
app.migration_runner reads DATABASE_URL from explicit CLI argument or process environment.
The smoke command was corrected to pass --database-url postgresql://noiseproof:noiseproof@localhost:55432/noiseproof.
```

This was a smoke-command environment issue, not a schema or endpoint failure.

## API Runtime

Server:

```text
uv run uvicorn app.main:app --host 127.0.0.1 --port 8037
```

Health check:

```json
{"status":"ok","service":"noiseproof-agent-api","workflow_version":"phase40-lineage-warning-code-dashboard"}
```

## Smoke Fixture

Created one document:

```text
document_id: cb063a18-2710-4312-90dc-d12a83f8148b
```

Created three chunks:

```text
demand_chunk_id: 3275cbbf-c902-43c6-bf77-2b8b23354508
noise_chunk_id: 9254df59-928e-44f0-af16-d5d3c11b56dd
missing_chunk_id: 595ab972-b991-43f4-9344-b15de323d6a9
```

Created two caller-provided embeddings:

```text
demand_embedding_id: 0fce153c-0a13-41d0-8ffa-c40bdc961324
noise_embedding_id: 28f5081e-f9bf-4e36-8360-d1e26493fdee
embedding_model: local-test-model
embedding_dimension: 2
distance_metric: cosine
embedding_status: created
```

The third chunk intentionally had no embedding.

## Semantic Preview Result

Endpoint:

```text
POST /documents/{document_id}/semantic-retrieval-preview -> 200
```

Observed response markers:

```text
retrieval_mode -> semantic_preview
persistence_boundary -> preview_only_not_persisted
ranking_boundary -> exact_cosine_caller_provided_query_vector
```

Candidate ordering:

```text
candidate_chunk_ids:
1. 3275cbbf-c902-43c6-bf77-2b8b23354508
2. 9254df59-928e-44f0-af16-d5d3c11b56dd

first_candidate_distance -> 0.0
second_candidate_distance -> 1.0
```

Missing embedding surface:

```text
missing_embedding_chunk_ids:
595ab972-b991-43f4-9344-b15de323d6a9
```

Persistence check:

```text
retrieval_run_count_before -> 7
retrieval_run_count_after -> 7
retrieval_runs_unchanged -> true
```

Warnings:

```text
Semantic retrieval preview uses a caller-provided query vector; it does not generate embeddings.
Semantic retrieval preview is preview-only and does not persist retrieval_runs.
Some persisted document_chunks have no matching created embedding for the requested model/dimension.
```

## Failure Boundary Check

Dimension mismatch:

```text
dimension mismatch -> 400
detail -> query_embedding length must match embedding_dimension.
```

Trace surface:

```text
semantic_trace_count -> 2
latest_semantic_trace_status -> failed
latest_semantic_trace_endpoint -> POST /documents/{document_id}/semantic-retrieval-preview
latest_semantic_trace_boundary -> preview_only_not_persisted
```

The latest semantic trace is failed because the final check intentionally sent a mismatched query vector.

## Explicit Non-claims

This is not retrieval_runs persistence.

This is not embedding generation.

This is not HNSW or IVFFlat index behavior.

This is not vector search quality evidence.

This is not Evidence Ledger generation.

This is not Critic / Noise Gate behavior.

This is not final report generation.

This is not external search.

This is not an LLM call.

This is not financial advice.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.

## Next Gate

Recommended next gate:

```text
semantic retrieval persistence review v0
```

That review should decide whether and how semantic preview candidates should be persisted into `retrieval_runs.metadata_json.candidate_chunk_ids` without weakening the existing Evidence Ledger handoff boundaries.
