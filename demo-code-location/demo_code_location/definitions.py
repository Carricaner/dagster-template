from dagster import Definitions, load_assets_from_modules

from . import assets
from .assets.assets import chained_job

# Load all assets from the assets module
all_assets = load_assets_from_modules([assets])

# Define all jobs
all_jobs = [chained_job]

# Create the main Definitions object
defs = Definitions(
    assets=all_assets,
    jobs=all_jobs,
)
