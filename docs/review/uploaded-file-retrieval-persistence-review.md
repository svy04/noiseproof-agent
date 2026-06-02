# Uploaded File Retrieval Persistence Review

Phase marker: uploaded file retrieval persistence review v0.

Status: review-only.

## Decision

Persist uploaded-file retrieval runs over already persisted document chunks by reusing the existing retrieval infrastructure first.

Selected future endpoint:

```text
POST /documents/{document_id}/retrieval-runs
GET /retrieval-runs
```

Selected source boundary:

```text
existing document_chunks table
source_table = document_chunks
```

Selected persistence boundary:

```text
existing retrieval_runs table
metadata_json.candidate_chunk_ids
metadata_json.source_table = document_chunks
metadata_json.document_id
```

## Why This Is The Smallest Next Step

NoiseProof already has:

- an existing `retrieval_runs` table
- an existing `document_chunks` table
- a lexical retrieval service that can rank source chunks
- `POST /documents/upload-chunks` to create a document row plus derived chunk rows
- `GET /documents/{document_id}/chunks` to inspect persisted chunks

The next implementation should connect those existing surfaces before adding a new retrieval-candidates table.

## What The Future Endpoint Should Do

`POST /documents/{document_id}/retrieval-runs` should:

1. read chunks from the existing `document_chunks` rows for the document
2. run lexical retrieval over those chunks
3. create one row in the existing `retrieval_runs` table
4. store candidate chunk ids in `metadata_json`
5. return retrieval candidates with chunk ids and evidence text in the response

## Explicit Non-decisions

Do not add a new retrieval_candidates table in the first implementation:

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

Do not make buy/sell, target price, or financial advice behavior.

This is not financial advice.

## Future Implementation Gate

The next product implementation gate should be:

```text
uploaded file retrieval persistence endpoint v0
```

That gate should still be lexical retrieval only. It should persist only the run record and inspectable candidate references, not embeddings, semantic retrieval, Evidence Ledger entries, Noise Gate records, reports, or financial advice.

## Boundaries

This review adds no runtime behavior.

It adds no schema, migration, endpoint code, retrieval rows, candidate rows, embeddings, semantic retrieval, Evidence Ledger generation, Noise Gate generation, report generation, LLM output, hosted deployment evidence, external reviewer feedback, customer validation, Braincrew acceptance, financial advice, or product-complete claim.
