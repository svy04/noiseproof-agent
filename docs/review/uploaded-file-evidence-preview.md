# Uploaded File Evidence Ledger Preview

Phase marker: uploaded file Evidence Ledger preview v0.

## What changed

NoiseProof now exposes `POST /documents/upload-evidence-preview` as a preview-only boundary from multipart upload to lexical retrieval preview to Evidence Ledger preview.

The endpoint accepts an uploaded file, infers or accepts a source type, decodes uploaded bytes as UTF-8 text, chunks the parsed content using the requested strategy, runs lexical retrieval over that uploaded file, and turns the returned candidates into preview Evidence Ledger entries.

## Current behavior

The response includes:

- `filename`
- `content_type`
- `byte_count`
- `persistence_boundary`
- `source_type`
- `question`
- status
- retrieval preview output
- Evidence Ledger preview output
- warnings

The persistence boundary is `preview_only_not_persisted`.

## Boundary

This endpoint is preview-only and does not create Evidence Ledger entries.

It also does not create retrieval_runs, documents, chunks, Noise Gate records, reports, workflow runs, or failure cases.

It is not Noise Gate, not Critic Agent execution, not final report generation, not semantic retrieval, not embeddings, not LLM output, not dashboard polish, not hosted deployment evidence, and not production readiness.

It does not claim robust PDF extraction.

Retrieval candidates are not truth. Evidence Ledger preview entries are only a structured inspection surface over candidate spans; they are not accepted claims.

Questions that drift toward buy/sell or financial advice are blocked at this preview boundary.

## Why this gate matters

The previous uploaded file retrieval preview proved that uploaded content could reach lexical retrieval without persistence.

Uploaded file Evidence Ledger preview v0 proves that uploaded retrieval candidates can be transformed into preview Evidence Ledger entries without creating durable retrieval_runs or Evidence Ledger records.

This keeps the system inspectable while preserving the core claim boundary: candidate evidence can be shaped before a Noise Gate exists, but it has not passed Noise Gate and has not become a final report.

## Next product gate

The next product implementation gate should remain bounded:

```text
uploaded file Noise Gate preview v0
```

That future gate may run deterministic Noise Gate checks over the uploaded file Evidence Ledger preview output without persistence, final report generation, embeddings, semantic retrieval, or LLM calls.
