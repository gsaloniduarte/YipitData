import pandas as pd
import re
from src.config import CURRENCY_RATES

MILLION = 1_000_000


def _parse_numbers(text: str) -> list[float]:
    """
    Extract full numbers including thousands separators.
    """
    matches = re.findall(r"\d{1,3}(?:,\d{3})*(?:\.\d+)?", text)
    return [float(m.replace(",", "")) for m in matches]


def _detect_currency(text: str) -> str:
    if "£" in text or "gbp" in text:
        return "GBP"
    if "€" in text or "eur" in text:
        return "EUR"
    return "USD"


def _parse_single_expression(text: str) -> float:
    """
    Parse a single budget expression (no 'or').
    Handles ranges and millions.
    """
    text = text.lower()

    currency = _detect_currency(text)
    is_million = "million" in text

    # Remove citations
    text = re.sub(r"\[.*?\]", "", text)

    numbers = _parse_numbers(text)
    if not numbers:
        return 0

    amount = max(numbers)  # handles ranges

    if is_million:
        amount *= MILLION

    return amount * CURRENCY_RATES.get(currency, 1.0)


def clean_budget_to_usd(value) -> int:
    """
    Normalize messy budget strings into USD integer.
    """
    if pd.isna(value):
        return 0

    text = str(value)

    # Split alternatives
    parts = re.split(r"\s+or\s+", text, flags=re.IGNORECASE)

    usd_values = [_parse_single_expression(p) for p in parts]

    return int(max(usd_values)) if usd_values else 0
