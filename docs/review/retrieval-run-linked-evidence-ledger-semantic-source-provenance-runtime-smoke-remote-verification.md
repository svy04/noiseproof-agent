# Retrieval-run-linked Evidence Ledger Semantic Source Provenance Runtime Smoke Remote Verification

Status: implemented.

Phase marker: retrieval-run-linked Evidence Ledger semantic source provenance runtime smoke remote verification v0.

## Purpose

Record remote GitHub Actions evidence that the Phase 625 runtime-smoke proof passed the repository CI and feedback-screen workflows on `main`.

This verifies the committed proof chain for `docs/review/retrieval-run-linked-evidence-ledger-semantic-source-provenance-runtime-smoke.md`.

It does not rerun the local Docker/FastAPI runtime smoke in GitHub Actions.

## Remote Runs

```text
head_sha -> 27b8ab349604defe5543a43627df730fd72c6383
CI run 27045552652 -> success
External Feedback Screen run 27045552666 -> success
```

CI URL: https://github.com/svy04/noiseproof-agent/actions/runs/27045552652

External Feedback Screen URL: https://github.com/svy04/noiseproof-agent/actions/runs/27045552666

## CI Job Evidence

```text
workflow -> CI
job -> api-smoke
job_id -> 79830671110
conclusion -> success
Compile API and local packages -> success
Check semantic retrieval quality report staleness -> success
Check ClamAV owner runtime input discovery no-payload missing state -> success
Check embedding provider owner runtime input discovery missing state -> success
Run API smoke tests -> success
```

## External Feedback Screen Evidence

```text
workflow -> External Feedback Screen
job -> screen
job_id -> 79830670945
conclusion -> success
Capture issue comments -> success
Screen issue comments -> success
Draft manual acceptance records -> success
Upload screening artifact -> success
Upload acceptance draft artifact -> success
```

## Boundary

This is remote workflow verification only.

This is not the local runtime smoke itself.

This is not semantic retrieval quality evidence.

This is not embedding generation.

This is not a live OpenAI provider call.

This is not Evidence Ledger quality evidence.

This is not final truth adjudication.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
