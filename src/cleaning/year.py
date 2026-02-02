import pandas as pd
import re

def clean_year(value) -> int:
    if pd.isna(value):
        return None

    match = re.search(r"\d{4}", str(value))
    return int(match.group()) if match else None
