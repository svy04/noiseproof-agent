# README Upload Handoff Claim-boundary Refresh

Status: accepted.

Phase marker: readme upload handoff claim-boundary refresh v0.

## Purpose

Refresh the README first-pass unclaimed list so external readers do not confuse two separate boundaries:

```text
explicit uploaded-file-to-chunks handoff exists through `POST /documents/upload-chunks`
implicit upload-preview auto-persistence remains intentionally unclaimed
```

## Context

NoiseProof already has a bounded route and runtime proof for the explicit upload-to-chunks handoff:

```text
POST /documents/upload-chunks
docs/review/uploaded-file-chunk-persistence-handoff-endpoint.md
docs/review/uploaded-file-chunk-persistence-handoff-runtime-smoke.md
docs/review/uploaded-file-chunk-persistence-handoff-application-refresh.md
```

The preview route remains preview-only by design:

```text
POST /documents/upload-chunk-preview
preview_only_not_persisted
```

## Change

The README now says:

```text
explicit uploaded-file-to-chunks handoff exists through `POST /documents/upload-chunks`
implicit upload-preview auto-persistence remains intentionally unclaimed
```

This replaces stale wording that could make the already implemented explicit handoff look absent.

## Boundary

This is not a new product runtime gate.

It adds no endpoint, schema, persistence behavior, upload automation, raw file storage, full parsed text persistence, embeddings, retrieval expansion, Evidence Ledger generation, Noise Gate behavior, report generation, LLM calls, hosted deployment evidence, external reviewer feedback, or product-complete claim.

## Allowed Claim

NoiseProof's README now separates the implemented explicit upload-to-chunks handoff from the intentionally unclaimed implicit upload-preview auto-persistence behavior.

## Non-claims

This is not automatic upload-preview persistence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not robust PDF extraction.

This is not product-complete.

## Verification

Targeted doc test:

```text
uv run pytest -q tests/test_docs.py -k "readme_upload_handoff_claim_boundary_refresh"
```

Full local verification should still run before reporting completion:

```text
uv run python -m compileall app ../../packages/ingestion ../../packages/review
uv run pytest -q
```
