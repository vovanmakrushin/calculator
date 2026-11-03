#!/bin/bash
# Скрипт для автоматической установки окружения и инициализации проекта
# Автор: Владимир Макрушин

cd "$(dirname "$0")"

# 1. Создание виртуального окружения (если его нет)
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

source venv/bin/activate

# 2. Установка зависимостей
pip install --upgrade pip
pip install -r requirements.txt

# 3. Инициализация базы данных
python3 -c "import db_manager; db_manager.init_db(); print('База данных успешно инициализирована.')"

deactivate
