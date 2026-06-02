# Uploaded File Retrieval Persistence Application Refresh

Phase marker: uploaded file retrieval persistence application refresh v0.

This refresh surfaces the local runtime proof for document-scoped retrieval persistence in the application-facing documentation set.

It adds no runtime behavior.

## Primary Proof

```text
docs/review/uploaded-file-retrieval-persistence-runtime-smoke.md
```

The runtime smoke records local Docker PostgreSQL plus live FastAPI evidence for:

```text
POST /documents/upload-chunks
POST /documents/{document_id}/retrieval-runs
GET /retrieval-runs
```

Observed retrieval boundary:

```text
metadata_json.candidate_chunk_ids
metadata_source_table = document_chunks
retrieval_result_count = 2
latest_listed_id_matches = True
```

Observed non-claim boundary:

```text
no Evidence Ledger generation
no embeddings
no semantic retrieval
not financial advice
```

## Application Surface Updated

This refresh points the following reader surfaces to the uploaded-file retrieval persistence proof:

- `README.md`
- `docs/GOAL.md`
- `docs/runbook.md`
- `docs/application/portfolio-index.md`
- `docs/application/braincrew-role-map.md`
- `docs/review/application-ready-review.md`

## Allowed Claim

NoiseProof has local Docker DB plus FastAPI HTTP evidence that `POST /documents/{document_id}/retrieval-runs` can read persisted `document_chunks`, create a `retrieval_runs` row, and preserve candidate chunk ids in `metadata_json.candidate_chunk_ids`.

## Boundaries

This is not hosted deployment evidence.

It is not external reviewer feedback, not customer validation, not Braincrew acceptance, not Evidence Ledger generation, not Noise Gate generation, not report generation, not embeddings, not semantic retrieval, not LLM output, not financial advice, and not product-complete.

External reviewer feedback v0 remains open.

## Next Product Candidate

The next reviewer-facing gate should refresh external review request surfaces:

```text
external reviewer retrieval persistence request refresh v0
```
