# ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Validator Leak-field Hardening

Status: implemented

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke validator leak-field hardening v0

## Goal

Reject a future owner-provided runtime smoke JSON report if it includes fields that could carry a raw or encoded test-signature payload, even when the normal metadata success fields match.

This is metadata validation only. It does not supply, store, print, upload, scan, or reconstruct a test signature.

## Guarded Fields

The validator now rejects reports that include payload-bearing field names such as:

```text
test_signature_text
encoded_payload
raw_payload
payload_base64
raw_bytes
content_bytes
download_url
```

The output reports field paths only:

```text
forbidden_payload_fields
forbidden payload field present: test_signature_text
forbidden payload field present: scan_result_summary.encoded_payload
```

The placeholder value used by the regression test is not echoed:

```text
redacted-placeholder not echoed
```

## Expected Rejection

```text
validation_status: rejected
accepted_owner_runtime_smoke: false
missing_or_failed_checks: non-empty
```

## Boundary

```text
metadata validation only
not endpoint malicious-detection runtime proof
not EICAR-through-API proof
not test signature input
not raw upload
not scan endpoint request
not production malware scanning evidence
not hosted deployment evidence
not external reviewer feedback
not product-complete
```

## Next Gate

ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
