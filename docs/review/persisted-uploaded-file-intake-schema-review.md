# Persisted Uploaded File Intake Schema Review

Phase marker: persisted uploaded file intake schema review v0.

## Purpose

This review decides the smallest safe persistence boundary after the uploaded-file intake manifest preview and runtime smoke.

It is review-only.

## Decision

Persist manifest metadata before raw uploaded bytes.

The next schema gate should create a manifest table, not file/blob storage:

```text
uploaded_file_intake_manifests
```

Candidate fields:

```text
id
content_sha256
filename
source_type
content_type
size_bytes
parser
profile_json
storage_decision
replayable
persistence_boundary
warnings_json
created_at
```

The first persisted upload artifact should keep `storage_decision = do_not_persist_raw_upload_yet` and `persistence_boundary = manifest_only_no_raw_file_storage`.

## Why this order

Manifest metadata lets the service record what it saw and how it classified the upload before opening raw file storage, parser output persistence, chunks, retrieval persistence, or report persistence.

This keeps the uploaded-file path inspectable while avoiding a premature storage contract.

## Explicit Non-changes

This review adds no migration.

It adds no endpoint.

It adds no raw uploaded bytes.

It adds no document row creation, chunk persistence, retrieval persistence, Evidence Ledger persistence, Noise Gate persistence, report persistence, workflow persistence, hosted deployment evidence, external reviewer feedback, customer validation, LLM calls, embeddings, semantic retrieval, or automatic failure-case creation.

## Next gate

```text
uploaded file intake manifest persistence schema v0
```
