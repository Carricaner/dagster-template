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

2. Modify corresponding `workspace.yaml` for different envs:
  
  - `dev`
  ```yaml
  load_from:
    - python_module: demo_code_location.definitions
    - python_module: with_openai.definitions
  ```

  - `prod`
  ```yaml
  load_from:
  # Each entry here corresponds to a service in the docker-compose file that exposes user code.
  - grpc_server:
      host: docker_example_user_code
      port: 4000
      location_name: "example_user_code"
  - grpc_server:
      host: demo_code_location
      port: 4001
      location_name: "demo_code_location_uii"
  ```
  and also remember to add a new service in docker-compose.yaml for prod, like:

  ```yaml
    demo_code_location:
    container_name: demo_code_location
    build:
      context: ../../demo-code-location
      dockerfile: Dockerfile
    image: dagster_demo_code_location
    restart: always
    environment:
      DAGSTER_POSTGRES_USER: "postgres_user"
      DAGSTER_POSTGRES_PASSWORD: "postgres_password"
      DAGSTER_POSTGRES_DB: "postgres_db"
      DAGSTER_CURRENT_IMAGE: "docker_example_user_code_image"
    expose:
      - "4001"
    networks:
      - docker_example_network
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

