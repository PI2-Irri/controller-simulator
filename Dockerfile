FROM python:3.6

RUN apt-get update && apt-get install -y cron

WORKDIR /central-service

COPY . /central-service

COPY cronjob /etc/cron.d/cronjob

RUN chmod 0644 /etc/cron.d/cronjob

RUN /usr/bin/crontab /etc/cron.d/cronjob

RUN pip install --no-cache-dir -r requirements.txt