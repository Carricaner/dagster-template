from dagster import Definitions, load_assets_from_modules, load_asset_checks_from_modules

from .assets import assets

# Load all assets from the assets module
all_assets = load_assets_from_modules([assets])
all_asset_checks = load_asset_checks_from_modules([assets])

# Create the main Definitions object
defs = Definitions(
    assets=all_assets,
    asset_checks=all_asset_checks
)
