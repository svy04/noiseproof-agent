# Uploaded Raw File Scan Result Schema Review

Status: review-only.

Phase marker: uploaded raw file scan result schema review v0.

## Purpose

This review decides the smallest durable schema boundary for scan evidence after the quarantined uploaded raw file storage safety review.

It does not add a migration.

It does not run a scanner.

It does not open a download path.

## Current State

NoiseProof currently has:

```text
uploaded_raw_files
POST /documents/upload-raw-files
GET /documents/upload-raw-files
raw_upload_quarantine_db_bytea_no_download_endpoint
max_raw_upload_bytes
metadata-only responses
```

The previous safety review selected this gate before any malware scanning, ClamAV adapter, or download endpoint:

```text
uploaded raw file scan result schema review v0
```

## Decision

Use a separate future `raw_file_scan_results` table instead of adding scan fields directly to `uploaded_raw_files`.

The future table should make scan provenance and failure modes inspectable:

```text
raw_file_scan_results
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

The future `raw_file_id` should reference:

```text
uploaded_raw_files(id)
```

## Status Vocabulary

Use `scan_status` for execution state:

```text
pending
running
completed
failed
skipped
```

Use `scan_verdict` for safety result:

```text
pending
clean
suspicious
infected
scan_error
skipped
```

`scan_error` must not be treated as `clean`.

`skipped` must require a visible reason in `metadata_json` or `error_message`.

## Why A Separate Table

Raw upload storage should stay the immutable quarantine record.

Scan results are derived artifacts that can change when:

- scanner engine changes
- scanner version changes
- signature database version changes
- scan timeout policy changes
- scan adapter changes from `clamscan` to `clamdscan`
- file type policy changes
- a file is re-scanned after definitions update

A separate `raw_file_scan_results` table allows multiple scan attempts for the same `uploaded_raw_files` row without rewriting the raw-file metadata or silently replacing previous verdicts.

## Required Metadata Before Migration

The future migration gate should require:

- `scanner_name`
- `scanner_version`
- `signature_db_version`
- `scan_started_at`
- `scan_finished_at`
- `scan_status`
- `scan_verdict`
- `matched_signature`
- `error_message`
- `metadata_json`

The first migration should also add an index on:

```text
raw_file_id
scan_status
scan_verdict
```

## Download Boundary

do not add a download endpoint in this gate.

Before any download endpoint, the project still needs:

```text
allowed extension and type policy
file signature validation
malware scan verdict
download authorization policy
retention and deletion policy
```

## Scanner Boundary

do not run ClamAV in this gate.

The future implementation path should be:

```text
uploaded raw file scan result schema v0
uploaded raw file scan result repository review v0
uploaded raw file scan result repository v0
uploaded raw file scan result endpoint review v0
uploaded raw file scan result endpoint v0
scanner adapter review v0
ClamAV adapter v0
```

This order keeps scan evidence persistence inspectable before a scanner process is introduced.

## Next Product Gate

The selected next product gate is:

```text
next product gate: uploaded raw file scan result schema v0
```

That gate may add a migration and init-schema update for `raw_file_scan_results`, but it should not add scanner execution, ClamAV integration, file signature validation, download behavior, hosted deployment evidence, or external reviewer feedback.

## Explicit Non-claims

This is not malware scanning.

This is not a download endpoint.

This is not runtime evidence.

This is not a migration.

This is not a ClamAV integration.

This is not file signature validation.

This is not a retention/deletion implementation.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not product-complete.

## Boundary

This review adds no schema, migration, endpoint, repository code, scanner adapter, scanner process, ClamAV dependency, file signature validation, download endpoint, retention/deletion behavior, hosted deployment evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete claim.
