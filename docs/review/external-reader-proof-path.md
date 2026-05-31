# External-reader Proof Path

Status: compact proof index.

Phase marker: external-reader proof path index v0.

This page is the shortest repository-native path for an external reviewer who wants to inspect what NoiseProof Agent currently proves without reading the entire phase history.

## 5-minute path

Read in this order:

1. `README.md`
   - Purpose, non-goals, implementation status, and current boundaries.
2. `docs/application/portfolio-index.md`
   - Repository map from system surface to proof artifacts.
3. `docs/review/failure-case-workflow-parent-linkage-proof-index.md`
   - Compact reader path for manual failure-case workflow parent linkage.
4. `docs/review/application-ready-review.md`
   - Current application-readiness judgment and claim boundaries.
5. `docs/application/braincrew-role-map.md`
   - Role mapping and application narrative.
6. `docs/review/portfolio-site-proof-artifact-route-verification.md`
   - Live portfolio route verification for the public NoiseProof proof surface.
7. `docs/review/demo-transcript-capture.md`
   - Self-authored local route transcript for collection planning, workflow preview, lineage, and dashboard inspection.
8. `docs/review/local-browser-screenshot-walkthrough.md`
   - Self-authored local browser screenshot walkthrough for the operations dashboard and workflow-run lineage link.
9. `docs/review/external-review-request.md`
   - Structured request packet for external critique. This is not feedback itself.
10. `docs/review/external-reviewer-brief.md`
    - 2-minute path for a reviewer before leaving feedback.
11. `docs/review/external-reviewer-live-proof-route-refresh.md`
    - Latest public portfolio proof route for reviewer orientation. This is not feedback itself.
12. `docs/review/external-reviewer-outreach-packet.md`
    - Copy-paste outreach messages for actual human reviewers. This is not feedback itself.

## Optional source-level provenance

Use `docs/review/readme-proof-marker-archive.md` only when you need legacy README proof-marker continuity after README scanability cleanup.

This archive is source-level provenance, not product runtime evidence, not hosted deployment evidence, not automatic failure-case creation, and not complete workflow failure causality.

## Public Portfolio Surface

The live portfolio proof artifact is:

```text
https://svy04.github.io/proof-artifacts/noiseproof-agent-phase-ladder-2026-05-30/
```

Use `docs/review/portfolio-site-proof-artifact-route-verification.md` for the current route verification record.

Latest public proof route refresh:

```text
https://svy04.github.io/proof-artifacts/noiseproof-live-route-verification-2026-06-01/
```

Use `docs/review/external-reviewer-live-proof-route-refresh.md` for the latest reviewer-facing public route refresh.

This public route is a proof surface for the portfolio. It is not hosted deployment evidence for NoiseProof Agent.

## Demo Transcript

Use `docs/review/demo-transcript-capture.md` for the current self-authored route walkthrough.

It is useful for reader orientation, but it is not external reviewer feedback, not hosted deployment evidence, and not customer validation.

## Local Browser Screenshot

Use `docs/review/local-browser-screenshot-walkthrough.md` for the current visual walkthrough.

It records `GET /ops/dashboard` after a deterministic workflow preview and checks that the dashboard includes workflow runs and lineage links.

It is useful for local visual inspection, but it is not external reviewer feedback, not hosted deployment evidence, not customer validation, and not production observability.

## External Review Request

Use `docs/review/external-reviewer-brief.md` first if the reviewer only has a few minutes.

Use `docs/review/external-review-request.md` when asking a reviewer to inspect the proof path.

It points reviewers to `.github/ISSUE_TEMPLATE/external-review-feedback.md` and asks for critique on over-stated claims, missing evidence, and hiring signal.

Use `docs/review/external-reviewer-outreach-packet.md` when you need a copy-paste message for an FDE/product engineer, RAG/data engineer, or founder/operator reviewer.

Public request issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

It is not external reviewer feedback.

## What This Path Proves

Allowed claim:

NoiseProof Agent is an inspectable local portfolio service with phased proof artifacts for data profiling, parser boundaries, chunking, lexical retrieval, evidence preview, gate preview, report preview, persisted proof records, workflow parent linkage, failure-case persistence, manual workflow parent provenance, and current application-facing boundaries.

Allowed claim:

Manual failure-case workflow parent linkage exists. A manually persisted `failure_cases` row can retain nullable `workflow_run_id` provenance to a `workflow_runs` parent, and that path has schema/API support, route-level smoke evidence, fresh DB evidence, dashboard surfacing, and a proof index.

## What This Path Does Not Prove

Forbidden claim:

NoiseProof Agent is production-ready, hosted, customer-validated, or a complete RAG/agent platform.

Forbidden claim:

NoiseProof Agent automatically creates failure cases from workflow failures or proves complete workflow failure causality.

Forbidden claim:

NoiseProof Agent has robust PDF extraction, embeddings, semantic retrieval, distributed tracing, market prediction quality, or free-form final answer generation.

## Boundary

This proof path adds no runtime behavior, schema, migration, API endpoint, dashboard rendering, smoke execution, hosted deployment evidence, automatic failure detection, automatic failure-case creation, automatic persistence from workflow failures, complete workflow failure causality, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

This is not hosted deployment evidence.
This is not automatic failure-case creation.
This is not complete workflow failure causality.

## Next Gate

```text
external reviewer feedback v0
```
