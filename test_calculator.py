import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


class TestArithmetic:
    def test_add(self, calc):
        assert calc.add(2, 3) == 5
        assert calc.add(-1, 1) == 0
        assert calc.add(0.1, 0.2) == pytest.approx(0.3)

    def test_subtract(self, calc):
        assert calc.subtract(10, 4) == 6
        assert calc.subtract(0, 5) == -5

    def test_multiply(self, calc):
        assert calc.multiply(3, 4) == 12
        assert calc.multiply(-2, 5) == -10
        assert calc.multiply(0, 100) == 0

    def test_divide(self, calc):
        assert calc.divide(10, 2) == 5
        assert calc.divide(7, 2) == 3.5

    def test_divide_by_zero(self, calc):
        with pytest.raises(ValueError, match="Деление на ноль"):
            calc.divide(5, 0)

    def test_power(self, calc):
        assert calc.power(2, 10) == 1024
        assert calc.power(9, 0.5) == 3

    def test_sqrt(self, calc):
        assert calc.sqrt(16) == 4
        assert calc.sqrt(0) == 0

    def test_sqrt_negative(self, calc):
        with pytest.raises(ValueError, match="отрицательного"):
            calc.sqrt(-4)