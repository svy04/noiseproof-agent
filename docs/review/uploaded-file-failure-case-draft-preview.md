# Uploaded File Failure-case Draft Preview

Phase marker: uploaded file failure-case draft preview v0.

## What changed

NoiseProof now exposes `POST /documents/upload-failure-case-draft-preview` as a preview-only boundary from multipart upload to report preview to failure-case draft preview.

The endpoint accepts an uploaded file, runs the upload report preview chain, then uses the existing failure-case draft preview shape to produce a human-confirmed draft when the uploaded report chain is blocked, needs revision, or otherwise requires review.

## Current behavior

The response includes:

- `filename`
- `content_type`
- `byte_count`
- `persistence_boundary`
- `source_type`
- `question`
- status
- upload report preview output
- failure-case draft preview output
- warnings

The persistence boundary is `preview_only_not_persisted`.

## Boundary

This endpoint is preview-only and does not create failure_cases.

It also does not create report records, Noise Gate records, Evidence Ledger entries, retrieval_runs, documents, chunks, workflow runs, or persisted failure records.

It requires human confirmation before any failure-case persistence.

It is not automatic failure detection, not root-cause automation, not LLM output, not hosted deployment evidence, not customer validation, and not production readiness.

The draft is a suggested payload for review. A human still needs to inspect the uploaded report preview, confirm the failure type, edit the draft if needed, and submit it through the existing `POST /failure-cases` path.

Questions that drift toward buy/sell or financial advice remain blocked and can produce a draft that records the boundary instead of creating advice.

## Why this gate matters

The previous uploaded file report preview proved that uploaded file evidence could reach the report-formatting boundary without persistence.

Uploaded file failure-case draft preview v0 proves that blocked or needs-revision uploaded report previews can be turned into inspectable failure-case draft payloads without pretending that failures are automatically detected, diagnosed, or persisted.

This keeps the system inspectable while preserving the human confirmation boundary.

## Next product gate

The next product implementation gate should stay small:

```text
uploaded file failure-case manual handoff smoke v0
```

That future gate may verify that a human-confirmed draft payload can be submitted through `POST /failure-cases` without claiming automatic failure-case creation.
