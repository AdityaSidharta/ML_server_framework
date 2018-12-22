def split_target_columns(df, schema):
    target_cols = schema.get_target_cols()
    non_target_cols = schema.get_non_target_cols()

    df_x, y_array = df[non_target_cols].copy(), df[target_cols].values
    return df_x, y_array
