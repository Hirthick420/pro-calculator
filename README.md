# Professional Calculator (CLI) — 100% Coverage

## Quick Start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest --cov=app --cov-report=term-missing
python -m app.calculator
