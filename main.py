# Автор: Владимир Макрушин, группа ПРЗ-23, 30.10.2026

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
    print("--- Модульный калькулятор ---")
    
    # 1. Запрос чисел
    num1 = get_number("Введите первое число: ")
    num2 = get_number("Введите второе число: ")
    
    # 2. Запрос операции с циклом до тех пор, пока ввод не станет верным
    while True:
        operation = input("Выберите операцию (+, -, *, /, **): ").strip()
        if operation in ['+', '-', '*', '/', '**']:
            break  # Ввод корректен, выходим из цикла запроса операции
        else:
            print("Ошибка: Неподдерживаемая операция. Используйте только +, -, * или /.")
    
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
