import pandas as pd

from sklearn.externals import joblib
from sklearn.preprocessing import OneHotEncoder

class Encoder:
    def __init__(self):
        self.encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
        self.is_trained = False

    def _check_trained(self):
        assert self.is_trained, "Encoder have not been initialized using read_encoder / create_encoder"

    def get_n_features(self):
        self._check_trained()
        return self.encoder.n_values_.sum()

    def read_encoder(self, encoder_path):
        self.encoder = joblib.load(encoder_path)
        self.is_trained = True

    def write_encoder(self, encoder_path):
        joblib.dump(self.encoder, encoder_path)

    def create_encoder(self, df, schema):
        encoder_columns = schema.get_oh_encoding_cols()
        df_oh = df[encoder_columns].copy().astype(str)
        x_oh = df_oh.values
        self.encoder.fit(x_oh)
        self.is_trained = True

    def apply_encoder(self, df, schema):
        encoder_columns = schema.get_oh_encoding_cols()
        non_columns = schema.get_non_encoding_cols()

        df_non = df[non_columns].copy()
        df_oh = df[encoder_columns].copy().astype(str)

        x_oh = df_oh.values
        x_transform = self.encoder.transform(x_oh)
        df_transform = pd.DataFrame
