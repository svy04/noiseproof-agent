# Uploaded File Retrieval Persistence Endpoint

Phase marker: uploaded file retrieval persistence endpoint v0.

Status: implemented locally through route tests.

## What Changed

NoiseProof now has a document-scoped retrieval persistence endpoint:

```text
POST /documents/{document_id}/retrieval-runs
```

The endpoint reads persisted chunks from the existing document chunk surface:

```text
existing document_chunks table
```

It stores one run in:

```text
existing retrieval_runs table
```

The run metadata records:

```text
metadata_json.source_table = document_chunks
metadata_json.document_id
metadata_json.candidate_chunk_ids
metadata_json.persistence_boundary = document_chunk_retrieval_run_only_no_evidence_ledger
```

## Runtime Boundary

The endpoint is lexical only.

It ranks already persisted `document_chunks` by matched query terms and returns candidate chunks with inspectable chunk ids, document ids, evidence text, matched terms, and source-table metadata.

It does not re-parse raw uploads.

It does not store raw uploaded bytes.

It does not store full parsed document text outside chunk rows.

## Existing Retrieval Listing

The existing listing endpoint remains:

```text
GET /retrieval-runs
```

It can show the persisted run row and the `metadata_json.candidate_chunk_ids` handoff without storing a new candidate table.

## Explicit Non-decisions

No new retrieval candidate table:

```text
no new retrieval_candidates table
```

No embeddings:

```text
no embeddings
```

No semantic retrieval:

```text
no semantic retrieval
```

No Evidence Ledger generation:

```text
no Evidence Ledger generation
```

Do not generate Noise Gate records.

Do not generate report records.

Do not treat retrieved chunks as truth.

This is not financial advice.

## Tests

Route tests cover:

- a document with persisted chunks
- candidate ranking from `document_chunks`
- `retrieval_runs.metadata_json.candidate_chunk_ids`
- no-results behavior when a document has no chunks
- financial-advice boundary text in warnings

## Next Gate

The next proof gate should be:

```text
uploaded file retrieval persistence runtime smoke v0
```

That gate should verify the endpoint against local Docker PostgreSQL and live FastAPI HTTP before claiming runtime evidence.

## Boundaries

This endpoint gate adds route-level behavior only.

It adds no schema, migration, retrieval candidate rows, retrieval-candidates table, embeddings, semantic retrieval, Evidence Ledger generation, Noise Gate generation, report generation, LLM output, hosted deployment evidence, external reviewer feedback, customer validation, Braincrew acceptance, financial advice, or product-complete claim.
