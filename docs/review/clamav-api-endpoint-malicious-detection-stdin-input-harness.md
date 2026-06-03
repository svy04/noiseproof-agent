# ClamAV API Endpoint Malicious-detection Stdin Input Harness

Status: implemented

Phase marker: ClamAV API endpoint malicious-detection stdin input harness v0

## Goal

Add a stdin owner-input path to the malicious/test-signature endpoint harness so a future manual runtime smoke can avoid placing the test signature in command arguments, docs, git, CI configuration, or shell-history examples.

## Implemented Surface

```text
app.services.clamav_api_malicious_detection_harness
--signature-stdin
input_source: stdin
```

The environment-variable input remains supported:

```text
NOISEPROOF_CLAMAV_TEST_SIGNATURE_TEXT
```

The stdin path is preferred for local manual proof attempts because it can accept owner-provided runtime input without printing the raw payload.

## Verified Behavior

Unit tests cover:

```text
stdin owner input can reach fake endpoint client
input_source: stdin
raw payload is not present in the JSON report
payload_committed_to_repo: false
raw_payload_logged: false
empty stdin remains not_configured
fake-client tests only
```

The fake-client infected-path test checks classification logic only. It is not real ClamAV endpoint evidence.

## Boundary

```text
not malware detection proof
not EICAR-through-API proof
not production malware scanning evidence
not hosted deployment evidence
not external reviewer feedback
not product-complete
```

This phase adds safer input plumbing for a future owner-provided runtime smoke. It does not supply the owner input and does not prove endpoint malicious/test-signature detection.

## Next Gate

ClamAV API endpoint malicious-detection stdin default smoke v0
