# Uploaded Raw File Scan Result Endpoint Review

Status: review-only.

Phase marker: uploaded raw file scan result endpoint review v0.

## Purpose

This gate selects the smallest API boundary for scan result metadata after repository-only persistence exists.

It does not add endpoint code.

It does not run scanners.

It does not expose raw uploaded bytes.

It does not open a download path.

## Current State

NoiseProof has:

```text
uploaded_raw_files
raw_file_scan_results
RawFileScanResultCreate
create_raw_file_scan_result
list_raw_file_scan_results
```

The repository can persist caller-provided scan result rows, but there is no API surface for scan results yet.

## Decision

Use parent-scoped metadata-only routes:

```text
POST /documents/upload-raw-files/{raw_file_id}/scan-results
GET /documents/upload-raw-files/{raw_file_id}/scan-results
```

This keeps the scan result surface attached to the quarantined raw upload record without creating a generic raw-file browsing API.

## POST Boundary

`POST /documents/upload-raw-files/{raw_file_id}/scan-results` should:

- accept scan metadata only
- set `raw_file_id` from the path
- call `create_raw_file_scan_result`
- return the persisted scan result row
- preserve caller-provided `scan_status` and `scan_verdict`

The request body should use:

```text
RawFileScanResultCreate
```

but the path `raw_file_id` should be the authoritative parent id.

If a future request body also includes `raw_file_id`, endpoint code should reject mismatches instead of silently rewriting identity.

## GET Boundary

`GET /documents/upload-raw-files/{raw_file_id}/scan-results` should:

- call `list_raw_file_scan_results`
- filter by path `raw_file_id`
- optionally accept `scan_status`
- optionally accept `scan_verdict`
- return metadata-only scan result rows

The endpoint must not return:

```text
uploaded_raw_files.raw_bytes
```

## Metadata-only Response

The future endpoint response should include scan evidence metadata:

```text
id
raw_file_id
scanner_name
scanner_version
signature_db_version
scan_started_at
scan_finished_at
scan_status
scan_verdict
matched_signature
error_message
metadata_json
created_at
```

It should not include raw bytes or a download URL.

## Safety Semantics

scan_error is not clean.

`scan_status = failed` and `scan_verdict = scan_error` means no clean verdict was established.

The endpoint should store and return this state as-is. It should not convert scanner failures into clean verdicts.

## Guardrails

do not run scanners in endpoint code.

do not add a download endpoint in this gate.

The future endpoint implementation must not:

- call ClamAV
- shell out to `clamscan`
- call `clamdscan`
- inspect file signatures
- classify files as safe by itself
- expose raw uploaded bytes
- create Evidence Ledger rows
- call LLMs
- create automatic failure cases

## Selected Next Gate

```text
next product gate: uploaded raw file scan result endpoint v0
```

That gate may add route code and tests for caller-provided scan result metadata, but it should not add scanner execution, ClamAV integration, file signature validation, download behavior, runtime smoke evidence, hosted deployment evidence, or external reviewer feedback.

## Explicit Non-claims

This is review-only.

This is not endpoint code.

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

## Boundary

This review adds no endpoint code, repository code, scanner adapter, scanner process, ClamAV dependency, file signature validation, download endpoint, runtime behavior, hosted deployment evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete claim.
