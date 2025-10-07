import pytest
from app.operation import add_vals, sub_vals, mul_vals, div_vals
from app.calculator.exceptions import CalculationError

@pytest.mark.parametrize("a,b,exp", [(1,2,3.0),(2.5,3.5,6.0),(-1,1,0.0)])
def test_add_vals(a,b,exp):
    assert add_vals(a,b) == pytest.approx(exp)

@pytest.mark.parametrize("a,b,exp", [(5,2,3.0),(2.5,3.5,-1.0),(-1,-1,0.0)])
def test_sub_vals(a,b,exp):
    assert sub_vals(a,b) == pytest.approx(exp)

@pytest.mark.parametrize("a,b,exp", [(3,4,12.0),(2.5,2,5.0),(-2,3,-6.0)])
def test_mul_vals(a,b,exp):
    assert mul_vals(a,b) == pytest.approx(exp)

def test_div_vals_ok():
    assert div_vals(8,2) == 4.0

def test_div_vals_zero_raises():
    with pytest.raises(CalculationError):
        div_vals(5,0)
