# Uploaded Raw File Scan Execution Endpoint

Status: implemented.

Phase marker: uploaded raw file scan execution endpoint v0.

## Purpose

This gate adds the explicit scan execution endpoint selected in `docs/review/uploaded-raw-file-scan-execution-review.md`.

It connects stored quarantined raw upload bytes to the configured scanner adapter and persists the adapter result as `raw_file_scan_results` metadata.

It does not prove real ClamAV execution.

It does not prove malware scanning.

It does not add a download endpoint.

## Implemented Surface

```text
POST /documents/upload-raw-files/{raw_file_id}/scan
```

Implemented files:

```text
apps/api/app/services/raw_file_scan_execution.py
apps/api/app/routes/documents.py
apps/api/app/db.py
apps/api/app/settings.py
apps/api/tests/test_routes.py
.env.example
```

## Execution Boundary

The endpoint:

```text
GET uploaded_raw_files row by path raw_file_id
  -> write raw_bytes to a service-generated temporary scan path
  -> build ScanAdapterRequest
  -> execute configured ScannerAdapter
  -> sanitize scan metadata
  -> persist RawFileScanResultCreate into raw_file_scan_results
  -> delete the temporary scan file through TemporaryDirectory cleanup
  -> return metadata-only RawFileScanResultOut
```

The endpoint does not accept caller-provided scan verdicts.

The existing endpoint below remains caller-provided metadata only:

```text
POST /documents/upload-raw-files/{raw_file_id}/scan-results
```

## Default Scanner Behavior

The default scanner is unavailable:

```text
NOISEPROOF_SCANNER=unavailable
```

Default behavior:

```text
scanner_name -> scanner-unavailable
scan_status -> failed
scan_verdict -> scan_error
failure_reason -> scanner_not_configured
```

If `NOISEPROOF_SCANNER=clamav`, the service uses `ClamAvScannerAdapter`.

That is still not a malware-scanning claim unless the runtime binary, signature database, and execution evidence are separately verified and recorded.

## Safety Rules

Implemented:

```text
path raw_file_id is authoritative
missing raw file returns 404
scan_error is never treated as clean
temporary scan path is service-generated
original filename is not used as the temporary scan filename
temporary scan file is removed after adapter execution
response contains no raw bytes
response contains no download URL
metadata sanitizes temporary_scan_path, raw_bytes, and file_bytes
default scanner unavailable returns scan_error
```

## Verification

Local targeted verification:

```bash
cd apps/api
uv run pytest -q tests/test_routes.py -k "scan_execution"
```

Observed result:

```text
3 passed, 108 deselected, 1 warning
```

The tests cover:

```text
default unavailable scanner persists failed / scan_error
fake scanner receives bytes through a temporary file
temporary file is deleted after endpoint completion
sensitive metadata keys do not leak
missing raw file returns 404
```

## Boundary

This is endpoint code.

This is not real ClamAV execution evidence.

This is not ClamAV installation evidence.

This is not ClamAV signature database evidence.

This is not malware scanning evidence.

This is not a download endpoint.

This is not hosted deployment evidence.

This is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.

## Next Product Gate

```text
uploaded raw file scan execution endpoint runtime smoke v0
```

That gate should verify the explicit scan endpoint against local Docker PostgreSQL and live FastAPI HTTP. It still must not claim real malware scanning unless `NOISEPROOF_SCANNER=clamav`, a real ClamAV binary, and signature database evidence are present and recorded.
