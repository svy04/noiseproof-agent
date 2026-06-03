# Uploaded Raw File Scan Execution Review

Status: review-only.

Phase marker: uploaded raw file scan execution review v0.

## Purpose

This gate selects the next bounded product path for connecting quarantined raw uploads to scanner adapter execution.

It does not add endpoint code.

It does not execute ClamAV.

It does not claim malware scanning evidence.

## Source-first Anchors

- ClamAV Scanning documentation: https://docs.clamav.net/manual/Usage/Scanning.html
- OWASP File Upload Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html
- Python subprocess documentation: https://docs.python.org/3/library/subprocess.html

Interpretation used for this review:

```text
ClamAV clamscan is appropriate as the first bounded one-time scanner adapter because it can scan a specified file path without a long-running clamd dependency.
OWASP treats upload safety as defense-in-depth, so scanner execution must not replace size limits, generated storage keys, metadata-only responses, no download endpoint, and explicit claim boundaries.
Python subprocess execution should use a sequence of arguments, capture output, and timeout handling; timeout behavior is still not a proof of complete process control.
```

## Existing Inputs

Already implemented:

```text
uploaded_raw_files metadata and PostgreSQL BYTEA storage
raw_file_scan_results metadata table
raw file scan result POST/GET endpoint for caller-provided scan metadata
ScannerAdapter boundary
ClamAvScannerAdapter
deterministic ClamAV adapter runtime smoke command
```

Still unimplemented:

```text
endpoint that executes a scanner against a stored raw upload
real ClamAV runtime verification
signature database verification
malware scanning evidence
download endpoint
```

## Selected Future Execution Boundary

Use a new explicit execution endpoint:

```text
POST /documents/upload-raw-files/{raw_file_id}/scan
```

Do not overload:

```text
POST /documents/upload-raw-files/{raw_file_id}/scan-results
```

Reason:

```text
scan-results stores caller-provided metadata.
scan executes configured scanner logic and then writes scan result metadata.
Those are different trust boundaries.
```

## Future Execution Flow

```text
GET uploaded_raw_files row by raw_file_id
  -> write BYTEA to generated temp scan path
  -> build ScanAdapterRequest
  -> execute configured scanner adapter
  -> persist ScanAdapterResult into raw_file_scan_results
  -> delete temp scan file in finally
  -> return metadata-only scan result response
```

## Required Safety Rules

Future implementation must keep:

```text
path raw_file_id is authoritative
no raw bytes in response
no download URL in response
no original filename in temp path
no user-controlled shell command string
no shell=True
no --remove
no --move in v0
no daemon TCP socket in v0
timeout maps to scan_error
missing scanner maps to scan_error
unknown return code maps to scan_error
scan_error is never treated as clean
```

Future temp file handling:

```text
service-controlled temp directory
generated filename only
write bytes from database
delete temp file in finally
metadata may record temporary_scan_path_present
metadata must not record the actual temporary path
```

## Selected Scanner Configuration

Future v0 should default to an unavailable scanner unless explicitly configured:

```text
NOISEPROOF_SCANNER=unavailable
NOISEPROOF_SCANNER=clamav
```

If `NOISEPROOF_SCANNER=clamav` and `clamscan` is unavailable:

```text
scan_status -> failed
scan_verdict -> scan_error
failure_reason -> missing_clamscan
```

## Non-selected Alternatives

Do not add a download endpoint before scanner execution.

Do not run `clamscan --remove`.

Do not use `clamd` or daemon sockets in v0.

Do not call public malware scanning APIs in v0.

Do not claim a clean verdict when the scanner is missing, timed out, or failed.

## Boundary

This is review-only.

This is not endpoint code.

This is not runtime evidence.

This is not malware scanning evidence.

This is not real ClamAV execution.

This is not ClamAV installation evidence.

This is not ClamAV signature database evidence.

This is not a download endpoint.

This is not hosted deployment evidence.

This is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.

## Next Product Gate

```text
uploaded raw file scan execution endpoint v0
```

That gate may add the explicit scan execution endpoint, but it should not claim real malware scanning unless the scanner runtime and signature database are actually verified and recorded.
