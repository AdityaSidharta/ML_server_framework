from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegressionCV


class Model:
    def __init__(self):
        self.model = None
        self.init = False

    def _is_init(self):
        assert self.init, "Model have not been initialized using load_model / train_model"

    def load_model(self, model_path):
        self.model = joblib.load(model_path)
        self.init = True

    def save_model(self, model_path):
        self._is_init()
        joblib.dump(self.model, model_path)

    def train_model(self, x_array, y_array):
        self.model = LogisticRegressionCV(100, cv=5, max_iter=1000, n_jobs=-1)
        self.model.fit(x_array, y_array)
        self.init = True

    def predict_model(self, x_array):
        self._is_init()
        result = self.model.predict_proba(x_array)
        return result[:, 0]
