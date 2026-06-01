# NoiseProof Agent

A noise-resilient data agent for messy market intelligence.

This project ingests messy documents and market data, evaluates chunking and retrieval strategies, detects contradictory evidence, and generates claim-bounded reports with citations. It is not a trading bot and does not provide buy/sell recommendations.

## External Reviewer Fast Path

Start with `docs/review/external-reader-proof-path.md`.

That file is the 5-minute repository-native path for reviewing what this project currently proves. It points to the README, portfolio index, failure-case workflow parent proof index, application-ready review, and Braincrew role map.

Boundary: this fast path is not hosted deployment evidence, not automatic failure-case creation, and not complete workflow failure causality.

## What This Is

NoiseProof Agent is a planned RAG/agent service for market intelligence work where the input data is inconsistent, noisy, and difficult to trust.

Current implemented capability groups:

- service skeleton, metadata persistence, PostgreSQL schema, migration runner, and CI
- document profiling, parser boundaries, chunk strategy comparison, and lexical retrieval
- collection planning, Evidence Ledger, Noise Gate, and claim-bounded report previews
- persisted evidence/gate/report records, trace lookup, filters, workflow parents, and derived lineage
- operations dashboard, failure-case persistence, manual workflow parent provenance, and proof-path documentation

Detailed phase history lives in `docs/GOAL.md`, `docs/application/portfolio-index.md`, and the phase-specific `docs/review/*` artifacts. This README now keeps the first-pass narrative focused on what the project currently demonstrates and what it still does not claim.
The product thesis:

> A good data agent does not start by answering well. It starts by preventing unsupported answers from passing.

## What This Is Not

NoiseProof Agent is not a trading bot.

This repository will not build:

- buy/sell signals
- automatic order execution
- return prediction
- stock recommendations
- financial advice
- real-time trading infrastructure
- reinforcement-learning trading logic
- a large-scale data lake
- a multi-tenant SaaS v1
- polished UI before evidence, logging, and evaluation work

Correct questions for this system:

- What happened?
- What evidence supports it?
- Which sources conflict?
- Which claims are weak?
- What data is missing?
- Why should this conclusion not be trusted yet?

Incorrect questions for this system:

- Should I buy?
- Should I sell?
- What is the target price?
- How much return will this make?

## Why This Exists

Market intelligence work often starts with mixed inputs: PDFs, CSVs, news pages, internal notes, reports, and stale or conflicting sources. LLMs can turn that mess into a confident answer too quickly.

NoiseProof Agent is designed to make unsupported answers harder to pass. The main artifact is not a fluent answer. The main artifact is an inspectable trail: source profiles, retrieval runs, evidence spans, contradictions, blocked claims, limitations, run logs, and failure cases.

## Target User Problem

The target user is a market researcher, analyst, founder, or operator who needs to read messy market material without accidentally treating weak evidence as a strong conclusion.

They need a system that can:

- ingest mixed document formats
- profile source quality
- compare chunk strategies
- retrieve source-linked evidence
- record which claims are supported, weak, contradicted, unsupported, or blocked
- show why a final report should or should not be trusted

## Planned Architecture

```text
Source Upload / URL Input
  -> Document Profiler
  -> Parser Selector
  -> Chunk Strategy Experiment
  -> Collection Plan Preview
  -> Indexing
  -> Retrieval
  -> Evidence Ledger
  -> Analysis Draft
  -> Critic / Noise Gate
  -> Claim-bounded Report
  -> Run Log / Failure Case
```

Implementation status:

Current status groups:

- documentation: product brief, architecture, ADRs, runbook, application package, and review artifacts
- service skeleton: FastAPI health, ops summary/dashboard, metadata routes, PostgreSQL schema, migration runner, and CI
- ingestion/RAG boundaries: document profiling, parser adapters, chunk strategy comparison, lexical retrieval, and collection planning
- evidence/report boundaries: Evidence Ledger, Noise Gate, claim-bounded report previews, trace lookup, filters, workflow parents, lineage, and warning codes
- proof surfaces: DB/failure smoke artifacts, reviewer path/request/brief/link-map/root-guide, live issue/request-surface checks, feedback screening artifacts, and Braincrew application mapping

Detailed implementation history remains in the lower detailed Implementation Status section, `docs/GOAL.md`, and phase-specific `docs/review/*` artifacts.

Still planned or explicitly unclaimed near the top:

- web app and polished dashboard UI
- persisted file upload parsing and robust PDF extraction
- persisted chunks, embeddings, semantic retrieval, and LLM calls
- hosted deployment evidence
- automatic failure-case creation from workflow failures
- complete workflow failure causality
- free-form final report generation

## Implementation Status

Major implementation milestones:

- Day 1 / Day 2: docs, FastAPI skeleton, metadata persistence, PostgreSQL schema, CI, runbook
- Ingestion path: fixtures, profiler, parsers, chunk experiment, lexical retrieval, collection plan preview
- Evidence path: Evidence Ledger, Noise Gate, report records, trace lookup, filters, workflow parent lineage
- Operations path: ops dashboard, warnings, workflow versions, migration runner, fresh DB/API smoke, failure proofs
- Application path: evaluation docs, Braincrew map, cover message, portfolio index, external proof path, README scanability
- README detailed implementation-status compression v0: implemented
- README proof-marker archive review v0: implemented
- README proof-marker archive extraction v0: implemented
- README proof-marker archive application refresh review v0: implemented
- README proof-marker archive application refresh v0: implemented
- README proof-marker archive external path review v0: implemented
- README proof-marker archive external path refresh v0: implemented
- Application current-claim compression review v0: implemented
- Application current-claim compression v0: implemented
- Braincrew role-map runtime proof compression review v0: implemented
- Braincrew role-map runtime proof compression v0: implemented
- Application proof surface final scan review v0: implemented
- Application-ready summary compression v0: implemented
- External-reader final proof-path dry-read review v0: implemented
- External-reader proof path next-gate refresh v0: implemented
- Application package final consistency review v0: implemented
- Portfolio site handoff review v0: implemented
- Portfolio site proof artifact route verification v0: implemented
- Demo transcript capture v0: implemented
- Local browser screenshot walkthrough v0: implemented
- External review request packet v0: implemented
- External feedback intake criteria v0: implemented
- External reviewer brief v0: implemented
- External reviewer live proof route refresh v0: implemented
- External reviewer link map v0: implemented
- External review root guide v0: implemented
- External review issue body encoding verification v0: implemented
- External review issue body root-guide verification v0: implemented
- External review issue body link-map verification v0: implemented
- External review issue template link-map refresh v0: implemented
- External review issue label verification v0: implemented
- External review owner request comment verification v0: implemented
- External reviewer outreach packet v0: implemented
- External feedback qualification preview v0: implemented
- External feedback screening CLI v0: implemented
- External feedback screening workflow v0: implemented
- External feedback screening workflow verification v0: implemented
- README next-gate stale-claim refresh v0: implemented
- External feedback acceptance template v0: implemented
- External feedback acceptance draft CLI v0: implemented
- External feedback acceptance draft workflow v0: implemented
- External feedback acceptance draft workflow verification v0: implemented
- Owner-approved product continuation decision v0: implemented
- File upload preview v0: implemented
- Uploaded file chunk preview v0: implemented
- Uploaded file retrieval preview v0: implemented
- Uploaded file Evidence Ledger preview v0: implemented
- Uploaded file Noise Gate preview v0: implemented
- Uploaded file report preview v0: implemented
- Uploaded file failure-case draft preview v0: implemented
- Uploaded file failure-case manual handoff smoke v0: implemented
- Uploaded file proof path index refresh v0: implemented
- Uploaded file runtime smoke packet v0: implemented
- Persisted uploaded file intake review v0: implemented
- Uploaded file intake manifest preview v0: implemented
- Uploaded file intake manifest runtime smoke v0: implemented
- Uploaded file intake manifest application refresh v0: implemented
- External reviewer upload-manifest request refresh v0: implemented
- External reviewer upload-manifest issue-body refresh v0: implemented
- Persisted uploaded file intake schema review v0: implemented
- Uploaded file intake manifest persistence schema v0: implemented
- Uploaded file intake manifest persistence repository review v0: implemented
- Uploaded file intake manifest persistence repository v0: implemented

For exhaustive phase history, use `docs/GOAL.md`; artifacts live in `docs/review/*` and `docs/application/portfolio-index.md`.

Not implemented yet:

- persisted file upload parsing
- robust PDF extraction
- persisted chunks
- autonomous workflow execution endpoints
- automatic failure-case persistence from workflow failures
- embeddings
- retrieval-run-linked Evidence Ledger records
- full distributed tracing or hosted observability


## Planned Agent Workflow

NoiseProof Agent will use five explicit roles before introducing any complex multi-agent abstraction:

1. Ingestion Agent: parse and profile inputs
2. Retrieval Agent: compare chunk strategies and retrieve source-linked evidence
3. Analysis Agent: draft claims from retrieved evidence
4. Critic Agent: block unsupported claims, contradictions, overconfident language, missing limitations, and trading-advice drift
5. Report Agent: generate a claim-bounded report with citations and next data needed

Each planned stage must log its input and output.

Auto Trace behavior records preview endpoint metadata in `agent_runs.trace_json` using the current workflow version. This is not full workflow tracing or distributed observability.

## Evidence Ledger

The Evidence Ledger is the control surface between retrieval and final answer generation. Phase 6 implements a deterministic preview boundary. Phase 12 persists generated ledger entries so operations views can count unsupported and contradicted claims.

Each ledger entry records:

- claim
- source id
- source type
- source date
- evidence span
- confidence
- limitation
- contradicting source ids
- status

Allowed status values:

```text
supported
weakly_supported
contradicted
unsupported
blocked
```

The system should generate the ledger before generating a final report. Current persistence is v0 and does not yet link entries to a retrieval run id.

## Noise Gate

The Noise Gate is the reviewer before a final response is allowed through. Phase 7 implements a deterministic preview boundary. Phase 13 persists gate decisions so blocked and revision-needed outputs remain inspectable.

It checks:

- Does every strong claim have evidence?
- Are there at least two sources for high-confidence claims?
- Is source recency visible?
- Are contradictions surfaced?
- Are quantitative and qualitative signals separated?
- Is the answer drifting into trading advice?
- Are limitations explicit?

The current preview returns `pass`, `needs_revision`, or `blocked`. `POST /noise-gates` stores the decision and checks. It does not generate the final report.

If the gate fails, the system should return:

```text
현재 근거만으로는 결론을 내릴 수 없습니다. 가능한 해석은 다음과 같고, 추가로 확인해야 할 데이터는 다음과 같습니다.
```

## Evaluation

Evaluation is organized around inspectability, not polished demo output.

The Phase 10 evaluation package tracks:

- sample dataset description
- retrieval hit rate
- citation coverage
- missing evidence count
- unsupported claim examples
- contradiction examples
- failure cases and next fixes

See:

- `docs/evaluation/eval-plan.md`
- `docs/evaluation/retrieval-eval-report.md`
- `docs/evaluation/failure-cases.md`

The project does not claim model, semantic retrieval, or answer quality success.

## Failure Cases

Failure cases are first-class artifacts. The planned system will record:

- failed questions
- retrieval misses
- unsupported claims
- contradicted claims
- trading-advice drift
- missing source recency
- parser failures
- root cause and next action

## Local Setup

The current local stack defines a PostgreSQL + pgvector database service and a FastAPI skeleton.

```bash
cp .env.example .env
docker compose up -d db
cd apps/api
uv sync
uv run uvicorn app.main:app --reload
```

Smoke checks:

```bash
curl http://localhost:8000/health
curl http://localhost:8000/ops/summary
curl http://localhost:8000/ops/dashboard
curl -X POST http://localhost:8000/documents/profile \
  -H "Content-Type: application/json" \
  -d "{\"source_type\":\"markdown\",\"text\":\"# Memo\nDate: 2026-05-28\nSource: https://example.com\nRevenue grew 12%.\"}"
curl -X POST http://localhost:8000/documents/parse-preview \
  -H "Content-Type: application/json" \
  -d "{\"source_type\":\"markdown\",\"content\":\"# Memo\nDate: 2026-05-28\nSource: https://example.com\nRevenue grew 12%.\"}"
curl -X POST http://localhost:8000/documents/chunk-preview \
  -H "Content-Type: application/json" \
  -d "{\"source_type\":\"markdown\",\"content\":\"# Market\nRevenue grew 12% in 2026.\n\n## Risks\nCosts rose 7%.\",\"max_characters\":80,\"overlap\":10}"
curl -X POST http://localhost:8000/retrieval-runs \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"strategy\":\"heading-aware\",\"sources\":[{\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"content\":\"# Demand\nEnterprise demand grew 12% in 2026.\"}]}"
curl -X POST http://localhost:8000/collection-plans/preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Did this company's AI narrative become materially stronger?\"}"
curl -X POST http://localhost:8000/evidence-ledgers/preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"retrieval_results\":[{\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"chunk_strategy\":\"heading-aware\",\"chunk_index\":0,\"text\":\"Enterprise demand grew 12% in 2026.\",\"score\":0.75,\"matched_terms\":[\"demand\",\"enterprise\",\"growth\"],\"metadata\":{\"source_date\":\"2026-05-28\"}}]}"
curl -X POST http://localhost:8000/evidence-ledgers \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Should I buy this company?\",\"retrieval_results\":[]}"
curl http://localhost:8000/evidence-ledgers
curl -X POST http://localhost:8000/noise-gates/preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"evidence_entries\":[{\"claim\":\"Enterprise demand grew\",\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"source_date\":\"2026-05-28\",\"evidence_span\":\"Enterprise demand grew 12% in 2026.\",\"confidence\":\"medium\",\"limitation\":\"Supported by one retrieved source.\",\"contradicting_source_ids\":[],\"status\":\"supported\",\"matched_terms\":[\"enterprise\",\"demand\",\"growth\"],\"role\":\"direct_support\"}],\"draft_claims\":[\"Enterprise demand grew, with the current evidence limited to one retrieved source.\"]}"
curl -X POST http://localhost:8000/noise-gates \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Should I buy this company?\",\"evidence_entries\":[{\"claim\":\"Should I buy this company\",\"source_id\":null,\"source_type\":null,\"source_date\":null,\"evidence_span\":\"\",\"confidence\":\"none\",\"limitation\":\"Question drifts into buy/sell or financial-advice intent.\",\"contradicting_source_ids\":[],\"status\":\"blocked\",\"matched_terms\":[],\"role\":\"user_intent_check\"}],\"draft_claims\":[\"Should I buy this company?\"]}"
curl http://localhost:8000/noise-gates
curl -X POST http://localhost:8000/reports/preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"evidence_entries\":[{\"claim\":\"Enterprise demand grew\",\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"source_date\":\"2026-05-28\",\"evidence_span\":\"Enterprise demand grew 12% in 2026.\",\"confidence\":\"medium\",\"limitation\":\"Supported by one retrieved source.\",\"contradicting_source_ids\":[],\"status\":\"supported\",\"matched_terms\":[\"enterprise\",\"demand\",\"growth\"],\"role\":\"direct_support\"}],\"draft_claims\":[\"Enterprise demand grew, with the current evidence limited to one retrieved source.\"]}"
curl -X POST http://localhost:8000/workflow-runs/execute-preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"strategy\":\"fixed-window\",\"sources\":[{\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"content\":\"Enterprise segment demand growth was 12 percent in 2026.\"}],\"draft_claims\":[\"Enterprise segment demand growth was supported by current retrieved evidence.\"]}"
curl http://localhost:8000/workflow-runs/<uuid>
curl http://localhost:8000/workflow-runs/<uuid>/lineage
curl http://localhost:8000/agent-runs
```

Reviewer-facing public proof route:

```text
docs/review/external-reviewer-live-proof-route-refresh.md
https://svy04.github.io/proof-artifacts/noiseproof-live-route-verification-2026-06-01/
```

This route helps external reviewers find the latest public proof surface, reviewer brief, and issue #1. It is not external reviewer feedback, not hosted deployment evidence for NoiseProof Agent, and not customer validation.

## Demo Flow

Planned demo flow after implementation:

1. Upload or reference messy PDF, CSV, URL/HTML, and markdown memo inputs.
2. Generate a document profile for each input.
3. Compare fixed-window, heading-aware, and row-aware chunk strategies.
4. Create a Collection Plan Preview for a market-intelligence question.
5. Run retrieval for source-linked candidate chunks.
6. Generate an Evidence Ledger Preview before the answer.
7. Ask the Critic Agent to block unsupported claims and surface contradictions.
8. Generate a claim-bounded report preview with citations and limitations.
9. Show the run log and failure case record.

## What I Would Improve Next

The current next evidence gate remains external reviewer feedback v0.

The project already has a reviewer request packet, intake criteria, reviewer brief, direct link map, root review guide, live issue-body encoding verification, live issue-body root-guide verification, live issue-body link-map verification, issue-template link-map refresh, issue-label verification, owner request comment rejection verification, outreach packet, screening CLI, screening workflow, and remote pending artifact verification. Those artifacts prepare the path, but they do not prove that an outside reviewer inspected the work.

The owner approved continuing implementation while that external-review gate stays pending. That approval is recorded in `docs/review/owner-approved-product-continuation-decision.md`; it is not external reviewer feedback, customer validation, Braincrew acceptance, hosted deployment evidence, or production readiness.

File upload preview v0 through uploaded file intake manifest persistence repository v0 are now implemented as bounded upload proof steps. The current next evidence gate remains `external reviewer feedback v0`; the current next product implementation gate is `uploaded file intake manifest persistence endpoint review v0`.

## Braincrew Role Alignment

Primary hiring target:

```text
Braincrew Forward Deployed Engineer
```

Secondary / long-term target:

```text
Braincrew Product Engineer
```

NoiseProof Agent is designed to produce evidence for customer problem definition, RAG/agent workflow design, full-stack service implementation, logging, monitoring, evaluation, deployment readiness, and technical decision documentation.

This repository is the implementation artifact. The portfolio blog is the strategy, explanation, and proof surface.
