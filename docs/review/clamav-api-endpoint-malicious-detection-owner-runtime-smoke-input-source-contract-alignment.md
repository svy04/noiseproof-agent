# ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Input-source Contract Alignment

Status: contract-alignment proof only.

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke input-source contract alignment v0.

## Purpose

This gate separates input discovery from validator acceptance for the future owner-provided runtime smoke.

Discovery can see whether an owner runtime input candidate is configured through file, stdin, or environment metadata.

The accepted validator handoff report sources remain narrower:

```text
accepted_input_sources: file, stdin
```

This avoids treating environment-variable payload plumbing as a validator-accepted proof source.

## Updated Contract

The discovery report now exposes both lists:

```text
discoverable_input_sources: file, stdin, environment
accepted_input_sources: file, stdin
```

Candidate metadata now marks which source types can produce a validator-accepted report:

```text
signature_text_env.validator_accepted: false
stdin.validator_accepted: true
```

The validator rejection message is now generated from the accepted source list:

```text
input_source must be one of: file, stdin
```

## Why Environment Is Discovery-only

`NOISEPROOF_CLAMAV_TEST_SIGNATURE_TEXT` can still be discovered as a legacy/runtime candidate without logging its value.

However, the validator-accepted owner runtime smoke report should come from stdin or an outside-repo signature file so the proof path stays explicit and easier to inspect.

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

```bash
cd apps/api
uv run pytest tests/test_clamav_api_malicious_detection_harness.py -q -k "owner_runtime_input_discovery or rejects_environment_input_source"
```

## Next Gate

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```
