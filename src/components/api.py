from src.components.schema import Schema
from src.components.model import Model
from src.components.encoder import Encoder

from src.data_prep.prep_titanic import do_format, do_fill_na_value, infer_schema
from src.feat_eng.feat_eng_titanic import do_encode, create_encoder_titanic
from src.ml_model.ml_model_titanic import create_model_titanic
from src.utils.ds import split_target_columns

class Api:
    def __init__(self, schema_path, encoder_path, model_path):
        self.schema_path = schema_path
        self.encoder_path = encoder_path
        self.model_path = model_path
        self.schema = Schema()
        self.schema.load_schema(schema_path)
        print(schema_path)
        print(self.schema.yaml_file)
        self.encoder = None
        self.model = None
        self.init = False


    def _is_init(self):
        assert self.init, "Model not been initialized using load_components / fit_api"

    def load_components(self):
        self.encoder = Encoder()
        self.encoder.read_encoder(self.encoder_path)
        self.model = Model()
        self.model.load_model(self.model_path)
        self.init = True

    def save_components(self):
        self._is_init()
        self.encoder.write_encoder(self.encoder_path)
        self.model.save_model(self.model_path)

    def fit_api(self, df_full):
        self.init = True

        # data_prep
        df, y_array = split_target_columns(df_full, self.schema)
        df = do_fill_na_value(df, self.schema)
        df = do_format(df, self.schema)

        # feat_eng
        self.encoder = create_encoder_titanic(df, self.schema)
        x_array = do_encode(df, self.schema, self.encoder)

        # ml_model
        self.model = create_model_titanic(x_array, y_array)

        self.save_components()


    def predict_api(self, df):
        self._is_init()

        # data_prep
        df = do_fill_na_value(df, self.schema)
        df = do_format(df, self.schema)

        # feat_eng
        x_array = do_encode(df, self.schema, self.encoder)

        return self.model.predict_model(x_array)
