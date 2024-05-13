# Сайт-портфолио

Проект "Сайт-портфолио" - это сайт для представления себя в информационном пространстве. Далее представлена инструкция по локальному развертыванию проекта.

## Этапы развертывания

1. **Создание виртуального окружения**:
   ```ps
   python -m venv venv
   ```

2. **Активация виртуального окружения**:
   ```ps
   ./venv/scripts/activate
   ```

3. **Установка зависимостей**:
   ```ps
   pip install -r requirements.txt
   ```

4. **Переход в папку с проектом**:
   ```ps
   cd chiganov_site
   ```

5. **Создание суперпользователя**:
   ```ps
   python manage.py createsuperuser
   ```

6. **Создание миграций**:
   ```ps
   python manage.py makemigrations
   ```

7. **Применение миграций**:
   ```ps
   python manage.py migrate
   ```

6. **Запуск проекта**:
   ```ps
   python manage.py runserver
   ```

Теперь ваш проект готов к запуску и использованию на локальном сервере. Для доступа к административной панели перейдите по адресу `http://localhost:8000/`.