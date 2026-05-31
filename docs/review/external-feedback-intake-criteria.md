# External Feedback Intake Criteria

Status: feedback qualification criteria.

Phase marker: external feedback intake criteria v0.

Label: External feedback intake criteria.

This artifact defines what can and cannot count toward the next gate:

```text
external reviewer feedback v0
```

Current public request issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

## Purpose

The project now has a request surface for outside critique, but a request is not feedback.

This document prevents self-authored proof, empty comments, or polite acknowledgements from being counted as external reviewer feedback.

## Qualifying Feedback

A comment can count as qualifying feedback only if all of these are true:

```text
reviewer is not the repository owner
specific artifact inspected
actionable critique
claim boundary or missing evidence is named
public URL or captured source is available
```

The feedback does not need to be positive. A critical comment is useful if it names what was inspected and what should change.

Examples of qualifying feedback:

- a reviewer says `docs/review/external-reader-proof-path.md` is too long and names the section that blocks scanning
- a reviewer says the Braincrew role map overstates Product Engineer evidence and explains why
- a reviewer says the screenshot proof is useful but still too self-authored to count as external validation
- a reviewer names one missing artifact required before they would trust the portfolio

## Non-qualifying Feedback

These must not count as external reviewer feedback:

```text
self-authored comment
request for feedback
empty acknowledgement
generic praise without inspected artifacts
private memory without source capture
bot-generated summary
automated CI status
issue opened by the repository owner
comment that does not name an artifact or claim
```

Examples of non-qualifying feedback:

- `Looks good`
- `Nice project`
- a self-authored comment restating the proof path
- a request asking others to review
- a CI success check

## Intake Record Shape

When a qualifying comment appears, the follow-up artifact should record:

```text
review source URL
reviewer role
evidence inspected
main critique
claim boundary raised
missing evidence
accepted changes
rejected changes with reason
what remains unproven
```

## Current State

External reviewer feedback remains pending.

Issue #1 is open, but no substantive external comment has been accepted into the proof path yet.

## Allowed Claim

NoiseProof Agent has explicit intake criteria for deciding whether a public comment qualifies as external reviewer feedback.

## Boundary

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not hosted deployment evidence.

This does not prove that any reviewer has inspected the repository.

This does not prove that the portfolio is stronger yet.

## Next Gate

The next gate remains:

```text
external reviewer feedback v0
```
