# ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Input Discovery CI Check

Status: implemented

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke input discovery ci check v0

## Goal

Make the no-payload owner runtime input discovery missing-state check run in GitHub Actions before the normal API test suite.

The intent is to keep the current blocker inspectable: owner runtime input is not configured in CI, and that missing-input state must remain explicit instead of silently passing as a no-op smoke.

## CI Step

```text
Check ClamAV owner runtime input discovery no-payload missing state
```

The step runs:

```bash
uv run python -m app.services.clamav_api_malicious_detection_harness --discover-owner-runtime-input
```

Expected status:

```text
expected_status=4
```

Expected JSON markers:

```text
owner_runtime_input_missing
input_payload_inspected: false
api_calls_attempted: false
malicious_detection_verified: false
payload_committed_to_repo: false
raw_payload_logged: false
required_owner_input_missing: true
```

## Boundary

```text
does not include a test signature payload
does not synthesize a test signature
does not store a payload in the repository
does not read or print the owner runtime signature value
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
uv run pytest tests/test_docs.py -q -k "input_discovery_ci_check"
```

Remote CI verification should be recorded separately after this workflow runs on GitHub Actions.

## Next Gate

ClamAV API endpoint malicious-detection owner-provided runtime smoke v0.

That gate still requires owner-provided runtime-only input and a report output path outside the repository.
