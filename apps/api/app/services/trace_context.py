from __future__ import annotations

import re
import secrets

TRACE_CONTEXT_BOUNDARY = "local_header_propagation_no_distributed_tracing"
_TRACEPARENT_RE = re.compile(r"^00-([0-9a-f]{32})-([0-9a-f]{16})-([0-9a-f]{2})$")


def resolve_traceparent(incoming_traceparent: str | None) -> tuple[str, str]:
    if incoming_traceparent and _is_valid_traceparent(incoming_traceparent):
        return incoming_traceparent, "incoming_traceparent"
    if incoming_traceparent:
        return _generate_traceparent(), "invalid_traceparent_generated_fallback"
    return _generate_traceparent(), "generated_traceparent"


def _is_valid_traceparent(traceparent: str) -> bool:
    match = _TRACEPARENT_RE.match(traceparent)
    if not match:
        return False
    trace_id, parent_id, _flags = match.groups()
    return trace_id != "0" * 32 and parent_id != "0" * 16


def _generate_traceparent() -> str:
    return f"00-{secrets.token_hex(16)}-{secrets.token_hex(8)}-01"
