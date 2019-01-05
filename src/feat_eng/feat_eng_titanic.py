from src.components.encoder import Encoder


def create_encoder_titanic(df, schema, minio_client, bucket_name):
    encoder = Encoder(minio_client, bucket_name)
    encoder.create_encoder(df, schema)
    return encoder


def do_encode(df, schema, encoder):
    x_array = encoder.apply_encoder(df, schema)
    return x_array
