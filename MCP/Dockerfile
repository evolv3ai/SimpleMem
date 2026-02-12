FROM python:3.12-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

COPY requirements.txt .
RUN uv venv /app/.venv && \
    uv pip install --python /app/.venv/bin/python -r requirements.txt

# ---

FROM python:3.12-slim

WORKDIR /app

COPY --from=builder /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

COPY server/ server/
COPY config/ config/
COPY frontend/ frontend/
COPY run.py .

RUN mkdir -p /app/data

ENV LLM_PROVIDER=openrouter
ENV DATA_DIR=/app/data
ENV LANCEDB_PATH=/app/data/lancedb
ENV USER_DB_PATH=/app/data/users.db

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/api/health')" || exit 1

CMD ["uvicorn", "server.http_server:app", "--host", "0.0.0.0", "--port", "8000"]
