# ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Post-run Validation Command

Status: implemented

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke post-run validation command v0

## Goal

Make the post-run metadata validation step explicit in the no-payload owner-runtime smoke packet.

The owner-provided runtime smoke remains pending. This phase only adds the follow-up command that should be run after a future owner-provided smoke writes a runtime report outside the repository.

## Implemented Behavior

The packet now includes:

```text
post_run_validation_command
```

Expected command:

```text
uv run python -m app.services.clamav_api_malicious_detection_harness --validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>
```

The validator output must be checked for:

```text
accepted_owner_runtime_smoke
validation_status
missing_or_failed_checks
```

This is validator metadata only.

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
