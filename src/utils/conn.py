from minio import Minio
from sqlalchemy import create_engine

from src.utils.envs import (
    minio_secret_key,
    minio_access_key,
    minio_ipaddress,
    postgres_ipaddress,
    postgres_password,
    postgres_username,
)

# TODO : Should have two types of minio client and db connections


def create_minio(access_key, secret_key, ip_address, port):
    print("{}:{}".format(ip_address, port))
    return Minio("{}:{}".format(ip_address, port), access_key=access_key, secret_key=secret_key, secure=False)


def create_db(username, password, ip_address, port):
    engine_path = "postgresql://{}:{}@{}:{}".format(username, password, ip_address, port)
    engine = create_engine(engine_path)
    connection = engine.connect()
    return engine, connection


docker_db_engine, docker_db_conn = create_db(postgres_username, postgres_password, postgres_ipaddress, 5432)


docker_minio_client = create_minio(minio_access_key, minio_secret_key, minio_ipaddress, 9000)
