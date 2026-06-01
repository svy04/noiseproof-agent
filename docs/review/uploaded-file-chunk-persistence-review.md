# Uploaded File Chunk Persistence Review

Phase marker: uploaded file chunk persistence review v0.

## Purpose

This review decides the smallest safe persistence boundary after uploaded-file parsed document persistence.

It is review-only.

## Decision

Persist document chunk records before embeddings, semantic retrieval, or Evidence Ledger generation.

The next schema gate should create a chunk table, not raw file storage and not full parsed text storage:

```text
document_chunks
```

Candidate fields:

```text
id
document_id
source_type
source_uri
filename
chunk_strategy
chunk_index
text
character_start
character_end
metadata_json
persistence_boundary
created_at
```

The first persisted chunk artifact should keep:

```text
persistence_boundary = chunk_text_only_no_raw_file_storage
```

## Why this order

NoiseProof can already create a `documents` row from uploaded-file parser/profile output, but retrieval and later evidence work still need inspectable chunk records.

Persisting chunk records before embeddings keeps the next gate small and reviewable:

- source document identity is visible
- chunk strategy is visible
- chunk index and character bounds are visible
- chunk text is inspectable
- raw uploaded bytes remain out of storage
- full parsed text persistence remains out of scope

## Explicit Non-changes

This review adds no migration.

It adds no endpoint.

It adds no repository code.

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
uploaded file chunk persistence schema v0
```
