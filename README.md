`dz221v2` - это проект Django, созданный для демонстрации функциональности веб-приложений на основе фреймворка Django. В проекте используются стандартные возможности Django, а также дополнительные пакеты для обработки изображений и взаимодействия с базой данных.

Установка и настройка

Установка зависимостей

1. Склонируйте репозиторий:

    ```bash
    git clone https://github.com/yourusername/dz221v2.git
    cd dz221v2
    ```

2. Создайте виртуальное окружение и активируйте его:

    ```bash
    python -m venv venv
    source venv/bin/activate  # на Windows используйте `venv\Scripts\activate`
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

### Настройка базы данных

1. Убедитесь, что у вас установлен PostgreSQL и запущен сервер.

2. Создайте базу данных для проекта:

    ```sql
    CREATE DATABASE dz221v2;
    ```

3. Создайте пользователя и предоставьте ему права на базу данных:

    ```sql
    CREATE USER your_database_user WITH PASSWORD 'your_database_password';
    GRANT ALL PRIVILEGES ON DATABASE dz221v2 TO your_database_user;
    ```

4. Обновите файл настроек `dz221v2/settings.py` с параметрами вашей базы данных:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'dz221v2',
            'USER': 'your_database_user',
            'PASSWORD': 'your_database_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

Миграции и запуск сервера

1. Выполните миграции:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

2. Запустите сервер разработки:

    ```bash
    python manage.py runserver
    ```

3. Откройте браузер и перейдите по адресу `http://127.0.0.1:8000/` для доступа к приложению.

Тестирование

Для проверки корректности подключения к базе данных вы можете использовать следующий скрипт:

```python
import psycopg2

conn = psycopg2.connect(
    dbname="dz221v2",
    user="your_database_user",
    password="your_database_password",
    host="localhost",
    port="5432"
)

print("Database connection successful")
conn.close()
