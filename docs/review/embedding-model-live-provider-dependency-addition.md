# Embedding Model Live-provider Dependency Addition

Status: implemented.

Phase marker:

```text
embedding model live-provider dependency addition v0
```

## Purpose

Add the pinned OpenAI Python SDK dependency needed for a future live embedding provider adapter while preserving the no-live-call runtime boundary.

This follows:

- `docs/review/embedding-model-live-provider-dependency-review.md`
- `docs/review/embedding-model-live-provider-code-review.md`

## Command

Executed from `apps/api`:

```bash
uv add "openai==2.41.0"
```

## Files Changed

```text
apps/api/pyproject.toml
apps/api/uv.lock
```

Added direct dependency:

```text
openai==2.41.0
```

Lockfile additions observed:

```text
openai==2.41.0
distro==1.9.0
jiter==0.15.0
sniffio==1.3.1
tqdm==4.67.3
```

The local uv environment installed the package set as part of `uv add`.

## Boundary

This is dependency metadata only.
dependency metadata only.

This phase adds no app code.
It makes no provider adapter.
It changes no route behavior.
It adds no live provider call.
It adds no network call from the API.
It adds no API cost.
It adds no embedding vector.
It adds no persistence.
It adds no retrieval expansion.
It adds no Evidence Ledger generation.
It adds no semantic retrieval quality evidence.
It adds no hosted deployment evidence.

There is no runtime behavior change.
no runtime behavior change.

No live provider call in CI remains required.
no live provider call in CI.

Actual live embedding model generation remains unproven.
actual live embedding model generation remains unproven.

## Required Verification

After dependency addition, run:

```bash
cd apps/api
uv run python -m compileall app ../../packages/ingestion ../../packages/review
uv run pytest -q
```

Additional checks:

```text
POST /chunks/embedding-model-preview must still avoid live provider calls by default.
OPENAI_API_KEY must not be required for tests.
No test may make a live provider call.
```

## Next Gate

The next smallest implementation gate should be:

```text
embedding model live-provider adapter disabled-code v0
```

That gate may add the adapter class and dependency injection wiring, but it must still keep live provider calls disabled by default and out of CI.
