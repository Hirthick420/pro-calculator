import pytest
from app.calculation import AddCalculation, SubCalculation, MulCalculation, DivCalculation

@pytest.mark.parametrize("cls,operands,exp", [
    (AddCalculation, (2.0,3.0), 5.0),
    (SubCalculation, (5.0,2.0), 3.0),
    (MulCalculation, (3.0,4.0), 12.0),
    (DivCalculation, (8.0,2.0), 4.0),
])
def test_calc_classes(cls, operands, exp):
    calc = cls(operands)
    assert calc.evaluate() == pytest.approx(exp)

def test_describe_strings():
    c = AddCalculation((1.0,2.0))
    assert c.describe("+") == "1.0 + 2.0"
