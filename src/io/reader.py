import pandas as pd

def read_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def read_json(path: str) -> pd.DataFrame:
    """
    Reads a JSON file into a pandas DataFrame.

    Supports:
    - Standard JSON (list of objects)
    - Line-delimited JSON (NDJSON / JSONL)
    """
    try:
        return pd.read_json(path)
    except ValueError:
        # Fallback for line-delimited JSON
        return pd.read_json(path, lines=True)