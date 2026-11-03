#Тестирование работы с БД


"""
Модуль тестов для db_manager.py
Содержит Unit-тесты для работы с базой данных.
"""
import os
import pytest
import db_manager


# Фикстура: выполняется перед каждым тестом
@pytest.fixture(autouse=True)
def setup_test_db():
    """Создает тестовую БД перед тестом и удаляет после."""
    # Подменяем имя БД на тестовое
    db_manager.DB_NAME = "test_history.db"
    db_manager.init_db()
    yield  # Здесь выполняется тест
    # Очистка после теста
    if os.path.exists("test_history.db"):
        os.remove("test_history.db")


class TestDBManager:
    """Тесты для модуля работы с БД."""

    def test_save_and_get_record(self):
        """Тест сохранения и получения записи."""
        db_manager.save_record("2 + 2", 4.0)
        history = db_manager.get_history(10)

        assert len(history) == 1
        assert history[0][1] == "2 + 2"
        assert history[0][2] == 4.0

    def test_save_multiple_records(self):
        """Тест сохранения нескольких записей."""
        db_manager.save_record("1 + 1", 2.0)
        db_manager.save_record("2 + 2", 4.0)
        db_manager.save_record("3 + 3", 6.0)

        history = db_manager.get_history(10)
        assert len(history) == 3

    def test_clear_history(self):
        """Тест очистки истории."""
        db_manager.save_record("1 + 1", 2.0)
        db_manager.clear_history()

        history = db_manager.get_history(10)
        assert len(history) == 0

    def test_get_history_limit(self):
        """Тест ограничения количества записей."""
        for i in range(15):
            db_manager.save_record(f"{i} + 0", float(i))

        history = db_manager.get_history(5)
        assert len(history) == 5