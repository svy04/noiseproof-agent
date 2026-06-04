# Guarded Raw File Download Endpoint

Status: implemented.

Phase marker: guarded raw file download endpoint v0.

## Purpose

NoiseProof now has an explicit raw upload download route:

```text
GET /documents/upload-raw-files/{raw_file_id}/download
```

This endpoint exists so stored raw upload bytes can be retrieved only through a scan-first application boundary.

It does not make raw bytes available through metadata list responses.

It does not make uploaded files public static assets.

## Implemented Behavior

The endpoint:

```text
looks up the uploaded_raw_files row by raw_file_id
looks up the latest raw_file_scan_results row for that raw_file_id
requires scan_status=completed
requires scan_verdict=clean
returns 409 when the latest clean scan result required check fails
returns 404 when raw_file_id does not exist
returns bytes only from the explicit download route
sets Content-Disposition: attachment
sets X-Content-Type-Options: nosniff
sets X-NoiseProof-Download-Boundary: scan_first_latest_clean_result_required
sets X-NoiseProof-Authorization-Boundary: local_v0_no_auth_not_production
sets X-NoiseProof-Download-Rate-Limit-Boundary: planned_not_enforced_local_v0
```

The upload persistence boundary for new raw upload rows is now:

```text
raw_upload_quarantine_db_bytea_guarded_download_endpoint
```

Fresh schema default migration:

```text
db/migrations/019_uploaded_raw_file_guarded_download_boundary.sql
```

## Guarded Failure Cases

The route returns `409` when:

```text
no scan result exists
the latest scan_status is not completed
the latest scan_verdict is not clean
quarantine_status does not allow controlled retrieval
```

This matters because an older clean result must not open a download after a newer failed, infected, pending, suspicious, skipped, or scan_error result.

## Runtime Tests

Added tests:

```text
test_document_upload_raw_file_download_requires_latest_clean_scan_result
test_document_upload_raw_file_download_returns_bytes_after_latest_clean_scan_only
```

These tests prove the local route behavior with the in-memory test repository:

```text
missing scan result -> 409
clean then later failed scan result -> 409
latest clean scan result -> 200 and raw bytes returned
metadata upload/list responses still omit raw_bytes
```

## Boundary

This is local API behavior.

This is not production malware scanning evidence.

This is not endpoint malicious-detection runtime proof.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not production authorization.

This is not enforced download rate limiting.

This is not file signature validation.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, autonomous workflow execution, and not product-complete.
