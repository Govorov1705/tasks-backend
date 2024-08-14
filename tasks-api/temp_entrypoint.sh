#!/bin/sh

echo "Waiting for DB..."

while ! nc -z $DB_HOST $DB_PORT; do
sleep 0.1
done

echo "DB started!"

python manage.py migrate --no-input
python manage.py collectstatic --no-input
gunicorn core.wsgi:application --bind 0.0.0.0:8000
