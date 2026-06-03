# CI Node24 Actions Runtime Opt-in

Status: implemented

Phase marker: ci node24 actions runtime opt-in v0

## Goal

Opt the GitHub Actions workflows into the Node.js 24 JavaScript action runtime after remote CI reported:

```text
Node.js 20 actions are deprecated
```

This is workflow runtime compatibility only. It is not application behavior, product runtime evidence, hosted deployment evidence, external reviewer feedback, or customer validation.

## Changed Workflows

```text
.github/workflows/ci.yml
.github/workflows/external-feedback-screen.yml
```

Both workflows now set:

```yaml
env:
  FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: "true"
```

## Expected Verification

The next remote push should show whether these JavaScript actions still run under the Node.js 24 opt-in:

```text
actions/checkout@v4
actions/setup-python@v5
astral-sh/setup-uv@v5
actions/upload-artifact@v4
```

## Boundary

```text
workflow runtime compatibility only
not API behavior
not product runtime evidence
not hosted deployment evidence
not external reviewer feedback
not malware scanning evidence
not product-complete
```
