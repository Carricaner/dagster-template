## Prerequisites

- Python 3.12
- uv (Global)
- Dagster

## Setup

- Install all the dependencies

    ```shell
    uv sync --all-extras
    ```

- Activate the environment

    ```shell
    source .venv/bin/activate
    ```

## Usage

### Add a new code location

1. Create a new code location

  ```shell
  dagster project scaffold --name <new-code-location-name>
  ```

2. Add a new line in `workspace.yaml` according to the project name.

  ```yaml
  load_from:
    - python_module: demo_code_location.definitions
    - python_module: with_openai.definitions
  ```

## Commands

- Start a local deployment of Dagster

    ```shell
    dagster dev -w env/dev/workspace.yaml -p <port>
    ```

## Notes

- Code Location
    - use only `pyproject.toml` and don't use `setup.py` to maintain single source of truth.
    - PEP 517/518 compliant

## References

- uv
    - [uv](https://docs.astral.sh/uv/)
- Dagster
    - [Dagster CLI](https://docs.dagster.io/api/dagster/cli#dagster-project)
    - [workspace.yaml](https://docs.dagster.io/deployment/code-locations/workspace-yaml)
    - [Dagster OSS deployment architecture](https://docs.dagster.io/deployment/oss/oss-deployment-architecture)

