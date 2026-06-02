# Embedding Endpoint v0

Phase marker: embedding endpoint v0.

Status: implemented route-level behavior.

## Implemented

```text
POST /chunks/{chunk_id}/embeddings
GET /chunks/{chunk_id}/embeddings
ChunkEmbeddingRequest
ChunkEmbeddingCreate
ChunkEmbeddingOut
```

Files changed:

```text
apps/api/app/routes/chunks.py
apps/api/app/main.py
apps/api/app/schemas.py
apps/api/tests/test_routes.py
```

`POST /chunks/{chunk_id}/embeddings` persists a caller-provided vector for an existing chunk id by calling `create_chunk_embedding`.

`GET /chunks/{chunk_id}/embeddings` lists persisted embedding rows by calling `list_chunk_embeddings`.

## Boundary

The endpoint accepts caller-provided vector input only.

It adds this metadata boundary:

```text
embedding_source = caller_provided_vector
persistence_boundary = caller_provided_embedding_only_no_generation
```

It rejects generated embedding claims by returning `400` when `metadata_json.embedding_source` is not `caller_provided_vector`.

It also rejects dimension mismatches between `embedding_dimension` and the caller-provided vector length.

## Verification

```text
uv run pytest tests/test_routes.py -q -k "chunk_embedding_endpoint"
```

Observed:

```text
2 passed, 98 deselected, 1 warning
```

## Explicit Non-claims

This is not embedding generation.

This is not semantic retrieval implementation.

This is not HNSW or IVFFlat index behavior.

This is not vector similarity search.

This is not Evidence Ledger generation.

This is not Noise Gate generation.

This is not report generation.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.

## Next Gate

```text
next product gate: embedding endpoint runtime smoke v0
```
