from src.cleaning.budget import clean_budget_to_usd

def test_budget_range():
    assert clean_budget_to_usd("$10,000,000 - $20,000,000") == 20_000_000
    assert clean_budget_to_usd("$10,000,000 to $40,000,000") == 40_000_000
    assert clean_budget_to_usd("$1 million or £467,000 [ 1 ]") == 1_000_000

def test_budget_nan():
    assert clean_budget_to_usd(None) == 0
