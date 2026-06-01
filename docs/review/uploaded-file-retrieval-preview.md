# Uploaded File Retrieval Preview

Phase marker: uploaded file retrieval preview v0.

## What changed

NoiseProof now exposes `POST /documents/upload-retrieval-preview` as a preview-only boundary from multipart upload to lexical retrieval preview.

The endpoint accepts an uploaded file, infers or accepts a source type, decodes uploaded bytes as UTF-8 text, chunks the parsed content using the requested strategy, and runs lexical retrieval over that uploaded file.

## Current behavior

The response includes:

- `filename`
- `content_type`
- `byte_count`
- `persistence_boundary`
- `question`
- retrieval strategy
- status
- retrieval metrics
- retrieval candidates
- warnings

The persistence boundary is `preview_only_not_persisted`.

## Boundary

This endpoint is preview-only and does not create retrieval_runs.

It also does not create documents, chunks, Evidence Ledger entries, Noise Gate records, reports, workflow runs, or failure cases.

It does not create Evidence Ledger entries.

It is lexical retrieval only, not semantic retrieval, not embeddings, not Evidence Ledger generation, not Critic / Noise Gate expansion, not final report generation, not dashboard polish, not hosted deployment evidence, and not production readiness.

It does not claim robust PDF extraction.

Questions that drift toward buy/sell or financial advice are blocked at this preview boundary.

## Why this gate matters

The previous uploaded file chunk preview proved that uploaded content could reach chunk strategy comparison without persistence.

Uploaded file retrieval preview v0 proves that uploaded content can reach the retrieval boundary without creating durable retrieval records or treating retrieved text as accepted evidence.

This keeps the system inspectable while preserving the core claim boundary: retrieval candidates are not truth, not Evidence Ledger entries, and not final report claims.

## Next product gate

The next product implementation gate should remain bounded:

```text
uploaded file Evidence Ledger preview v0
```

That future gate may convert upload retrieval candidates into preview Evidence Ledger entries without persistence, Critic / Noise Gate expansion, report generation, embeddings, or semantic retrieval.
