# Uploaded File Chunk Persistence Application Refresh

Phase marker: uploaded file chunk persistence application refresh v0.

This refresh surfaces the local runtime proof for explicit document-scoped chunk persistence in the application-facing documentation set.

It adds no runtime behavior.

## Primary Proof

```text
docs/review/uploaded-file-chunk-persistence-runtime-smoke.md
```

The runtime smoke records local Docker PostgreSQL plus live FastAPI evidence for:

```text
POST /documents/{document_id}/chunks
GET /documents/{document_id}/chunks
```

Observed persisted boundary:

```text
persistence_boundary = chunk_text_only_no_raw_file_storage
chunk_count = 1
document_chunk_count = 1
```

Observed preview boundary:

```text
POST /documents/upload-chunk-preview
preview_boundary = preview_only_not_persisted
chunk_count_after_upload_preview = 1
```

## Application Surface Updated

This refresh points the following reader surfaces to the uploaded-file chunk persistence proof:

- `README.md`
- `docs/GOAL.md`
- `docs/runbook.md`
- `docs/application/portfolio-index.md`
- `docs/application/braincrew-role-map.md`
- `docs/review/application-ready-review.md`

## Allowed Claim

NoiseProof has local Docker DB plus FastAPI HTTP evidence that derived chunk text can be manually persisted and listed for an explicit document id through `POST /documents/{document_id}/chunks` and `GET /documents/{document_id}/chunks`, while uploaded-file chunk preview remains preview-only.

## Boundaries

This is not hosted deployment evidence.

It is not external reviewer feedback, not customer validation, not Braincrew acceptance, not automatic persistence from upload preview, not raw uploaded byte storage, not full parsed text persistence, not embeddings, not semantic retrieval, not retrieval persistence, not Evidence Ledger generation, not Noise Gate generation, not report generation, not LLM output, not automatic failure-case creation, and not product-complete.

External reviewer feedback v0 remains open.

## Next Product / Request Gate

```text
external reviewer chunk persistence request refresh v0
```
