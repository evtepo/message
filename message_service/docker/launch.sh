#!/usr/bin/env bash

while ! nc -z $MONGO_HOST $MONGO_PORT; do
      sleep 0.1
done 

gunicorn main:app --bind 0.0.0.0:8000 --workers 3 -k uvicorn.workers.UvicornWorker