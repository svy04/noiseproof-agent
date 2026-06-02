# Uploaded Raw File Storage Application Refresh

Phase marker: uploaded raw file storage application refresh v0.

This refresh surfaces the local runtime proof for quarantined raw upload storage in the application-facing documentation set.

It adds no runtime behavior.

## Primary Proof

```text
docs/review/uploaded-raw-file-storage-runtime-smoke.md
```

The runtime smoke records local Docker PostgreSQL plus live FastAPI evidence for:

```text
POST /documents/upload-raw-files
GET /documents/upload-raw-files
oversized upload -> 413
```

Observed storage boundary:

```text
post_status -> stored_quarantined
boundary -> raw_upload_quarantine_db_bytea_no_download_endpoint
backend -> postgres_bytea
raw_file_storage -> true
response_has_raw_bytes -> false
storage_key_contains_filename -> false
```

Observed rejection boundary:

```text
oversized upload -> 413
oversized_detail -> raw upload size 1000001 exceeds max_raw_upload_bytes 1000000
```

## Application Surface Updated

This refresh points the following reader surfaces to the uploaded raw file storage runtime proof:

- `README.md`
- `docs/GOAL.md`
- `docs/runbook.md`
- `docs/application/portfolio-index.md`
- `docs/application/braincrew-role-map.md`
- `docs/review/application-ready-review.md`

## Allowed Claim

NoiseProof has local Docker DB plus FastAPI HTTP evidence that `POST /documents/upload-raw-files` can store original uploaded bytes in a quarantined PostgreSQL BYTEA table while returning metadata-only responses and rejecting oversized uploads.

## Boundaries

This is not hosted deployment evidence.

It is not external reviewer feedback, not customer validation, not Braincrew acceptance, not malware scanning, not a download endpoint, not robust PDF extraction, not parser quality evidence, not semantic retrieval evidence, not Evidence Ledger generation, not Critic / Noise Gate behavior, not final report generation, and not product-complete.

External reviewer feedback v0 remains open.

## Next Product Candidate

The next reviewer-facing gate can refresh external review request surfaces:

```text
external reviewer raw file storage request refresh v0
```
