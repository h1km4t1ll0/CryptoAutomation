FROM ubuntu
RUN apt-get update && apt-get install -y apt-transport-https
RUN DEBIAN_FRONTEND=noninteractive apt install -y nginx python3 python3-pip gunicorn sudo net-tools nano postgresql-contrib libpq-dev curl
COPY . /srv/telegram_admin
WORKDIR /srv/telegram_admin
RUN pip3 install -r requirements.txt && cp /srv/telegram_admin/nginx.conf /etc/nginx/sites-available/default
RUN chown -R www-data:www-data /srv && chmod +x /srv/telegram_admin/run.sh && chmod +x /srv
COPY cron /etc/cron.d/hello-cron
RUN chmod 0644 /etc/cron.d/hello-cron && crontab /etc/cron.d/hello-cron && crontab -l
# RUN psql postgresql://postgres:postgres@database45 -f psql.sql

