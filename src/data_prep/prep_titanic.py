from src.components.schema import Schema
from src.utils.envs import titanic_schema_path
from src.utils.formatting import df_format, df_na_value


def create_titanic_schema(df):
    schema = Schema()
    schema.infer_schema(df)
    schema.write_schema(titanic_schema_path)


def do_fill_na_value(df, schema):
    df = df_na_value(df, schema)
    return df


def do_format(df, schema):
    df = df_format(df, schema)
    return df
