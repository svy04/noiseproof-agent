# External Review Issue Body Evidence Quality Draft Preview Route Refresh

Status: implemented.

Phase marker: external review issue body evidence quality draft preview route refresh v0.

## Purpose

Record the owner-authored issue #1 body edit that routes external reviewers to the Evidence quality failure-case draft preview proof chain as the latest proof to inspect.

## Updated Issue

```text
issue: https://github.com/svy04/noiseproof-agent/issues/1
updatedAt: 2026-06-06T11:32:26Z
comment_count: 1
starts_with_request: true
first_codepoint: 35
body_length: 6291
```

## Latest Proof Route In Issue Body

```text
Evidence quality failure-case draft preview proof
docs/review/evidence-quality-risk-failure-case-draft-preview.md
docs/review/evidence-quality-risk-failure-case-draft-preview-runtime-smoke.md
docs/review/evidence-quality-risk-failure-case-draft-preview-runtime-smoke-remote-verification.md
docs/review/external-reader-proof-path-evidence-quality-draft-preview-route-refresh.md
docs/review/external-reader-proof-path-evidence-quality-draft-preview-route-refresh-remote-verification.md
```

Issue body markers:

```text
has_evidence_quality_draft_preview: true
has_evidence_quality_draft_preview_runtime_smoke: true
has_evidence_quality_draft_preview_runtime_remote_verification: true
has_evidence_quality_draft_preview_route_refresh: true
has_evidence_quality_draft_preview_route_remote_verification: true
old_workflow_markdown_latest_label_present: false
```

## What Changed

- Issue #1 `Latest Proof To Inspect` now points to the Evidence quality failure-case draft preview proof chain.
- The issue links the runtime proof, runtime remote verification, external-reader route refresh, and route refresh remote verification.
- The earlier Evidence quality ops proof remains visible as predecessor proof.
- The workflow markdown proof remains visible as predecessor proof but no longer appears as the latest proof label.
- The issue still states that self-authored issue edits or comments do not close the external reviewer feedback v0 gate.
- The final issue body starts with `## Request` and first codepoint `35`.

## Boundary

This is owner-authored issue body routing only.

It is not external reviewer feedback.
It is not hosted deployment evidence.
It is not customer validation.
It is not Braincrew acceptance.
It is not automatic failure-case creation.
It is not final truth adjudication.
It is not retrieval quality evidence.
It is not Evidence Ledger quality evidence.
It is not embedding generation.
It is not an LLM call.
It is not product-complete.

Self-authored issue edits or comments do not close the external reviewer feedback v0 gate.

## Next Gate

Next gate: external feedback current-state evidence quality draft preview issue verification v0, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when `OPENAI_API_KEY` is configured by the owner, or another source-first product gate selected from the current repository state.
