# ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Report Path Guard

Status: implemented

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke report path guard v0

## Goal

Reject future owner-runtime smoke report validation when the report JSON is read from inside the repository.

The owner-provided runtime smoke packet tells the operator to write the runtime report outside the repo. This guard makes that boundary executable in the validator path.

## Implemented Behavior

The `--validate-owner-runtime-smoke-report` command now reports:

```text
report_path_boundary
report_path_allowed: false
required_location: outside_repository
```

when the report path resolves inside the repository.

Expected rejection marker:

```text
report path must be outside repository
```

## Boundary

```text
does not include a test signature payload
does not synthesize a test signature
does not store a payload in the repository
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
