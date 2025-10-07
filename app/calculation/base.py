from dataclasses import dataclass
from typing import Tuple

@dataclass(frozen=True)
class BaseCalculation:
    """
    Base class for a calculation with two operands.
    Subclasses implement .evaluate().
    """
    operands: Tuple[float, float]

    def evaluate(self) -> float:  # pragma: no cover (abstract-ish line)
        raise NotImplementedError("Subclasses must implement evaluate().")

    def describe(self, op_symbol: str) -> str:
        a, b = self.operands
        return f"{a} {op_symbol} {b}"
