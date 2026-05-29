# Meaningful Information Collection

Status: implementation note
Source context: adapted from the `svy04.github.io` research note with the same title
Implemented boundary: Phase 5.5 - Collection Plan Preview v0

## Why This Exists

Before NoiseProof can remove noise or generate an Evidence Ledger, it must decide what information roles a question needs.

The missing boundary is:

```text
question -> collection plan preview -> retrieval candidates -> Evidence Ledger
```

This does not mean collecting more information. It means collecting role-diverse information that can change what the system may claim, doubt, ask, or block.

## Information Is Not Evidence Yet

NoiseProof separates these terms:

| Term | Meaning |
|---|---|
| raw information | anything collected or provided |
| candidate information | information that might matter to the question |
| evidence | candidate information tied to a claim, source span, and limitation |
| signal | evidence or pattern that changes what can be said |
| noise | related-looking information that does not change the allowed claim |

Collection Plan Preview does not produce evidence. It only defines the roles needed before evidence work starts.

## Required Roles

Phase 5.5 supports these role labels:

```text
direct_support
contradiction
quantitative_anchor
timeline_anchor
definition_anchor
source_quality_check
missing_data_signal
scope_boundary
user_intent_check
```

## Implemented Output

`POST /collection-plans/preview` returns:

```text
question
information_need
possible_claims
required_roles
source_types_to_check
minimum_evidence_needed
known_risks
stop_conditions
warnings
```

## Current Boundaries

Phase 5.5 does not:

- call LLMs
- search external sources
- expand retrieval
- persist collection plans
- generate Evidence Ledger entries
- run a Critic / Noise Gate
- generate final answers or reports
- judge truth

## One-Sentence Principle

NoiseProof should not collect more information to sound smarter.

It should collect the minimum role-diverse information needed to decide what the agent is allowed to claim, doubt, ask, or block.
