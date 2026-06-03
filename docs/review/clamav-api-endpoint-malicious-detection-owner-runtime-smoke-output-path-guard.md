# ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Output Path Guard

Status: implemented

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke output path guard v0

## Goal

Reject actual owner-runtime smoke attempts when `--output` points inside the repository.

The cross-shell packet tells the operator to write runtime reports outside the repo. This guard makes the actual harness path enforce that rule before reading or uploading owner-provided stdin input.

## Implemented Behavior

The actual harness command:

```text
--signature-stdin --require-owner-input --output
```

now rejects repository-internal output paths with:

```text
harness_status: output_path_rejected
output_path_boundary
output_path_allowed: false
required_location: outside_repository
output path must be outside repository
api_calls_attempted: false
malicious_detection_verified: false
```

## Boundary

```text
does not include a test signature payload
does not synthesize a test signature
does not store a payload in the repository
does not write the runtime report inside the repository
does not call the API
does not upload raw bytes
does not call the scan endpoint
not endpoint malicious-detection runtime proof
not EICAR-through-API proof
not production malware scanning evidence
not hosted deployment evidence
not external reviewer feedback
not product-complete
```

## Next Gate

ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
