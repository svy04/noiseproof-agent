# ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Signature-file Read Guard

Status: implemented

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke signature-file read guard v0

## Goal

Return a structured no-payload report when an outside-repo owner runtime signature file cannot be read.

This keeps missing files, directory paths, unreadable files, and undecodable files from surfacing raw exceptions or accidentally reaching the API.

## Implemented Behavior

Expected read-failure markers:

```text
harness_status: signature_file_read_failed
input_source: file
exit_code: 8
signature_file_readable: false
raw_exception_logged: false
api_calls_attempted: false
malicious_detection_verified: false
payload_committed_to_repo: false
raw_payload_logged: false
```

The blocked reason is intentionally generic:

```text
signature file could not be read
```

The report does not include the signature-file path, raw exception text, file contents, or a payload.

## Boundary

```text
does not include a test signature payload
does not synthesize a test signature
does not store a payload in the repository
does not print raw payload bytes
does not log the raw file-read exception
does not call the API
does not upload raw bytes
does not call the scan endpoint
not endpoint malicious-detection runtime proof
not EICAR-through-API proof
not production malware scanning evidence
not hosted deployment evidence
not external reviewer feedback
not product-complete
```

## Verification

```bash
cd apps/api
uv run pytest tests/test_clamav_api_malicious_detection_harness.py -q -k "missing_signature_file or directory_signature_file"
```

## Next Gate

ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
