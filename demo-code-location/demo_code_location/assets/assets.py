"""Demo assets for the Dagster code location.

This module contains example assets and jobs demonstrating
basic data processing patterns.
"""

from typing import List

import dagster as dg


@dg.asset(description="Raw sample data for demonstration")
def raw_data() -> List[int]:
    """Generate raw sample data.
    
    Returns:
        List of sample integers for processing.
    """
    return [1, 2, 3, 4, 5]


@dg.asset(description="Processed data from raw_data")
def processed_data(raw_data: List[int]) -> List[int]:
    """Process raw data by doubling each value.
    
    Args:
        raw_data: List of integers from raw_data asset.
        
    Returns:
        List of processed integers (doubled values).
    """
    return [x * 2 for x in raw_data]


@dg.asset(description="Final analysis results")
def analysis_results(processed_data: List[int]) -> dict:
    """Analyze processed data and return summary statistics.
    
    Args:
        processed_data: List of processed integers.
        
    Returns:
        Dictionary containing analysis results.
    """
    return {
        "count": len(processed_data),
        "sum": sum(processed_data),
        "average": sum(processed_data) / len(processed_data),
        "max": max(processed_data),
        "min": min(processed_data),
    }


# Legacy job-based operations (for backward compatibility)
@dg.op(description="Fetch data operation")
def fetch_data() -> List[int]:
    """Simulate fetching data (e.g., from API or S3).
    
    Returns:
        List of sample data.
    """
    return [1, 2, 3, 4, 5]


@dg.op(description="Process data operation")
def process_data_op(data: List[int]) -> List[int]:
    """Process data (e.g., transform, clean, filter).
    
    Args:
        data: Input data to process.
        
    Returns:
        Processed data.
    """
    return [x * 2 for x in data]


@dg.op(description="Save results operation")
def save_result(processed_data: List[int]) -> str:
    """Save processed data to storage.
    
    Args:
        processed_data: Data to save.
        
    Returns:
        Status message.
    """
    dg.get_dagster_logger().info(f"Saving result: {processed_data}")
    return f"Saved {len(processed_data)} records"


@dg.job(description="Example job demonstrating op chaining")
def chained_job():
    """Example job that chains fetch -> process -> save operations."""
    data = fetch_data()
    processed = process_data_op(data)
    save_result(processed)
