# ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Cross-shell Packet

Status: implemented

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke cross-shell packet v0

## Goal

Make the owner-provided runtime smoke packet easier to execute from both POSIX shells and PowerShell without exposing or storing the owner-provided test signature payload.

## Implemented Behavior

The no-payload packet now includes `command_templates` for:

```text
posix
powershell
```

Both templates read from:

```text
owner-provided-runtime-only-signature-file-outside-repo
```

Both templates write the JSON result to:

```text
runtime-report-path-outside-repo
```

Runtime report handling is explicit:

```text
runtime_report_handling
write_report_outside_repo: true
validate_metadata_only: true
emit_validator_handoff_report: true
do_not_commit_report_if_it_contains_payload_fields: true
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
