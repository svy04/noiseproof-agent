# ClamAV API Endpoint Malicious-detection Owner-runtime Input-source Contract CI Check

Status: CI guard only.

Phase marker: ClamAV API endpoint malicious-detection owner runtime input-source contract ci check v0.

## Purpose

This gate extends the existing no-payload CI discovery guard so it checks the owner-runtime input-source contract directly.

The CI step remains:

```text
Check ClamAV owner runtime input discovery no-payload missing state
```

It now checks that discovery and validator acceptance are separated:

```text
discoverable_input_sources: file, stdin, environment
accepted_input_sources: file, stdin
signature_text_env.validator_accepted: false
stdin.validator_accepted: true
```

## Boundary

This does not run the owner-provided runtime smoke.

This does not include a test signature payload.

This does not call the API.

This does not upload raw bytes.

This does not call the scan endpoint.

This is not endpoint malicious-detection runtime proof.

This is not production malware scanning evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.

## Verification

Local verification:

```bash
cd apps/api
uv run pytest tests/test_docs.py -q -k "input_source_contract_ci_check"
uv run python -m app.services.clamav_api_malicious_detection_harness --discover-owner-runtime-input
```

Expected command result:

```text
exit_code: 4
owner_runtime_input_missing
api_calls_attempted: false
input_payload_inspected: false
discoverable_input_sources: file, stdin, environment
accepted_input_sources: file, stdin
```

## Next Gate

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```
