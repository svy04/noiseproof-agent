# Deterministic Text Embedding Preview

Status: implemented.

Phase marker:

```text
deterministic text embedding preview v0
```

## Purpose

Add a small local preview boundary for turning direct text into a deterministic vector-shaped artifact before any retrieval expansion.

This helps inspect question/chunk vector preparation without claiming semantic embedding quality.

## Endpoint

```text
POST /chunks/embedding-preview
```

Input shape:

```json
{
  "text": "Enterprise demand growth reached 12% in Q1.",
  "embedding_model": "local-hash-embedding-preview-v0",
  "embedding_dimension": 8,
  "distance_metric": "cosine"
}
```

Output fields:

```text
embedding_model
embedding_dimension
embedding_text_hash
distance_metric
embedding_status
embedding
metadata_json
warnings
```

## Implemented Behavior

- uses `local-hash-embedding-preview-v0`
- uses deterministic lowercase alphanumeric token hashing
- returns `embedding_text_hash` as a SHA-256 hash of the input text
- returns a fixed-size cosine-oriented vector
- returns `embedding_status: preview_generated`
- returns `metadata_json.persistence_boundary: preview_only_not_persisted`
- returns `metadata_json.quality_boundary: not_semantic_quality_evidence`
- rejects blank text with no tokens
- rejects non-local embedding model names

## Boundary

This preview is not a semantic embedding model.

It uses no external model.
It uses no LLM.
It is not persisted.
It does not modify chunk_embeddings.
It is not vector search quality evidence.
It is not semantic retrieval quality evidence.
It is not a model comparison or benchmark.

The existing persisted endpoint remains caller-provided only:

```text
POST /chunks/{chunk_id}/embeddings
```

That endpoint still stores only caller-provided vectors and does not generate embeddings.

## Verification

Focused tests:

```bash
cd apps/api
uv run pytest -q tests/test_routes.py -k "text_embedding_preview"
uv run pytest -q tests/test_docs.py -k "deterministic_text_embedding_preview"
```

Expected route behaviors:

```text
POST /chunks/embedding-preview -> 200
blank text -> 400
non-local embedding model -> 400
```
