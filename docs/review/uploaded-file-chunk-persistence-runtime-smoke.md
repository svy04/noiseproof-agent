# Uploaded File Chunk Persistence Runtime Smoke

Phase marker: uploaded file chunk persistence runtime smoke v0.

## Purpose

This smoke verifies the explicit document-scoped chunk persistence endpoints against the local Docker PostgreSQL database.

It checks that derived chunk rows can be persisted and listed, while uploaded-file chunk preview remains preview-only.

## Environment

```text
DB: docker compose db on localhost:55432
API: uvicorn app.main:app on http://127.0.0.1:8034
DATABASE_URL: postgresql://noiseproof:noiseproof@localhost:55432/noiseproof
```

## Migration Evidence

Before applying the latest pending migration:

```text
Applied migrations: 11
Pending migrations: 1
pending 013_document_chunks.sql
```

After applying:

```text
Applied migrations: 12
Pending migrations: 0
applied 013_document_chunks.sql
```

Final status:

```text
Applied migrations: 12
Pending migrations: 0
```

## HTTP Smoke

Endpoints exercised:

```text
GET /health
POST /documents
POST /documents/{document_id}/chunks
GET /documents/{document_id}/chunks
POST /documents/upload-chunk-preview
GET /documents/{document_id}/chunks
```

Observed output:

```json
{
  "health_status": "ok",
  "document_id": "4ffda6fc-8753-44b5-a679-9f1173ec249f",
  "chunk_id": "2dbf68a5-0b93-422a-8bff-e6c05a207f81",
  "chunk_boundary": "chunk_text_only_no_raw_file_storage",
  "chunk_count": 1,
  "upload_preview_boundary": "preview_only_not_persisted",
  "upload_preview_strategy_count": 3,
  "chunk_count_after_upload_preview": 1
}
```

The unchanged `chunk_count_after_upload_preview` shows that the upload chunk preview did not automatically create chunk rows.

## SQL Check

```text
document_chunk_count | boundary
---------------------+-------------------------------------
1                    | chunk_text_only_no_raw_file_storage
```

## Boundary

This is runtime smoke evidence for local chunk persistence only.

It is not automatic persistence from upload preview.

It does not store raw uploaded bytes.

It does not store full parsed text.

It adds no embeddings.

Boundary shorthand:

```text
no embeddings
```

It adds no retrieval persistence.

It adds no Evidence Ledger generation.

It adds no Noise Gate generation.

It adds no report generation.

It is not hosted deployment evidence, external reviewer feedback, customer validation, Braincrew acceptance, LLM output, semantic retrieval, automatic failure-case creation, or product-complete claim.

## Next gate

```text
uploaded file chunk persistence application refresh v0
```
