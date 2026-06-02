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
| RAG/Agent platform interest | phased retrieval/evidence/gate/report workflow plus caller-provided chunk embedding endpoint | no LLM, embedding generation, or semantic retrieval yet |

## Runtime Proof Surfaces

External-reader proof path: `docs/review/external-reader-proof-path.md`.

README proof-marker archive: `docs/review/readme-proof-marker-archive.md`.

These are the 5-minute path and source-level provenance path, not product runtime evidence, hosted deployment evidence, automatic failure-case creation, or complete workflow failure causality.

The runtime proof links below are local proof surfaces, not hosted deployment evidence.

Runtime proof summary:

- Migration/API: migration runner, fresh DB API smoke, and local Docker DB runtime checks exist for bounded service paths only.
- Failure/provenance: manual failure-case persistence, workflow parent linkage, and dashboard proof keep human handoff visible; not automatic failure-case creation, not automatic failure detection, and not complete workflow failure causality.
- Preserved proof markers: failure-case persistence smoke; linked failure-case proof; failed workflow parent proof; historical failure-case workflow linkage review; human-confirmed draft payload; route-level smoke; draft.fix_status from draft to open; fresh migrated Docker DB handoff proof; workflow failure-to-draft smoke; workflow parent linkage fresh DB proof; dashboard manual workflow parent link; fresh DB dashboard Workflow Parent proof; workflow parent proof index; reader path; manual workflow parent linkage now exists.
- Preserved boundary markers: preview_only_not_persisted; not fresh Docker DB evidence; not automatic failure-case persistence; automatic failure-case creation remains unclaimed.
- Upload path: intake manifest, parsed-document metadata, chunk persistence/handoff, and document-scoped retrieval persistence are locally smoke-tested with no raw file storage, no robust PDF claim, no semantic retrieval, and no hosted deployment evidence.
- Preserved upload proof markers: upload intake manifest runtime smoke; upload intake manifest persistence runtime smoke; upload parsed document persistence runtime smoke.
- Preserved upload boundary markers: not raw file storage.
- Retrieval handoffs: linked Evidence Ledger, Noise Gate, and Report endpoints have local Docker runtime smoke; no external feedback, LLM judgment, free-form final answer, or automatic failure-case creation.
- Caller-provided chunk embedding endpoint: `POST /chunks/{chunk_id}/embeddings`, `GET /chunks/{chunk_id}/embeddings`, generated-claim rejection `400`, and pgvector normalization are locally smoke-tested; no embedding generation, semantic retrieval, vector search quality claim, or hosted deployment evidence.

Detailed proof links:

- `docs/review/failure-case-workflow-parent-linkage-proof-index.md`
- `docs/review/uploaded-file-chunk-persistence-application-refresh.md`
- `docs/review/uploaded-file-chunk-persistence-handoff-application-refresh.md`
- `docs/review/uploaded-file-retrieval-persistence-runtime-smoke.md`
- `docs/review/retrieval-run-linked-evidence-ledger-runtime-smoke.md`
- `docs/review/retrieval-run-linked-noise-gate-runtime-smoke.md`
- `docs/review/retrieval-run-linked-report-runtime-smoke.md`
- `docs/review/embedding-endpoint-runtime-smoke.md`

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
