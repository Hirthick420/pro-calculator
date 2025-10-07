from .base import BaseCalculation
from app.operation import add_vals

class AddCalculation(BaseCalculation):
    def evaluate(self) -> float:
        a, b = self.operands
        return add_vals(a, b)
