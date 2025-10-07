from typing import Tuple, Type, Dict
from app.calculation import (
    BaseCalculation,
    AddCalculation,
    SubCalculation,
    MulCalculation,
    DivCalculation,
)
from app.calculator.exceptions import CalculationError

class CalculationFactory:
    """
    Maps an op token to a Calculation subclass and creates instances.
    """
    _map: Dict[str, Type[BaseCalculation]] = {
        "add": AddCalculation,
        "sub": SubCalculation,
        "multiply": MulCalculation,
        "mul": MulCalculation,   # friendly alias
        "divide": DivCalculation,
        "div": DivCalculation,   # friendly alias
    }

    @classmethod
    def create(cls, op_token: str, operands: Tuple[float, float]) -> BaseCalculation:
        op_token = op_token.lower().strip()
        try:
            klass = cls._map[op_token]
        except KeyError as exc:
            raise CalculationError(f"Unsupported operation: {op_token}") from exc
        return klass(operands)
