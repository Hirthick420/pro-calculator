from .base import BaseCalculation
from app.operation import mul_vals

class MulCalculation(BaseCalculation):
    def evaluate(self) -> float:
        a, b = self.operands
        return mul_vals(a, b)
