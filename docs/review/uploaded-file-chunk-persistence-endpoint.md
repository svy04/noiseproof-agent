# Uploaded File Chunk Persistence Endpoint

Phase marker: uploaded file chunk persistence endpoint v0.

## Purpose

This gate exposes explicit document-scoped endpoints for persisted document chunk rows.

It keeps chunk persistence separate from uploaded-file preview endpoints.

## Implemented Surface

```text
POST /documents/{document_id}/chunks
GET /documents/{document_id}/chunks
```

Request/response schemas:

```text
DocumentChunkRequest
DocumentChunkCreate
DocumentChunkOut
```

Repository calls:

```text
create_document_chunk(payload)
list_document_chunks(document_id, limit)
```

## Persistence Boundary

The endpoint persists derived chunk text and chunk metadata only:

```text
persistence_boundary = chunk_text_only_no_raw_file_storage
```

It does not store raw uploaded bytes.

It does not store full parsed text.

It does not add embeddings.

Boundary shorthand:

```text
no embeddings
```

## Explicit Non-changes

This is not automatic persistence from upload preview.

It does not wire `POST /documents/upload-chunk-preview` to chunk creation.

It does not wire `POST /documents/upload-parsed-documents` to chunk creation.

It adds no retrieval persistence.

It adds no Evidence Ledger generation.

It adds no Noise Gate generation.

It adds no report generation.

It is not raw file storage.

It is not full parsed text persistence.

It is not hosted deployment evidence, external reviewer feedback, customer validation, Braincrew acceptance, LLM output, semantic retrieval, automatic failure-case creation, or product-complete claim.

## Test Evidence

Route tests:

```text
tests/test_routes.py::test_document_chunk_persistence_endpoint_roundtrip_explicit_document_scope
tests/test_routes.py::test_upload_chunk_preview_does_not_auto_persist_document_chunks
```

Docs guard:

```text
tests/test_docs.py::test_uploaded_file_chunk_persistence_endpoint_documents_route_boundary
```

## Next gate

```text
uploaded file chunk persistence runtime smoke v0
```
