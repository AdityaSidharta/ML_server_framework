from src.components.schema import Schema
from src.utils.formatting import df_format, df_na_value


def infer_schema(df):
    schema = Schema()
    schema.infer_schema(df)
    return schema


def do_fill_na_value(df, schema):
    df = df_na_value(df, schema)
    return df


def do_format(df, schema):
    df = df_format(df, schema)
    return df
