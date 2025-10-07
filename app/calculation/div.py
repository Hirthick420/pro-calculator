from .base import BaseCalculation
from app.operation import div_vals

class DivCalculation(BaseCalculation):
    def evaluate(self) -> float:
        a, b = self.operands
        return div_vals(a, b)
