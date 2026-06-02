# Embedding Endpoint Review

Phase marker: embedding endpoint review v0.

Status: review-only.

## Purpose

Select the smallest endpoint boundary for caller-provided chunk embeddings before adding route code.

This review does not implement the endpoint.

## Decision

Add chunk-scoped embedding endpoints next:

```text
POST /chunks/{chunk_id}/embeddings
GET /chunks/{chunk_id}/embeddings
```

The future endpoints should call the existing repository surface:

```text
ChunkEmbeddingCreate
ChunkEmbeddingOut
create_chunk_embedding(payload)
list_chunk_embeddings(chunk_id, embedding_model, embedding_status, limit)
```

The write endpoint should take `chunk_id` from the path and embedding metadata from the body.

Required write boundary:

```text
embedding_source = caller_provided_vector
```

## Why This Route Shape

Embedding rows belong to persisted `document_chunks`. A caller must already have a persisted chunk row before creating an embedding row.

`POST /chunks/{chunk_id}/embeddings` keeps the first endpoint smaller than a document-scoped path because `chunk_id` is already globally unique. It also keeps embedding creation separate from upload, parsing, chunking, retrieval, Evidence Ledger, Noise Gate, and report behavior.

## Future Request Shape

The future POST body should contain metadata and a caller-provided vector only:

```json
{
  "embedding_model": "local-test-model",
  "embedding_dimension": 3,
  "embedding_text_hash": "sha256:...",
  "distance_metric": "cosine",
  "embedding_status": "created",
  "embedding": [0.1, 0.2, 0.3],
  "metadata_json": {
    "embedding_source": "caller_provided_vector"
  }
}
```

The endpoint should reject or warn on attempts to imply generated embeddings unless a later gate explicitly adds generation.

## Explicit Non-changes

This review adds no endpoint code.

This is not endpoint code.

It creates no embedding rows.

It does not generate embeddings.

This is not embedding generation.

It does not call Sentence Transformers.

It does not call an external embedding API.

It does not implement semantic retrieval.

It is not semantic retrieval implementation.

It does not add HNSW or IVFFlat indexes.

It is not HNSW or IVFFlat index behavior.

It does not run vector similarity search.

It does not generate retrieval runs.

It is not Evidence Ledger generation.

It does not generate Noise Gate records.

It does not generate report records.

It does not provide financial advice, buy/sell behavior, target prices, or return predictions.

It is not hosted deployment evidence, external reviewer feedback, customer validation, Braincrew acceptance, LLM output, or product-complete claim.

## Next Gate

```text
next product gate: embedding endpoint v0
```
