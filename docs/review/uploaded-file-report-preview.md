# Uploaded File Report Preview

Phase marker: uploaded file report preview v0.

## What changed

NoiseProof now exposes `POST /documents/upload-report-preview` as a preview-only boundary from multipart upload to lexical retrieval preview, Evidence Ledger preview, deterministic Noise Gate preview, and claim-bounded report preview.

The endpoint accepts an uploaded file, infers or accepts a source type, decodes uploaded bytes as UTF-8 text, runs the upload retrieval and Evidence Ledger preview chain, and asks the deterministic report preview to format output only if the Noise Gate allows it.

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
- report preview output, including the embedded Noise Gate result
- warnings

The persistence boundary is `preview_only_not_persisted`.

## Boundary

This endpoint is preview-only and does not create report records.

It also does not create Noise Gate records, does not create Evidence Ledger entries, does not create retrieval_runs, documents, chunks, workflow runs, or failure cases.

It is not LLM output, not semantic retrieval, not embeddings, not dashboard polish, not hosted deployment evidence, not customer validation, and not production readiness.

It does not claim robust PDF extraction.

The report preview still obeys the Noise Gate. If uploaded evidence is missing source recency, has contradictions, lacks enough source support, or drifts toward buy/sell or financial advice, the response can remain `needs_revision` or `blocked` with no generated report body.

Questions that drift toward buy/sell or financial advice are blocked at this preview boundary.

## Why this gate matters

The previous uploaded file Noise Gate preview proved that uploaded file evidence could reach the deterministic gate without persistence.

Uploaded file report preview v0 proves that the same uploaded file chain can reach the report-formatting boundary while preserving the rule that unsupported or unsafe claims do not become report output.

This keeps the system inspectable while preserving the core claim boundary: a report preview is only a deterministic formatting surface over gate-allowed evidence, not a generated answer, product-complete workflow, external review, or customer-validated result.

## Next product gate

The next product implementation gate should be chosen after inspecting the current proof path. A bounded candidate is:

```text
uploaded file failure-case draft preview v0
```

That future gate may turn blocked or needs-revision upload report previews into failure-case draft candidates without persistence, semantic retrieval, embeddings, or LLM calls.
