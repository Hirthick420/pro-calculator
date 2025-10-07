import pytest
from app.calculator.factory import CalculationFactory
from app.calculator.history import CalcHistory
from app.calculator.exceptions import CalculationError
from app.calculation import AddCalculation, MulCalculation

def test_factory_known_and_aliases():
    add = CalculationFactory.create("add", (1.0,2.0))
    assert isinstance(add, AddCalculation)
    mul = CalculationFactory.create("mul", (2.0,3.0))
    assert isinstance(mul, MulCalculation)
    mul2 = CalculationFactory.create("multiply", (2.0,3.0))
    assert isinstance(mul2, MulCalculation)

def test_factory_unknown():
    with pytest.raises(CalculationError):
        CalculationFactory.create("power", (2.0,3.0))

def test_history_record_and_clear():
    h = CalcHistory()
    assert h.entries() == []
    h.record("1 + 2", 3.0)
    assert h.entries() == [("1 + 2", 3.0)]
    h.clear()
    assert h.entries() == []
