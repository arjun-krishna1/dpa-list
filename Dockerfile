# syntax=docker/dockerfile:1
FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /app

# Installing OS Dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev

RUN pip install -U pip setuptools

COPY requirements.txt /app/

RUN pip install -r /app/requirements.txt

ADD . /app/

EXPOSE 3000

WORKDIR /app/app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:3000"]