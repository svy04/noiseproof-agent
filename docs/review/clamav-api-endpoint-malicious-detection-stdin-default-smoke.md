# ClamAV API Endpoint Malicious-detection Stdin Default Smoke

Status: implemented

Phase marker: ClamAV API endpoint malicious-detection stdin default smoke v0

## Goal

Record the default stdin command behavior for the malicious/test-signature endpoint harness, proving that stdin mode also remains a safe no-op when no owner-provided runtime input is supplied.

## Command

```bash
cd apps/api
uv run python -m app.services.clamav_api_malicious_detection_harness --signature-stdin
```

## Observed Result

```text
exit_code: 0
harness_status: not_configured
input_source: stdin
api_calls_attempted: false
malicious_detection_verified: false
payload_committed_to_repo: false
raw_payload_logged: false
payload_length_bytes: 0
scan_result_summary: null
```

Observed blocked reason:

```text
set NOISEPROOF_ALLOW_TEST_SIGNATURE_SMOKE=1 and provide owner-provided test signature text on stdin
```

## Boundary

```text
owner-provided runtime smoke remains pending
not malware detection proof
not EICAR-through-API proof
not production malware scanning evidence
not hosted deployment evidence
not external reviewer feedback
not product-complete
```

This artifact proves safe default stdin behavior only. It does not provide owner input and does not prove endpoint malicious/test-signature detection.

## Next Gate

ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
