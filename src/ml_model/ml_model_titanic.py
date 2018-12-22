from src.components.model import Model


def create_model_titanic(x_array, y_array):
    model = Model()
    model.train_model(x_array, y_array)
    return model
