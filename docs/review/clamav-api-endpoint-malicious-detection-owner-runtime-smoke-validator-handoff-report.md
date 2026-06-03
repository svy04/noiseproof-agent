# ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Validator Handoff Report

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke validator handoff report v0.

## What changed

The opt-in malicious-detection harness now supports `--owner-runtime-smoke-report` for future owner-provided runtime smokes.

When combined with `--signature-stdin --require-owner-input --output <runtime-report-path-outside-repo>`, the command writes a validator-accepted metadata shape rather than the broader internal harness report.

The cross-shell packet also advertises:

```text
emit_validator_handoff_report: true
```

## Expected command shape

```text
uv run python -m app.services.clamav_api_malicious_detection_harness --signature-stdin --require-owner-input --owner-runtime-smoke-report --output <runtime-report-path-outside-repo>
```

The resulting JSON is intended to be checked with:

```text
uv run python -m app.services.clamav_api_malicious_detection_harness --validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>
```

## Handoff report boundary

The handoff report is a validator-accepted metadata shape only.

Expected included fields:

```text
harness_status
malicious_detection_verified
api_calls_attempted
payload_committed_to_repo
raw_payload_logged
input_source
required_owner_input_missing
scan_result_summary
```

Expected excluded fields:

```text
phase_marker not emitted
payload_length_bytes not emitted
claims not emitted
boundary not emitted
blocked_reason not emitted when the run verifies infected
```

The report does not include a test signature payload.

## Claim boundary

This phase is fake-client handoff coverage plus no-payload documentation.

It is not endpoint malicious-detection runtime proof.

It is not the ClamAV API endpoint malicious-detection owner-provided runtime smoke v0.

It does not provide EICAR-through-API proof, production malware scanning evidence, hosted deployment evidence, external reviewer feedback, customer validation, Braincrew acceptance, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete status.

## Next gate

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```
