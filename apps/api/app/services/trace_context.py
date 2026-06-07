from __future__ import annotations

from contextvars import ContextVar, Token
import re
import secrets

TRACE_CONTEXT_BOUNDARY = "local_header_propagation_no_distributed_tracing"
_TRACEPARENT_RE = re.compile(r"^00-([0-9a-f]{32})-([0-9a-f]{16})-([0-9a-f]{2})$")
_CURRENT_HTTP_TRACE_CONTEXT: ContextVar[dict | None] = ContextVar(
    "noiseproof_http_trace_context",
    default=None,
)


def resolve_traceparent(incoming_traceparent: str | None) -> tuple[str, str]:
    if incoming_traceparent and _is_valid_traceparent(incoming_traceparent):
        return incoming_traceparent, "incoming_traceparent"
    if incoming_traceparent:
        return _generate_traceparent(), "invalid_traceparent_generated_fallback"
    return _generate_traceparent(), "generated_traceparent"


def set_current_http_trace_context(*, traceparent: str, source: str) -> Token:
    return _CURRENT_HTTP_TRACE_CONTEXT.set(
        {
            "http_traceparent": traceparent,
            "http_trace_source": source,
            "http_trace_context_boundary": TRACE_CONTEXT_BOUNDARY,
            "distributed_tracing": False,
            "opentelemetry_span_export": False,
        }
    )


def reset_current_http_trace_context(token: Token) -> None:
    _CURRENT_HTTP_TRACE_CONTEXT.reset(token)


def get_current_http_trace_context() -> dict:
    context = _CURRENT_HTTP_TRACE_CONTEXT.get()
    if not context:
        return {}
    return dict(context)


def _is_valid_traceparent(traceparent: str) -> bool:
    match = _TRACEPARENT_RE.match(traceparent)
    if not match:
        return False
    trace_id, parent_id, _flags = match.groups()
    return trace_id != "0" * 32 and parent_id != "0" * 16


def _generate_traceparent() -> str:
    return f"00-{secrets.token_hex(16)}-{secrets.token_hex(8)}-01"
