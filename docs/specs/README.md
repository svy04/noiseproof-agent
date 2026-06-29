# Short-term Specs

Every non-trivial NoiseProof gate starts here after reading:

```text
docs/MASTER-SPEC.md
docs/GOAL.md
```

Short-term specs translate the master spec into a single implementable gate.
They prevent the project from drifting into impressive but uninspectable work.

## Naming

Use:

```text
YYYY-MM-DD-<gate-slug>.md
```

## Required Shape

Each spec must include:

```text
title:
status:
date:
target_gate:
current_repo_state:
sources_to_absorb:
non_goals:
implementation_scope:
data_or_api_contract:
tests:
docs_to_update:
stop_conditions:
claim_boundaries:
next_gate_if_passed:
```

## Gate Rule

The agent may implement only the current spec. If research suggests a better
direction, update the spec first and keep the change bounded.

If implementation diverges from the spec, stop and record:

```text
planned_path:
actual_state:
blocking_mismatch:
why_this_blocks_the_gate:
minimum_action_to_resume:
```

## Boundary

This folder is not a backlog dump. It is the local contract for the next small
piece of work.
