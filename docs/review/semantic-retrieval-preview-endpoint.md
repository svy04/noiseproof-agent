# Semantic Retrieval Preview Endpoint

Phase marker: semantic retrieval preview endpoint v0.

Status: implemented.

## Purpose

Add the smallest semantic retrieval surface that can be inspected before it is allowed to feed persisted retrieval runs or Evidence Ledger handoff.

The endpoint ranks existing persisted `document_chunks` by existing persisted `chunk_embeddings` using a caller-provided query vector. It does not generate embeddings and does not persist a `retrieval_runs` row.

## Endpoint

```text
POST /documents/{document_id}/semantic-retrieval-preview
```

Input:

```json
{
  "question": "Which chunk is closest to demand growth?",
  "query_embedding": [1.0, 0.0],
  "embedding_model": "local-test-model",
  "embedding_dimension": 2,
  "limit": 5
}
```

Output includes:

```text
question
retrieval_mode = semantic_preview
persistence_boundary = preview_only_not_persisted
ranking_boundary = exact_cosine_caller_provided_query_vector
candidates
missing_embedding_chunk_ids
warnings
metadata_json.candidate_chunk_ids
```

## Implemented Boundary

The preview reads:

```text
document_chunks
chunk_embeddings
```

The Postgres repository ranks with:

```text
chunk_embeddings.embedding <=> query_embedding
exact cosine ranking
```

The query filters to:

```text
embedding_status = 'created'
distance_metric = 'cosine'
embedding_model = requested model
embedding_dimension = requested dimension
```

The route rejects a caller-provided query vector when its length does not match `embedding_dimension`.

## Why Preview-only

Semantic retrieval can look stronger than it is. This gate makes candidate selection visible before semantic candidates become part of the persisted retrieval-to-Evidence-Ledger chain.

This endpoint records an `agent_runs` trace through the existing route wrapper, but it does not create a `retrieval_runs` row and does not create downstream evidence records.

## Verification

Tests added:

```text
tests/test_routes.py::test_semantic_retrieval_preview_ranks_caller_provided_vectors_without_persistence
tests/test_routes.py::test_semantic_retrieval_preview_rejects_query_dimension_mismatch
tests/test_db.py::test_preview_semantic_retrieval_candidates_uses_pgvector_exact_cosine_ranking
tests/test_docs.py::test_semantic_retrieval_preview_endpoint_keeps_preview_only_boundary
```

Expected route behavior:

```text
caller-provided query vector -> exact cosine candidate ranking
dimension mismatch -> 400
missing chunk embeddings -> structured warning
retrieval_runs list remains unchanged
```

## Explicit Non-claims

This is not retrieval_runs persistence.

This is not embedding generation.

This is not HNSW or IVFFlat index behavior.

This is not vector search quality evidence.

This is not Evidence Ledger generation.

This is not Critic / Noise Gate behavior.

This is not final report generation.

This is not an LLM call.

This is not external search.

This is not financial advice.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.

## Next Gate

Recommended next gate:

```text
semantic retrieval preview runtime smoke v0
```

That gate should run the endpoint against a local Docker Postgres/pgvector runtime and record the exact HTTP behavior before adding semantic retrieval persistence.
