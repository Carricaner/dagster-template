from typing import List

import dagster as dg
from dagster import AssetCheckResult


@dg.asset(description="Raw sample data for demonstration")
def raw_data() -> List[int]:
    return [1, 2, 3, 4, 5]


@dg.asset_check(asset="raw_data", description="Ensure raw_data is not empty and all values are positive.")
def check_raw_data_not_empty(raw_data: List[int]) -> AssetCheckResult:
    is_not_empty = len(raw_data) > 0
    all_positive = all(x > 0 for x in raw_data)
    return AssetCheckResult(
        passed=is_not_empty and all_positive,
        metadata={"length": len(raw_data), "all_positive": all_positive}
    )


@dg.asset(description="Processed data from raw_data")
def processed_data(raw_data: List[int]) -> List[int]:
    return [x * 2 for x in raw_data]


@dg.asset_check(asset="processed_data", description="Ensure processed data contains only even values.")
def check_processed_data_even(processed_data: List[int]) -> AssetCheckResult:
    all_even = all(x % 2 == 0 for x in processed_data)
    return AssetCheckResult(
        passed=all_even,
        metadata={"length": len(processed_data), "all_even": all_even}
    )


@dg.asset(description="Final analysis results")
def analysis_results(processed_data: List[int]) -> dict:
    return {
        "count": len(processed_data),
        "sum": sum(processed_data),
        "average": sum(processed_data) / len(processed_data),
        "max": max(processed_data),
        "min": min(processed_data),
    }
