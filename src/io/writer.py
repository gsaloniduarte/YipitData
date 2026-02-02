import pandas as pd

def write_csv(df: pd.DataFrame, path: str):
    """
    Writes a DataFrame to a CSV file.
    """
    df.to_csv(path, index=False)


def write_json(df: pd.DataFrame, path: str):
    """
    Writes a DataFrame to a JSON file.
    Uses records orientation for easy downstream consumption.
    """
    df.to_json(path, orient="records", indent=2)
