import os

import oyaml as yaml
import pandas as pd
from sklearn.externals import joblib

from src.utils.envs import data_path


def read_data(table_name):
    table_path = os.path.join(data_path, "{}".format(table_name))
    df = pd.read_csv(table_path)
    return df


def write_data(df, table_name):
    table_path = os.path.join(data_path, "{}".format(table_name))
    df.to_csv(table_path, index=None)


def read_db(db_name, con):
    sql_query = "SELECT * FROM {}".format(db_name)
    df = pd.read_sql(sql_query, con)
    return df


def write_db(df, db_name, con):
    df.to_sql(db_name, con=con, index=False)


def read_yaml(filename):
    path = os.path.join(data_path, filename)
    with open(path, "r") as stream:
        try:
            yaml_file = yaml.load(stream)
        except yaml.YAMLError as exc:
            raise yaml.YAMLError(exc)
    return yaml_file


def write_yaml(data, filename):
    path = os.path.join(data_path, filename)
    with open(path, "w") as outfile:
        yaml.dump(data, stream=outfile, default_flow_style=False)


def read_model(filename):
    path = os.path.join(data_path, filename)
    return joblib.load(path)


def write_model(data, filename):
    path = os.path.join(data_path, filename)
    return joblib.dump(data, path)


def list_bucket_minio(minio_client):
    return [x.name for x in minio_client.list_buckets()]


def write_minio(minio_client, bucket_name, object_name):
    file_path = os.path.join(data_path, object_name)
    list_bucket = list_bucket_minio(minio_client)
    if bucket_name not in list_bucket:
        minio_client.make_bucket(bucket_name)
    minio_client.fput_object(bucket_name, object_name, file_path)


def read_minio(minio_client, bucket_name, object_name):
    minio_client.get_object(bucket_name, object_name)


def download_minio(minio_client, bucket_name, object_name):
    file_path = os.path.join(data_path, object_name)
    minio_client.fget_object(bucket_name, object_name, file_path)
