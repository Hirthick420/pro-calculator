from typing import Callable, Iterable, Tuple
from app.calculator.factory import CalculationFactory
from app.calculator.history import CalcHistory
from app.calculator.exceptions import CalculationError

HELP_TEXT = (
    "Commands:\n"
    "  add a b        -> add two numbers\n"
    "  sub a b        -> subtract b from a\n"
    "  mul a b        -> multiply a and b\n"
    "  div a b        -> divide a by b\n"
    "  history        -> show successful calculations\n"
    "  help           -> show this help\n"
    "  exit           -> quit\n"
)

class CalculatorREPL:
    """
    The user-facing REPL engine. Parsing + orchestration live here.
    Shows EAFP for numeric parsing, LBYL is in div operation.
    """
    def __init__(self) -> None:
        self.history = CalcHistory()

    def _parse_numbers_eafp(self, token_a: str, token_b: str) -> Tuple[float, float]:
        # EAFP: try conversion; fail gracefully.
        try:
            return float(token_a), float(token_b)
        except ValueError as exc:
            raise CalculationError(f"Could not parse numbers: '{token_a}', '{token_b}'") from exc

    def handle_line(self, line: str) -> Tuple[bool, str]:
        """
        Returns (continue_loop, message).
        """
        cleaned = (line or "").strip()
        if not cleaned:
            return True, "Please type a command. Try 'help'."

        parts = cleaned.split()
        cmd = parts[0].lower()

        # Special commands
        if cmd == "help":
            return True, HELP_TEXT
        if cmd == "history":
            entries = self.history.entries()
            if not entries:
                return True, "No calculations yet."
            lines = [f"{idx+1}. {expr} = {res}" for idx, (expr, res) in enumerate(entries)]
            return True, "\n".join(lines)
        if cmd == "exit":
            return False, "Goodbye!"

        # Operations
        if cmd in {"add", "sub", "mul", "multiply", "div", "divide"}:
            if len(parts) != 3:
                return True, "Usage: <op> <a> <b>  (e.g., add 2 3)"
            a_token, b_token = parts[1], parts[2]
            try:
                a_val, b_val = self._parse_numbers_eafp(a_token, b_token)  # EAFP
                calc = CalculationFactory.create(cmd, (a_val, b_val))
                result = calc.evaluate()
                expr = calc.describe(
                    {"add": "+", "sub": "-", "mul": "×", "multiply": "×", "div": "÷", "divide": "÷"}[cmd]
                )
                self.history.record(expr, result)
                return True, f"{expr} = {result}"
            except CalculationError as c_err:
                return True, f"Error: {c_err}"

        return True, f"Unknown command: {cmd}. Try 'help'."

def run_repl(input_source: Iterable[str] | None = None, output_sink: Callable[[str], None] = print) -> None:
    """
    Run the REPL. For tests, pass a list/iterator as input_source and a custom output_sink.
    When input_source is None, we use real input() (excluded from coverage).
    """
    engine = CalculatorREPL()

    def _real_inputs():  # pragma: no cover
        while True:
            yield input("calc> ")

    iterator = iter(input_source) if input_source is not None else _real_inputs()
    output_sink("Type 'help' to see commands.")
    keep_going = True
    while keep_going:
        try:
            line = next(iterator)
        except StopIteration:
            break
        keep_going, msg = engine.handle_line(line)
        output_sink(msg)
