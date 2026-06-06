# Retrieval-run-linked Gate/Report Semantic Source Provenance Runtime Smoke Remote Verification

Status: implemented.

Phase marker: retrieval-run-linked Gate/Report semantic source provenance runtime smoke remote verification v0.

## Purpose

Record remote GitHub Actions evidence that the Phase 634 runtime-smoke proof passed the repository CI and feedback-screen workflows on `main`.

This verifies the committed proof chain for `docs/review/retrieval-run-linked-gate-report-semantic-source-provenance-runtime-smoke.md`.

It does not rerun the local Docker/FastAPI runtime smoke in GitHub Actions.

## Remote Runs

```text
head_sha -> 7e7995ff5657a8c970683ce6dd0afea1dd350c48
CI run 27048811299 -> success
External Feedback Screen run 27048811288 -> success
```

CI URL: https://github.com/svy04/noiseproof-agent/actions/runs/27048811299

External Feedback Screen URL: https://github.com/svy04/noiseproof-agent/actions/runs/27048811288

## CI Job Evidence

```text
workflow -> CI
job -> api-smoke
job_id -> 79840166726
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
job_id -> 79840166751
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

This is not Noise Gate quality evidence.

This is not report quality evidence.

This is not final truth adjudication.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
