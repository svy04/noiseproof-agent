FROM python:3.13-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

RUN pip install --no-cache-dir uv

COPY apps/api/pyproject.toml apps/api/uv.lock /app/apps/api/

WORKDIR /app/apps/api
RUN uv sync --frozen --no-dev

COPY apps/api /app/apps/api
COPY packages /app/packages

EXPOSE 8000

CMD uv run uvicorn app.main:create_app --factory --host 0.0.0.0 --port 8000
