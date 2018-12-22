import os

project_path = os.getenv("PROJECT_PATH")
data_path = os.path.join(project_path, "data")
output_path = os.path.join(project_path, "output")

titanic_path = os.path.join(data_path, "titanic.csv")
titanic_schema_path = os.path.join(output_path, "titanic.yml")
