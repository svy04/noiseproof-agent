# ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Packet

Status: implemented

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke packet v0

## Goal

Generate a no-payload owner-runtime smoke packet that describes the exact future proof contract without supplying, storing, printing, uploading, or scanning a test signature.

## Command

```bash
cd apps/api
uv run python -m app.services.clamav_api_malicious_detection_harness --print-owner-runtime-smoke-packet
```

## Observed Packet

```text
packet_status: ready_for_owner_input
required_input: owner-provided runtime-only test signature via stdin
api_calls_attempted: false
payload_committed_to_repo: false
raw_payload_logged: false
```

Command template:

```text
command_template: cat <owner-provided-runtime-only-signature-file-outside-repo> | NOISEPROOF_ALLOW_TEST_SIGNATURE_SMOKE=1 uv run python -m app.services.clamav_api_malicious_detection_harness --signature-stdin --require-owner-input --owner-runtime-smoke-report --output <runtime-report-path-outside-repo>
command_templates.posix
command_templates.powershell
runtime_report_handling
emit_validator_handoff_report: true
post_run_validation_command: uv run python -m app.services.clamav_api_malicious_detection_harness --validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>
```

Success criteria:

```text
scanner_name: clamav-clamd
scan_status: completed
scan_verdict: infected
matched_signature: Eicar-Test-Signature
```

Failure states:

```text
not_configured
blocked_by_environment
unexpected_clean
scan_error
```

## Boundary

```text
does not include a test signature payload
does not call the API
does not upload raw bytes
does not call the scan endpoint
not malware detection proof
owner-provided runtime smoke remains pending
```

This packet is proof infrastructure only. It is not endpoint malicious-detection runtime proof.

## Next Gate

ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
