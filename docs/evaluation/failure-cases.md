# Failure Cases

Status: Phase 10 initial failure record.

NoiseProof treats failures as evidence. A small system that records where it cannot answer is better than a broad demo that always sounds confident.

## Current Failure Classes

| Failure type | Current handling | Status |
|---|---|---|
| `runtime_verification` | Docker DB runtime smoke inserted a sample failure case record during local verification. | recorded |
| `parse_warning` | parser stubs return structured warnings and failure-case candidates. | implemented |
| `retrieval_no_results` | retrieval run records `status: no_results` and missing evidence count. | implemented |
| `unsupported_claim` | Evidence Ledger Preview can produce unsupported or blocked entries. | implemented |
| `contradiction_candidate` | contradiction language is surfaced as contradicted or revision-needed. | implemented |
| `trading_advice_drift` | buy/sell questions are blocked before report output. | implemented |

## No LLM Boundary

No LLM is currently called.

That means these failure records are deterministic preview boundaries, not model judgment.

## Example: Buy/Sell Drift

Question:

```text
Should I buy this stock?
```

Expected behavior:

- collection plan includes user intent check
- Evidence Ledger Preview can produce a blocked entry
- Noise Gate blocks final response allowance
- Report Preview returns fallback message and required revisions

## Example: No Evidence

Question:

```text
Was semiconductor backlog reduced?
```

If retrieval candidates are empty, the system should not invent an answer.

Expected behavior:

- Evidence Ledger Preview creates a blocked entry
- limitation mentions that no retrieval candidates were provided
- report generation is blocked by the gate

## Next Failure Records To Add

- actual PDF extraction failure
- malformed CSV parse failure
- HTML boilerplate/noise extraction failure
- conflicting source dates
- high-confidence single-source claim downgrade
- dashboard visibility regression
