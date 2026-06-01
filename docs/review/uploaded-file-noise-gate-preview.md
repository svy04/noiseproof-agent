# Uploaded File Noise Gate Preview

Phase marker: uploaded file Noise Gate preview v0.

## What changed

NoiseProof now exposes `POST /documents/upload-noise-gate-preview` as a preview-only boundary from multipart upload to lexical retrieval preview, Evidence Ledger preview, and deterministic Noise Gate preview.

The endpoint accepts an uploaded file, infers or accepts a source type, decodes uploaded bytes as UTF-8 text, runs the upload retrieval and Evidence Ledger preview chain, and checks the resulting preview entries with the existing deterministic Noise Gate.

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
- Noise Gate preview output
- warnings

The persistence boundary is `preview_only_not_persisted`.

## Boundary

This endpoint is preview-only and does not create Noise Gate records.

It also does not create Evidence Ledger entries, does not create retrieval_runs, documents, chunks, reports, workflow runs, or failure cases.

It is not final report generation, not Critic Agent expansion beyond the deterministic Noise Gate preview, not semantic retrieval, not embeddings, not LLM output, not dashboard polish, not hosted deployment evidence, and not production readiness.

It does not claim robust PDF extraction.

Retrieval candidates are not truth. Evidence Ledger preview entries are not accepted durable claims. The Noise Gate preview checks those entries, but it does not create a report or prove external validation.

Questions that drift toward buy/sell or financial advice are blocked at this preview boundary.

## Why this gate matters

The previous uploaded file Evidence Ledger preview proved that uploaded retrieval candidates could become preview Evidence Ledger entries without persistence.

Uploaded file Noise Gate preview v0 proves that uploaded file evidence can be checked by the same deterministic gate used elsewhere in the API before any report stage exists for uploaded files.

This keeps the system inspectable while preserving the core claim boundary: an uploaded file can reach the gate, but it has not become a final answer, production workflow, external review, or customer-validated result.

## Next product gate

The next product implementation gate should remain bounded:

```text
uploaded file report preview v0
```

That future gate may format claim-bounded report preview output from the uploaded file Noise Gate preview without persistence, semantic retrieval, embeddings, or LLM calls.
