# ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Input Discovery

Status: implemented

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke input discovery v0

## Goal

Make owner runtime input presence inspectable without reading, logging, uploading, scanning, or generating a test signature payload.

This is a no-payload discovery command for the next gate. It does not run the owner-provided runtime smoke.

## Command

```bash
cd apps/api
uv run python -m app.services.clamav_api_malicious_detection_harness --discover-owner-runtime-input
```

## Implemented Behavior

The command checks for possible owner runtime input locations without printing secrets or payload material:

```text
accepted_input_sources: file, stdin, environment
input_payload_inspected: false
api_calls_attempted: false
raw_payload_logged: false
value_logged: false
path_logged: false
```

Current local result:

```text
owner_runtime_input_missing
required_owner_input_missing: true
malicious_detection_verified: false
payload_committed_to_repo: false
payload_length_bytes: 0
```

Exit code:

```text
0 when owner runtime input is discoverable
4 when owner runtime input is missing
```

## Boundary

```text
does not include a test signature payload
does not synthesize a test signature
does not store a payload in the repository
does not read or print the owner runtime signature value
does not log owner runtime signature file paths
does not call the API
does not upload raw bytes
does not call the scan endpoint
not endpoint malicious-detection runtime proof
not EICAR-through-API proof
not production malware scanning evidence
not hosted deployment evidence
not external reviewer feedback
not customer validation
not Braincrew acceptance
not product-complete
```

## Verification

```bash
cd apps/api
uv run pytest tests/test_clamav_api_malicious_detection_harness.py -q -k "input_discovery"
uv run pytest tests/test_docs.py -q -k "input_discovery"
```

## Next Gate

ClamAV API endpoint malicious-detection owner-provided runtime smoke v0.

That gate still requires owner-provided runtime-only input and a report output path outside the repository.
