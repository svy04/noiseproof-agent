# Uploaded File Intake Manifest Persistence Repository Review

Phase marker: uploaded file intake manifest persistence repository review v0.

## Purpose

This is a review-only gate before adding repository code for uploaded-file intake manifests.

The goal is to keep the first repository boundary small: record and read manifest metadata from `uploaded_file_intake_manifests` without storing raw uploaded bytes.

## Proposed Repository Surface

```text
create_manifest(manifest)
list_recent_manifests(limit)
```

`create_manifest` should accept only manifest metadata already produced by the upload intake manifest preview path.

`list_recent_manifests` should support operator inspection and later ops-summary wiring, not user-facing file browsing.

## Required Manifest Fields

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
```

The repository should preserve these defaults unless a later reviewed gate changes them:

```text
storage_decision = do_not_persist_raw_upload_yet
persistence_boundary = manifest_only_no_raw_file_storage
replayable = false
```

## Boundary

This gate adds no repository code.

It adds no endpoint.

It stores no raw uploaded bytes.

It adds no parser output persistence, document row creation, chunk persistence, retrieval persistence, Evidence Ledger persistence, Noise Gate persistence, report persistence, workflow persistence, hosted deployment evidence, external reviewer feedback, customer validation, LLM calls, embeddings, semantic retrieval, or automatic failure-case creation.

## Next Gate

```text
uploaded file intake manifest persistence repository v0
```
