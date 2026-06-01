# Uploaded File Intake Manifest Persistence Schema

Phase marker: uploaded file intake manifest persistence schema v0.

## Purpose

This gate adds the first manifest-only upload persistence table.

It records upload intake metadata, not raw uploaded bytes.

## Implemented Schema

```text
uploaded_file_intake_manifests
```

Key fields:

```text
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

The table keeps the default boundary:

```text
storage_decision = do_not_persist_raw_upload_yet
persistence_boundary = manifest_only_no_raw_file_storage
```

## Boundary

This is schema only.

It adds no endpoint.

It stores no raw uploaded bytes.

It adds no parser output persistence, document row creation, chunk persistence, retrieval persistence, Evidence Ledger persistence, Noise Gate persistence, report persistence, workflow persistence, hosted deployment evidence, external reviewer feedback, customer validation, LLM calls, embeddings, semantic retrieval, or automatic failure-case creation.

## Files

- `db/init/001_schema.sql`
- `db/migrations/012_uploaded_file_intake_manifests.sql`

## Next gate

```text
uploaded file intake manifest persistence repository review v0
```
