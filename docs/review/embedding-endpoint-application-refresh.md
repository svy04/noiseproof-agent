# Embedding Endpoint Application Refresh

Phase marker: embedding endpoint application refresh v0.

Status: documentation-only application surface refresh.

## Purpose

Surface the caller-provided chunk embedding endpoint runtime proof in the reviewer-facing application docs.

This refresh exists because the repo now has local runtime evidence for a bounded embedding persistence surface, but still has no embedding generation or semantic retrieval implementation.

## Updated Surfaces

```text
docs/review/application-ready-review.md
docs/application/braincrew-role-map.md
docs/review/external-reader-proof-path.md
docs/application/portfolio-index.md
docs/runbook.md
README.md
docs/GOAL.md
```

Primary proof artifact:

```text
docs/review/embedding-endpoint-runtime-smoke.md
```

## Runtime Proof Surfaced

```text
POST /chunks/{chunk_id}/embeddings
GET /chunks/{chunk_id}/embeddings
caller_provided_embedding_only_no_generation
generated embedding claim -> 400
pgvector vector text normalization fix
```

The surfaced runtime proof is local Docker DB plus live FastAPI HTTP evidence only. It shows caller-provided vector persistence and readback through the `chunk_embeddings` table.

## Claim Update

Allowed claim:

```text
NoiseProof has local runtime evidence for a caller-provided chunk embedding endpoint.
```

Forbidden claim:

```text
NoiseProof does not generate embeddings, does not perform semantic retrieval, and does not prove vector search quality.
```

## Boundary

This is not embedding generation.

This is not semantic retrieval implementation.

This is not HNSW or IVFFlat index behavior.

This is not vector search quality.

This is not Evidence Ledger generation.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not Braincrew acceptance.

This is not product-complete.

## Next Gate

```text
next product gate: semantic retrieval implementation review v0
```
