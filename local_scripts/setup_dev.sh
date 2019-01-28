#!/bin/bash

export PYTHONPATH=${PWD}
export PROJECT_PATH=${PWD}

export POSTGRES_USERNAME=ml_server_postgres
export POSTGRES_PASSWORD=ml_server_password
export POSTGRES_IPADDRESS=ml_server_db
export POSTGRES_PORT=5432

export MINIO_ACCESS_KEY=ml_server_minio
export MINIO_SECRET_KEY=ml_server_password
export MINIO_IPADDRESS=ml_server_minio
export MINIO_PORT=9000

export FLASK_PORT=1234

python ./src/flask/run_deploy.py