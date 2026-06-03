# ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Validator

Status: implemented

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke validator v0

## Goal

Validate a future owner-provided runtime smoke report without supplying, storing, printing, uploading, or scanning a test signature.

This is metadata validation only. It checks whether a JSON report from the owner-provided runtime smoke matches the accepted proof contract.

## Command

```bash
cd apps/api
uv run python -m app.services.clamav_api_malicious_detection_harness \
  --validate-owner-runtime-smoke-report path/to/owner-runtime-smoke-report.json
```

## Accepted Report Contract

```text
harness_status: verified_infected
malicious_detection_verified: true
api_calls_attempted: true
input_source: stdin
required_owner_input_missing: false
payload_committed_to_repo: false
raw_payload_logged: false
scanner_name: clamav-clamd
scan_status: completed
scan_verdict: infected
matched_signature: Eicar-Test-Signature
metadata_boundary: metadata_only_no_raw_bytes_no_download_url
```

## Accepted Validator Output

```text
validation_status: accepted
accepted_owner_runtime_smoke: true
missing_or_failed_checks: []
payload_committed_to_repo: false
raw_payload_logged: false
```

## Rejected Validator Output

```text
validation_status: rejected
accepted_owner_runtime_smoke: false
missing_or_failed_checks: non-empty
```

## Boundary

```text
metadata validation only
does not include a test signature payload
does not call the API
does not upload raw bytes
does not call the scan endpoint
not production malware scanning evidence
not hosted deployment evidence
not external reviewer feedback
not product-complete
```

The validator is proof infrastructure only. It is not endpoint malicious-detection runtime proof by itself. The owner-provided runtime smoke remains pending until a real runtime report is produced with owner-provided stdin input.

## Next Gate

ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
