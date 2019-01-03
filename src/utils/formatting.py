import pandas as pd


def df_na_value(df, schema):
    column_names = schema.get_col_names()
    for column_name in column_names:
        if column_name in df.columns:
            column_na_value = schema.get_col_na_value(column_name)
            df[column_name] = df[column_name].fillna(column_na_value)
    return df


def df_format(df, schema):
    """converting all columns within a dataframe to have a certain type, as defined in int_cols, float_cols, str_cols,
    and date_cols"""
    int_cols = schema.get_int_cols()
    float_cols = schema.get_float_cols()
    str_cols = schema.get_str_cols()
    date_cols = schema.get_date_cols()
    time_cols = schema.get_time_cols()

    for column_name in int_cols:
        if column_name in df.columns:
            df[column_name] = df[column_name].astype(int)
    for column_name in float_cols:
        if column_name in df.columns:
            df[column_name] = df[column_name].astype(float)
    for column_name in str_cols:
        if column_name in df.columns:
            df[column_name] = df[column_name].astype(str)
    for column_name in date_cols:
        if column_name in df.columns:
            date_format = schema.get_col_format(column_name)
            df[column_name] = pd.to_datetime(df[column_name], format=date_format)
    for column_name in time_cols:
        if column_name in df.columns:
            time_format = schema.get_col_format(column_name)
            df[column_name] = pd.to_datetime(df[column_name], format=time_format)
    return df
