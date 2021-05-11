FROM python:3.9-slim-buster

WORKDIR /opt
ARG TZ="Asia/Kolkata"

COPY requirements.txt .
RUN apt-get update && \
    apt-get install supervisor -y && \
    pip install -r requirements.txt && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY . .

CMD gunicorn bhavcopy.bhavcopy.wsgi