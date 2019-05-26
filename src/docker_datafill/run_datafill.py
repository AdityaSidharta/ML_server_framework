from src.utils.conn import docker_db_conn, docker_minio_client
from src.utils.envs import titanic_filename, titanic_schema_filename, titanic_schema_bucket
from src.utils.io import read_data, write_db, write_minio


def main():
    titanic_df = read_data(titanic_filename)
    write_db(titanic_df, titanic_filename, docker_db_conn)
    write_minio(docker_minio_client, titanic_schema_bucket, titanic_schema_filename)


if __name__ == "__main__":
    main()
