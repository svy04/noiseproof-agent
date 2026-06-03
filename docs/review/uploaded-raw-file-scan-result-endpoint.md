# Uploaded Raw File Scan Result Endpoint

Status: implemented.

Phase marker: uploaded raw file scan result endpoint v0.

## Purpose

This gate adds metadata-only API endpoints for caller-provided raw file scan result rows.

It does not run scanners.

It does not run ClamAV.

It does not expose raw uploaded bytes.

It does not open a download path.

## Added Routes

```text
POST /documents/upload-raw-files/{raw_file_id}/scan-results
GET /documents/upload-raw-files/{raw_file_id}/scan-results
```

The routes use:

```text
RawFileScanResultCreate
RawFileScanResultOut
create_raw_file_scan_result
list_raw_file_scan_results
```

## POST Boundary

`POST /documents/upload-raw-files/{raw_file_id}/scan-results` stores caller-provided scan metadata for one quarantined raw upload.

The endpoint rejects mismatched parent identity:

```text
raw_file_id path/body mismatch
```

The route returns the persisted scan result row.

It does not return raw bytes.

It does not return a download URL.

## GET Boundary

`GET /documents/upload-raw-files/{raw_file_id}/scan-results` lists scan result rows for one quarantined raw upload.

It supports:

```text
scan_status
scan_verdict
limit
```

The response is metadata-only.

It does not return raw bytes.

It does not return a download URL.

## Safety Semantics

scan_error is not clean.

`scan_status = failed` and `scan_verdict = scan_error` means no clean verdict was established.

The endpoint stores and returns this state as-is. It does not convert scanner failures into clean verdicts.

## Guardrails

The endpoint does not run scanners.

It does not:

- call ClamAV
- shell out to `clamscan`
- call `clamdscan`
- inspect file signatures
- classify files as safe by itself
- expose raw uploaded bytes
- add a download endpoint
- generate Evidence Ledger rows
- call LLMs
- create automatic failure cases

## Verification

Unit tests verify that:

```text
POST persists metadata-only scan results
GET lists metadata-only scan results by raw_file_id
scan_status and scan_verdict filters work through the repository
raw bytes are absent from responses
download_url is absent from responses
path/body raw_file_id mismatch returns 400
```

## Explicit Non-claims

This is endpoint code only.

This is metadata-only scan result persistence.

This is not malware scanning.

This is not scanner execution.

This is not ClamAV integration.

This is not file signature validation.

This is not a download endpoint.

This is not runtime evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not product-complete.

## Next Product Gate

The selected next product gate is:

```text
uploaded raw file scan result endpoint runtime smoke v0
```

That gate may verify the metadata-only endpoints against local Docker PostgreSQL and live FastAPI HTTP, but it should not add scanner execution, ClamAV integration, file signature validation, download behavior, hosted deployment evidence, or external reviewer feedback.
