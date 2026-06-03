# ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Report Contract

Status: implemented

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke report contract v0

## Goal

Expose the no-payload JSON metadata contract that a future owner-provided runtime smoke report must satisfy before the validator can accept it.

This is a contract artifact only. It does not supply, store, print, upload, scan, or reconstruct a test signature.

## Command

```bash
cd apps/api
uv run python -m app.services.clamav_api_malicious_detection_harness \
  --print-owner-runtime-smoke-report-contract
```

## Contract Markers

```text
contract_status: ready_for_owner_runtime_report
accepted_report
accepted_input_sources
accepted_scan_result_summary
forbidden_payload_fields
accepted_validator_output
rejected_validator_output
```

Accepted report markers:

```text
harness_status: verified_infected
malicious_detection_verified: true
api_calls_attempted: true
input_source: stdin
accepted_input_sources: file, stdin
required_owner_input_missing: false
payload_committed_to_repo: false
raw_payload_logged: false
```

Accepted scan result summary:

```text
scanner_name: clamav-clamd
scan_status: completed
scan_verdict: infected
matched_signature: Eicar-Test-Signature
metadata_boundary: metadata_only_no_raw_bytes_no_download_url
```

Accepted validator output:

```text
validation_status: accepted
accepted_owner_runtime_smoke: true
missing_or_failed_checks: []
```

Rejected validator output:

```text
validation_status: rejected
accepted_owner_runtime_smoke: false
missing_or_failed_checks: non-empty
```

## Boundary

```text
contract only
does not include a test signature payload
does not call the API
does not upload raw bytes
does not call the scan endpoint
not endpoint malicious-detection runtime proof
not production malware scanning evidence
not hosted deployment evidence
not external reviewer feedback
not product-complete
```

## Next Gate

ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
