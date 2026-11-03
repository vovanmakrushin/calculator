#Создание первого теста

"""
Модуль тестов для calc_logic.py
Содержит Unit-тесты для математических функций калькулятора.
"""
import pytest
import calc_logic


class TestAdd:
    """Тесты для функции сложения."""
    
    def test_add_positive_numbers(self):
        """Тест сложения двух положительных чисел."""
        assert calc_logic.add(2, 3) == 5
    
    def test_add_negative_numbers(self):
        """Тест сложения отрицательных чисел."""
        assert calc_logic.add(-1, -1) == -2
    
    def test_add_mixed_numbers(self):
        """Тест сложения положительного и отрицательного."""
        assert calc_logic.add(-1, 1) == 0
    
    def test_add_floats(self):
        """Тест сложения дробных чисел."""
        assert calc_logic.add(0.1, 0.2) == pytest.approx(0.3)


class TestSubtract:
    """Тесты для функции вычитания."""
    
    def test_subtract_positive(self):
        """Тест вычитания положительных чисел."""
        assert calc_logic.subtract(5, 3) == 2
    
    def test_subtract_negative_result(self):
        """Тест вычитания с отрицательным результатом."""
        assert calc_logic.subtract(3, 5) == -2


class TestMultiply:
    """Тесты для функции умножения."""
    
    def test_multiply_positive(self):
        """Тест умножения положительных чисел."""
        assert calc_logic.multiply(4, 5) == 20
    
    def test_multiply_by_zero(self):
        """Тест умножения на ноль."""
        assert calc_logic.multiply(10, 0) == 0
    
    def test_multiply_negative(self):
        """Тест умножения отрицательных чисел."""
        assert calc_logic.multiply(-3, -4) == 12


class TestDivide:
    """Тесты для функции деления."""
    
    def test_divide_positive(self):
        """Тест деления положительных чисел."""
        assert calc_logic.divide(10, 2) == 5
    
    def test_divide_with_remainder(self):
        """Тест деления с остатком."""
        assert calc_logic.divide(10, 3) == pytest.approx(3.333, rel=1e-2)
    
    def test_divide_by_zero(self):
        """Тест деления на ноль (должно вызвать ValueError)."""
        with pytest.raises(ValueError, match="Ошибка: Деление на ноль невозможно!"):
            calc_logic.divide(10, 0)
