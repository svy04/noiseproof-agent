# NoiseProof Agent

A noise-resilient data agent for messy market intelligence.

This project ingests messy documents and market data, evaluates chunking and retrieval strategies, detects contradictory evidence, and generates claim-bounded reports with citations. It is not a trading bot and does not provide buy/sell recommendations.

## What This Is

NoiseProof Agent is a planned RAG/agent service for market intelligence work where the input data is inconsistent, noisy, and difficult to trust.

The project started with a documentation-first Day 1 package. Day 2 added a small service skeleton: FastAPI routes, metadata persistence boundaries, PostgreSQL schema init SQL, and API smoke CI. Phase 2 added messy-data fixtures and Document Profiler v0. Phase 3 added parser adapter stubs for parse-preview boundaries. Phase 4 added a small chunk strategy experiment boundary. Phase 5 added lexical retrieval v0 over chunks and records retrieval runs. Phase 5.5 added a deterministic Collection Plan Preview so a question declares required information roles before evidence work starts. Phase 6 added Evidence Ledger Preview v0 so retrieval candidates can be promoted, weakened, contradicted, or blocked before any final answer exists. Phase 7 added Noise Gate Preview v0 so ledger entries can be blocked, downgraded, or allowed before report generation. Phase 8 added Claim-bounded Report Preview v0 so only gate-passing claims become report-shaped output. Phase 9 added Operations Dashboard v0 so the existing run, retrieval, and failure records are inspectable from the browser. Phase 11 added Auto Trace Recording v0 so preview endpoints leave `agent_runs.trace_json` metadata before the project claims a full agent workflow. Phase 12 added persisted Evidence Ledger records so unsupported and contradiction counts are no longer dashboard placeholders. Phase 13 added persisted Noise Gate records so gate decisions can be inspected after the preview call. Phase 14 added persisted Report Preview records so generated, blocked, and revision-needed report-shaped outputs can be inspected after the preview call. Phase 15 added `workflow_trace_id` linkage across persisted evidence, gate, report records, and their matching `agent_runs.trace_json`. Phase 16 added `GET /traces/{workflow_trace_id}` so a trace id can be inspected directly. Phase 17 added lightweight filters for persisted Evidence Ledger, Noise Gate, and Report record lists. Phase 18 added trace lookup and filter links to the plain operations dashboard. Phase 18.5 reviewed direct `agent_run_id` foreign-key linkage and kept it unimplemented until the run lifecycle is changed. Phase 19 added an agent-run lifecycle so traced operations create a parent run before execution and update that same run after completion or failure. Phase 20 added `agent_run_id` linkage on persisted Evidence Ledger, Noise Gate, and Report records. Phase 21 added parent-run provenance links to persisted gate and report rows in the plain dashboard. Phase 22 added a persisted Evidence Ledger table to the dashboard. Phase 22.5 reviewed evidence-to-gate/report cross-links and deferred them until a single workflow parent exists. Phase 23 reviewed the single workflow parent boundary and chose a future separate `workflow_runs` table over reusing `agent_runs`. Phase 24 added the `workflow_runs` schema and migration without adding workflow execution behavior. Phase 25 added minimal `workflow_runs` create/list metadata persistence without adding orchestration or child `workflow_run_id` links. Phase 26 surfaced workflow-run metadata in the plain operations dashboard while labeling it as metadata-only, not workflow execution. Phase 27 reviewed child `workflow_run_id` links and deferred them until a workflow execution boundary exists. Phase 28 added a deterministic workflow execution preview that creates a parent workflow run and runs retrieval -> evidence -> gate -> report preview steps. Phase 29 added nullable child `workflow_run_id` links for retrieval, evidence, gate, and report records created by that deterministic preview. Phase 30 added `GET /workflow-runs/{id}` so those linked child records can be inspected from the workflow parent.

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
- Persisted Evidence Ledger records v0: implemented with `POST /evidence-ledgers`, `GET /evidence-ledgers`, and real ops counts for unsupported and contradicted entries
- Persisted Noise Gate records v0: implemented with `POST /noise-gates`, `GET /noise-gates`, and ops counts for blocked/revision gate decisions
- Persisted Report Preview records v0: implemented with `POST /reports`, `GET /reports`, and ops counts for generated/blocked/revision report-shaped outputs
- Record Linkage v0: implemented with shared `workflow_trace_id` values on persisted evidence, gate, report records, and matching agent-run traces
- Trace-id lookup v0: implemented with `GET /traces/{workflow_trace_id}`
- Persisted record filtering v0: implemented for `GET /evidence-ledgers`, `GET /noise-gates`, and `GET /reports`
- Dashboard trace/filter links v0: implemented in `GET /ops/dashboard`
- Agent-run linkage review v0: implemented as `docs/review/agent-run-linkage-review.md`
- Agent-run lifecycle v0: implemented in `run_with_trace()`
- Persisted child record agent-run linkage v0: implemented for Evidence Ledger, Noise Gate, and Report records
- Dashboard parent/child provenance links v0: implemented for Noise Gate and Report record rows
- Evidence Ledger dashboard table v0: implemented for persisted evidence rows
- Evidence-to-gate/report local cross-links review v0: implemented as a review-only decision artifact
- Single workflow parent review v0: implemented as a review-only decision artifact
- WorkflowRun schema v0: implemented as `workflow_runs` table SQL and migration
- WorkflowRun metadata persistence v0: implemented with `POST /workflow-runs` and `GET /workflow-runs`
- WorkflowRun dashboard table v0: implemented as metadata-only visibility in `GET /ops/dashboard`
- WorkflowRun child-link review v0: implemented as a review-only decision artifact
- Deterministic workflow execution preview v0: implemented with `POST /workflow-runs/execute-preview`
- WorkflowRun child-record links v0: implemented with nullable `workflow_run_id` on retrieval, evidence, gate, and report records
- WorkflowRun child inspection surface v0: implemented with `GET /workflow-runs/{id}`
- Web app, file upload parsing, robust PDF extraction, persisted chunks, embeddings, and free-form final report generation: planned, not implemented

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
- LLM calls, persisted report records, final reports, dashboard UI polish, and answer generation: not implemented

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
- Phase 9 originally kept unsupported claim and contradiction counts as placeholders; Phase 12 connects those counts to persisted Evidence Ledger entries
- Next.js, UI polish, new model behavior, new retrieval behavior, and persisted report records: not implemented

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
- Full distributed tracing, hosted observability, agent-run-linked gate records, and persisted report records: not implemented

### Phase 12 - Persisted Evidence Ledger Records v0

- `POST /evidence-ledgers`: done
- `GET /evidence-ledgers`: done
- `evidence_ledger_entries` table and migration: done
- unsupported and contradiction counts in `/ops/summary`: done
- unsupported and contradiction counts in `/ops/dashboard`: done
- Retrieval-run-linked ledger persistence, persisted report records, embeddings, and semantic retrieval: not implemented in Phase 12
- Direct agent-run linkage was added later in Phase 20

### Phase 13 - Persisted Noise Gate Records v0

- `POST /noise-gates`: done
- `GET /noise-gates`: done
- `noise_gate_records` table and migration: done
- blocked and needs-revision gate counts in `/ops/summary`: done
- Noise Gate Records section in `/ops/dashboard`: done
- Phase 13 persisted gate records without direct agent-run linkage; that linkage was added later in Phase 20
- LLM calls, embeddings, semantic retrieval, and free-form final report generation: not implemented

### Phase 14 - Persisted Report Preview Records v0

- `POST /reports`: done
- `GET /reports`: done
- `report_records` table and migration: done
- generated, blocked, and needs-revision report counts in `/ops/summary`: done
- Report Records section in `/ops/dashboard`: done
- Phase 14 used deterministic report persistence without direct `agent_run_id`; that linkage was added later in Phase 20
- LLM calls, embeddings, semantic retrieval, and free-form final report generation: not implemented

### Phase 15 - Record Linkage v0

- `workflow_trace_id` on `evidence_ledger_entries`: done
- `workflow_trace_id` on `noise_gate_records`: done
- `workflow_trace_id` on `report_records`: done
- Matching `workflow_trace_id` in `agent_runs.trace_json` for persisted evidence/gate/report endpoints: done
- Phase 15 used `workflow_trace_id` correlation before direct `agent_run_id` child-record linkage was added in Phase 20
- distributed tracing, LLM calls, embeddings, and semantic retrieval: not implemented

### Phase 16 - Trace-id Lookup v0

- `GET /traces/{workflow_trace_id}`: done
- Trace lookup returns matching agent runs, Evidence Ledger entries, Noise Gate records, Report records, and summary counts: done
- It is a local inspectability endpoint, not distributed tracing or hosted observability

### Phase 17 - Persisted Record Filtering v0

- `GET /evidence-ledgers?workflow_trace_id=...`: done
- `GET /evidence-ledgers?status=...`: done
- `GET /noise-gates?workflow_trace_id=...`: done
- `GET /noise-gates?decision=...`: done
- `GET /reports?workflow_trace_id=...`: done
- `GET /reports?status=...`: done
- This is read-only filtering, not a search engine or dashboard polish

### Phase 18 - Dashboard Trace/Filter Links v0

- `GET /ops/dashboard` includes quick links to trace lookup and persisted record filters: done
- Noise Gate records link to `GET /traces/{workflow_trace_id}` and `GET /noise-gates?workflow_trace_id=...`: done
- Report records link to `GET /traces/{workflow_trace_id}` and `GET /reports?workflow_trace_id=...`: done
- Static filter links are exposed for evidence statuses, gate decisions, and report statuses: done
- This is still a plain inspectability surface, not visual dashboard polish

### Phase 18.5 - Agent-run Linkage Review v0

- `docs/review/agent-run-linkage-review.md`: done
- Direct `agent_run_id` foreign-key linkage: reviewed here, implemented later in Phase 20
- At that review gate, the accepted link remained `workflow_trace_id`
- Future implementation should create the agent run first, then persist child records with its id

### Phase 19 - Agent-run Lifecycle v0

- `run_with_trace()` creates a parent `agent_runs` row with `status: running` before executing the operation: done
- the same `agent_runs` row is updated to `completed` or `failed`: done
- failed operations keep one failed parent run instead of creating a separate trace row after failure: done
- `ended_at`, `latency_ms`, `error_message`, and final `trace_json` are updated on the parent run: done
- direct `agent_run_id` foreign-key linkage for persisted Evidence Ledger, Noise Gate, and Report records: added in the following Phase 20 gate

### Phase 20 - Persisted Child Record Agent-run Linkage v0

- `agent_run_id` on persisted Evidence Ledger entries: done
- `agent_run_id` on persisted Noise Gate records: done
- `agent_run_id` on persisted Report records: done
- `db/migrations/006_child_agent_run_ids.sql`: done
- `GET /traces/{workflow_trace_id}` returns child records with the matching parent run id: done
- this is local parent/child linkage, not distributed tracing or hosted observability

### Phase 21 - Dashboard Parent/Child Provenance Links v0

- `GET /ops/dashboard` shows parent run links for persisted Noise Gate rows: done
- `GET /ops/dashboard` shows parent run links for persisted Report rows: done
- Parent run links route through `GET /traces/{workflow_trace_id}`: done
- This is still a plain inspectability surface, not dashboard polish or distributed tracing

### Phase 22 - Evidence Ledger Dashboard Table v0

- `GET /ops/dashboard` shows persisted Evidence Ledger rows: done
- Evidence rows include trace links, parent run links, status filters, claim, evidence span, source, and confidence: done
- This is still a bounded operations view, not dashboard polish or semantic search

### Phase 22.5 - Evidence-to-gate/report Local Cross-links Review v0

- `docs/review/evidence-to-gate-report-cross-links-review.md`: done
- Direct evidence -> gate -> report cross-link columns: deferred
- Future acceptance requires a single workflow parent before cross-stage links are claimed
- This is a review-only gate, not a migration, endpoint, dashboard behavior, or workflow orchestration change

### Phase 23 - Single Workflow Parent Review v0

- `docs/review/single-workflow-parent-review.md`: done
- Reusing `agent_runs` as the workflow parent: rejected
- Future `workflow_runs` table direction: accepted for a later implementation gate
- This is a review-only gate, not a migration, endpoint, dashboard behavior, or workflow orchestration change

### Phase 24 - WorkflowRun Schema v0

- `workflow_runs` table in `db/init/001_schema.sql`: done
- `db/migrations/007_workflow_runs.sql`: done
- Workflow parent status boundary: done
- Workflow execution endpoints, child `workflow_run_id` links, and dashboard behavior: not implemented in this phase

### Phase 25 - WorkflowRun Metadata Persistence v0

- `POST /workflow-runs`: done
- `GET /workflow-runs`: done
- WorkflowRun route, schemas, and repository methods: done
- Workflow orchestration, child `workflow_run_id` links, and dashboard behavior: not implemented in this phase

### Phase 26 - WorkflowRun Dashboard Table v0

- `GET /ops/dashboard` shows workflow-run metadata rows: done
- Dashboard copy labels the table as metadata-only and not workflow execution: done
- Workflow orchestration and child `workflow_run_id` links: not implemented in this phase

### Phase 27 - WorkflowRun Child-link Review v0

- `docs/review/workflow-run-child-link-review.md`: done
- Child `workflow_run_id` columns: deferred until a workflow execution boundary exists
- This is a review-only gate, not a migration, endpoint, dashboard behavior, or orchestration change

### Phase 28 - Deterministic Workflow Execution Preview v0

- `POST /workflow-runs/execute-preview`: done
- Parent `workflow_runs` row is created before deterministic execution and updated after completion or failure: done
- Deterministic retrieval -> evidence -> gate -> report preview sequence: done
- Child records are correlated with `workflow_trace_id`: done
- Child `workflow_run_id` columns were added in Phase 29
- Semantic retrieval, embeddings, LLM calls, external search, and free-form final answer generation: not implemented

### Phase 29 - WorkflowRun Child-record Links v0

- `workflow_run_id` on `retrieval_runs`: done
- `workflow_run_id` on `evidence_ledger_entries`: done
- `workflow_run_id` on `noise_gate_records`: done
- `workflow_run_id` on `report_records`: done
- `db/migrations/008_child_workflow_run_ids.sql`: done
- `POST /workflow-runs/execute-preview` attaches deterministic child records to its parent workflow run: done
- Direct evidence -> gate -> report foreign-key links, autonomous workflow execution, semantic retrieval, embeddings, LLM calls, external search, and free-form final answer generation: not implemented

### Phase 30 - WorkflowRun Child Inspection Surface v0

- `GET /workflow-runs/{id}`: done
- Response returns workflow parent, linked retrieval runs, Evidence Ledger entries, Noise Gate records, Report records, and summary counts: done
- It inspects existing local child links; it does not add direct evidence -> gate -> report foreign-key links or autonomous workflow execution

Not implemented yet:

- file upload parsing
- robust PDF extraction
- persisted chunks
- autonomous workflow execution endpoints
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

After WorkflowRun Child Inspection Surface v0, the next phase should improve cross-stage lineage carefully without overstating the runtime:

- review whether direct evidence -> gate -> report links are now justified
- keep the links inspectable without introducing LLM calls, dashboard polish, semantic retrieval, or free-form answer generation
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
