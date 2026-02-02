
# 📄 EXPLAIN.md

## Overview

This project was designed to demonstrate how messy real-world datasets can be cleaned, transformed, and analyzed using a small, readable ETL pipeline. The focus was on correctness, clarity, and reproducibility rather than performance optimization.

---

## Design Approach

The solution is organized around clear separation of concerns:

- **Ingestion**: Read raw JSON input files
- **Cleaning**: Normalize budget and year fields
- **Querying**: Perform SQL-based analysis with DuckDB
- **Exporting**: Write structured outputs to CSV

This mirrors how lightweight analytical ETL pipelines are commonly structured in production environments.

---

## Budget Cleaning Assumptions

The `budget` field contains highly inconsistent formats. The following rules were applied:

- Missing or null values → `0`
- Budget ranges (e.g. `$10M - $20M`) → use the **maximum**
- Alternative values (e.g. `$1M or £467k`) → parse each independently, convert to USD, and retain the **largest**
- Supported currencies and fixed conversion rates:
  - USD → 1.0
  - EUR → 1.1
  - GBP → 1.3

Currency rates are defined in `config.py` to make assumptions explicit and reproducible.

---

## Year Cleaning Assumptions

Release dates appear in many textual formats. The year is extracted by identifying the first four-digit value (`YYYY`) found in the string.

If no valid year is detected, the value is set to `NULL`.

---

## DuckDB Usage

DuckDB is used as an embedded analytical engine to:

- Register Pandas DataFrames as tables
- Execute SQL queries over transformed data
- Return results as Pandas DataFrames for export

This allows SQL-based analysis without requiring an external database or service.

---

## Query Logic

The final exported dataset includes:

- Movies that **won an Oscar**
- Release year **≥ 1955**
- Budget **≥ $15,000,000 USD**

Query logic is decoupled from the ETL pipeline so analytical requirements can change independently.

---

## Tradeoffs and Limitations

- Currency conversion rates are static
- Budget parsing favors conservative interpretation
- No attempt is made to infer or impute missing budgets

These decisions were made to keep the solution simple, deterministic, and easy to reason about within the scope of the assignment.

---

## Conclusion

This ETL toolkit demonstrates how messy historical data can be normalized, queried, and exported using a modular Python codebase with clear assumptions and minimal setup.
