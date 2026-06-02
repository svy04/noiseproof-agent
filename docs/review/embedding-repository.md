# Embedding Repository v0

Status: implemented local repository code.

Phase marker: embedding repository v0.

This phase adds metadata/persistence only repository code for `chunk_embeddings`.

## Implemented

```text
ChunkEmbeddingCreate
create_chunk_embedding
list_chunk_embeddings
```

Files changed:

```text
apps/api/app/schemas.py
apps/api/app/db.py
apps/api/tests/test_db.py
```

`create_chunk_embedding` inserts a caller-provided vector into `chunk_embeddings`. It does not compute embeddings.

`list_chunk_embeddings` reads rows with optional filters:

```text
chunk_id
embedding_model
embedding_status
limit
```

## Boundary

The repository is metadata/persistence only.

The accepted vector path is caller-provided vector -> repository insert.

This is not endpoint behavior.
This is not endpoint.
This is not embedding generation.
This is not semantic retrieval implementation.
This is not Sentence Transformers integration.
This is not external embedding API integration.
This is not HNSW or IVFFlat index behavior.
This is not Evidence Ledger generation.
This is not report behavior.
This is not hosted deployment evidence.
This is not external reviewer feedback.
This is not product-complete.

## Verification

```text
uv run pytest tests/test_db.py -q -k "chunk_embedding"
```

Observed:

```text
2 passed, 4 deselected
```

## Next Gate

```text
next product gate: embedding endpoint review v0
```
