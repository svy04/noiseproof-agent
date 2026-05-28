# ADR 004: Why This Is Not a Trading Bot

## Status

Accepted

## Context

NoiseProof Agent uses market documents and market intelligence examples. That can easily drift into trading-bot framing: signals, target prices, return prediction, or financial advice.

That direction would weaken the project. The intended portfolio evidence is messy data handling, RAG/agent workflow design, claim boundaries, logging, evaluation, and operational clarity.

## Decision

NoiseProof Agent will not build trading functionality.

Do not build:

- buy/sell signals
- automatic order execution
- return prediction
- stock recommendation
- financial advice
- real-time trading system
- reinforcement-learning trader

If a user asks for trading advice, the system should refuse or reframe into evidence-based market intelligence.

Allowed framing:

```text
What happened?
What evidence supports it?
Which sources conflict?
Which claims are weak?
What data is missing?
Why should this conclusion not be trusted yet?
```

## Alternatives considered

1. Build a trading assistant
   - More attention-grabbing, but legally and ethically riskier and less aligned with evidence-first system design.
2. Build a prediction dashboard
   - Still risks return and target-price framing before evidence handling is proven.
3. Avoid market data entirely
   - Safer, but less connected to the user's existing market-intelligence interests and portfolio story.

## Consequences

- The product remains an intelligence and evidence system.
- Reports must include limitations and avoid financial advice.
- The Critic Agent must detect trading-advice drift.
- Some flashy demo ideas are intentionally rejected.

## What would change this decision

This decision would change only if the project were redesigned under proper legal, compliance, and domain-supervision constraints. That is explicitly outside the MVP.
