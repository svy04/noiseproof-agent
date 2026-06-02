# Semantic Retrieval Persistence Endpoint

Phase marker: semantic retrieval persistence endpoint v0.

Status: implemented.

## Purpose

Persist caller-provided-vector semantic retrieval candidates as a bounded `retrieval_runs` row.

This endpoint is the implementation gate selected by `docs/review/semantic-retrieval-persistence-review.md`.

## Endpoint

```text
POST /documents/{document_id}/semantic-retrieval-runs
```

Request shape:

```text
question
query_embedding
embedding_model
embedding_dimension
limit
```

Response shape:

```text
RetrievalRunResponse
```

## Implemented Behavior

The endpoint:

- validates that `query_embedding` length equals `embedding_dimension`
- reads existing `document_chunks`
- ranks existing `chunk_embeddings` with exact cosine distance through the existing semantic preview repository query
- creates one `retrieval_runs` row
- uses `strategy = semantic-cosine`
- returns semantic candidates mapped into `RetrievalCandidateOut`
- keeps `matched_terms = []` because this is vector ranking, not lexical term matching
- records missing embedding chunk ids in metadata and warnings
- keeps the existing preview endpoint preview-only

Required metadata is stored on the `retrieval_runs` row:

```text
metadata_json.source_table = document_chunks
metadata_json.embedding_table = chunk_embeddings
metadata_json.retrieval_mode = semantic_persisted
metadata_json.preview_source = semantic_preview_runtime_smoke
metadata_json.candidate_chunk_ids
metadata_json.candidate_embedding_ids
metadata_json.missing_embedding_chunk_ids
metadata_json.embedding_model
metadata_json.embedding_dimension
metadata_json.query_vector_source = caller_provided_vector
metadata_json.ranking_boundary = exact_cosine_caller_provided_query_vector
metadata_json.persistence_boundary = semantic_retrieval_run_only_no_evidence_ledger
metadata_json.no_embedding_generation = true
metadata_json.no_evidence_ledger_generation = true
metadata_json.not_financial_advice = true
```

## Boundary

This is endpoint code and route-level test evidence.

This is not runtime smoke evidence.

This is not embedding generation.

This is not HNSW or IVFFlat index behavior.

This is not vector search quality evidence.

This is not Evidence Ledger generation.

This is not Critic / Noise Gate behavior.

This is not final report generation.

This is not financial advice.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.

## Verification

Route-level tests cover:

```text
POST /documents/{document_id}/semantic-retrieval-runs -> 201
query_embedding length mismatch -> 400
GET /retrieval-runs includes the semantic persisted run
GET /evidence-ledgers remains empty after semantic retrieval persistence
```

## Next Gate

Recommended next gate:

```text
semantic retrieval persistence runtime smoke v0
```
