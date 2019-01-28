import time
from src.utils.io import list_bucket_minio


def split_target_columns(df, schema):
    target_cols = schema.get_target_cols()
    non_target_cols = schema.get_non_target_cols()

    df_x, y_array = df[non_target_cols].copy(), df[target_cols].values
    return df_x, y_array.ravel()


def get_latest_version(minio_client):
    list_version = [x for x in list_bucket_minio(minio_client) if x.isdigit()]
    while not list_version:
        print("Waiting for model....")
        time.sleep(10)
        list_version = [x for x in list_bucket_minio(minio_client) if x.isdigit()]
    return sorted(list_version)[-1]
