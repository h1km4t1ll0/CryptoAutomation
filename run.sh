#!/bin/bash
# 1 раз запускается во время запуска контейнера
sleep 10
psql postgresql://postgres:postgres@database -f psql.sql -p 5435
echo "successesful"
service nginx start
# service postgresql start
python3 manage.py collectstatic --noinput
sleep 1
# chmod -R u+w /srv/
python3 manage.py migrate
sleep 1
# chown www-data:www-data /srv/db.sqlite3
python3 manage.py makemigrations 
sleep 1
python3 manage.py migrate
sleep 1
python3 manage.py initadmin
sleep 1
curl http://127.0.0.1:8000/entrypoint/
sudo service cron start
crontab -l
/bin/gunicorn3 wsgi:application -b 127.0.0.1:8000 --env DJANGO_SETTINGS_MODULE=settings --user www-data --group www-data  # запускаем сервер
# python3 manage.py runserver
