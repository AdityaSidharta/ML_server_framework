from src.components.model import Model


def create_model_titanic(x_array, y_array, minio_client, bucket_name):
    model = Model(minio_client, bucket_name)
    model.train_model(x_array, y_array)
    return model
