# TestClient Dependency Warning Remote Verification

Status: implemented

Phase marker: testclient dependency warning remote verification v0

## Goal

Record remote GitHub Actions evidence after adding `httpx2` and turning `StarletteDeprecationWarning` into a pytest error.

This is test dependency hygiene evidence only. It is not API behavior, product runtime evidence, hosted deployment evidence, external reviewer feedback, customer validation, or product-complete evidence.

## Verified Remote Runs

CI:

```text
remote run: 26969672909
workflow: CI
head: 29f1afa
job: api-smoke
job id: 79581346237
conclusion: success
```

External Feedback Screen:

```text
remote run: 26969672911
workflow: External Feedback Screen
head: 29f1afa
job: screen
job id: 79581346224
conclusion: success
```

## Annotation And Log Check

Check-run annotations:

```text
CI check-run annotations: []
External Feedback Screen check-run annotations: []
```

Exact TestClient warning search:

```text
StarletteDeprecationWarning observed: no
TestClient fallback warning observed: no
```

Boundary on generic warning text:

```text
generic `warning` text still appears in unrelated checkout hints and external-feedback JSON fields
```

That generic text is not the Starlette TestClient dependency fallback warning.

## Boundary

```text
test dependency hygiene evidence only
not API behavior
not product runtime evidence
not hosted deployment evidence
not external reviewer feedback
not customer validation
not product-complete
```
