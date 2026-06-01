# Uploaded File Chunk Persistence Endpoint Review

Phase marker: uploaded file chunk persistence endpoint review v0.

## Purpose

This review selects the smallest endpoint boundary for persisted uploaded-file chunk rows.

It is review-only.

## Decision

Add explicit document-scoped chunk endpoints next:

```text
POST /documents/{document_id}/chunks
GET /documents/{document_id}/chunks
```

The endpoints should call the existing repository surface:

```text
DocumentChunkCreate
DocumentChunkOut
create_document_chunk(payload)
list_document_chunks(document_id, limit)
```

The write endpoint should take `document_id` from the path and chunk fields from the request body. It should preserve:

```text
persistence_boundary = chunk_text_only_no_raw_file_storage
```

## Why this route shape

`POST /documents/{document_id}/chunks` keeps persistence explicit. A caller must already have a persisted document row before creating chunk rows.

This is smaller and safer than automatically wiring uploaded-file previews into persistence, because preview endpoints currently prove parser/profile/chunk behavior without creating records.

## Explicit Non-changes

This review adds no endpoint code.

It is not automatic persistence from upload preview.

It does not wire `POST /documents/upload-chunk-preview` to chunk creation.

It does not wire `POST /documents/upload-parsed-documents` to chunk creation.

It creates no chunk rows.

It stores no raw uploaded bytes.

It stores no full parsed text.

It adds no embeddings.

It adds no retrieval persistence.

It adds no Evidence Ledger generation.

It adds no Noise Gate generation.

It adds no report generation.

It is not hosted deployment evidence, external reviewer feedback, customer validation, Braincrew acceptance, LLM output, semantic retrieval, automatic failure-case creation, or product-complete claim.

## Next gate

```text
uploaded file chunk persistence endpoint v0
```
