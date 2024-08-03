FROM python:3.11-slim

WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
COPY docker/launch.sh launch.sh

RUN apt-get update \
    && apt-get -y install netcat-traditional \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "sh", "launch.sh" ]
