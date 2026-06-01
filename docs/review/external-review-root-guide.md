# External Review Root Guide

Status: external review root guide artifact.

Phase marker: external review root guide v0.

Label: External review root guide.

This artifact records that the repository now has a root-level `CONTRIBUTING.md` dedicated to external review. It reduces GitHub entry friction for reviewers who start from the repository root, but it does not claim that external reviewer feedback has been received.

## Added Surface

```text
CONTRIBUTING.md
```

## Purpose

Root-level GitHub files are easier to find than deep `docs/review/*` paths for people arriving cold. This guide points outside reviewers to:

```text
README.md
docs/review/external-reader-proof-path.md
docs/review/external-reviewer-link-map.md
docs/application/portfolio-index.md
docs/review/external-feedback-intake-criteria.md
https://github.com/svy04/noiseproof-agent/issues/1
```

## What It Asks For

The guide asks reviewers to leave one evidence-referenced comment that names inspected artifacts and addresses one of:

```text
over-stated claim
easiest evidence to inspect
too self-authored or too weak evidence
missing evidence
FDE signal
Product Engineer gap
compression or removal
```

## Allowed Claim

NoiseProof Agent has a root-level external review guide that sends reviewers to the public feedback issue and intake criteria.

## Boundary

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not hosted deployment evidence.

This does not prove that any outside reviewer has inspected the repository.

This does not accept any issue comment into the proof path.

## Next Gate

The next gate remains:

```text
external reviewer feedback v0
```
