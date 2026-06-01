# Uploaded File Intake Manifest Persistence Repository

Phase marker: uploaded file intake manifest persistence repository v0.

## Purpose

This gate adds the first repository code for uploaded-file intake manifests.

It persists and reads manifest metadata from `uploaded_file_intake_manifests`. It does not persist raw uploaded bytes.

## Implemented Repository Surface

```text
UploadedFileIntakeManifestCreate
create_uploaded_file_intake_manifest(payload)
list_uploaded_file_intake_manifests(limit)
```

`create_uploaded_file_intake_manifest` inserts manifest metadata only.

`list_uploaded_file_intake_manifests` returns recent manifest metadata for operator inspection and later bounded ops wiring.

## Boundary

This is repository code only.

It adds no endpoint.

It stores no raw uploaded bytes.

It is not automatic persistence from upload preview.

It adds no parser output persistence, document row creation, chunk persistence, retrieval persistence, Evidence Ledger persistence, Noise Gate persistence, report persistence, workflow persistence, hosted deployment evidence, external reviewer feedback, customer validation, LLM calls, embeddings, semantic retrieval, or automatic failure-case creation.

## Files

- `apps/api/app/schemas.py`
- `apps/api/app/db.py`
- `apps/api/tests/test_db.py`

## Next Gate

```text
uploaded file intake manifest persistence endpoint review v0
```
