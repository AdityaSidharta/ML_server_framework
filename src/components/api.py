import datetime as dt

from src.components.encoder import Encoder
from src.components.model import Model
from src.components.schema import Schema
from src.components.ml.preparation.prep_titanic import do_format, do_fill_na_value
from src.components.ml.transformation.feat_eng_titanic import do_encode, create_encoder_titanic
from src.components.ml.model.ml_model_titanic import create_model_titanic
from src.utils.ds import split_target_columns


class Api:
    def __init__(self, schema_name, encoder_name, model_name, minio_client):
        self.schema_name = schema_name
        self.encoder_name = encoder_name
        self.model_name = model_name
        self.minio_client = minio_client
        self.bucket_name = dt.datetime.now().strftime("%Y%m%d%H%M")
        self.schema = Schema(self.minio_client)
        self.schema.load_schema(schema_name)
        self.encoder = None
        self.model = None
        self.init = False

    def _is_init(self):
        assert self.init, "Model not been initialized using load_components / fit_api"

    def save_components(self):
        self._is_init()
        self.encoder.save_encoder(self.encoder_name)
        self.model.save_model(self.model_name)

    def load_api(self):
        self.encoder = Encoder(self.minio_client, self.bucket_name)
        self.encoder.load_encoder(self.encoder_name)
        self.model = Model(self.minio_client, self.bucket_name)
        self.model.load_model(self.model_name)
        self.init = True

    def fit_api(self, df_full):
        self.init = True

        # data_prep
        df_full = do_fill_na_value(df_full, self.schema)
        df_full = do_format(df_full, self.schema)
        df, y_array = split_target_columns(df_full, self.schema)

        # feat_eng
        self.encoder = create_encoder_titanic(df, self.schema, self.minio_client, self.bucket_name)
        x_array = do_encode(df, self.schema, self.encoder)

        # ml_model
        self.model = create_model_titanic(x_array, y_array, self.minio_client, self.bucket_name)

        self.save_components()

    def predict_api(self, df):
        self._is_init()

        # data_prep
        df = do_fill_na_value(df, self.schema)
        df = do_format(df, self.schema)

        # feat_eng
        x_array = do_encode(df, self.schema, self.encoder)

        return self.model.predict_model(x_array).item()
