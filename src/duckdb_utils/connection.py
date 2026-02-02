import duckdb
import pandas as pd

def create_connection(df: pd.DataFrame, table_name: str = "movies"):
    con = duckdb.connect()
    con.register(table_name, df)
    return con
