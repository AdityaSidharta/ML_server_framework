from minio import Minio
from sqlalchemy import create_engine

from src.utils.envs import (
    minio_secret_key,
    minio_access_key,
    minio_port,
    postgres_port,
    postgres_ipaddress,
    postgres_password,
    postgres_username,
)


def create_minio(access_key, secret_key, port):
    minio_client = Minio(
        "127.0.0.1:{}".format(port),
        access_key=access_key,
        secret_key=secret_key,
        secure=False,
    )
    return minio_client


def create_db(username, password, ip_address, port):
    engine_path = "postgresql://{}:{}@{}:{}".format(
        username, password, ip_address, port
    )
    engine = create_engine(engine_path)
    connection = engine.connect()
    return engine, connection


minio_client = create_minio(minio_access_key, minio_secret_key, minio_port)
db_engine, db_connection = create_db(
    postgres_username, postgres_password, postgres_ipaddress, postgres_port
)
