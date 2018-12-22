import numpy as np

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
        self.encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
        encoder_columns = schema.get_oh_encoding_cols()
        df_oh = df[encoder_columns].copy().astype(str)
        x_oh = df_oh.values
        self.encoder.fit(x_oh)
        self.init = True

    def apply_encoder(self, df, schema):
        self._is_init()
        encoder_columns = schema.get_oh_encoding_cols()
        non_columns = schema.get_non_encoding_cols()

        df_non = df[non_columns].copy()
        df_oh = df[encoder_columns].copy().astype(str)

        x_non = df_non.values
        x_oh = df_oh.values
        x_transform = self.encoder.transform(x_oh)
        x_full = np.concatenate((x_non, x_transform), axis = 1)
        return x_full
