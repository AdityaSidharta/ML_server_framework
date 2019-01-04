#!/usr/bin/env bash

docker build -t ml_server_db -f ./docker/docker-postgres/Dockerfile .
docker run -d -it -e POSTGRES_USER=${POSTGRES_USERNAME} -e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} -p ${POSTGRES_PORT}:${POSTGRES_PORT} ml_server_db
python ./docker/docker-postgres/fill_data.py
