# Uploaded File Chunk Persistence Handoff Endpoint

Status: route-level implementation artifact.

Phase marker: uploaded file chunk persistence handoff endpoint v0.

Label: Uploaded file chunk persistence handoff endpoint.

This artifact records the implementation of an explicit upload-to-chunks handoff endpoint. It connects uploaded file parsing, profiling, chunking, document metadata persistence, and derived chunk-text persistence without changing the existing preview route.

## Implemented Surface

```text
POST /documents/upload-chunks
```

Response model:

```text
UploadChunkPersistenceOut
```

The endpoint creates a document row and creates document_chunks rows for a selected chunk strategy.

It uses:

```text
documents
document_chunks
preview_uploaded_chunks()
DocumentCreate
DocumentChunkCreate
```

## Boundary

The existing upload chunk preview remains preview-only.

The endpoint uses a separate explicit handoff boundary:

```text
explicit_upload_to_chunks_no_raw_file_storage
```

Persisted chunk rows keep:

```text
chunk_text_only_no_raw_file_storage
```

The document metadata row records:

```text
document_metadata_and_chunks_only_no_raw_file_storage
raw_file_storage = false
parsed_text_storage = false
```

## Route Test Evidence

Route-level test:

```text
tests/test_routes.py::test_document_upload_chunks_persists_document_and_chunks_without_raw_file_storage
```

The test verifies:

```text
POST /documents/upload-chunks -> 201
document row created
document_chunks rows created
returned chunks share the created document id
chunk_text_only_no_raw_file_storage boundary
explicit_upload_to_chunks_no_raw_file_storage handoff boundary
no raw uploaded byte storage
no full parsed text persistence
no embeddings
no retrieval persistence
```

## Allowed Claim

NoiseProof has a route-level implementation for explicit uploaded-file-to-document-chunks handoff. It can create document metadata plus derived chunk rows from uploaded content through `POST /documents/upload-chunks`.

## Boundary / Non-claims

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not raw uploaded byte storage.

This is not full parsed text persistence.

This adds no embeddings.

This adds no retrieval persistence.

This adds no Evidence Ledger persistence.

This adds no Noise Gate persistence.

This adds no report persistence.

This is not robust PDF extraction.

This is not semantic retrieval.

This is not product-complete.

## Next Gate

The next bounded proof gate should be a runtime smoke:

```text
uploaded file chunk persistence handoff runtime smoke v0
```
