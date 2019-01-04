import os
import pandas as pd
from sqlalchemy import create_engine
from src.utils.envs import data_path
import oyaml as yaml


def read_data(table_name):
    table_path = os.path.join(data_path, "{}.csv".format(table_name))
    df = pd.read_csv(table_path)
    return df


def write_data(df, table_name):
    table_path = os.path.join(data_path, "{}.csv".format(table_name))
    df.to_csv(table_path, index=None)


def read_db(db_name, con):
    sql_query = "SELECT * FROM {}".format(db_name)
    df = pd.read_sql(sql_query, con)
    return df


def write_db(df, db_name, con):
    df.to_sql(db_name, con=con, index=False)


def create_db_connection(username, password, ip_address, port):
    engine_path = "postgresql://{}:{}@{}:{}".format(
        username, password, ip_address, port
    )
    engine = create_engine(engine_path)
    connection = engine.connect()
    return connection


def read_yaml(path):
    with open(path, "r") as stream:
        try:
            yaml_file = yaml.load(stream)
        except yaml.YAMLError as exc:
            raise yaml.YAMLError(exc)
    return yaml_file


def write_yaml(yaml_file, path):
    with open(path, "w") as outfile:
        yaml.dump(yaml_file, stream=outfile, default_flow_style=False)
