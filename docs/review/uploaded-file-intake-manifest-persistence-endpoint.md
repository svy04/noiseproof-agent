# Uploaded File Intake Manifest Persistence Endpoint

Phase marker: uploaded file intake manifest persistence endpoint v0.

## Purpose

This gate adds HTTP API behavior for persisting uploaded-file intake manifests as metadata only.

It keeps the raw upload boundary closed.

## Implemented Endpoint Surface

```text
POST /documents/upload-intake-manifests
GET /documents/upload-intake-manifests
```

`POST /documents/upload-intake-manifests` reads an uploaded file, generates the bounded intake manifest, and persists only manifest metadata through `create_uploaded_file_intake_manifest`.

`GET /documents/upload-intake-manifests` returns recent manifest metadata through `list_uploaded_file_intake_manifests`.

Persisted rows keep:

```text
persistence_boundary = manifest_only_no_raw_file_storage
storage_decision = do_not_persist_raw_upload_yet
replayable = false
```

## Boundary

This endpoint stores no raw uploaded bytes.

It is not document creation.

It is not parser output persistence.

It adds no chunk persistence, retrieval persistence, Evidence Ledger persistence, Noise Gate persistence, report persistence, workflow persistence, hosted deployment evidence, external reviewer feedback, customer validation, LLM calls, embeddings, semantic retrieval, or automatic failure-case creation.

## Files

- `apps/api/app/routes/documents.py`
- `apps/api/app/db.py`
- `apps/api/app/schemas.py`
- `apps/api/tests/test_routes.py`

## Next Gate

```text
uploaded file intake manifest persistence runtime smoke v0
```
