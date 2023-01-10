python ./manage.py collectstatic --no-input
python ./manage.py migrate
gunicorn configs.wsgi:application --bind 0.0.0.0:8010 --workers 3