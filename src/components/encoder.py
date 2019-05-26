from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

from src.utils.ds import get_latest_version
from src.utils.io import download_minio, write_minio, read_model, write_model


class Encoder:
    def __init__(self, minio_client, bucket_name):
        self.encoder = None
        self.init = False
        self.minio_client = minio_client
        self.bucket_name = bucket_name

    def _is_init(self):
        assert self.init, "Encoder have not been initialized using read_encoder / create_encoder"

    def get_n_features(self):
        self._is_init()
        return self.encoder.n_values_.sum()

    def load_encoder(self, encoder_name):
        self.init = True
        bucket_name = get_latest_version(self.minio_client)
        print("Using version: {}".format(bucket_name))
        download_minio(self.minio_client, bucket_name, encoder_name)
        self.encoder = read_model(encoder_name)

    def save_encoder(self, encoder_name):
        self._is_init()
        write_model(self.encoder, encoder_name)
        write_minio(self.minio_client, self.bucket_name, encoder_name)

    def create_encoder(self, df, schema):
        encoder_columns = schema.get_oh_encoding_cols()
        for column in encoder_columns:
            df[column] = df[column].astype(str)
        self.encoder = ColumnTransformer(
            [("oh_enc", OneHotEncoder(sparse=False, handle_unknown="ignore"), encoder_columns)],
            remainder="passthrough",
            sparse_threshold=0.0,
        )
        self.encoder.fit(df)
        self.init = True

    def apply_encoder(self, df, schema):
        self._is_init()
        encoder_columns = schema.get_oh_encoding_cols()
        for column in encoder_columns:
            df[column] = df[column].astype(str)
        x_values = self.encoder.transform(df)
        return x_values
