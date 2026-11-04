# Автор: Владимир Макрушин, группа ПРЗ-23, 03.11.2026
# Для МДК.02.02

"""
Главный модуль приложения Калькулятор.
Отвечает за меню пользователя, вычисления и взаимодействие с БД.
"""
import calc_logic  # Импортируем модуль с математической логикой
import db_manager  # Импортируем модуль для работы с БД


def get_number(prompt):
    """Функция для безопасного получения числа от пользователя."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: Пожалуйста, введите корректное число (буквы и спецсимволы недопустимы).")


def show_history():
    """Показывает последние 10 записей из истории."""
    history = db_manager.get_history(10)

    if not history:
        print("История пуста.")
        return

    print("\n--- История вычислений ---")
    for record in history:
        print(f"  [{record[3]}] {record[1]} = {record[2]}")


def show_statistics():
    """Запрашивает и выводит статистические показатели базы данных вычислений."""
    stats = db_manager.get_statistics()
    print("\n--- Статистика базы данных вычислений ---")
    print(f" Общее количество вычислений: {stats['total_count']}")
    print(f" Среднее значение результатов: {stats['avg_value']}")
    print(f" Самое большое значение результатов: {stats['max_value']}")
    print(f" Самое маленькое значение результатов: {stats['min_value']}")
    print("-----------------------------------------")


def execute_search():
    """Получает ключевое слово от пользователя и выводит результаты поиска."""
    keyword = input("Введите поисковый запрос (например, число '5' или 'sqrt'): ").strip()
    results = db_manager.search_history(keyword)
    
    print(f"\n--- Результаты поиска по запросу '{keyword}' ---")
    if not results:
        print("Записи, соответствующие критериям поиска, не найдены.")
        return
        
    for record in results:
        print(f"  [{record[3]}] {record[1]} = {record[2]}")
    print(f"Всего найдено совпадений: {len(results)}")


def perform_calculation():
    """Функция проведения одного вычисления и сохранения его в базу данных."""
    # Запрос операции с расширенным выбором
    while True:
        operation = input("Выберите операцию (+, -, *, /, **, sqrt, %): ").strip()
        if operation in ['+', '-', '*', '/', '**', 'sqrt', '%']:
            break
        else:
            print("Ошибка: Неподдерживаемая операция. Используйте только: +, -, *, /, **, sqrt или %.")

    # Запрос чисел в зависимости от операции
    if operation == 'sqrt':
        num1 = get_number("Введите число для извлечения корня: ")
    else:
        num1 = get_number("Введите первое число: ")
        num2 = get_number("Введите второе число: ")
    
    # Вычисление и обработка результата
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
        elif operation == '%':
            result = calc_logic.modulo(num1, num2)
        elif operation == 'sqrt':
            result = calc_logic.square_root(num1)
        else:
            print("Неизвестная операция!")
            return

        # Формируем строку выражения для базы данных
        if operation == 'sqrt':
            expression = f"sqrt({num1})"
        else:
            expression = f"{num1} {operation} {num2}"

        # Сохраняем запись в базу данных через db_manager
        db_manager.save_record(expression, result)

        # Вывод результата
        if result.is_integer():
            print(f"Результат: {int(result)}")
        else:
            print(f"Результат: {result}")

    except ValueError as e:
        print(f"Ошибка вычисления: {e}")


def main():
    print("--- Модульный калькулятор v4.0 (с историей) ---")

    # Инициализируем БД при старте (добавили скобки вызова функции)
    db_manager.init_db()

    while True:
        print("\n--- Меню ---")
        print("1. Выполнить вычисление")
        print("2. Показать историю (последние 10)")
        print("3. Очистить историю")
        print("4. Показать статистику")
        print("5. Поиск по истории")
        print("0. Выход")
        
        choice = input("Выберите действие: ").strip()
        
        if choice == '0':
            print("До свидания!")
            break
        elif choice == '1':
            perform_calculation()
        elif choice == '2':
            show_history()
        elif choice == '3':
            db_manager.clear_history()
            print("История очищена.")
        elif choice == '4':
            show_statistics()
        elif choice == '5':
            execute_search()
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
