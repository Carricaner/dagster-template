## Prerequisites

- Python 3.12
- uv (Global)
- Dagster

## Setup

1. Install all the dependencies

    ```shell
    uv sync --all-extras
    ```

2. Activate the environment

    ```shell
    source .venv/bin/activate
    ```

## Commands

- Create a brand-new code location

    ```shell
    dagster project scaffold --name <brand-new-code-location>
    ```

- Start a local deployment of Dagster

    ```shell
    deagster dev -p <port>
    ```

## Notes

- Code Location
    - use only `pyproject.toml` and don't use `setup.py` to maintain single source of truth.
    - PEP 517/518 compliant
    -

## References

- uv
    - [uv](https://docs.astral.sh/uv/)
- Dagster
    - [Dagster CLI](https://docs.dagster.io/api/dagster/cli#dagster-project)
    - [workspace.yaml](https://docs.dagster.io/deployment/code-locations/workspace-yaml)
    - [Dagster OSS deployment architecture](https://docs.dagster.io/deployment/oss/oss-deployment-architecture)

