# Professional Calculator (CLI) — 100% Test Coverage

A modular, professional-grade command-line calculator built in Python with clean architecture, robust error handling (EAFP + LBYL), full unit tests, and GitHub Actions enforcing **100%** coverage.

## Contents
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup (WSL/Ubuntu or Linux/macOS)](#setup-wslubuntu-or-linuxmacos)
- [Run the App (REPL)](#run-the-app-repl)
- [Commands](#commands)
- [Examples](#examples)
- [Design & Architecture](#design--architecture)
- [Error Handling (EAFP + LBYL)](#error-handling-eafp--lbyl)
- [Testing & Coverage](#testing--coverage)
- [Continuous Integration (GitHub Actions)](#continuous-integration-github-actions)
- [Coverage Exceptions](#coverage-exceptions)
- [Troubleshooting](#troubleshooting)

## Project Structure
```
app/
  __init__.py
  calculator/
    __init__.py
    __main__.py
    calculator.py        # REPL engine + orchestration
    factory.py           # CalculationFactory (op token -> class)
    history.py           # in-memory history of results
    exceptions.py        # domain error type
  calculation/
    __init__.py
    base.py              # BaseCalculation dataclass
    add.py
    sub.py
    mul.py
    div.py
  operation/
    __init__.py
    operations.py        # pure arithmetic functions
tests/
  test_operations.py
  test_calculations.py
  test_factory_and_history.py
  test_cli.py
.coveragerc
pytest.ini
requirements.txt
.github/workflows/python-app.yml
README.md
```

## Prerequisites
- Python 3.11+ (tested on 3.12)
- Git (for CI)
- WSL/Ubuntu on Windows (recommended)

## Setup (WSL/Ubuntu or Linux/macOS)
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Note: pytest.ini sets `pythonpath = .` so tests can import the `app` package.

## Run the App (REPL)
```bash
python -m app.calculator
```
Type `exit` to quit.

## Commands
| Command | Meaning | Example |
|---|---:|---|
| add a b | Add two numbers | `add 3 4` |
| sub a b | Subtract b from a | `sub 10 3` |
| mul a b | Multiply (alias: `*`) | `mul 5 6` |
| div a b | Divide (guards ÷0) | `div 8 2` |
| history | Show successful calculations | |
| help | Show command help | |
| exit | Quit the app | |

## Examples
```
calc> add 3 4
3.0 + 4.0 = 7.0
calc> mul 5 6
5.0 × 6.0 = 30.0
calc> history
1. 3.0 + 4.0 = 7.0
2. 5.0 × 6.0 = 30.0
calc> exit
Goodbye!
```

## Design & Architecture
- operation/: pure functions (add_vals, sub_vals, mul_vals, div_vals).
- calculation/: BaseCalculation dataclass + subclasses implementing `.evaluate()` / `.execute()`.
- calculator/: REPL engine (CalculatorREPL), CalculationFactory, CalcHistory, and domain `CalculationError`.

DRY & modular: aliases are handled centrally in the factory; history prints a numbered list.

## Error Handling (EAFP + LBYL)
- EAFP: parsing helpers attempt `float()` and raise friendly `CalculationError` messages on invalid input.
- LBYL: division checks denominator before dividing and raises `CalculationError` for divide-by-zero.

## Testing & Coverage
Run tests:
```bash
pytest -q
```
Run coverage:
```bash
pytest --cov=app --cov-report=term-missing
```
- Parameterized tests cover operations and calculation classes.
- Factory tests include aliases and unknown operation errors.
- REPL tests cover help, usage errors, parse errors, empty history, division by zero, aliases, and immediate StopIteration.

The project aims for 100% line and branch coverage.

## Continuous Integration (GitHub Actions)
Workflow: `.github/workflows/python-app.yml`  
Runs on push/PR to main, installs dependencies, runs tests, and enforces coverage. To fail CI when coverage is below 100%:
```bash
coverage report --fail-under=100
```

## Coverage Exceptions
`.coveragerc` omits only the launcher:
```
[run]
branch = True
omit =
    app/calculator/__main__.py

[report]
show_missing = True
```

## Troubleshooting
- Markdown looks plain → ensure file is named `README.md`. In VS Code press Ctrl+Shift+V to preview.
- ModuleNotFoundError: `app` → ensure `pytest.ini` has `pythonpath = .` and `app/__init__.py` exists.
- Coverage config errors → overwrite `.coveragerc` with the block above and normalize line endings:
```bash
sed -i 's/\r$//' .coveragerc
```

## License
Add a LICENSE file (MIT recommended) or include your preferred license text here.
Workflow: .github/workflows/python-app.yml

On every push/PR to main:

Set up Python

Install deps

Run tests with coverage

Fail the build if coverage < 100%:

coverage report --fail-under=100


(Optional) Add a badge once the repo is on GitHub:

![tests](https://github.com/<YOUR-USER>/<YOUR-REPO>/actions/workflows/python-app.yml/badge.svg)

Coverage Exceptions

Minimal, intentional exclusions:

app/calculator/__main__.py is omitted via .coveragerc since it only starts the REPL.

Any truly untestable line can be annotated with # pragma: no cover (not needed beyond __main__ in this project).

.coveragerc:

[run]
branch = True
omit =
    app/calculator/__main__.py

[report]
show_missing = True

Troubleshooting

ModuleNotFoundError: No module named 'app'
Ensure pytest.ini contains:

[pytest]
pythonpath = .


And make sure app/__init__.py exists.

Coverage config error (“duplicate section” or “parsing error”)
Overwrite .coveragerc with the exact block above and convert line endings:

sed -i 's/\r$//' .coveragerc


Exit the app: type exit.
(You can also add graceful handling for Ctrl+C/EOF if desired.)

License
