from .base import BaseCalculation
from app.operation import sub_vals

class SubCalculation(BaseCalculation):
    def evaluate(self) -> float:
        a, b = self.operands
        return sub_vals(a, b)
