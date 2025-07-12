FROM python:3.10-slim

WORKDIR /opt/dagster/app

COPY pyproject.toml ./

RUN pip install --no-cache-dir uv

RUN uv sync --all-extras

# Ensure the .venv/bin directory is in PATH so dagster command can be found
ENV PATH="/opt/dagster/app/.venv/bin:$PATH"

COPY with_openai ./with_openai
COPY with_openai ./with_openai

CMD ["dagster", "api", "grpc", "-h", "0.0.0.0", "-p", "4002", "-m", "with_openai"]
