import pandas as pd



def df_format_datatype(
    df, schema, date_format=None
):
    """converting all columns within a dataframe to have a certain type, as defined in int_cols, float_cols, str_cols,
    and date_cols"""
    for column in int_cols:
        if column in df.columns:
            df[column] = df[column].astype(int)
    for column in float_cols:
        if column in df.columns:
            df[column] = df[column].astype(float)
    for column in str_cols:
        if column in df.columns:
            df[column] = df[column].astype(str)
    if date_format:
        for column in date_cols:
            if column in df.columns:
                df[column] = pd.to_datetime(df[column], format=date_format)
    else:
        for column in date_cols:
            if column in df.columns:
                df[column] = pd.to_datetime(df[column])
    return df