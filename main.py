# Автор: Владимир Макрушин, группа ПРЗ-23, 31.10.2026

"""
Главный модуль приложения Калькулятор.
Отвечает за взаимодействие с пользователем.
"""
import calc_logic  # Импортируем модуль с математической логикой

def get_number(prompt):
    """Функция для безопасного получения числа от пользователя."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: Пожалуйста, введите корректное число (буквы и спецсимволы недопустимы).")

def main():
    print("--- Модульный калькулятор v2.0 ---")
    
    # 1. Запрос операции с расширенным выбором
    while True:
        operation = input("Выберите операцию (+, -, *, /, **, sqrt): ").strip()
        if operation in ['+', '-', '*', '/', '**', 'sqrt']:
            break
        else:
            print("Ошибка: Неподдерживаемая операция. Используйте только: ++, -, *, /, ** или sqrt.")

    # 2. Запрос чисел в зависимости от операции
    if operation == 'sqrt':
        num1 = get_number("Введите число для извлечения корня: ")
    else:
        num1 = get_number("Введите первое число: ")
        num2 = get_number("Введите второе число: ")
    
    # 3. Вычисление и обработка результата
    try:
        if operation == '+':
            result = calc_logic.add(num1, num2)
        elif operation == '-':
            result = calc_logic.subtract(num1, num2)
        elif operation == '*':
            result = calc_logic.multiply(num1, num2)
        elif operation == '**':
            result = calc_logic.power(num1, num2)
        elif operation == '/':
            result = calc_logic.divide(num1, num2)
        elif operation == 'sqrt':
            result = calc_logic.square_root(num1)
        else:
            print("Неизвестная операция!")
            return

        # Вывод результата
        if result.is_integer():
            print(f"Результат: {int(result)}")
        else:
            print(f"Результат: {result}")

    except ValueError as e:
        print(f"Ошибка вычисления: {e}")

if __name__ == "__main__":
    main()
