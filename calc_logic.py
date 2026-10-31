"""
Модуль calc_logic.py
Содержит математические функции для калькулятора.
"""

import math  # Импортируем встроенный модуль для извлечения корня

def add(a: float, b: float) -> float:
    """Складывает два числа."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Вычитает второе число из первого."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Умножает два числа."""
    return a * b

def power(a: float, b: float) -> float:
    """Возводит первое число в степень второго."""
    return a ** b

def divide(a: float, b: float) -> float:
    """
    Делит первое число на второе.
    Вызывает ValueError, если делитель равен 0.
    """
    if b == 0:
        raise ValueError("Ошибка: Деление на ноль невозможно!")
    return a / b

def square_root(a: float) -> float:
    """
    Вычисляет квадратный корень из числа.

    Аргументы:
    a (float): Число, из которого извлекается корень.

    Возвращает:
    float: Результат извлечения квадратного корня.

    Исключения:
    ValueError: Если передано отрицательное число.
    """
    if a < 0:
        raise ValueError("Ошибка: Нельзя извлечь корень из отрицательного числа!")
    return math.sqrt(a)