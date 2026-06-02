# Semantic Retrieval Persistence Runtime Smoke

Phase marker:

```text
semantic retrieval persistence runtime smoke v0
```

## Summary

This smoke test verifies the semantic retrieval persistence endpoint against a local Docker DB plus live FastAPI HTTP.

It confirms that caller-provided query vectors can rank existing chunk embeddings, persist one semantic retrieval run, expose the run through `GET /retrieval-runs`, reject dimension mismatches, and leave Evidence Ledger rows unchanged.

This is local runtime evidence only.

## Environment

```text
local Docker DB plus live FastAPI HTTP
database: noiseproof-agent-db
db image: pgvector/pgvector:pg16
db port: localhost:55432
api port: localhost:8038
migrations: Applied migrations: 14, Pending migrations: 0
```

## Observed Requests

```text
GET /health -> 200
POST /documents/{document_id}/semantic-retrieval-runs -> 201
GET /retrieval-runs -> 200
dimension mismatch -> 400
```

## Observed Runtime Facts

```text
health_status = ok
workflow_version = phase40-lineage-warning-code-dashboard
document_id = 812018e8-4d28-4ab4-b1e2-3dd2427334c1
demand_chunk_id = 8bb4cb92-b853-4d4f-81bf-0ed18cb3e862
noise_chunk_id = f3b1f329-05c8-40b3-84b4-eb2c8ef8b85c
missing_embedding_chunk_id = c6342c3c-1e69-4624-9daf-31367631fa71
demand_embedding_id = dc9fc6c2-4d81-473a-9c74-a07a8e82c2a2
noise_embedding_id = d1d98a7d-3839-4b9f-883c-77cd2136df82
semantic_run_id = 2e37cc1b-12a8-45ac-8b48-4a3bc05af358
semantic_strategy = semantic-cosine
semantic_status = completed
semantic_result_count = 2
first_result_source_type = markdown
first_result_score = 1.0
retrieval_run_count_before = 7
retrieval_run_count_after = 8
retrieval_run_count_after = retrieval_run_count_before + 1
evidence_ledger_count_before = 1
evidence_ledger_count_after = 1
evidence_ledger_count_unchanged -> true
retrieval_run_count_after_mismatch = 8
mismatch_did_not_create_retrieval_run = true
```

## Persisted Metadata Boundary

The persisted run includes the semantic retrieval metadata selected in the review and endpoint gates:

```text
metadata_json.retrieval_mode = semantic_persisted
metadata_json.persistence_boundary = semantic_retrieval_run_only_no_evidence_ledger
metadata_json.no_embedding_generation = true
metadata_json.no_evidence_ledger_generation = true
metadata_json.query_vector_source = caller_provided_vector
metadata_json.ranking_boundary = exact_cosine_caller_provided_query_vector
```

Observed IDs:

```text
metadata_json.candidate_chunk_ids = [
  8bb4cb92-b853-4d4f-81bf-0ed18cb3e862,
  f3b1f329-05c8-40b3-84b4-eb2c8ef8b85c
]

metadata_json.candidate_embedding_ids = [
  dc9fc6c2-4d81-473a-9c74-a07a8e82c2a2,
  d1d98a7d-3839-4b9f-883c-77cd2136df82
]

metadata_json.missing_embedding_chunk_ids = [
  c6342c3c-1e69-4624-9daf-31367631fa71
]
```

## What This Proves

- The semantic persistence endpoint can run through live HTTP against local PostgreSQL/pgvector.
- The endpoint creates one `retrieval_runs` row for a valid caller-provided query vector.
- The persisted run records candidate chunk IDs, candidate embedding IDs, and missing embedding chunk IDs.
- The run remains retrieval-only and does not create Evidence Ledger rows.
- Dimension mismatch returns `400` and does not create a retrieval run.

## Claim Boundary

This is not embedding generation.

This is not Evidence Ledger generation.

This is not vector search quality evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not a product-complete claim.
