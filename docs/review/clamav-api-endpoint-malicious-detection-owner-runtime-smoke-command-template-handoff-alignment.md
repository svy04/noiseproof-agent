# ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Command-template Handoff Alignment

Status: implemented

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke command-template handoff alignment v0

## Goal

Align the packet's singular command_template with the validator handoff report path.

Before this phase, the packet's `command_templates.posix` and `command_templates.powershell` entries included `--owner-runtime-smoke-report --output <runtime-report-path-outside-repo>`, but the singular command_template still stopped at `--signature-stdin --require-owner-input`.

That was safe, but stale. A future owner-provided runtime smoke could follow the shorter command and produce the broader internal harness JSON instead of the validator handoff report.

## Implemented Behavior

The singular command_template now includes:

```text
--owner-runtime-smoke-report
--output <runtime-report-path-outside-repo>
```

The packet still declares:

```text
emit_validator_handoff_report: true
```

This keeps the visible default command aligned with the strict validator handoff report path.

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

This is command metadata alignment only.

## Next Gate

ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
