# Используем базовый образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

# Копируем файл с зависимостями в контейнер
RUN pip install --upgrade pip
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt
# Копируем весь проект в контейнер
COPY . /app/

# Указываем порт, который будет использоваться в контейнере
EXPOSE 8000

# Команда для запуска сервера
# CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]