# Uploaded Raw File Scan Result Endpoint Runtime Smoke

Status: implemented.

Phase marker: uploaded raw file scan result endpoint runtime smoke v0.

## Purpose

This smoke verifies the metadata-only raw file scan result endpoints against local Docker PostgreSQL and a live FastAPI process.

It does not run scanners.

It does not run ClamAV.

It does not expose raw uploaded bytes.

It does not prove hosted deployment behavior.

## Environment

```text
Docker version 29.4.3
Docker Compose version v5.1.3
noiseproof-agent-db healthy on localhost:55432
FastAPI on http://127.0.0.1:8033
```

Compose was checked with:

```text
docker compose config
```

Migration runner status:

```text
Applied migrations: 16
Pending migrations: 0
```

## Live HTTP Checks

Observed:

```text
GET /health -> 200
POST /documents/upload-raw-files -> 201
raw_file_id -> b7772383-2eb5-47da-953f-d4fafdf088ec
POST /documents/upload-raw-files/{raw_file_id}/scan-results -> 201
scan_result_id -> 9db5efd8-dad8-40b3-970f-671e5131cc43
scan_verdict -> scan_error
GET /documents/upload-raw-files/{raw_file_id}/scan-results -> 200
listed_count -> 1
path/body mismatch -> 400
```

Mismatch detail:

```json
{"detail":"raw_file_id path/body mismatch"}
```

Response boundary checks:

```text
response_has_raw_bytes -> false
list_has_raw_bytes -> false
download_url_present -> false
list_download_url_present -> false
```

Uvicorn log confirmed:

```text
GET /health HTTP/1.1 200 OK
POST /documents/upload-raw-files HTTP/1.1 201 Created
POST /documents/upload-raw-files/{raw_file_id}/scan-results HTTP/1.1 201 Created
GET /documents/upload-raw-files/{raw_file_id}/scan-results?scan_status=failed&scan_verdict=scan_error HTTP/1.1 200 OK
POST /documents/upload-raw-files/{raw_file_id}/scan-results HTTP/1.1 400 Bad Request
```

## Interpretation

This proves only that the local API can:

- store a quarantined raw uploaded file
- store caller-provided scan result metadata for that raw file
- list scan result metadata by raw file id
- preserve `scan_error` as a non-clean verdict
- reject path/body raw file id mismatch
- keep raw bytes and download URLs out of scan result responses

## Explicit Non-claims

This is not malware scanning.

This is not scanner execution.

This is not ClamAV integration.

This is not file signature validation.

This is not a download endpoint.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not product-complete.

## Next Product Gate

The selected next product gate is:

```text
external reviewer scan-result endpoint request refresh v0
```

That gate may point reviewer-facing surfaces to this local runtime proof, but it should not claim hosted deployment evidence, scanner execution, ClamAV integration, download behavior, external reviewer feedback, customer validation, or product completeness.
