# Persisted Uploaded File Intake Review

Phase marker: persisted uploaded file intake review v0.

## Purpose

This is a review-only gate for the question:

```text
Should uploaded files move from preview-only runtime behavior into persisted intake records now?
```

The answer for this phase is no.

Preview-only remains the current runtime boundary.

## Current evidence

The current upload chain already proves these bounded surfaces:

- `POST /documents/upload-preview`
- `POST /documents/upload-chunk-preview`
- `POST /documents/upload-retrieval-preview`
- `POST /documents/upload-evidence-preview`
- `POST /documents/upload-noise-gate-preview`
- `POST /documents/upload-report-preview`
- `POST /documents/upload-failure-case-draft-preview`
- manual `POST /failure-cases` handoff

`docs/review/uploaded-file-runtime-smoke-packet.md` records that this path runs over local Docker PostgreSQL plus live FastAPI HTTP.

## Current storage boundary

NoiseProof currently has a persisted `documents` metadata table, but uploaded file previews do not create document rows, chunk rows, retrieval runs, Evidence Ledger rows, Noise Gate records, report records, workflow runs, or failure cases.

That boundary is still correct.

The uploaded file path can inspect and transform input, but it has not yet earned raw file storage or automatic persistence.

## Options considered

### Option A - Keep upload previews preview-only

This preserves the current honest boundary. It is the safest default, but it does not give later stages a reusable uploaded-file intake artifact.

### Option B - Persist a `documents` row from upload preview

This would reuse the existing table, but it would make `source_uri = upload://filename` look more durable than it is. Without a persisted raw file, content hash, parser output, or storage location, the document row would be a weak replay artifact.

### Option C - Add raw file storage now

This would make uploaded files replayable, but it expands scope into file lifecycle, size limits, retention, privacy boundaries, and storage cleanup. That is too much for the current gate.

### Option D - Add a non-persisted intake manifest preview next

This would expose the exact manifest shape a future persisted intake would need, without creating storage or schema pressure yet.

The manifest can include filename, content type, byte count, inferred source type, content hash, parser/profile summary, warnings, and explicit persistence boundary.

## Decision

Do not persist raw uploaded bytes yet.

In short: do not persist raw uploaded bytes yet.

Do not create a persisted uploaded-file intake table yet.

Do not auto-create `documents` from upload preview yet.

The next product implementation gate should be:

```text
uploaded file intake manifest preview v0
```

That gate should return a deterministic intake manifest for uploaded content while keeping `persistence_boundary = preview_only_not_persisted`.

## Boundaries

This review adds no schema.

It adds no migration.

It adds no endpoint.

It adds no file storage.

It adds no retrieval persistence.

It adds no raw byte persistence, no object storage, no document row creation, no chunk persistence, no Evidence Ledger persistence, no Noise Gate persistence, no report persistence, no workflow persistence, no hosted deployment evidence, no external reviewer feedback, no customer validation, no LLM calls, no embeddings, no semantic retrieval, and no production readiness claim.

It is not automatic failure-case creation.

## Acceptance

A future upload intake implementation should not be accepted until it can answer:

- What durable artifact is created?
- Can the uploaded content be replayed?
- Is raw content stored or only summarized?
- What retention and privacy boundary applies?
- Which later stages are allowed to reference the intake artifact?
- What does the system refuse to infer from a filename alone?

Until then, preview-only remains the current runtime boundary.
