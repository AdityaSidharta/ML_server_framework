from src.utils.conn import db_connection, minio_client
from src.utils.envs import (
    titanic_filename,
    titanic_schema_filename,
    titanic_schema_bucket,
)
from src.utils.io import read_data, write_db, write_minio


def setup_db():
    titanic_df = read_data(titanic_filename)
    write_db(titanic_df, titanic_filename, db_connection)
    write_minio(minio_client, titanic_schema_bucket, titanic_schema_filename)


if __name__ == "__main__":
    setup_db()
