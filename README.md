# 🎬 Oscar Movies ETL Toolkit

This project implements a small, self-contained ETL toolkit to clean, transform, and analyze Oscar-nominated movie data using **Python**, **Pandas**, and **DuckDB**.

The pipeline ingests raw JSON files, normalizes messy fields (budget and year), executes analytical SQL queries via DuckDB, and exports a curated dataset to CSV.

---

## 📁 Project Structure
```
.
├── data/
│ ├── raw/ # Input JSON files
│ └── processed/ # Generated outputs
├── src/
│ ├── cleaning/ # Budget and year normalization
│ ├── duckdb_utils/ # DuckDB connection and query execution
│ ├── io/ # Readers and writers
│ ├── pipeline/ # Pipeline orchestration
│ └── config.py # Shared configuration (currency rates)
├── tests/ # Unit tests
├── README.md
├── EXPLAIN.md
└── requirements.txt
```

---

## ⚙️ Setup

### 1. Create and activate a virtual environment

```bash
python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)
```
### 2. Install dependencies

```
pip install -r requirements.txt
```

▶️ Run the Pipeline
```
PYTHONPATH=. python src/pipeline/run_pipeline.py
```

This will:
- Read raw movie data from data/raw/
- Clean and normalize budget and year fields
- Join datasets using a stable identifier
- Execute a DuckDB SQL query
- Write the final CSV to:
    - data/processed/oscar_winners_post_1955_min_15mm.csv (This is defined in config.py)

🧪 Run Tests
```
PYTHONPATH=. pytest
```
Unit tests validate:
- Budget normalization edge cases
- Year extraction logic
- DuckDB query execution

🛠 Troubleshooting
- ModuleNotFoundError: Ensure PYTHONPATH=. is set
- Empty output file: Verify budget and year cleaning logic
- DuckDB errors: Ensure column names in SQL match the DataFrame schema

