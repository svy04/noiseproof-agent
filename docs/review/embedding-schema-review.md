# Embedding Schema Review

Status: review-only.

Phase marker: embedding schema review v0.

This review decides the smallest durable schema boundary for future embeddings without adding a vector column, migration, model dependency, or semantic retrieval behavior in this gate.

## Current State

NoiseProof currently has:

- `document_chunks` as the persisted text-chunk source table
- lexical retrieval over `document_chunks`
- `retrieval_runs.metadata_json.candidate_chunk_ids` as the current retrieval candidate handoff
- PostgreSQL with the `vector` extension available through the local pgvector image

Current retrieval remains lexical. There are no persisted embeddings and no semantic retrieval implementation.

## Decision

Use a separate future `chunk_embeddings` table instead of adding an embedding column directly to `document_chunks`.

The first schema should make embedding provenance inspectable:

```text
chunk_embeddings
  id
  chunk_id
  embedding_model
  embedding_dimension
  embedding_text_hash
  embedding_created_at
  distance_metric
  embedding_status
  embedding
  metadata_json
```

The future `chunk_id` should reference `document_chunks(id)`.

The future `embedding` column should use pgvector only after a migration gate explicitly adds it.

The initial distance choice should be cosine distance unless a later evaluation proves another distance metric is better.

## Why A Separate Table

`document_chunks` should remain the stable text and chunk-strategy record.

Embeddings are derived artifacts that can change when:

- the embedding model changes
- the embedding_dimension changes
- the source text normalization changes
- the rebuild strategy changes
- the distance_metric changes

A separate `chunk_embeddings` table allows multiple embedding versions for the same chunk without rewriting the base chunk row or losing lexical retrieval comparability.

## Required Metadata Before Migration

Future implementation must record:

- `embedding_model`
- `embedding_dimension`
- `embedding_text_hash`
- `embedding_created_at`
- `distance_metric`
- `embedding_status`
- rebuild strategy
- lexical baseline comparison notes

This keeps semantic retrieval comparable against the current lexical baseline rather than silently replacing it.

## Index Decision Boundary

Do not add HNSW or IVFFlat in the first schema migration by default.

HNSW and IVFFlat should be considered only after:

- enough persisted embeddings exist to justify approximate nearest neighbor indexing
- exact search has a baseline result
- lexical baseline comparison exists
- retrieval evaluation can report whether the index changed recall or latency

## Migration Shape For The Next Gate

The selected next product gate is:

```text
next product gate: embedding schema migration v0
```

That gate may add a migration for `chunk_embeddings`, but it should still avoid embedding generation, semantic retrieval, external API calls, or vector index tuning unless explicitly accepted by a later gate.

## Search Marker

do not add a vector column in this gate.

## Explicit Non-claims

This is not embeddings.

This is not semantic retrieval implementation.

This is not runtime evidence.

This is not vector index tuning.

This is not HNSW runtime evidence.

This is not IVFFlat runtime evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not product-complete.

## Boundary

This review adds no schema, migration, vector column, pgvector index, embedding model dependency, embedding job, semantic retrieval endpoint, retrieval ranking behavior, LLM call, hosted deployment evidence, financial advice behavior, or dashboard behavior.
