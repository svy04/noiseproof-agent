# CI Node24 Action Version Refresh

Status: implemented

Phase marker: ci node24 action version refresh v0

## Goal

Refresh GitHub Actions JavaScript action references to current upstream refs after the repository proved that the workflows run under the forced Node.js 24 runtime but still emit a forced-runtime annotation.

This is workflow runtime compatibility only. It is not API behavior, product runtime evidence, hosted deployment evidence, external reviewer feedback, customer validation, or product-complete evidence.

## Source Check

The version choice was based on upstream tag check commands, not package-manager guessing:

```text
git ls-remote --tags https://github.com/actions/checkout.git
git ls-remote --tags https://github.com/actions/setup-python.git
git ls-remote --tags https://github.com/astral-sh/setup-uv.git
git ls-remote --tags https://github.com/actions/upload-artifact.git
```

Observed selected current refs:

```text
actions/checkout: v6
actions/setup-python: v6
astral-sh/setup-uv: v8
astral-sh/setup-uv exact ref: v8.2.0
actions/upload-artifact: v7
```

Primary background source already used for the runtime deprecation gate:

```text
https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
```

## Changed References

```text
.github/workflows/ci.yml
  actions/checkout@v6
  actions/setup-python@v6
  astral-sh/setup-uv@v8.2.0

.github/workflows/external-feedback-screen.yml
  actions/checkout@v6
  actions/setup-python@v6
  actions/upload-artifact@v7
```

## Verification Boundary

The local test only verifies repository configuration and proof-surface consistency. The remote annotation result remains unverified until the next push runs on GitHub Actions.

If the next remote run still emits a Node.js action runtime annotation, record that result separately rather than claiming the warning is gone.

## Boundary

```text
workflow runtime compatibility only
remote annotation result remains unverified until the next push
not API behavior
not product runtime evidence
not hosted deployment evidence
not external reviewer feedback
not customer validation
not product-complete
```
