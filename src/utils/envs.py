import os

project_path = os.getenv("PROJECT_PATH")
postgres_username = os.getenv("POSTGRES_USERNAME")
postgres_password = os.getenv("POSTGRES_PASSWORD")
postgres_ipaddress = os.getenv("POSTGRES_IPADDRESS")
postgres_port = os.getenv("POSTGRES_PORT")

data_path = os.path.join(project_path, "data")
output_path = os.path.join(project_path, "output")

titanic_path = os.path.join(data_path, "titanic.csv")
titanic_filename = "titanic"

titanic_schema_path = os.path.join(output_path, "titanic.yml")
titanic_encoder_path = os.path.join(output_path, "titanic_enc.pkl")
titanic_model_path = os.path.join(output_path, "titanic_model.pkl")
