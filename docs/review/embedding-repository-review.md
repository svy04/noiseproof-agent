# Embedding Repository Review

Status: review-only.

Phase marker: embedding repository review v0.

This review selects the smallest repository boundary for `chunk_embeddings` after the schema was locally verified.

## Current State

NoiseProof has:

- `document_chunks` for persisted chunk text
- `chunk_embeddings` schema and migration
- local runtime verification that `chunk_embeddings.embedding` uses pgvector `vector`

NoiseProof does not yet have repository code for `chunk_embeddings`.

## Decision

Add repository code next, but keep it metadata/persistence only.

The selected boundary is:

```text
ChunkEmbeddingCreate
create_chunk_embedding
list_chunk_embeddings
```

`create_chunk_embedding` should insert a caller-provided embedding row. It must not compute embeddings.

`list_chunk_embeddings` should list rows by optional `chunk_id`, `embedding_model`, and `embedding_status` filters.

## Persistence Boundary

The repository should write to:

```text
chunk_embeddings
```

The parent text source remains:

```text
document_chunks
```

The `embedding vector stays nullable` so a future job can create metadata rows before an actual vector exists, or record failed/stale status without fabricating a vector.

Required fields for create:

```text
chunk_id
embedding_model
embedding_dimension
embedding_text_hash
distance_metric
embedding_status
embedding
metadata_json
```

## Guardrails

Search marker: do not generate embeddings in repository.

The repository must not:

- call Sentence Transformers
- call external embedding APIs
- run semantic retrieval
- choose HNSW or IVFFlat
- create Evidence Ledger rows
- change report behavior

## Selected Next Gate

```text
next product gate: embedding repository v0
```

## Explicit Non-claims

This is not repository code.

This is not embedding generation.

This is not semantic retrieval implementation.

This is not runtime evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not product-complete.
