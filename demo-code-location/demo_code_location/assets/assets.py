import dagster as dg


@dg.asset
def raw_data():
    return [1, 2, 3]
