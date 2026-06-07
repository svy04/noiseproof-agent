from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager
from typing import Any

from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.sdk.trace.export.in_memory_span_exporter import (
    InMemorySpanExporter,
)

LOCAL_OTEL_SPAN_EXPORT_BOUNDARY = (
    "local_in_memory_otel_span_export_not_distributed_tracing"
)
DISABLED_OTEL_SPAN_EXPORT_BOUNDARY = "disabled_no_span_export"


class LocalOtelSpanRecorder:
    def __init__(self, *, service_name: str, enabled: bool) -> None:
        self.enabled = enabled
        self._service_name = service_name
        self._exporter: InMemorySpanExporter | None = None
        self._tracer = None
        if enabled:
            resource = Resource.create({"service.name": service_name})
            provider = TracerProvider(resource=resource)
            exporter = InMemorySpanExporter()
            provider.add_span_processor(SimpleSpanProcessor(exporter))
            self._exporter = exporter
            self._tracer = provider.get_tracer("noiseproof-agent-api.local")

    @contextmanager
    def request_span(
        self,
        *,
        method: str,
        path: str,
        traceparent: str,
        trace_source: str,
    ) -> Iterator[Any]:
        if not self.enabled or self._tracer is None:
            yield None
            return

        span_name = f"HTTP {method.upper()} {path}"
        with self._tracer.start_as_current_span(span_name) as span:
            span.set_attribute("http.request.method", method.upper())
            span.set_attribute("url.path", path)
            span.set_attribute("noiseproof.http_traceparent", traceparent)
            span.set_attribute("noiseproof.http_trace_source", trace_source)
            span.set_attribute("noiseproof.otel_boundary", LOCAL_OTEL_SPAN_EXPORT_BOUNDARY)
            yield span

    def finish_request_span(self, span: Any, *, status_code: int) -> None:
        if span is None:
            return
        span.set_attribute("http.response.status_code", status_code)

    def snapshot(self) -> dict[str, Any]:
        if not self.enabled or self._exporter is None:
            return {
                "span_export_enabled": False,
                "span_export_boundary": DISABLED_OTEL_SPAN_EXPORT_BOUNDARY,
                "span_count": 0,
                "spans": [],
                "non_claims": _non_claims(),
            }

        spans = self._exporter.get_finished_spans()
        return {
            "span_export_enabled": True,
            "span_export_boundary": LOCAL_OTEL_SPAN_EXPORT_BOUNDARY,
            "span_count": len(spans),
            "spans": [_serialize_span(span) for span in spans],
            "non_claims": _non_claims(),
        }


def build_otel_span_recorder(*, service_name: str, enabled: bool) -> LocalOtelSpanRecorder:
    return LocalOtelSpanRecorder(service_name=service_name, enabled=enabled)


def _serialize_span(span: Any) -> dict[str, Any]:
    context = span.get_span_context()
    return {
        "name": span.name,
        "trace_id": f"{context.trace_id:032x}",
        "span_id": f"{context.span_id:016x}",
        "attributes": dict(span.attributes or {}),
    }


def _non_claims() -> dict[str, bool]:
    return {
        "distributed_tracing": False,
        "external_collector": False,
        "hosted_observability": False,
        "production_monitoring": False,
        "product_complete": False,
    }
