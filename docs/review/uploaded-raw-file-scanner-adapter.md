# Uploaded Raw File Scanner Adapter

Status: implemented.

Phase marker: uploaded raw file scanner adapter v0.

## Purpose

This gate adds the generic scanner adapter boundary selected in `docs/review/uploaded-raw-file-scanner-adapter-review.md`.

It does not add ClamAV.

It does not execute scanner processes.

It does not validate file signatures.

It does not open a download endpoint.

## Added Code

```text
packages/ingestion/scanning/__init__.py
packages/ingestion/scanning/adapter.py
apps/api/tests/test_raw_file_scanning.py
```

Exported names:

```text
ScanAdapterRequest
ScanAdapterResult
ScannerAdapter
ScannerUnavailableAdapter
build_scan_error_result
```

## Behavior

`ScanAdapterRequest` carries scanner input metadata:

```text
raw_file_id
storage_key
original_filename
declared_content_type
byte_size
content_sha256
temporary_scan_path
scanner_timeout_seconds
metadata
```

`ScanAdapterResult` maps to the existing `raw_file_scan_results` payload shape:

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

Required failure mapping now has code coverage:

```text
missing_scanner_binary -> failed / scan_error
timeout -> failed / scan_error
```

`ScannerUnavailableAdapter` returns a failed scan result instead of pretending the file is clean.

```text
do not write clean when the scanner is unavailable
```

`build_scan_error_result` returns:

```text
scan_status = failed
scan_verdict = scan_error
matched_signature = null
```

## Temporary Path Boundary

`temporary_scan_path` is accepted as internal scanner input context.

`temporary_scan_path is not persisted` in `metadata_json`.

The result records only:

```text
temporary_scan_path_present
```

This keeps raw upload quarantine inspectable without exposing private local file paths.

## Tests

Focused tests:

```bash
uv run pytest -q tests/test_raw_file_scanning.py
```

Observed:

```text
2 passed
```

## Boundary

This is not ClamAV integration.

This is not malware scanning.

This is not scanner process execution.

This is not file signature validation.

This is not a download endpoint.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

It is not Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.

## Next Product Gate

```text
uploaded raw file ClamAV adapter review v0
```
