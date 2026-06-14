# ClamAV API Endpoint Malicious-detection Owner-runtime Smoke

Status: implemented

Phase marker: clamav api endpoint malicious-detection owner runtime smoke v0

## Goal

Verify the local API endpoint path for owner-provided runtime malicious-detection input without committing, printing, or storing the test signature payload in the repository.

This is local endpoint runtime evidence for the ClamAV/EICAR path only. It is not production malware scanning evidence, not hosted deployment evidence, not external reviewer feedback, not customer validation, and not product-complete evidence.

## Runtime Preconditions

```text
docker compose --profile scanner --profile api up -d --build api
NOISEPROOF_SCANNER=clamd
CLAMD_HOST=clamav
CLAMD_PORT=3310
GET /health -> status: ok
clamd PING -> PONG
```

The API container was restarted with `NOISEPROOF_SCANNER=clamd` before the smoke. Earlier `NOISEPROOF_SCANNER=unavailable` state was not used as malicious-detection evidence.

## Execution Boundary

The owner-provided runtime-only test signature was passed through stdin to:

```text
uv run python -m app.services.clamav_api_malicious_detection_harness
  --signature-stdin
  --require-owner-input
  --owner-runtime-smoke-report
  --output <runtime-report-path-outside-repo>
```

The command does not include the test signature payload in this artifact.

The runtime report path was outside the repository:

```text
report_path: <runtime-report-path-outside-repo>
report_inside_repo: false
```

## Observed Result

```text
smoke_exit: 0
validation_exit: 0
harness_status: verified_infected
malicious_detection_verified: true
api_calls_attempted: true
input_source: stdin
payload_committed_to_repo: false
raw_payload_logged: false
scanner_name: clamav-clamd
scan_status: completed
scan_verdict: infected
matched_signature: Eicar-Test-Signature
metadata_boundary: metadata_only_no_raw_bytes_no_download_url
validation_status: accepted
accepted_owner_runtime_smoke: true
missing_or_failed_checks_count: 0
```

The payload-free validator report also showed:

```text
forbidden_payload_fields: []
unexpected_fields: []
reported_payload_committed_to_repo: false
reported_raw_payload_logged: false
```

## API Path Evidence

API logs showed the endpoint sequence:

```text
GET /health -> 200
POST /documents/upload-raw-files -> 201
POST /documents/upload-raw-files/71bd1cab-89d9-43ab-bf3e-91f6469ee624/scan -> 201
```

The scan result row before cleanup:

```text
raw_file_id: 71bd1cab-89d9-43ab-bf3e-91f6469ee624
scan_status: completed
scan_verdict: infected
scanner_name: clamav-clamd
matched_signature: Eicar-Test-Signature
```

## Cleanup

Because this local smoke necessarily uploads runtime-only raw bytes into the local quarantine table before scanning, the test row was deleted after recording the payload-free report:

```text
raw_file_id: 71bd1cab-89d9-43ab-bf3e-91f6469ee624
DELETE 1
remaining_raw: 0
remaining_scans: 0
```

The report remains outside the repository. The repository contains this metadata artifact only; it does not include the test signature payload or an encoded payload.

## Boundary

```text
local Docker FastAPI plus ClamAV endpoint path only
does not include the test signature payload
does not include encoded payload
payload_committed_to_repo: false
raw_payload_logged: false
local raw-file and scan rows cleaned up after proof capture
not production malware scanning evidence
not hosted deployment evidence
not external reviewer feedback
not customer validation
not product-complete
```
