# NoiseProof Agent

A noise-resilient data agent for messy market intelligence.

This project ingests messy documents and market data, evaluates chunking and retrieval strategies, detects contradictory evidence, and generates claim-bounded reports with citations. It is not a trading bot and does not provide buy/sell recommendations.

## What This Is

NoiseProof Agent is a planned RAG/agent service for market intelligence work where the input data is inconsistent, noisy, and difficult to trust.

The project started with a documentation-first Day 1 package. Day 2 added a small service skeleton: FastAPI routes, metadata persistence boundaries, PostgreSQL schema init SQL, and API smoke CI. Phase 2 added messy-data fixtures and Document Profiler v0. Phase 3 added parser adapter stubs for parse-preview boundaries. Phase 4 added a small chunk strategy experiment boundary. Phase 5 added lexical retrieval v0 over chunks and records retrieval runs. Phase 5.5 added a deterministic Collection Plan Preview so a question declares required information roles before evidence work starts. Phase 6 added Evidence Ledger Preview v0 so retrieval candidates can be promoted, weakened, contradicted, or blocked before any final answer exists. Phase 7 added Noise Gate Preview v0 so ledger entries can be blocked, downgraded, or allowed before report generation. Phase 8 added Claim-bounded Report Preview v0 so only gate-passing claims become report-shaped output. Phase 9 added Operations Dashboard v0 so the existing run, retrieval, and failure records are inspectable from the browser. Phase 11 adds Auto Trace Recording v0 so preview endpoints leave `agent_runs.trace_json` metadata before the project claims a full agent workflow.

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

- Product definition: documented
- Architecture: documented
- ADRs: documented
- Local database service: configured
- FastAPI health endpoint: implemented
- PostgreSQL schema init: implemented
- Document metadata endpoints: implemented
- Agent run metadata endpoints: implemented
- Failure case endpoints: implemented
- Ops summary placeholder: implemented
- Messy market data fixtures: implemented
- Document Profiler v0: implemented
- Parser adapter stubs: implemented for markdown, CSV, HTML/URL, PDF text-only fallback, and unknown source types
- Chunk strategy experiment v0: implemented for fixed-window, heading-aware, and row-aware strategies
- Retrieval v0: implemented for lexical candidate search over chunk-preview output with source ids
- Collection Plan Preview: implemented for role-based information needs before Evidence Ledger work
- Evidence Ledger Preview: implemented for deterministic claim-level entries over retrieval candidates
- Noise Gate Preview: implemented for deterministic pre-report checks over ledger entries and draft claims
- Claim-bounded Report Preview: implemented for gate-passing ledger entries
- Operations Dashboard v0: implemented as a plain FastAPI HTML view over current metadata records
- Evaluation/Application Package v0: implemented for evaluation planning, failure cases, Braincrew role mapping, cover message, and portfolio index
- Application-ready review: implemented as a partial/pass boundary checklist
- Auto Trace Recording v0: implemented for document profile, parse, chunk, collection plan, evidence ledger, noise gate, and report preview endpoints
- Web app, file upload parsing, robust PDF extraction, persisted chunks, embeddings, persisted Evidence Ledger entries, persisted reports: planned, not implemented

## Implementation Status

### Day 1 - Documentation-first package

- Product brief: done
- Architecture: done
- ADRs: done
- Docker Compose database target: done

### Day 2 - Service skeleton

- FastAPI health endpoint: done
- PostgreSQL schema init: done
- Document metadata endpoints: done
- Agent run metadata endpoints: done
- Failure case endpoints: done
- Ops summary placeholder: done
- GitHub Actions API smoke CI: done
- Runbook: done

### Phase 2 - Ingestion fixtures and Document Profiler v0

- Messy market data fixture pack: done
- Reusable profiler package: done
- `POST /documents/profile`: done
- Profile fields for source type, counts, table/url/date/number detection, extraction quality, recommended strategy, and warnings: done

### Phase 3 - Parser adapter stubs

- Parser boundary package: done
- Markdown parser metadata for headings, links, and bullets: done
- CSV parser metadata for rows, columns, headers, and malformed row warnings: done
- HTML/URL text preview and link metadata: done
- PDF text-only fallback with explicit non-claim about robust PDF extraction: done
- Unknown source type structured failure candidate: done
- `POST /documents/parse-preview`: done

### Phase 4 - Chunk strategy experiment v0

- `POST /documents/chunk-preview`: done
- Fixed-window chunking with max-character and overlap controls: done
- Heading-aware chunking with `header_path` metadata: done
- Row-aware chunking with CSV header and row metadata: done
- Strategy comparison metrics for chunk count, character distribution, boundary count, oversized chunks, and estimated tokens: done
- Unknown source types keep parser failure candidates and skip chunking: done

### Phase 5 - Retrieval v0

- `POST /retrieval-runs`: done
- `GET /retrieval-runs`: done
- Lexical candidate search over generated chunks: done
- Source ids returned on each retrieval candidate: done
- Retrieval run records stored in `retrieval_runs`: done
- No-results retrieval case recorded with `status: no_results`: done

### Phase 5.5 - Collection Plan Preview

- `POST /collection-plans/preview`: done
- Question-only input: done
- Required information roles returned before Evidence Ledger work: done
- Buy/sell drift questions include `user_intent_check` and stop conditions: done
- Underspecified, numeric, and source-quality questions expose role-specific warnings: done
- LLM calls, external search, retrieval expansion, Evidence Ledger generation, final reports, dashboard, and DB persistence were not implemented in Phase 5.5

### Phase 6 - Evidence Ledger Preview v0

- `POST /evidence-ledgers/preview`: done
- Retrieval candidates can become claim-level ledger entries: done
- Supported, weakly_supported, contradicted, unsupported, and blocked statuses: done
- Source id, source type, source date, evidence span, confidence, limitation, contradicting source ids, matched terms, and role are returned: done
- No-evidence questions produce a blocked ledger entry: done
- Buy/sell drift questions produce a blocked ledger entry: done
- Contradiction language is surfaced before report generation: done
- LLM calls, external search, Critic / Noise Gate, final reports, dashboard, and Evidence Ledger DB persistence: not implemented

### Phase 7 - Noise Gate Preview v0

- `POST /noise-gates/preview`: done
- Checks whether ledger entries can pass into a future report stage: done
- Blocks unsupported or blocked ledger entries: done
- Blocks buy/sell and financial-advice drift: done
- Requires revision for contradictions, missing source recency, missing limitations, and high-confidence claims with fewer than two source ids: done
- Flags overconfident draft language: done
- Returns decision, checks, blocked claims, downgraded claims, allowed claims, required revisions, fallback message, and warnings: done
- LLM calls, persisted gate records, final reports, dashboard, and answer generation: not implemented

### Phase 8 - Claim-bounded Report Preview v0

- `POST /reports/preview`: done
- Runs Noise Gate before report formatting: done
- Generates report output only when the gate decision is `pass`: done
- Includes summary, claims, source ids, evidence spans, confidence, limitations, contradictions, and next data needed: done
- Returns fallback message and required revisions when the gate is `blocked` or `needs_revision`: done
- LLM calls, persisted report records, and free-form answer generation: not implemented

### Phase 9 - Operations Dashboard v0

- `GET /ops/dashboard`: done
- Browser-readable operations surface for current metadata: done
- Shows summary counts, recent agent runs, failure cases, and retrieval runs: done
- Keeps unsupported claim and contradiction counts as placeholders until persisted Evidence Ledger entries exist: done
- Next.js, UI polish, new model behavior, new retrieval behavior, persisted Evidence Ledger entries, and persisted report records: not implemented

### Phase 10 - Evaluation/Application Package v0

- `docs/evaluation/eval-plan.md`: done
- `docs/evaluation/retrieval-eval-report.md`: done
- `docs/evaluation/failure-cases.md`: done
- `docs/application/braincrew-role-map.md`: done
- `docs/application/cover-message.md`: done
- `docs/application/portfolio-index.md`: done
- `docs/review/application-ready-review.md`: done
- Runtime product behavior, new retrieval behavior, LLM calls, and deployment: not implemented in Phase 10

### Phase 11 - Auto Trace Recording v0

- Preview endpoints auto-create `agent_runs` metadata records: done
- `trace_json` records endpoint, phase, source type, counts, decisions, and report status where available: done
- Failed preview operations are wrapped so a failed trace can be recorded before the exception is re-raised: done
- Full distributed tracing, hosted observability, persisted Evidence Ledger records, persisted gate records, and persisted report records: not implemented

Not implemented yet:

- file upload parsing
- robust PDF extraction
- persisted chunks
- embeddings
- persisted Evidence Ledger entries
- persisted Critic / Noise Gate records
- persisted report records
- full distributed tracing or hosted observability

## Planned Agent Workflow

NoiseProof Agent will use five explicit roles before introducing any complex multi-agent abstraction:

1. Ingestion Agent: parse and profile inputs
2. Retrieval Agent: compare chunk strategies and retrieve source-linked evidence
3. Analysis Agent: draft claims from retrieved evidence
4. Critic Agent: block unsupported claims, contradictions, overconfident language, missing limitations, and trading-advice drift
5. Report Agent: generate a claim-bounded report with citations and next data needed

Each planned stage must log its input and output.

Current Phase 11 behavior records preview endpoint metadata in `agent_runs.trace_json`. This is not full workflow tracing or distributed observability.

## Evidence Ledger

The Evidence Ledger is the control surface between retrieval and final answer generation. Phase 6 implements a deterministic preview boundary; persisted ledger entries are still planned.

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

The system should generate the ledger preview before generating a final report.

## Noise Gate

The Noise Gate is the reviewer before a final response is allowed through. Phase 7 implements a deterministic preview boundary; persisted gate records and final reports are still planned.

It checks:

- Does every strong claim have evidence?
- Are there at least two sources for high-confidence claims?
- Is source recency visible?
- Are contradictions surfaced?
- Are quantitative and qualitative signals separated?
- Is the answer drifting into trading advice?
- Are limitations explicit?

The current preview returns `pass`, `needs_revision`, or `blocked`. It does not generate the final report.

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
curl -X POST http://localhost:8000/noise-gates/preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"evidence_entries\":[{\"claim\":\"Enterprise demand grew\",\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"source_date\":\"2026-05-28\",\"evidence_span\":\"Enterprise demand grew 12% in 2026.\",\"confidence\":\"medium\",\"limitation\":\"Supported by one retrieved source.\",\"contradicting_source_ids\":[],\"status\":\"supported\",\"matched_terms\":[\"enterprise\",\"demand\",\"growth\"],\"role\":\"direct_support\"}],\"draft_claims\":[\"Enterprise demand grew, with the current evidence limited to one retrieved source.\"]}"
curl -X POST http://localhost:8000/reports/preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"evidence_entries\":[{\"claim\":\"Enterprise demand grew\",\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"source_date\":\"2026-05-28\",\"evidence_span\":\"Enterprise demand grew 12% in 2026.\",\"confidence\":\"medium\",\"limitation\":\"Supported by one retrieved source.\",\"contradicting_source_ids\":[],\"status\":\"supported\",\"matched_terms\":[\"enterprise\",\"demand\",\"growth\"],\"role\":\"direct_support\"}],\"draft_claims\":[\"Enterprise demand grew, with the current evidence limited to one retrieved source.\"]}"
curl http://localhost:8000/agent-runs
```

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

After Auto Trace Recording v0, the next phase should reduce the remaining dashboard placeholder gap:

- persist Evidence Ledger preview entries or a minimal claim-status summary
- connect persisted unsupported and contradiction counts to the operations dashboard
- keep deterministic preview behavior before adding LLM calls or embeddings

It should not start with UI polish, LLM prompt tuning, new retrieval behavior, or broad agent abstractions.

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
