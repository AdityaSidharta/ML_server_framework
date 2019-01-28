#!/usr/bin/env bash

source config.sh
docker build -t ml_server_minio -f ./docker/docker-minio/Dockerfile .
docker run -d -it -e MINIO_ACCESS_KEY=${MINIO_ACCESS_KEY} -e MINIO_SECRET_KEY=${MINIO_SECRET_KEY} -p ${MINIO_PORT}:9000 ml_server_minio server ${PWD}/docker/docker-minio/data