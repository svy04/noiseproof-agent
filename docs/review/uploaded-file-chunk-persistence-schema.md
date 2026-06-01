# Uploaded File Chunk Persistence Schema

Phase marker: uploaded file chunk persistence schema v0.

## Purpose

This gate adds the schema needed to persist derived chunk records for uploaded-file parsed documents.

It is schema-only.

## Implemented Schema

```text
document_chunks
```

Source files:

- `db/init/001_schema.sql`
- `db/migrations/013_document_chunks.sql`

Fields:

```text
id
document_id
source_type
source_uri
filename
chunk_strategy
chunk_index
chunk_text
character_start
character_end
metadata_json
persistence_boundary
created_at
```

Boundary:

```text
persistence_boundary = chunk_text_only_no_raw_file_storage
```

Indexes:

```text
idx_document_chunks_document_id
idx_document_chunks_strategy
```

## Explicit Non-changes

This adds no endpoint.

It adds no repository code.

It creates no chunk rows.

It stores no raw uploaded bytes.

It is not raw file storage.

It is not full parsed text persistence.

It adds no embeddings.

It adds no semantic retrieval.

It adds no retrieval-run-linked Evidence Ledger records.

It adds no Noise Gate generation.

It adds no report generation.

It is not hosted deployment evidence, external reviewer feedback, customer validation, Braincrew acceptance, LLM output, automatic failure-case creation, or product-complete claim.

## Next gate

```text
uploaded file chunk persistence repository review v0
```
