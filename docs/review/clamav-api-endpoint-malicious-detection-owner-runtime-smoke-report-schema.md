# ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Report Schema

Status: implemented

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke report schema v0

## Goal

Expose a no-payload JSON Schema-shaped accepted report shape for future owner-provided runtime smoke reports.

This schema artifact is only a strict report-shape aid. The Python validator remains authoritative.

## Command

```bash
cd apps/api
uv run python -m app.services.clamav_api_malicious_detection_harness \
  --print-owner-runtime-smoke-report-schema
```

## Schema Markers

```text
https://json-schema.org/draft/2020-12/schema
title: NoiseProof ClamAV owner runtime smoke report
type: object
additionalProperties: false
forbidden_payload_fields
```

Accepted top-level constants:

```text
harness_status: verified_infected
malicious_detection_verified: true
api_calls_attempted: true
payload_committed_to_repo: false
raw_payload_logged: false
input_source: stdin
required_owner_input_missing: false
```

Accepted scan result summary constants:

```text
scanner_name: clamav-clamd
scan_status: completed
scan_verdict: infected
matched_signature: Eicar-Test-Signature
metadata_boundary: metadata_only_no_raw_bytes_no_download_url
```

Non-claims:

```text
validator_replacement: false
not endpoint malicious-detection runtime proof
not production malware scanning evidence
```

## Boundary

```text
schema artifact only
validator remains authoritative
does not include a test signature payload
does not call the API
does not upload raw bytes
does not call the scan endpoint
not endpoint malicious-detection runtime proof
not hosted deployment evidence
not external reviewer feedback
not product-complete
```

## Next Gate

ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
