import os
from minio import Minio
from sqlalchemy import create_engine


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


project_path = os.getenv("PROJECT_PATH")
postgres_username = os.getenv("POSTGRES_USERNAME")
postgres_password = os.getenv("POSTGRES_PASSWORD")
postgres_ipaddress = os.getenv("POSTGRES_IPADDRESS")
postgres_port = int(os.getenv("POSTGRES_PORT"))

db_engine, db_connection = create_db(
    postgres_username, postgres_password, postgres_ipaddress, postgres_port
)

minio_access_key = os.getenv("MINIO_ACCESS_KEY")
minio_secret_key = os.getenv("MINIO_SECRET_KEY")
minio_port = os.getenv("MINIO_PORT")

minio_client = create_minio(minio_access_key, minio_secret_key, minio_port)

data_path = os.path.join(project_path, "data")

titanic_path = os.path.join(data_path, "titanic.csv")
titanic_filename = "titanic.csv"

titanic_schema_path = os.path.join(data_path, "titanic_schema.yml")
titanic_schema_bucket = "schema"
titanic_schema_filename = "titanic_schema.yml"
