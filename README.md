# Rent Roll & Maintenance Hub

A Python back end for a fictional apartment portfolio. It imports a property-management export into SQL Server, serves it through a FastAPI REST API, builds Excel rent-roll and delinquency reports on a schedule, and uses the Claude API to triage maintenance requests. See [docs/spec.md](docs/spec.md) for the full plan.

## Quick start

Requires Docker, Python 3.12+, and [Microsoft ODBC Driver 18 for SQL Server](https://learn.microsoft.com/sql/connect/odbc/download-odbc-driver-for-sql-server).

```sh
cp .env.example .env          # set MSSQL_SA_PASSWORD and the same password in DATABASE_URL
docker compose up -d          # SQL Server 2022 on localhost:1433
python -m venv .venv
.venv/bin/pip install -e ".[dev]"   # Windows: .venv\Scripts\pip
alembic upgrade head
uvicorn hub.api:app --reload  # open http://localhost:8000/docs
```

## Tests

```sh
ruff check . && ruff format --check .
pytest --cov=hub
```

Tests run against the real SQL Server from `docker compose`. CI does the same with a SQL Server service container.
