Professional Calculator (CLI) — 100% Test Coverage

A modular, professional-grade command-line calculator built in Python with clean architecture, robust error handling (EAFP + LBYL), full unit tests, and GitHub Actions enforcing 100% coverage.

Contents

Project Structure

Prerequisites

Setup (WSL/Ubuntu or Linux/macOS)

Run the App (REPL)

Commands

Examples

Design & Architecture

Error Handling (EAFP + LBYL)

Testing & Coverage

Continuous Integration (GitHub Actions)

Coverage Exceptions

Troubleshooting

License

Project Structure
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
    add.py sub.py mul.py div.py
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

Prerequisites

Python 3.11+ (tested on 3.12)

Git (for CI, optional locally)

WSL/Ubuntu if running from Windows (recommended)

Setup (WSL/Ubuntu or Linux/macOS)
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


pytest.ini sets pythonpath = . so tests can import the app package without extra env vars.

Run the App (REPL)
python -m app.calculator


Exit cleanly by typing exit.

Commands
Command	Meaning	Example
add a b	Add two numbers	add 3 4
sub a b	Subtract b from a	sub 10 3
mul a b / multiply a b	Multiply	mul 5 6
div a b / divide a b	Divide (guards ÷0)	div 8 2
history	Show successful calculations	
help	Show command help	
exit	Quit the app	
Examples
calc> add 3 4
3.0 + 4.0 = 7.0
calc> mul 5 6
5.0 × 6.0 = 30.0
calc> history
1. 3.0 + 4.0 = 7.0
2. 5.0 × 6.0 = 30.0
calc> exit
Goodbye!

Design & Architecture

Separation of concerns

operation/operations.py: pure functions (add_vals, sub_vals, mul_vals, div_vals).

calculation/*: OO layer with BaseCalculation and per-operation subclasses, each implementing .evaluate().

calculator/calculator.py: REPL engine (CalculatorREPL), user parsing, messaging.

calculator/factory.py: CalculationFactory maps tokens (add, mul, divide, aliases) → calculation classes.

calculator/history.py: stores (expression, result) tuples for history.

calculator/exceptions.py: single domain exception CalculationError.

DRY & modular: reusable ops + classes; aliases handled centrally in the factory.

Error Handling (EAFP + LBYL)

EAFP (Easier to Ask Forgiveness than Permission):

_parse_numbers_eafp() tries float() and catches ValueError, returning a friendly message (e.g., “Could not parse numbers: 'a', 'b'”).

LBYL (Look Before You Leap):

div_vals() checks for b == 0.0 before dividing and raises CalculationError("Division by zero is not allowed (LBYL).").

User-facing errors are caught in the REPL and printed clearly.

Testing & Coverage

Run the full suite with coverage:

pytest --cov=app --cov-report=term-missing


Includes parameterized tests for operations and calculation classes.

Factory tests cover known ops + aliases + unknown token path.

REPL tests cover: help, usage errors, parse errors, empty history, division by zero, alias rendering, immediate StopIteration.

Achieves 100% line and branch coverage.

Continuous Integration (GitHub Actions)

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
