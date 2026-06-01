# Uploaded File Intake Manifest Preview

Phase marker: uploaded file intake manifest preview v0.

## What changed

NoiseProof now exposes:

```text
POST /documents/upload-intake-manifest-preview
```

The endpoint returns a deterministic manifest for an uploaded file before any persisted file intake boundary is opened.

## Response contract

The preview includes:

- `filename`
- `content_type`
- `byte_count`
- `content_sha256`
- `source_type`
- `parser`
- `profile`
- `parse_warnings`
- `manifest`
- `storage_decision`
- `replayable`
- `persistence_boundary`
- `warnings`

The storage decision is intentionally explicit:

```text
do_not_persist_raw_upload_yet
```

The persistence boundary remains:

```text
preview_only_not_persisted
```

## Why this gate matters

The previous review decided not to persist raw uploaded bytes yet.

This gate creates the smallest inspectable bridge between upload preview and future persistence: a manifest shape that can later become an intake record if storage, retention, and replay boundaries are accepted.

It lets reviewers see what would be persisted before the project adds storage.

## Boundaries

This is not raw file storage.

It is not retrieval persistence.

It is not document row creation.

It adds no schema.

It adds no migration.

It does not create chunks, retrieval runs, Evidence Ledger records, Noise Gate records, report records, workflow runs, or failure cases.

It is not robust PDF extraction, not semantic retrieval, not embeddings, not LLM output, not hosted deployment evidence, not external reviewer feedback, not customer validation, not automatic failure-case creation, and not production readiness.

## Next gate

The next bounded evidence gate is:

```text
uploaded file intake manifest runtime smoke v0
```

That gate should call the new endpoint through a live local FastAPI server and record observed fields without claiming hosted deployment.
