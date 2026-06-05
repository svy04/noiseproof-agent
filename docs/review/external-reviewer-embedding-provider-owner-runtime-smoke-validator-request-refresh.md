# External Reviewer Embedding Provider Owner-runtime Smoke Validator Request Refresh

Status: implemented request-surface refresh.

Phase marker: external reviewer embedding provider owner-runtime smoke validator request refresh v0.

## Purpose

Make the embedding provider owner-runtime smoke validator and post-run validation command discoverable from reviewer-facing repository paths.

This refresh points reviewers to:

```text
docs/review/embedding-model-live-provider-owner-runtime-smoke-packet.md
docs/review/embedding-model-live-provider-owner-runtime-smoke-validator.md
docs/review/embedding-model-live-provider-owner-runtime-smoke-post-run-validation-command.md
```

It also records this request-refresh artifact:

```text
docs/review/external-reviewer-embedding-provider-owner-runtime-smoke-validator-request-refresh.md
```

It updates repository request surfaces only.

It does not edit the live public GitHub issue body.

## Reviewer-facing Surfaces Refreshed

Updated surfaces:

```text
CONTRIBUTING.md
.github/ISSUE_TEMPLATE/external-review-feedback.md
README.md
docs/GOAL.md
docs/application/portfolio-index.md
docs/review/external-reader-proof-path.md
docs/review/external-review-request.md
docs/review/external-reviewer-brief.md
docs/review/external-reviewer-link-map.md
docs/runbook.md
```

## Validation Path Now Highlighted

Post-run validation command:

```bash
uv run python -m app.services.embedding_model_live_provider_harness --validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>
```

Expected success markers:

```text
accepted_owner_runtime_smoke: true
missing_or_failed_checks: []
```

The validator accepts only a secret-free, outside-repository runtime report with:

```text
embedding_status: owner_runtime_provider_generated
embedding_length: 1536
provider_response_dimension_check: passed
openai_api_key_printed: false
secret_logged: false
secret_committed_to_repo: false
```

## Explicit Non-claims

This is request-surface refresh only.

It is not a live issue body edit.

It is not live embedding generation proof.

It is not external reviewer feedback.

It is not hosted deployment evidence.

It is not semantic retrieval quality evidence.

It is not customer validation.

It is not Braincrew acceptance.

It is not product-complete.

## Next Gate

```text
external review issue body embedding provider owner-runtime smoke validator refresh v0, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from docs/GOAL.md
```
