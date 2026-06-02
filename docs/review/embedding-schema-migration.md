# Embedding Schema Migration

Status: schema-only.

Phase marker: embedding schema migration v0.

This phase adds the future embedding storage table to the static schema and migration set without adding embedding generation, semantic retrieval, repository code, API endpoints, vector indexes, or runtime smoke evidence.

## Added Files

```text
db/migrations/015_chunk_embeddings.sql
```

## Updated Files

```text
db/init/001_schema.sql
docs/GOAL.md
docs/application/portfolio-index.md
docs/review/readme-proof-marker-archive.md
docs/runbook.md
```

## Schema Boundary

The table is:

```text
chunk_embeddings
```

It links derived embeddings to persisted chunk text:

```text
document_chunks.id -> chunk_embeddings.chunk_id
```

## Fields

```text
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
created_at
```

The table keeps embedding provenance visible before semantic retrieval is introduced.

## Index Boundary

The migration adds only basic lookup indexes:

```text
idx_chunk_embeddings_chunk_id
idx_chunk_embeddings_model
idx_chunk_embeddings_status
```

It does not add HNSW or IVFFlat indexes. Those require runtime size, latency, and recall evidence later.

## Current Non-claims

This is not embedding generation.

This is not semantic retrieval implementation.

This is not runtime evidence.

This is not vector index tuning.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not product-complete.

## Next Gate

```text
embedding schema runtime verification v0
```

The next gate should apply migrations against the local PostgreSQL/pgvector service and prove the new table exists before any repository or endpoint behavior is added.
