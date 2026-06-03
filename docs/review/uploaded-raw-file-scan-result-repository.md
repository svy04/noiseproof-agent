# Uploaded Raw File Scan Result Repository

Status: implemented.

Phase marker: uploaded raw file scan result repository v0.

## Purpose

This gate adds repository-only persistence for caller-provided scan result rows.

It does not add endpoint code.

It does not run scanners.

It does not run ClamAV.

It does not expose raw uploaded bytes.

## Added Code

Schema models:

```text
RawFileScanResultCreate
RawFileScanResultOut
```

Repository methods:

```text
create_raw_file_scan_result
list_raw_file_scan_results
```

Persistence table:

```text
raw_file_scan_results
```

Parent table:

```text
uploaded_raw_files
```

## Create Boundary

`create_raw_file_scan_result` accepts caller-provided scan metadata:

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

The method inserts into:

```text
raw_file_scan_results
```

and returns the persisted row.

It does not read or return:

```text
uploaded_raw_files.raw_bytes
```

## List Boundary

`list_raw_file_scan_results` supports operator-facing filters:

```text
raw_file_id
scan_status
scan_verdict
limit
```

It reads from `raw_file_scan_results` only.

It does not join raw upload bytes.

It does not expose a download path.

## Failure Semantics

scan_error is not clean.

The repository records the caller-provided status and verdict. It does not infer file safety.

A row with:

```text
scan_status = failed
scan_verdict = scan_error
```

means scanner execution did not establish a clean verdict.

## Guardrails

This repository boundary intentionally does less than a security scanner.

It does not run scanners.

It does not:

- call ClamAV
- shell out to `clamscan`
- call `clamdscan`
- inspect file signatures
- classify files as safe
- add an API endpoint
- add a download endpoint
- expose raw uploaded bytes
- generate Evidence Ledger rows
- create automatic failure cases

## Verification

Unit tests verify that:

```text
RawFileScanResultCreate exists
create_raw_file_scan_result inserts caller-provided rows
list_raw_file_scan_results filters by raw_file_id, scan_status, and scan_verdict
repository SQL does not expose raw_bytes
repository code does not invoke scanner commands
```

## Explicit Non-claims

This is repository code only.

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

## Next Product Gate

The selected next product gate is:

```text
uploaded raw file scan result endpoint review v0
```

That gate should decide whether scan results need an explicit POST/GET endpoint, and if so how to keep it metadata-only before any scanner execution, ClamAV integration, file signature validation, download endpoint, hosted deployment evidence, or external reviewer feedback.
