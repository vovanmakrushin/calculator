"""
Модуль db_manager.py
Отвечает за работу с базой данных SQLite.
Хранит историю вычислений калькулятора.
"""
import sqlite3
from datetime import datetime

DB_NAME = "history.db"


def get_connection():
    """
    Создает и возвращает соединение с базой данных.
    
    Returns:
        sqlite3.Connection: Объект соединения с БД.
    """
    return sqlite3.connect(DB_NAME)


def init_db():
    """
    Инициализирует базу данных: создает таблицу history, если её нет.
    Вызывается при первом запуске программы.
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            expression TEXT NOT NULL,
            result REAL NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()


def save_record(expression: str, result: float) -> int:
    """
    Сохраняет запись о вычислении в базу данных.
    
    Args:
        expression (str): Математическое выражение (например, "2 + 2").
        result (float): Результат вычисления.
    
    Returns:
        int: ID созданной записи.
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute(
        "INSERT INTO history (expression, result, timestamp) VALUES (?, ?, ?)",
        (expression, result, timestamp)
    )
    
    record_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return record_id


def get_history(limit: int = 10) -> list:
    """
    Получает последние записи из истории вычислений.
    
    Args:
        limit (int, optional): Количество записей. По умолчанию 10.
    
    Returns:
        list: Список кортежей (id, expression, result, timestamp).
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT id, expression, result, timestamp FROM history ORDER BY id DESC LIMIT ?",
        (limit,)
    )
    
    records = cursor.fetchall()
    conn.close()
    
    return records


def clear_history():
    """Удаляет все записи из истории."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM history")
    
    conn.commit()
    conn.close()


def get_statistics() -> dict:
    """
    Вычисляет и возвращает статистические показатели вычислений.
    
    Returns:
        dict: Словарь с общим количеством, средним, максимальным и минимальным значениями результатов.
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(result), AVG(result), MAX(result), MIN(result) FROM history")
    total_count, avg_value, max_value, min_value = cursor.fetchone()
    
    conn.close()
    
    return {
        "total_count": total_count if total_count else 0,
        "avg_value": round(avg_value, 4) if avg_value else 0.0,
        "max_value": max_value if max_value else 0.0,
        "min_value": min_value if min_value else 0.0
    }


def search_history(keyword: str) -> list:
    """
    Ищет записи в истории по ключевому слову в математическом выражении.
    
    Args:
        keyword (str): Ключевое слово для поиска (например, число или знак операции).
        
    Returns:
        list: Список кортежей найденных записей.
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    # Используем оператор LIKE для поиска подстроки
    cursor.execute(
        "SELECT id, expression, result, timestamp FROM history WHERE expression LIKE ? ORDER BY id DESC",
        (f"%{keyword}%",)
    )
    
    records = cursor.fetchall()
    conn.close()
    
    return records