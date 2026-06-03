# ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Post-run Validation Cross-shell Commands

Status: implemented

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke post-run validation cross-shell commands v0

## Goal

Add POSIX and PowerShell post-run validator commands to match the existing cross-shell owner-runtime smoke command templates.

The packet already had:

```text
command_templates.posix
command_templates.powershell
post_run_validation_command
```

This phase adds:

```text
post_run_validation_commands
posix
powershell
```

## Implemented Behavior

POSIX validator command:

```text
uv run python -m app.services.clamav_api_malicious_detection_harness --validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>
```

PowerShell validator command:

```text
uv run python -m app.services.clamav_api_malicious_detection_harness --validate-owner-runtime-smoke-report '<runtime-report-path-outside-repo>'
```

This is validator metadata only. The validator reports `validation_status`, `accepted_owner_runtime_smoke`, and `missing_or_failed_checks`.

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
