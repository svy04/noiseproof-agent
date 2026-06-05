# Persisted Report Markdown Export Remote Verification

Status: remote GitHub Actions verification only.

Phase marker: persisted report markdown export remote verification v0.

## Purpose

This gate records that the persisted report markdown export implementation reached remote `main` and passed the repository's two current GitHub Actions screens.

It verifies only the remote workflow state for the commit that added `GET /reports/{report_record_id}/markdown`.

## Commit

```text
head_sha: b477ec855ed922119391d81ea0cac9f9213c38f3
commit: b477ec8 feat: add persisted report markdown export
committed_at: 2026-06-06 00:06:50 +0900
```

Related local artifact:

```text
docs/review/persisted-report-markdown-export.md
```

Implemented endpoint on that commit:

```text
GET /reports/{report_record_id}/markdown
```

## Remote Verification

CI run 27022884406:

```text
workflow: CI
url: https://github.com/svy04/noiseproof-agent/actions/runs/27022884406
status: completed
conclusion: success
job: api-smoke -> success
job_id: 79755212714
createdAt: 2026-06-05T15:07:13Z
updatedAt: 2026-06-05T15:07:56Z
```

CI steps observed:

```text
Compile API and local packages -> success
Check semantic retrieval quality report staleness -> success
Check ClamAV owner runtime input discovery no-payload missing state -> success
Check embedding provider owner runtime input discovery missing state -> success
Run API smoke tests -> success
```

External Feedback Screen run 27022884394:

```text
workflow: External Feedback Screen
url: https://github.com/svy04/noiseproof-agent/actions/runs/27022884394
status: completed
conclusion: success
job: screen -> success
job_id: 79755212239
createdAt: 2026-06-05T15:07:13Z
updatedAt: 2026-06-05T15:07:23Z
```

External Feedback Screen steps observed:

```text
Capture issue comments -> success
Screen issue comments -> success
Draft manual acceptance records -> success
Upload screening artifact -> success
Upload acceptance draft artifact -> success
```

## Boundary

This is remote workflow verification for the persisted report markdown export gate only.

The External Feedback Screen success is a workflow screen only.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not customer validation.

This is not Braincrew acceptance.

This is not free-form report generation.

This is not a new report-generation path.

This is not an LLM call.

This is not retrieval.

This is not Evidence Ledger creation.

This is not Noise Gate behavior.

This is not Report record creation.

This is not financial advice.

This is not product-complete.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
