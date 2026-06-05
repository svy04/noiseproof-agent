# Embedding Model Live-provider Owner-runtime Smoke Packet Command-template Handoff Alignment

Status: implemented.

Phase marker: embedding model live-provider owner-runtime smoke packet command-template handoff alignment v0.

## Goal

Make the no-secret owner-runtime smoke packet point to the response-to-report handoff path from Phase 494, so a future manual owner-runtime embedding route response can be converted into a strict validator report without committing secrets, vectors, or raw provider metadata.

This is packet command-template alignment only. It does not call OpenAI, does not read `OPENAI_API_KEY`, and does not prove live embedding generation.

## Packet Fields

`--print-owner-runtime-smoke-packet` now emits these handoff markers:

```text
response_handoff_command
response_handoff_commands
runtime_report_handling.emit_response_handoff_report: true
runtime_report_handling.write_response_capture_outside_repo: true
```

Authoritative command template:

```bash
uv run python -m app.services.embedding_model_live_provider_harness --build-owner-runtime-smoke-report-from-response <owner-runtime-response-json-outside-repo> --output <runtime-report-path-outside-repo>
```

PowerShell command template:

```powershell
uv run python -m app.services.embedding_model_live_provider_harness --build-owner-runtime-smoke-report-from-response '<owner-runtime-response-json-outside-repo>' --output '<runtime-report-path-outside-repo>'
```

## Expected Handoff Flow

```text
owner-runtime route response capture outside repo
-> --build-owner-runtime-smoke-report-from-response
-> validator report outside repo
-> --validate-owner-runtime-smoke-report
```

The generated report remains metadata-only and validator-shaped. It intentionally excludes the embedding vector and `metadata_json`.

## Safety Boundaries

```text
command-template metadata only
no provider call
no OPENAI_API_KEY read
no OPENAI_API_KEY print
no secret in command templates
response capture path must be outside repository
report output path must be outside repository
not live embedding generation proof
not semantic retrieval quality evidence
not hosted deployment evidence
not external reviewer feedback
not product-complete
```

## Next Gate

```text
owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from docs/GOAL.md
```
