# Uploaded Raw File Download Endpoint Review

Status: review-only.

Phase marker: uploaded raw file download endpoint review v0.

## Purpose

NoiseProof can store quarantined raw upload bytes, persist scan result metadata, and run an explicit scan endpoint with the configured scanner adapter.

This gate decides what must be true before opening any endpoint that returns stored raw bytes.

It does not implement a download endpoint.

It does not return raw bytes.

It does not claim malware scanning evidence.

## Source-first Review

This is a source-first review.

Primary source:

- OWASP File Upload Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html

Relevant interpretation for NoiseProof:

- file upload handling should be defense-in-depth, not a single scanner check
- user-controlled filenames should not determine storage or retrieval paths
- uploaded content should be stored in a controlled location and retrieved through an application handler when retrieval is needed
- upload and download limits should both exist
- access to uploaded files should be controlled by permissions
- antivirus or sandbox checks can reduce risk, but they do not prove a file is safe in every context

## Current NoiseProof Boundary

Already implemented:

```text
POST /documents/upload-raw-files
GET /documents/upload-raw-files
POST /documents/upload-raw-files/{raw_file_id}/scan-results
GET /documents/upload-raw-files/{raw_file_id}/scan-results
POST /documents/upload-raw-files/{raw_file_id}/scan
uploaded_raw_files table
raw_file_scan_results table
generated raw_file_id and storage_key
metadata-only raw upload list responses
raw_upload_quarantine_db_bytea_no_download_endpoint
```

Still not implemented:

```text
download endpoint
authorization policy
download rate limit
retention/deletion policy
content-disposition policy
file signature validation
production malware scanning evidence
endpoint malicious-detection runtime proof
```

## Decision

Do not implement the download endpoint in this gate.

Boundary marker:

```text
do not implement the download endpoint in this gate
```

The next product gate may implement a guarded raw file download endpoint only if it keeps these constraints:

```text
scan-first
latest clean scan result required
scan_error, infected, suspicious, pending, skipped, or missing scan blocks download
generated raw_file_id and storage_key are used instead of original filename paths
metadata-only list response remains default
authorization boundary remains planned and explicit
download rate limit remains planned and explicit
no raw bytes are included in JSON metadata responses
no hosted deployment or production scanning claim is made
```

## Proposed Future Endpoint

Future endpoint shape:

```text
GET /documents/upload-raw-files/{raw_file_id}/download
```

Future success preconditions:

```text
uploaded_raw_files row exists
latest raw_file_scan_results row for raw_file_id has scan_status=completed
latest raw_file_scan_results row for raw_file_id has scan_verdict=clean
quarantine_status allows controlled retrieval
size_bytes is within download limit
caller authorization boundary is explicit, even if local-only v0 uses a placeholder
```

Future blocked cases:

```text
404 when raw_file_id does not exist
409 when no scan result exists
409 when latest scan_status is not completed
409 when latest scan_verdict is not clean
409 when quarantine_status is not eligible for controlled retrieval
```

Future response requirements:

```text
return raw bytes only from the explicit download endpoint
do not include raw bytes in JSON responses
use safe Content-Disposition with sanitized fallback filename
include X-Content-Type-Options: nosniff
prefer application/octet-stream when content type is uncertain
do not use original filename as a filesystem path
```

## Non-selected Alternatives

Do not add direct database byte download before scan checks.

Do not expose storage_key as a public download token.

Do not treat scanner-unavailable or scan_error as clean.

Do not create a public static file path for uploaded bytes.

Do not claim that a clean ClamAV result proves a file is safe for production use.

## Boundary

This is review-only.

This is not endpoint code.

This is not a download endpoint.

This is not malware scanning evidence.

This is not endpoint malicious-detection runtime proof.

This is not hosted deployment evidence.

This is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, autonomous workflow execution, and not product-complete.

## Next Product Gate

```text
next product gate: guarded raw file download endpoint v0
```

That gate may implement the explicit download route with scan-first blocking behavior, but it must still avoid claiming production malware scanning, hosted deployment evidence, or external reviewer feedback.
