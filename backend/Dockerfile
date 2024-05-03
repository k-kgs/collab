FROM python:3.10 as builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install libpq-dev gcc && pip install psycopg2
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
FROM builder
COPY . /app
EXPOSE 8000