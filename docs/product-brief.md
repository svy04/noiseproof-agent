# Product Brief: NoiseProof Agent

## 1. User

The target user is a market researcher, analyst, founder, operator, or forward-deployed engineer working with messy market intelligence inputs.

They are not asking for a trading recommendation. They are trying to understand what the available evidence supports, which sources conflict, and which conclusions are not ready to trust.

## 2. Messy Data Problem

Market intelligence inputs are rarely clean.

Common input types:

- PDF reports
- CSV exports
- HTML pages and URLs
- news articles
- market memos
- copied notes
- public filings
- internal research snippets

Common failures:

- source dates are unclear
- numbers and narrative disagree
- documents contain duplicated or low-quality text extraction
- one source uses a different timeframe than another
- confident claims appear without evidence spans
- retrieval quality changes depending on chunk strategy
- failed questions are not recorded for later improvement

## 3. Why LLM Answers Fail Here

LLMs can produce a fluent answer before the evidence trail is ready.

In this domain, that creates several risks:

- unsupported claims sound plausible
- contradictions get smoothed over
- source recency disappears
- quantitative and qualitative signals get mixed
- missing data is hidden behind confident language
- market intelligence drifts into trading advice

The problem is not that the model cannot write. The problem is that the system can let unsupported writing pass.

## 4. Why Evidence-First Is Better Than Answer-First

NoiseProof Agent는 똑똑한 답변보다 근거 없는 답변이 통과하지 못하게 만드는 데이터 에이전트다.

Evidence-first means the system must produce inspectable evidence before it produces a final report.

The intended order is:

```text
source profile -> chunk experiment -> retrieval run -> evidence ledger -> critic gate -> claim-bounded report
```

This makes the final report easier to review because every strong claim should be linked to source ids, evidence spans, confidence, limitations, and contradictions.

## 5. Why This Is Not a Trading Bot

NoiseProof Agent does not decide whether to buy or sell an asset.

It does not generate:

- buy/sell signals
- target prices
- expected returns
- automatic orders
- stock recommendations
- financial advice

Trading-bot framing asks:

```text
Should I buy?
Should I sell?
How much return will this make?
```

NoiseProof framing asks:

```text
What happened?
What evidence supports it?
Which sources conflict?
Which claims are weak?
What data is missing?
Why should this conclusion not be trusted yet?
```

If a user asks for trading functionality, the system should refuse that direction and reframe the request into evidence-based market intelligence.

## 6. MVP

The MVP must prove a small but inspectable workflow:

1. ingest PDF, CSV, URL/HTML, and markdown memo inputs
2. generate a document profile
3. compare three chunk strategies
4. run source-linked retrieval
5. create an Evidence Ledger
6. block unsupported claims
7. surface contradictions
8. generate a claim-bounded report
9. record agent runs and failure cases
10. show a basic operations dashboard
11. run locally with Docker Compose
12. include CI, README, architecture, ADRs, runbook, and evaluation docs

Day 1 only defines the repo, product brief, architecture, ADRs, and database compose target.

## 7. Explicitly Out of Scope

Out of scope for MVP:

- trading signals
- order execution
- return prediction
- financial advice
- real-time market data feed
- large-scale data lake
- multi-tenant SaaS
- reinforcement-learning trader
- polished dashboard before logs and failure cases work
- complex multi-agent framework before explicit workflow works

## 8. Working Evidence

The project starts to count as working only when it has visible artifacts, not just a persuasive story.

Required evidence:

- local stack runs
- sample messy dataset exists
- document profile is generated
- chunk strategies can be compared
- retrieval returns source ids
- Evidence Ledger exists before final answer
- unsupported claims are blocked
- contradictions are surfaced
- trading advice is refused or reframed
- each agent run leaves a trace
- failure cases are recorded
- operations dashboard shows runs and failures
- README and architecture are understandable without explanation

## 9. Braincrew Mapping

Primary application target:

```text
Forward Deployed Engineer
```

NoiseProof Agent is meant to show:

- customer-like problem definition
- messy data handling
- RAG and agent workflow design
- full-stack service planning
- deployment-aware local stack design
- logging and failure tracking
- technical decision documentation

Secondary / long-term target:

```text
Product Engineer
```

The project should still be built to Product Engineer-level evidence, but the first application narrative is FDE-first because it is closer to customer environment interpretation, solution design, and operating real services.
