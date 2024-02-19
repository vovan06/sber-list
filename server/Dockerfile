FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apk --update add
RUN apk add gcc libc-dev libffi-dev jpeg-dev zlib-dev libjpeg
RUN apk add postgresql-dev

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


RUN chmod +x /app/entrypoint.sh

EXPOSE 4000