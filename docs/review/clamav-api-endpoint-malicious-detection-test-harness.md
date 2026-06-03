# ClamAV API Endpoint Malicious-detection Test Harness

Status: implemented

Phase marker: ClamAV API endpoint malicious-detection test harness v0

## Goal

Add a small opt-in command harness for the future malicious/test-signature endpoint runtime smoke, while keeping the default path safe, disabled, and non-claiming.

## Implemented Surface

```text
app.services.clamav_api_malicious_detection_harness
build_malicious_detection_harness_report()
UrllibEndpointClient
python -m app.services.clamav_api_malicious_detection_harness
```

The command is disabled by default. Without explicit opt-in, it returns:

```text
harness_status: not_configured
malicious_detection_verified: false
payload_committed_to_repo: false
raw_payload_logged: false
api_calls_attempted: false
```

## Opt-in Inputs

The future runtime smoke requires both variables:

```text
NOISEPROOF_ALLOW_TEST_SIGNATURE_SMOKE=1
NOISEPROOF_CLAMAV_TEST_SIGNATURE_TEXT
```

The test signature must be owner-provided at runtime. It is not committed, generated, printed, or stored by this repository.

## Harness States

The harness can classify results into:

```text
not_configured
verified_infected
blocked_by_environment
unexpected_clean
scan_error
```

`verified_infected` requires the API scan response to include:

```text
scanner_name: clamav-clamd
scan_status: completed
scan_verdict: infected
matched_signature: Eicar-Test-Signature
```

Any host, network, container, endpoint, or scanner block is represented as:

```text
blocked_by_environment
```

## Verification

Unit tests cover:

```text
not_configured does not call the API
verified_infected classification through a fake endpoint client
blocked_by_environment classification through a fake endpoint client error
CLI default JSON output without opt-in
```

The fake-client tests intentionally do not provide runtime ClamAV evidence.

## Boundary

```text
payload_committed_to_repo: false
raw_payload_logged: false
not malware detection proof
not EICAR-through-API proof
not production malware scanning evidence
not hosted deployment evidence
not external reviewer feedback
not product-complete
```

This is implementation plumbing for a future runtime smoke. It is not proof that the endpoint detected a malicious/test-signature input in the current environment.

## Next Gate

ClamAV API endpoint malicious-detection harness default smoke v0
