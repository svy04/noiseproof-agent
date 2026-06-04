# Embedding Model Live-provider Dependency Review

Status: implemented.

Phase marker:

```text
embedding model live-provider dependency review v0
```

## Purpose

Record the dependency candidate and lockfile procedure for a future live OpenAI embedding provider implementation without installing anything in this phase.

This review follows:

- `docs/review/embedding-model-live-provider-implementation-review.md`
- `docs/review/embedding-model-live-provider-code-review.md`

## Official Sources Checked

OpenAI official documentation:

- `https://platform.openai.com/docs/libraries`
- `https://platform.openai.com/docs/api-reference/embeddings/create`
- `https://platform.openai.com/docs/guides/embeddings`

Registry observation:

```text
command: python -m pip index versions openai
observed_latest: openai==2.41.0
observed_at: 2026-06-05 Asia/Seoul local workspace run
```

This is a dependency candidate only.
dependency candidate only.

Package registry state can drift. Re-run the registry check before the actual dependency addition.

## Current Project Dependency State

Current API dependency file:

```text
apps/api/pyproject.toml
```

Current lockfile:

```text
uv.lock
```

Current dependency boundary:

```text
openai is not listed in apps/api/pyproject.toml
openai is not added to uv.lock by this phase
do not install in this phase
```

## Selected Future Candidate

Future candidate:

```text
openai==2.41.0
```

Future implementation should prefer an explicit pinned addition first:

```bash
uv add "openai==2.41.0"
```

Then inspect:

```bash
git diff -- apps/api/pyproject.toml uv.lock
uv lock --dry-run
uv run pytest -q tests/test_routes.py -k "embedding_model_preview"
uv run pytest -q tests/test_docs.py -k "embedding_model_live_provider"
```

Do not accept the dependency if it forces unrelated upgrades or changes the no-live-call CI boundary.

## Required Future Dependency Checks

Before adding the dependency, the next implementation gate must verify:

```text
the package resolves for Python >=3.11
uv.lock changes are limited to openai and required transitive dependencies
no test requires a real OPENAI_API_KEY
no live provider call in CI
no secret appears in test output
default endpoint behavior still returns configured_no_call or disabled_missing_api_key
allow_provider_call true without owner runtime client still avoids accidental network calls
```

## Boundary

This phase adds no runtime behavior.
no runtime behavior.

It does not install `openai`.
It does not modify `apps/api/pyproject.toml`.
It does not modify `uv.lock`.
It adds no provider adapter code.
It adds no live provider call.
It adds no network call.
It adds no API cost.
It adds no embedding vector.
It adds no persistence.
It adds no retrieval expansion.
It adds no Evidence Ledger generation.
It adds no semantic retrieval quality evidence.
It adds no hosted deployment evidence.

Actual live embedding model generation remains unproven.
actual live embedding model generation remains unproven.

## Next Gate

The next smallest implementation gate should be:

```text
embedding model live-provider dependency addition v0
```

That gate may add the `openai` dependency only if tests keep CI no-live-call behavior explicit and the lockfile diff is inspectable.
