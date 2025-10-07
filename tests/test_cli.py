from typing import List
from app.calculator import run_repl

def run_inputs_get_output(lines: List[str]) -> str:
    out: List[str] = []
    run_repl(lines, out.append)
    return "\n".join(out)

def test_help_and_unknown_and_empty():
    output = run_inputs_get_output(["", "help", "whoknows", "exit"])
    assert "Type 'help'" in output
    assert "Please type a command" in output
    assert "Commands:" in output
    assert "Unknown command" in output
    assert "Goodbye!" in output

def test_valid_flow_and_history():
    output = run_inputs_get_output(["add 3 4", "mul 5 6", "history", "exit"])
    assert "3.0 + 4.0 = 7.0" in output
    assert "5.0 × 6.0 = 30.0" in output
    # history prints numbered list; ensure both entries appear
    assert "1." in output and "2." in output

def test_usage_errors_and_parsing():
    output = run_inputs_get_output(["add 1", "sub a b", "exit"])
    assert "Usage: <op> <a> <b>" in output
    assert "Could not parse numbers" in output

def test_division_by_zero_in_repl():
    output = run_inputs_get_output(["div 9 0", "exit"])
    assert "Division by zero is not allowed" in output

def test_history_when_empty():
    out = run_inputs_get_output(["history", "exit"])
    assert "No calculations yet." in out

def test_immediate_stopiteration_with_empty_input():
    out = run_inputs_get_output([])  # iterator is empty; next() raises StopIteration on first loop
    assert "Type 'help' to see commands." in out

def test_aliases_in_repl():
    out = run_inputs_get_output(["multiply 2 3", "divide 8 2", "exit"])
    assert "2.0 × 3.0 = 6.0" in out
    assert "8.0 ÷ 2.0 = 4.0" in out
