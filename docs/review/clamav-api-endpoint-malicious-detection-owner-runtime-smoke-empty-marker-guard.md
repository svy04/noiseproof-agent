# ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Empty-marker Guard

Status: implemented

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke empty-marker guard v0

## Goal

Prevent shell empty-input mistakes from being treated as owner-provided runtime smoke input.

The owner-provided runtime smoke must not call the scan endpoint merely because a shell piped a quote-only stdin marker.

## Implemented Behavior

Quote-only stdin markers and BOM-only stdin are normalized to missing owner input:

```text
""
''
BOM-only stdin
```

Expected guard result:

```text
exit_code: 4
harness_status: not_configured
required_owner_input_missing: true
api_calls_attempted: false
payload_committed_to_repo: false
raw_payload_logged: false
```

This keeps `--signature-stdin --require-owner-input` fail-fast when the provided stdin is only an empty-string marker or shell-generated BOM-only empty pipe rather than owner-provided runtime input.

## Boundary

```text
does not include a test signature payload
does not synthesize a test signature
does not store a payload in the repository
does not print raw payload bytes
does not call the API for quote-only stdin
does not upload raw bytes for quote-only stdin
does not call the scan endpoint for quote-only stdin
not endpoint malicious-detection runtime proof
not EICAR-through-API proof
not production malware scanning evidence
not hosted deployment evidence
not external reviewer feedback
not product-complete
```

## Verification

```bash
cd apps/api
uv run pytest tests/test_clamav_api_malicious_detection_harness.py -q -k "quote_only_stdin"
```

## Next Gate

ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
