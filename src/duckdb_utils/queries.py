def run_query(con, query: str):
    """
    Execute a SQL query against DuckDB and return a pandas DataFrame.
    """
    return con.execute(query).df()



def export(con, query: str, path: str, fmt: str):
    if fmt == "csv":
        con.execute(f"COPY ({query}) TO '{path}' (HEADER, DELIMITER ',')")
    elif fmt == "parquet":
        con.execute(f"COPY ({query}) TO '{path}' (FORMAT PARQUET)")
    elif fmt == "json":
        con.execute(f"COPY ({query}) TO '{path}' (FORMAT JSON)")
