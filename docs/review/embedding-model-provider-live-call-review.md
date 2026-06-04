# Embedding Model Provider Live-call Review

Status: implemented.

Phase marker:

```text
embedding model provider live-call review v0
```

## Purpose

Define the guardrails required before `POST /chunks/embedding-model-preview` is allowed to make a real provider call.

This review follows:

- `docs/review/embedding-provider-source-review.md`
- `docs/review/embedding-model-provider-disabled-path.md`

## Proposed Runtime Gate

The existing endpoint should not start calling OpenAI just because `OPENAI_API_KEY` exists.

Future request field:

```text
allow_provider_call
```

Required behavior:

```text
allow_provider_call: false -> configured_no_call
allow_provider_call: true + OPENAI_API_KEY absent -> disabled_missing_api_key
allow_provider_call: true + OPENAI_API_KEY present -> provider call allowed
```

## Required Live-call Guardrails

Before adding the first provider call, the implementation must include:

- input text hash
- provider request timeout
- provider response dimension check
- secret redaction
- provider error boundary
- token/usage metadata boundary
- no automatic persistence
- no retrieval expansion
- no Evidence Ledger generation
- no semantic retrieval quality claim

## Required Test Order

Implement with mocked client first.

```text
mocked client first
no live provider call in CI
no real OPENAI_API_KEY required for tests
fake key must not appear in response text
provider response dimension check must reject mismatched vectors
provider timeout/error must return structured warning or error
```

## Boundary

This phase is not implemented as a provider call.

It adds no runtime behavior.
It adds no API call.
It adds no dependency.
It adds no network call.
It adds no cost-incurring path.
It adds no embedding vector.
It adds no automatic persistence.
It adds no semantic retrieval quality evidence.

Actual embedding model generation remains unproven.
actual embedding model generation remains unproven.

## Next Gate

The next smallest implementation gate should be:

```text
embedding model mocked-provider call v0
```

That gate should use dependency injection or a local adapter seam so tests can verify the provider response handling without live network calls.
