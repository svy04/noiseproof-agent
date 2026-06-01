# Uploaded File Parsed Document Persistence Application Refresh

Phase marker: uploaded file parsed document persistence application refresh v0.

This refresh surfaces the local runtime proof for uploaded-file parsed document persistence in the application-facing documentation set.

Primary proof:

```text
docs/review/uploaded-file-parsed-document-persistence-runtime-smoke.md
```

The runtime smoke shows local Docker PostgreSQL plus live FastAPI evidence for:

```text
POST /documents/upload-parsed-documents
GET /documents
```

Observed persisted boundary:

```text
status = parsed_metadata_only
persistence_boundary = document_metadata_and_profile_only_no_raw_file_storage
raw_file_storage = false
parsed_text_storage = false
```

## Application Surface Updated

This refresh points the following reader surfaces to the uploaded-file parsed document persistence proof:

- `README.md`
- `docs/GOAL.md`
- `docs/runbook.md`
- `docs/application/portfolio-index.md`
- `docs/application/braincrew-role-map.md`
- `docs/review/application-ready-review.md`

## Allowed Claim

NoiseProof now has local runtime evidence that an uploaded markdown file can be parsed/profiled in-process and persisted as a `documents` metadata/profile row without raw uploaded bytes or parsed text storage.

## Boundaries

This is not hosted deployment evidence.

It is not external reviewer feedback, not customer validation, not Braincrew acceptance, not robust PDF extraction, not raw uploaded byte storage, not parsed text persistence, not persisted chunks, not retrieval-run creation, not Evidence Ledger generation, not Noise Gate generation, not report generation, not LLM calls, not embeddings, not semantic retrieval, not automatic failure-case creation, and not a product-complete claim.

External reviewer feedback v0 remains open.
