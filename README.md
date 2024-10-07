# Tasks

Backend приложения **Tasks** для создания и отслеживания задач.

## Технологии

- Python 3.12.4
- Django 5.0.6
- Django REST Framework 3.15.2
- Gunicorn 22.0.0
- Djoser 2.2.3
- PostgreSQL
- Nginx

## Установка

Склонируйте проект:

`$ git clone https://github.com/Govorov1705/tasks-backend.git`

Перейдите в папку _tasks-backend/tasks-api/_:

`$ cd ./tasks-backend/tasks-api/`

Создайте виртуальное окружение:

`$ python3 -m venv venv`

Активируйте виртуальное окружение:

`$ source ./venv/bin/activate`

Установите зависимости:

`$ pip3 install -r requirements.txt`

В папке _tasks-api_ cоздайте файл с переменными окружения _.env.local_, скопируйте в него примеры из файла _.env.local.example_ и внесите необходимые данные, следуя примерам:

```
DEVELOPMENT_MODE=True
SECRET_KEY=djangosecretkeyhere
DEBUG=True
CORS_ALLOWED_ORIGINS=http://localhost:5173
EMAIL_HOST_USER=someappinbox@gmail.com # Email-адрес Gmail, для которого создан пароль приложения.
EMAIL_HOST_PASSWORD=some app password here # Пароль приложения для email-адреса, указанного выше.
DOMAIN=localhost:5173
ALLOWED_HOSTS=127.0.0.1,localhost
CSRF_TRUSTED_ORIGINS=http://127.0.0.1:5173,http://localhost:5173
AUTH_COOKIE_SECURE=True
```

Выполните миграции:

`$ python3 manage.py migrate`

Запустите локальный сервер:

`$ python3 manage.py runserver localhost:8000`

Готово! Backend доступен по адресу [http://localhost:8000](http://localhost:8000).

Следующий шаг - запуск frontend-части приложения. Для этого прочитайте _README.md_ в соответствующем [репозитории](https://github.com/Govorov1705/tasks-frontend).
