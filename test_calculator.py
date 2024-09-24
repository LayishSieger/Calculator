# test_calculator.py
import pytest
from calculator import Calculator

@pytest.fixture
def calculator():
    """Fixture for creating a Calculator instance."""
    return Calculator()

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add(calculator, a, b, expected):
    assert calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [(2, 3, -1), (-1, 1, -2), (0, 0, 0)])
def test_subtract(calculator, a, b, expected):
    assert calculator.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [(2, 3, 6), (-1, 1, -1), (0, 0, 0)])
def test_smultiply(calculator, a, b, expected):
    assert calculator.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (5, 0, "Cannot divide by zero!"),  # Expected exception case
])
def test_divide(calculator, a, b, expected):
    if b == 0:
        with pytest.raises(ValueError, match=expected):
            calculator.divide(a, b)
    else:
        assert calculator.divide(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [(2, 3, 8), (-1, 2, 1), (0, 0, 1)])
def test_power(calculator, a, b, expected):
    assert calculator.power(a, b) == expected