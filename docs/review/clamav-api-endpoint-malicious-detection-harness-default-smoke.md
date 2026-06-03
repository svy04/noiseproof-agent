# ClamAV API Endpoint Malicious-detection Harness Default Smoke

Status: implemented

Phase marker: ClamAV API endpoint malicious-detection harness default smoke v0

## Goal

Record the default command behavior for the malicious/test-signature endpoint harness, proving that it is disabled by default and does not call the API or claim detection without explicit owner-provided runtime input.

## Command

```bash
cd apps/api
uv run python -m app.services.clamav_api_malicious_detection_harness
```

## Observed Result

```text
exit_code: 0
harness_status: not_configured
api_calls_attempted: false
malicious_detection_verified: false
payload_committed_to_repo: false
raw_payload_logged: false
payload_length_bytes: 0
scan_result_summary: null
```

The default smoke confirms that the harness does not run the malicious/test-signature path unless both explicit opt-in variables are present:

```text
NOISEPROOF_ALLOW_TEST_SIGNATURE_SMOKE=1
NOISEPROOF_CLAMAV_TEST_SIGNATURE_TEXT
```

## Boundary

This is a safe no-op smoke only.

It is:

```text
default harness behavior evidence
disabled-by-default evidence
no API call evidence
```

It is not:

```text
not malware detection proof
not EICAR-through-API proof
not production malware scanning evidence
not hosted deployment evidence
not external reviewer feedback
not product-complete
```

## Next Gate

ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
