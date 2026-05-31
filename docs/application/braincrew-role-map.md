# Braincrew Role Map

Status: Phase 10 application artifact.

Primary application narrative: FDE-first, targeting Forward Deployed Engineer.

Secondary / long-term narrative: Product Engineer.

Sources checked on 2026-05-30:

- https://brain-crew.com/apply/forward-deployed-engineer
- https://brain-crew.com/apply/product-engineer
- https://brain-crew.com/fields/product/deep-docurator/

## Positioning

NoiseProof Agent is not a trading bot.

It is a small service that shows how I define a messy customer-like data problem, design an evidence-first RAG/Agent workflow, implement the service skeleton, log runs and failures, and explain technical decisions.

## FDE-first Mapping

| Braincrew FDE signal | NoiseProof evidence | Artifact |
|---|---|---|
| Customer requirement interpretation | messy market intelligence framed as unsupported-answer prevention | `docs/product-brief.md` |
| Solution design and implementation | FastAPI service, PostgreSQL schema, phase-gated workflow | `docs/architecture.md` |
| RAG and Agent interest | retrieval, Evidence Ledger, Noise Gate, report preview | `README.md` |
| Logging and operations | agent runs, failure cases, retrieval runs, ops dashboard | `GET /ops/dashboard` |
| CI/CD and maintainability | GitHub Actions CI, migration runner, and repeatable smoke checks | `.github/workflows/ci.yml`, `docs/runbook.md`, `docs/review/fresh-db-api-smoke-verification.md` |
| Technical decision documentation | ADRs for RAG, stack, Evidence Ledger, non-trading, human approval | `docs/adr/*` |

## Product Engineer Secondary Mapping

| Product Engineer signal | Current evidence | Boundary |
|---|---|---|
| Full-stack service design | API service and operations dashboard exist | Next.js app is not implemented |
| Infrastructure judgment | Docker Compose DB, migration runner, CI, and fresh migrated Docker DB API smoke exist | hosted deployment is not claimed |
| Product surface ownership | dashboard and docs explain workflow | not a polished product UI |
| RAG/Agent platform interest | phased retrieval/evidence/gate/report workflow | no LLM or embeddings yet |

## Runtime Proof Surfaces

External-reader proof path: `docs/review/external-reader-proof-path.md`.

Use this 5-minute path first when a reviewer needs the shortest repository-native route through the evidence chain. It is not hosted deployment evidence, not automatic failure-case creation, and not complete workflow failure causality.

README proof-marker archive: `docs/review/readme-proof-marker-archive.md`.

Use this only when a reviewer wants source-level provenance for legacy README proof markers after README scanability cleanup. It is not product runtime evidence, not hosted deployment evidence, not automatic failure-case creation, and not complete workflow failure causality.

The newest local runtime evidence is:

- Migration runner fresh DB verification: `docs/review/migration-runner-fresh-db-verification.md`
- Fresh DB API smoke verification: `docs/review/fresh-db-api-smoke-verification.md`
- Failure-case persistence smoke: `docs/review/failure-case-persistence-smoke-verification.md`
- Agent-run failure linkage smoke: `docs/review/agent-run-failure-linkage-smoke-verification.md`
- Workflow failure linkage smoke: `docs/review/workflow-failure-linkage-smoke-verification.md`
- Failure-case workflow linkage review: `docs/review/failure-case-workflow-linkage-review.md`
- Failure-case draft preview: `POST /failure-cases/draft-preview`
- Failure-case draft preview smoke: `docs/review/failure-case-draft-preview-smoke-verification.md`
- Failure-case draft manual handoff smoke: `docs/review/failure-case-draft-manual-handoff-smoke-verification.md`
- Failure-case draft fresh DB handoff smoke: `docs/review/failure-case-draft-fresh-db-handoff-smoke-verification.md`
- Workflow failure-to-draft smoke: `docs/review/workflow-failure-to-draft-smoke-verification.md`
- Failure-case workflow parent linkage fresh DB proof: `docs/review/failure-case-workflow-parent-linkage-fresh-db-verification.md`
- Failure-case dashboard manual workflow parent link: `GET /ops/dashboard`
- Failure-case fresh DB dashboard Workflow Parent proof: `docs/review/failure-case-workflow-parent-linkage-fresh-db-dashboard-smoke-verification.md`
- Failure-case workflow parent proof index: `docs/review/failure-case-workflow-parent-linkage-proof-index.md`

These show a fresh migrated Docker DB can run the local service path for `/health`, `/ops/summary`, `POST /documents`, and `GET /documents`.

The failure-case persistence smoke shows the service can store and list a `parser_timeout` failure record and reflect the count in `/ops/summary`.

The linked failure-case proof shows a manually created `failure_cases` row can retain `agent_run_id` linkage to a failed `agent_runs` row.

The failed workflow parent proof shows a route-level test fixture can make a downstream workflow stage raise and leave the deterministic workflow parent as `failed`.

The historical failure-case workflow linkage review explains why workflow parent linkage was deferred before the manual linkage path existed. manual workflow parent linkage now exists for reviewer-confirmed failure cases, while automatic failure-case creation remains unclaimed.

The failure-case draft preview can turn workflow failure evidence into a human-confirmed draft payload with `preview_only_not_persisted`. It is a preparation boundary only; it does not persist the failure case, classify incidents automatically, or prove complete workflow failure causality.

The draft-preview smoke is a route-level smoke that confirms `preview_only_not_persisted`, `human_confirmation_required`, and unchanged `failure_cases`. It is not fresh Docker DB evidence.

The manual handoff smoke shows a reviewer-controlled step: `draft.fix_status from draft to open`, then `POST /failure-cases`. That proves the existing endpoints can carry a human-confirmed draft into persistence, but it is not automatic failure-case persistence.

The fresh migrated Docker DB handoff proof verifies the same manual path through a real FastAPI process and PostgreSQL repository, ending with `ops_failure_case_count: 1`. It is not hosted deployment evidence.

The workflow failure-to-draft smoke is a route-level smoke showing that a failed deterministic workflow parent can feed `POST /failure-cases/draft-preview` while preserving `preview_only_not_persisted` and unchanged `failure_cases`. This is not automatic failure-case creation, not automatic persistence, and not complete workflow failure causality.

The workflow parent linkage fresh DB proof verifies that a manually persisted `failure_cases` row can retain `workflow_run_id` through FastAPI and PostgreSQL, and that `/ops/summary` reports one linked failure case afterward. This is local runtime proof for manual workflow parent linkage only; it is not hosted deployment evidence, not automatic failure-case creation, and not complete workflow failure causality.

The dashboard manual workflow parent link surfaces the same manual `workflow_run_id` value in the Failure Cases table and links to `/workflow-runs/{id}`. It is a reviewer navigation aid over persisted manual provenance, not automatic failure-case creation or automatic failure detection.

The fresh DB dashboard Workflow Parent proof verifies that the same manual dashboard link appears through a fresh migrated Docker DB and real FastAPI process, with `dashboard_contains_workflow_link: true`. This is local dashboard smoke evidence only; it is not hosted deployment evidence, not automatic failure-case creation, and not complete workflow failure causality.

The workflow parent proof index gives the reader path for this proof chain: schema boundary, manual persistence, fresh DB persistence, dashboard surfacing, fresh DB dashboard proof, and application-facing boundary. Use it first when a reviewer asks how these artifacts fit together.

Boundary: the DB smoke checks are fresh migrated Docker DB evidence. The workflow failure linkage smoke is not fresh Docker DB evidence. None of these proofs are hosted deployment evidence, production migration orchestration, rollback proof, automatic failure detection, complete workflow failure causality, or external customer validation.

Short boundary phrase: not automatic failure detection.

Second boundary phrase: not complete workflow failure causality.

## DeepDocurator Alignment

Braincrew product surface around DeepDocurator emphasizes document analysis, parser/chunk strategy iteration, and RAG bottlenecks.

NoiseProof aligns with that problem shape by making these boundaries visible:

- Document Profiler v0
- Parser Adapter Stubs
- Chunk Strategy Experiment v0
- Retrieval v0
- Evidence Ledger Preview
- Noise Gate Preview

The difference is domain framing: NoiseProof applies the shape to messy market intelligence and claim-bounded reporting.

## Unproven

- production document extraction quality
- real customer deployment
- semantic retrieval quality
- external user validation
- Braincrew review outcome
- Product Engineer-level infrastructure ownership

## Application Message

Use this message:

```text
저는 고객의 지저분한 데이터 환경에서 근거 없는 AI 답변이 통과하지 못하게 만드는 RAG/Agent 시스템에 관심이 있습니다.

NoiseProof Agent는 PDF, CSV, 웹 문서, 메모처럼 형태가 제각각인 시장 데이터를 수집하고, 문서 프로파일링, chunk 전략 비교, retrieval 평가, Evidence Ledger, Noise Gate를 통해 출처와 한계가 붙은 리포트 preview를 만드는 작은 데이터 에이전트입니다.

이 프로젝트는 트레이딩 봇이 아니라, 실제 업무 환경에서 노이즈와 모순을 견디는 데이터 에이전트를 작게 구현하는 시도입니다.
```
