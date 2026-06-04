# TestClient Dependency Warning Cleanup

Status: implemented

Phase marker: testclient dependency warning cleanup v0

## Goal

Remove the recurring Starlette/FastAPI TestClient deprecation warning from local and CI test output by satisfying the dependency boundary that Starlette now asks for.

This is test dependency hygiene only. It is not API behavior, product runtime evidence, hosted deployment evidence, external reviewer feedback, customer validation, or product-complete evidence.

## Source Check

Local Starlette testclient source shows the boundary:

```text
local Starlette testclient source: apps/api/.venv/Lib/site-packages/starlette/testclient.py
tries import httpx2 as httpx
falls back to httpx
warns with StarletteDeprecationWarning when httpx2 is missing
warning text: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
```

PyPI metadata check:

```text
httpx2 2.3.0
summary: The next generation HTTP client.
```

Installed before cleanup:

```text
fastapi 0.136.3
starlette 1.2.0
httpx 0.28.1
httpx2 missing
pytest 9.0.3
```

## Change

```text
apps/api/pyproject.toml
  dev dependency: httpx2>=2.3.0
  pytest filter: error::starlette.exceptions.StarletteDeprecationWarning

apps/api/uv.lock
  httpx2==2.3.0
  httpcore2==2.3.0
  truststore==0.10.4
```

The pytest warning filter is intentional: if the dependency boundary regresses and Starlette falls back to deprecated `httpx` behavior again, test collection fails instead of emitting a quiet warning.

## Local Verification

RED:

```text
uv run pytest -q
ERROR tests/test_routes.py
starlette.exceptions.StarletteDeprecationWarning
Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
```

GREEN:

```text
uv run python -W error::DeprecationWarning -c "from fastapi.testclient import TestClient; print(TestClient)"
<class 'starlette.testclient.TestClient'>

uv run pytest -q
626 passed
```

Remote warning result remains unverified until the next push.

## Boundary

```text
test dependency hygiene only
remote warning result remains unverified until the next push
not API behavior
not product runtime evidence
not hosted deployment evidence
not external reviewer feedback
not customer validation
not product-complete
```
