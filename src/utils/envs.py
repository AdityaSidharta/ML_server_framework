import os

project_path = os.getenv("PROJECT_PATH")

postgres_username = os.getenv("POSTGRES_USERNAME")
postgres_password = os.getenv("POSTGRES_PASSWORD")
postgres_ipaddress = os.getenv("POSTGRES_IPADDRESS")

minio_access_key = os.getenv("MINIO_ACCESS_KEY")
minio_secret_key = os.getenv("MINIO_SECRET_KEY")
minio_ipaddress = os.getenv("MINIO_IPADDRESS")

data_path = os.path.join(project_path, "data")

titanic_path = os.path.join(data_path, "titanic.csv")
titanic_filename = "titanic.csv"

titanic_schema_path = os.path.join(data_path, "titanic_schema.yml")
titanic_schema_bucket = "schema"
titanic_schema_filename = "titanic_schema.yml"

titanic_encoder_filename = "titanic_encoder.pkl"
titanic_model_filename = "titanic_model.pkl"
