# Uploaded Raw File Scan Result Repository Review

Status: review-only.

Phase marker: uploaded raw file scan result repository review v0.

## Purpose

This gate selects the smallest repository boundary for future scan-attempt persistence after `raw_file_scan_results` was added.

It does not add repository code.

It does not add an endpoint.

It does not run scanners.

It does not run ClamAV.

It does not open a download path.

## Current State

NoiseProof has:

```text
uploaded_raw_files
raw_file_scan_results
db/migrations/017_raw_file_scan_results.sql
```

The raw file table is quarantine storage.

The scan result table is a derived evidence table for future scan attempts.

## Decision

Add repository code next, but keep it persistence-only.

The selected boundary is:

```text
RawFileScanResultCreate
create_raw_file_scan_result
list_raw_file_scan_results
```

`create_raw_file_scan_result` should insert a caller-provided scan result row for an existing `uploaded_raw_files` record.

`list_raw_file_scan_results` should support operator inspection by:

```text
raw_file_id
scan_status
scan_verdict
limit
```

The repository must not infer safety, hide failed scans, or convert errors into clean verdicts.

scan_error is not clean.

## Required Create Fields

`RawFileScanResultCreate` should accept:

```text
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
```

The repository should preserve the database defaults unless the caller explicitly passes safer reviewed values:

```text
scan_status = pending
scan_verdict = pending
metadata_json = {}
```

## Read Boundary

`list_raw_file_scan_results` should read from:

```text
raw_file_scan_results
```

and may join or validate against:

```text
uploaded_raw_files
```

only to ensure the parent raw file exists or to support later operator inspection.

It should return metadata and verdict fields only. It must not return raw uploaded bytes.

## Guardrails

do not run scanners in repository code.

do not add an endpoint in this gate.

The future repository implementation must not:

- call ClamAV
- shell out to `clamscan`
- call `clamdscan`
- inspect raw file signatures
- classify files as safe by itself
- add a download endpoint
- expose `uploaded_raw_files.raw_bytes`
- generate Evidence Ledger rows
- call LLMs
- create automatic failure cases

## Selected Next Gate

```text
next product gate: uploaded raw file scan result repository v0
```

That gate may add repository code and tests around caller-provided rows, but it should not add endpoint code, scanner execution, ClamAV integration, file signature validation, download behavior, runtime smoke evidence, hosted deployment evidence, or external reviewer feedback.

## Explicit Non-claims

This is review-only.

This is not repository code.

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

This review adds no repository code, endpoint, scanner adapter, scanner process, ClamAV dependency, file signature validation, download endpoint, runtime behavior, hosted deployment evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete claim.
