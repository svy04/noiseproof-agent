# Uploaded Raw File Scanner Adapter Review

Status: review-only source-first adapter decision.

Phase marker: uploaded raw file scanner adapter review v0.

## Purpose

NoiseProof now has:

```text
uploaded raw file quarantine storage
raw_file_scan_results schema
raw file scan result repository
metadata-only scan result endpoints
local runtime proof for caller-provided scan result rows
```

The next product step should not jump directly to ClamAV execution.

This review selects the smallest scanner adapter boundary that can later produce scan result rows without opening a download endpoint or claiming malware scanning before it exists.

## Source-first Inputs

Primary references:

- OWASP File Upload Cheat Sheet: `https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html`
- ClamAV Scanning: `https://docs.clamav.net/manual/Usage/Scanning.html`
- Python subprocess: `https://docs.python.org/3/library/subprocess.html`

Relevant source observations:

- OWASP File Upload Cheat Sheet recommends defense in depth for uploads: allowlisted extensions, untrusted content-type handling, file signature checks, generated filename safety, file size limits, authorized uploads, storage controls, and upload/download limits.
- OWASP notes that content-type is user-provided and can be spoofed, and that file signature validation should not be used alone.
- ClamAV documents both `clamscan` one-time scanning and `clamdscan` daemon-backed scanning. `clamdscan` has path/socket/streaming implications, and daemon TCP sockets should not be exposed broadly.
- ClamAV also warns that automatic removal is dangerous because false positives can happen.
- Python subprocess exposes return codes, stdout/stderr capture, and timeout behavior, but timeouts must be treated as scan errors rather than clean results.

## Current Boundary

Already implemented:

```text
POST /documents/upload-raw-files
GET /documents/upload-raw-files
POST /documents/upload-raw-files/{raw_file_id}/scan-results
GET /documents/upload-raw-files/{raw_file_id}/scan-results
raw_upload_quarantine_db_bytea_no_download_endpoint
raw_file_scan_results
scanner_name
scanner_version
signature_db_version
scan_status
scan_verdict
matched_signature
error_message
metadata_json
```

Still not implemented:

```text
ScannerAdapter code
ClamAV adapter
scanner binary discovery
scan process execution
file signature validation
allowed extension policy
download endpoint
scan quarantine transition policy
retention/deletion policy
```

## Decision

Add a generic scanner adapter boundary before adding a ClamAV-specific adapter.

Selected future interface names:

```text
ScannerAdapter
ScanAdapterRequest
ScanAdapterResult
```

Selected future request fields:

```text
raw_file_id
storage_key
original_filename
declared_content_type
byte_size
content_sha256
temporary_scan_path
scanner_timeout_seconds
metadata_json
```

Selected future result fields should map directly to `RawFileScanResultCreate`:

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

## Required Failure Mapping

The adapter must treat scanner unavailability as failure evidence, not as a clean verdict.

Required mappings:

```text
missing_scanner_binary -> scan_error
scanner_process_crash -> scan_error
timeout -> scan_error
unparseable_output -> scan_error
permission_denied -> scan_error
unsupported_file_type_policy -> skipped
explicit_policy_skip -> skipped
clean_scan -> clean
malicious_or_suspicious_match -> infected or suspicious
```

Implementation rule:

```text
do not write clean when the scanner is unavailable
```

## Temporary File Boundary

Because raw bytes are stored in quarantine and there is no download endpoint, a future scanner runner may need to materialize bytes to a private temporary file.

Rules for that future gate:

```text
use a generated temporary filename, not original_filename
write under an internal scanner temp directory
delete the temporary_scan_path after scanning when possible
record cleanup errors in metadata_json
never return temporary_scan_path in public API responses
never expose a raw file download URL
```

## Why Not ClamAV Yet

do not add ClamAV in this gate.

The adapter review should happen before binding to `clamscan`, `clamdscan`, socket configuration, streaming choices, or signature database setup.

The future ClamAV adapter gate should decide:

```text
clamscan vs clamdscan
path scan vs stream scan
how scanner version is captured
how signature_db_version is captured
return-code and output parsing
timeout and process cleanup
local development behavior when ClamAV is absent
```

## Next Product Gate

```text
next product gate: uploaded raw file scanner adapter v0
```

That gate may add generic adapter types and tests for failure mapping, but it should not run ClamAV, add scanner process execution, validate file signatures, open a download endpoint, or claim malware scanning.

## Boundary

This is review-only.

This adds no runtime behavior.

This is not malware scanning.

This is not scanner execution.

This is not ClamAV integration.

This is not file signature validation.

This is not a download endpoint.

do not add a download endpoint.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

It is not Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.
