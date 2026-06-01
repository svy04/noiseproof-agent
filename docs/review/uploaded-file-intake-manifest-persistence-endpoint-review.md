# Uploaded File Intake Manifest Persistence Endpoint Review

Phase marker: uploaded file intake manifest persistence endpoint review v0.

## Purpose

This is a review-only gate before adding HTTP API behavior for uploaded-file intake manifest persistence.

The endpoint should persist manifest metadata only, using the existing upload intake manifest preview path and repository methods. It should not persist raw uploaded bytes.

## Proposed Endpoint Surface

```text
POST /documents/upload-intake-manifests
GET /documents/upload-intake-manifests
```

`POST /documents/upload-intake-manifests` should accept one uploaded file, generate the same bounded manifest used by the preview route, and call `create_uploaded_file_intake_manifest`.

`GET /documents/upload-intake-manifests` should call `list_uploaded_file_intake_manifests` for recent operator inspection.

## Boundary

This gate is review-only.

It adds no endpoint code.

It stores no raw uploaded bytes.

It is not document creation.

It adds no parser output persistence, chunk persistence, retrieval persistence, Evidence Ledger persistence, Noise Gate persistence, report persistence, workflow persistence, hosted deployment evidence, external reviewer feedback, customer validation, LLM calls, embeddings, semantic retrieval, or automatic failure-case creation.

## Next Gate

```text
uploaded file intake manifest persistence endpoint v0
```
