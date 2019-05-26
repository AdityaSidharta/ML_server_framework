from src.components.api import Api
from src.utils.conn import docker_minio_client
from src.utils.io import *


def main():
    df_full = read_data("titanic.csv")
    api = Api("titanic_schema.yml", "titanic_encoder.pkl", "titanic_model.pkl", docker_minio_client)
    api.fit_api(df_full)


if __name__ == "__main__":
    main()
