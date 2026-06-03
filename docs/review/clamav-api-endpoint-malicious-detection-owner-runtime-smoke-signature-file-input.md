# ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Signature-file Input

Status: implemented

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke signature-file input v0

## Goal

Add a safer owner-runtime input path that avoids shell-pipe encoding surprises while keeping test-signature material outside the repository.

This feature does not supply or synthesize a test signature. It only lets a future owner provide a runtime-only signature file outside the repository.

## Implemented Behavior

Preferred file command:

```text
NOISEPROOF_ALLOW_TEST_SIGNATURE_SMOKE=1 uv run python -m app.services.clamav_api_malicious_detection_harness --signature-file <owner-provided-runtime-only-signature-file-outside-repo> --require-owner-input --owner-runtime-smoke-report --output <runtime-report-path-outside-repo>
```

Path guard:

```text
signature_file_path_allowed: false
required_location: outside_repository
api_calls_attempted: false
```

Validator contract:

```text
accepted_input_sources: file, stdin
input_source: file or stdin
```

## Boundary

```text
does not include a test signature payload
does not synthesize a test signature
does not store a payload in the repository
does not print raw payload bytes
does not allow a signature file path inside the repository
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
uv run pytest tests/test_clamav_api_malicious_detection_harness.py -q -k "signature_file"
```

## Next Gate

ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
