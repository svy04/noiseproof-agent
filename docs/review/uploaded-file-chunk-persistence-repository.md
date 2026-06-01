# Uploaded File Chunk Persistence Repository

Phase marker: uploaded file chunk persistence repository v0.

## Purpose

This gate adds the first repository code for persisted document chunk rows.

It keeps chunk persistence behind repository methods only. No upload endpoint calls this path yet.

## Implemented Surface

```text
DocumentChunkCreate
create_document_chunk(payload)
list_document_chunks(document_id, limit)
```

`create_document_chunk` inserts into:

```text
document_chunks
```

`list_document_chunks` returns recent chunk rows for one document ordered by strategy and chunk index.

## Persistence Boundary

The repository stores derived chunk text and chunk metadata only:

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

This adds no endpoint.

It is not automatic persistence from upload preview.

It does not wire `POST /documents/upload-parsed-documents` to chunk creation.

It adds no retrieval persistence.

It adds no Evidence Ledger generation.

It adds no Noise Gate generation.

It adds no report generation.

It is not raw file storage.

It is not full parsed text persistence.

It is not hosted deployment evidence, external reviewer feedback, customer validation, Braincrew acceptance, LLM output, semantic retrieval, automatic failure-case creation, or product-complete claim.

## Test Evidence

Repository tests:

```text
tests/test_db.py::test_create_document_chunk_inserts_chunk_text_without_embeddings
tests/test_db.py::test_list_document_chunks_reads_recent_chunks_for_document
```

Docs guard:

```text
tests/test_docs.py::test_uploaded_file_chunk_persistence_repository_documents_code_boundary
```

## Next gate

```text
uploaded file chunk persistence endpoint review v0
```
