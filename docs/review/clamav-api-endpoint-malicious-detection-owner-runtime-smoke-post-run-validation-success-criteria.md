# ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Post-run Validation Success Criteria

Status: implemented

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke post-run validation success criteria v0

## Goal

Make the validator success criteria explicit in the no-payload owner-runtime smoke packet.

The future owner-provided runtime smoke should not be treated as accepted merely because a report file exists. The post-run validator must accept the metadata.

## Implemented Behavior

The packet now includes:

```text
post_run_validation_success_criteria
validation_status: accepted
accepted_owner_runtime_smoke: true
missing_or_failed_checks: []
```

This is validator metadata only. It describes the expected result of:

```text
uv run python -m app.services.clamav_api_malicious_detection_harness --validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>
```

## Boundary

```text
does not include a test signature payload
does not synthesize a test signature
does not store a payload in the repository
does not print raw payload bytes
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
