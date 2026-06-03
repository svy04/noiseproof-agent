# ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Validator Strict-shape Alignment

Status: implemented

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke validator strict-shape alignment v0

## Goal

Align the Python owner-runtime smoke report validator with the schema artifact's strict `additionalProperties: false` boundary.

## Implemented Behavior

The validator now rejects otherwise successful metadata reports if they include unknown fields.

Rejected examples:

```text
template_status
scan_result_summary.extra_note
```

Expected rejection markers:

```text
validation_status: rejected
accepted_owner_runtime_smoke: false
unexpected_fields
unexpected field present: template_status
unexpected field present: scan_result_summary.extra_note
```

## Boundary

```text
schema and validator alignment only
additionalProperties: false
does not include a test signature payload
does not call the API
does not upload raw bytes
does not call the scan endpoint
not endpoint malicious-detection runtime proof
not production malware scanning evidence
not hosted deployment evidence
not external reviewer feedback
not product-complete
```

## Next Gate

ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
