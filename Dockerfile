FROM python:3.8-slim as base

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt

FROM base as dev
COPY . /app/