"""
Pure arithmetic functions. EAFP for type conversion happens in caller (REPL).
LBYL example used for division-by-zero.
"""
from typing import Union

NumberLike = Union[int, float]

def add_vals(a: NumberLike, b: NumberLike) -> float:
    return float(a) + float(b)

def sub_vals(a: NumberLike, b: NumberLike) -> float:
    return float(a) - float(b)

def mul_vals(a: NumberLike, b: NumberLike) -> float:
    return float(a) * float(b)

def div_vals(a: NumberLike, b: NumberLike) -> float:
    # LBYL: check denominator first
    if float(b) == 0.0:
        # We raise a clean error; the REPL will catch and show a friendly message.
        from app.calculator.exceptions import CalculationError
        raise CalculationError("Division by zero is not allowed (LBYL).")
    return float(a) / float(b)
