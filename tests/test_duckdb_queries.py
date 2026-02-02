import pandas as pd
from src.duckdb_utils.connection import create_connection

def test_duckdb_connection():
    df = pd.DataFrame({"a": [1, 2]})
    con = create_connection(df)
    result = con.execute("SELECT COUNT(*) FROM df").fetchone()[0]
    assert result == 2
