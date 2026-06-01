# File Upload Preview

Phase marker: file upload preview v0.

## What changed

NoiseProof now exposes `POST /documents/upload-preview` as a preview-only upload boundary.

The endpoint accepts a multipart file upload, infers or accepts a source type, decodes uploaded bytes as UTF-8 text, runs the existing parser preview and document profiler, and returns the parse/profile result with upload metadata.

## Current behavior

The response includes:

- `filename`
- `content_type`
- `byte_count`
- `persistence_boundary`
- parser result
- document profile
- parser warnings
- failure-case candidate when the source type is unsupported

The persistence boundary is `preview_only_not_persisted`.

## Boundary

This endpoint is preview-only and does not create documents.

It also does not create parse records, chunks, retrieval runs, Evidence Ledger entries, Noise Gate records, reports, workflow runs, or failure cases.

It does not claim robust PDF extraction. PDF remains a text-only parser fallback unless a later tested gate adds real PDF extraction.

This is not retrieval, not embeddings, not semantic search, not Evidence Ledger generation, not Critic / Noise Gate expansion, not final report generation, not hosted deployment evidence, and not production readiness.

## Why this gate matters

Before a data agent can reason over messy data, it needs a visible boundary where user-provided files can enter the service and be inspected without being prematurely treated as trusted evidence.

File upload preview v0 gives reviewers a small, inspectable upload path while preserving the claim boundary: uploaded text can be previewed, but it is not yet trusted, indexed, retrieved, or reported.

## Next product gate

The next product implementation gate should stay small:

```text
uploaded file chunk preview v0
```

That future gate may pass uploaded preview text into chunk strategy comparison without adding persistence, retrieval expansion, embeddings, Evidence Ledger generation, or dashboard polish.
