# Uploaded File Chunk Preview

Phase marker: uploaded file chunk preview v0.

## What changed

NoiseProof now exposes `POST /documents/upload-chunk-preview` as a preview-only boundary from multipart upload to chunk strategy comparison.

The endpoint accepts an uploaded file, infers or accepts a source type, decodes uploaded bytes as UTF-8 text, runs parser/profile preview, and compares the existing chunk strategies against that uploaded text.

## Current behavior

The response includes:

- `filename`
- `content_type`
- `byte_count`
- `persistence_boundary`
- parser result
- document profile
- parse warnings
- chunk strategies and metrics

The persistence boundary is `preview_only_not_persisted`.

## Boundary

This endpoint is preview-only and does not create documents.

It also does not create chunks, retrieval runs, Evidence Ledger entries, Noise Gate records, reports, workflow runs, or failure cases.

It is not retrieval, not embeddings, not semantic search, not Evidence Ledger generation, not Critic / Noise Gate expansion, not final report generation, not dashboard polish, not hosted deployment evidence, and not production readiness.

It does not claim robust PDF extraction.

## Why this gate matters

The previous upload gate only proved parser/profile inspection over uploaded content.

Uploaded file chunk preview v0 proves uploaded user-provided text can reach the chunk strategy experiment boundary without being persisted or treated as trusted evidence.

## Next product gate

The next product implementation gate should remain bounded:

```text
uploaded file retrieval preview v0
```

That future gate may run lexical retrieval over uploaded chunk-preview output without adding embeddings, semantic retrieval, Evidence Ledger generation, or report generation.
