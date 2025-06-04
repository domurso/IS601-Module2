from Calculator import Calculator
import pytest

@pytest.fixture
def calc():
    return Calculator()

def test_addition(calc):
    assert calc.add(5,6) == 11

def test_subtraction(calc):
    assert calc.subtract(9,8) == 1

def test_multiply(calc):
    assert calc.multiply(6,8) == 48

def test_divide(calc):
    assert calc.divide(50,10) == 5

def test_divideByZero(calc):
    with pytest.raises(ValueError):
        calc.divide(1,0)


