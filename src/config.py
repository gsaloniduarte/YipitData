CURRENCY_RATES = {
    "USD": 1.0,
    "EUR": 1.1,
    "GBP": 1.3
}
MOVIES_PATH = "data/raw/movies.json"
DETAILS_PATH = "data/raw/movie-detail.json"
OUTPUT_PATH = "data/processed/oscar_winners_post_1955_min_15mm.csv"
OSCAR_WINNERS_QUERY = """
SELECT
    film,
    year,
    wiki_url AS wikipedia_url,
    budget AS original_budget,
    budget_usd
FROM movies
WHERE winner = TRUE
  AND year >= 1955
  AND budget_usd >= 15000000
ORDER BY year
"""