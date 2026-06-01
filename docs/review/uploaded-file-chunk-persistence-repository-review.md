# Uploaded File Chunk Persistence Repository Review

Phase marker: uploaded file chunk persistence repository review v0.

## Purpose

This review selects the smallest repository boundary over the new `document_chunks` schema before adding code.

It is review-only.

## Decision

Add repository code only after the schema exists, and keep the first write/read surface narrow:

```text
DocumentChunkCreate
create_document_chunk(payload)
list_document_chunks(document_id, limit)
```

The repository should write to:

```text
document_chunks
```

Required inputs:

```text
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
```

The first repository implementation should preserve:

```text
persistence_boundary = chunk_text_only_no_raw_file_storage
```

## Why this order

The schema is present, but there is still no safe write path for chunk records. A repository boundary lets tests prove metadata and chunk text persistence before any endpoint, retrieval, embedding, or Evidence Ledger wiring.

## Explicit Non-changes

This review adds no repository code.

It adds no endpoint.

It creates no chunk rows.

It adds no embeddings.

It adds no retrieval persistence.

It adds no Evidence Ledger generation.

It adds no Noise Gate generation.

It adds no report generation.

It is not raw file storage.

It is not full parsed text persistence.

It is not hosted deployment evidence, external reviewer feedback, customer validation, Braincrew acceptance, LLM output, semantic retrieval, automatic failure-case creation, or product-complete claim.

## Next gate

```text
uploaded file chunk persistence repository v0
```
