# Автор: Владимир Макрушин, группа ПРЗ-23, 30.10.2026

def get_number(prompt):
    """Функция для безопасного получения числа от пользователя."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: Пожалуйста, введите корректное число (буквы и спецсимволы недопустимы).")

def main():
    print("--- Консольный калькулятор v2.0 ---")
    
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
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '**':
        result = num1 ** num2
    elif operation == '/':
        # 4. Обработка деления на ноль
        if num2 == 0:
            print("Ошибка: Деление на ноль невозможно!")
            return
        result = num1 / num2

    # Вывод результата
    if result.is_integer():
        print(f"Результат: {int(result)}")
    else:
        print(f"Результат: {result}")

if __name__ == "__main__":
    main()
