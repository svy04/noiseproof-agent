# Embedding Model Live-provider Owner-runtime Smoke Post-run Validation Cross-shell Commands

Status: implemented.

Phase marker: embedding model live-provider owner-runtime smoke post-run validation cross-shell commands v0.

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
uv run python -m app.services.embedding_model_live_provider_harness --validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>
```

PowerShell validator command:

```text
uv run python -m app.services.embedding_model_live_provider_harness --validate-owner-runtime-smoke-report '<runtime-report-path-outside-repo>'
```

This is validator metadata only. The validator reports `validation_status`, `accepted_owner_runtime_smoke`, and `missing_or_failed_checks`.

## Boundary

```text
does not read OPENAI_API_KEY
does not print OPENAI_API_KEY
does not call the OpenAI provider
does not run the owner-runtime smoke
does not persist embeddings
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
