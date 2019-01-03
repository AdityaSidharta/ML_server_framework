import numpy as np

from sklearn.compose import ColumnTransformer
from sklearn.externals import joblib
from sklearn.preprocessing import OneHotEncoder


class Encoder:
    def __init__(self):
        self.encoder = None
        self.init = False

    def _is_init(self):
        assert self.init, "Encoder have not been initialized using read_encoder / create_encoder"

    def get_n_features(self):
        self._is_init()
        return self.encoder.n_values_.sum()

    def read_encoder(self, encoder_path):
        self.encoder = joblib.load(encoder_path)
        self.init = True

    def write_encoder(self, encoder_path):
        self._is_init()
        joblib.dump(self.encoder, encoder_path)

    def create_encoder(self, df, schema):
        encoder_columns = schema.get_oh_encoding_cols()
        for column in encoder_columns:
            df[column] = df[column].astype(str)
        self.encoder = ColumnTransformer([('oh_enc', OneHotEncoder(sparse=False, handle_unknown='ignore'),
                                           encoder_columns)],
                                         remainder='passthrough', sparse_threshold=0.0)
        self.encoder.fit(df)
        self.init = True

    def apply_encoder(self, df, schema):
        self._is_init()
        encoder_columns = schema.get_oh_encoding_cols()
        for column in encoder_columns:
            df[column] = df[column].astype(str)
        x_values = self.encoder.transform(df)
        return x_values
