# Report Markdown Local Inspection Paths Runtime Smoke Remote Verification

Status: implemented.

Phase marker: report markdown local inspection paths runtime smoke remote verification v0.

## Purpose

Record remote GitHub Actions evidence that the Phase 648 runtime-smoke proof passed CI and External Feedback Screen after push.

This verifies that the committed runtime-smoke artifact and docs tests were accepted by the repository's remote workflows.

## Verified Commit

```text
head_sha -> 10f330cce3fd093fe4160574c6f3af83d26856c0
commit -> docs: record report markdown inspection path runtime smoke
```

## Remote Workflow Results

```text
CI run 27051818097: success
External Feedback Screen run 27051818098: success
CI job_id -> 79848747552
External Feedback Screen job_id -> 79848747569
Run API smoke tests -> success
Screen issue comments -> success
```

Links:

```text
https://github.com/svy04/noiseproof-agent/actions/runs/27051818097
https://github.com/svy04/noiseproof-agent/actions/runs/27051818098
```

## Verified Artifact

```text
docs/review/report-markdown-local-inspection-paths-runtime-smoke.md
```

The local runtime-smoke artifact records Docker PostgreSQL plus live FastAPI HTTP proof that `GET /reports/{report_record_id}/markdown` rendered `## Local Inspection Paths` and the expected local inspection paths from a persisted Report record.

## Boundary

This is remote workflow verification only.

It is not the local Docker/FastAPI runtime smoke itself.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not semantic retrieval quality evidence.

It is not embedding generation.

It is not Evidence Ledger quality evidence.

It is not Noise Gate quality evidence.

It is not report quality evidence.

It is not new retrieval behavior.

It is not Evidence Ledger creation logic.

It is not Noise Gate creation logic.

It is not report generation logic.

It is not an LLM call.

It is not product-complete.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
