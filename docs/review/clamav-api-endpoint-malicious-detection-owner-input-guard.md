# ClamAV API Endpoint Malicious-detection Owner-input Guard

Status: implemented

Phase marker: ClamAV API endpoint malicious-detection owner-input guard v0

## Goal

Prevent a future owner-provided malicious/test-signature runtime smoke from being mistaken for success when the owner input is missing.

## Implemented Surface

```text
--require-owner-input
required_owner_input_missing
```

When `--require-owner-input` is used and the owner-provided test signature is missing, the harness returns a non-zero exit code.

## Command

```bash
cd apps/api
uv run python -m app.services.clamav_api_malicious_detection_harness --signature-stdin --require-owner-input
```

## Observed Result

```text
exit_code: 4
harness_status: not_configured
input_source: stdin
required_owner_input_missing: true
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

This guard is not detection proof. It makes the future proof attempt harder to overclaim by failing fast when the owner input is absent.

## Next Gate

ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
