FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APERTUS_EVIDENCE_DB=/app/demo.db \
    APERTUS_WEB_HOST=0.0.0.0 \
    APERTUS_WEB_PORT=8787

COPY pyproject.toml ./
COPY src ./src
RUN python -m pip install --no-cache-dir --no-build-isolation .

COPY data ./data
RUN apertus-evidence --db /app/demo.db ingest /app/data/sample-policy.md \
    && useradd --system --uid 10001 appuser \
    && chown -R appuser:appuser /app

USER appuser
EXPOSE 8787

HEALTHCHECK --interval=10s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8787/health', timeout=2).read()"

CMD ["apertus-evidence-web"]
