FROM python:3.10-slim

WORKDIR /opt/dagster/app

COPY pyproject.toml ./

RUN pip install --no-cache-dir uv

RUN uv sync --all-extras

# Ensure the .venv/bin directory is in PATH so dagster command can be found
ENV PATH="/opt/dagster/app/.venv/bin:$PATH"

COPY demo_code_location ./demo_code_location
COPY demo_code_location_tests ./demo_code_location_tests

CMD ["dagster", "api", "grpc", "-h", "0.0.0.0", "-p", "4001", "-m", "demo_code_location"]
