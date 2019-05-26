from sklearn.linear_model import LogisticRegressionCV

from src.utils.ds import get_latest_version
from src.utils.io import download_minio, read_model, write_minio, write_model, list_bucket_minio


class Model:
    def __init__(self, minio_client, bucket_name):
        self.model = None
        self.init = False
        self.minio_client = minio_client
        self.bucket_name = bucket_name

    def _is_init(self):
        assert self.init, "Model have not been initialized using load_model / train_model"

    def load_model(self, model_name):
        self.init = True
        bucket_name = get_latest_version(self.minio_client)
        print(bucket_name)
        download_minio(self.minio_client, bucket_name, model_name)
        self.model = read_model(model_name)

    def save_model(self, model_name):
        self._is_init()
        write_model(self.model, model_name)
        write_minio(self.minio_client, self.bucket_name, model_name)

    def train_model(self, x_array, y_array):
        self.model = LogisticRegressionCV(100, cv=5, max_iter=1000, n_jobs=-1)
        self.model.fit(x_array, y_array)
        self.init = True

    def predict_model(self, x_array):
        self._is_init()
        result = self.model.predict_proba(x_array)
        return result[:, 0]
