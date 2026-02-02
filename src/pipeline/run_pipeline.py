from src.io.reader import read_csv,read_json
from src.io.writer import write_csv,write_json
from src.cleaning.budget import clean_budget_to_usd
from src.cleaning.year import clean_year
from src.duckdb_utils.connection import create_connection
from src.duckdb_utils.queries import run_query
from src.config import MOVIES_PATH, DETAILS_PATH, OUTPUT_PATH, OSCAR_WINNERS_QUERY


def main(query: str):
    movies = read_json(MOVIES_PATH)
    details = read_json(DETAILS_PATH)

    # Assumption: both datasets share `film` as the join key
    df = movies.merge(details, on="detail_url", how="left")

    df["year"] = df["release_dates"].apply(clean_year)
    df["budget_usd"] = df["budget"].apply(clean_budget_to_usd)

    con = create_connection(df)
    result = run_query(con, query)

    write_csv(result, OUTPUT_PATH)

if __name__ == "__main__":
    main(OSCAR_WINNERS_QUERY)
