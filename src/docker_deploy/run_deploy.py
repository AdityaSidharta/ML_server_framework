import pandas as pd
from flask_restful import reqparse, Resource

from src.components.api import Api
from src.docker_deploy import app, api
from src.utils.conn import docker_minio_client
from src.utils.envs import titanic_schema_filename, titanic_encoder_filename, titanic_model_filename
from src.utils.validation import validate_int, validate_str


class Prediction(Resource):
    def __init__(self, **kwargs):
        self.model = kwargs["model"]
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("class")
        self.parser.add_argument("sex")
        self.parser.add_argument("age")
        self.parser.add_argument("embarked")

    @staticmethod
    def _validate(input_class, input_sex, input_age, input_embarked):
        status_message = dict()
        if input_class is not None:
            if not validate_int(input_class, 1, 3):
                status_message["class"] = "Class of the Passenger, should be in range[1, 3]"
        if input_sex is not None:
            if not validate_str(input_sex, ["male", "female"]):
                status_message["sex"] = "Gender of the Passenger, one of the following [male, female]"
        if input_age is not None:
            if not validate_int(input_age, 0, 100):
                status_message["age"] = "Age of the Passenger, should be in range [0, 100]"
        if input_embarked is not None:
            if not validate_str(input_embarked, ["C", "S", "Q"]):
                status_message["embarked"] = "Port of Embarkation of the Passenger, one of the following [C, S, Q]"
        if status_message:
            return 400, status_message
        else:
            return 200, "OK"

    @staticmethod
    def _output(status_code, status_message, args, result):
        return (
            {
                "data": {"result": result},
                "message": {"status_code": status_code, "status_message": status_message, "args": args},
            },
            status_code,
        )

    def get(self):
        args = self.parser.parse_args()
        input_class, input_sex, input_age, input_embarked = (args["class"], args["sex"], args["age"], args["embarked"])
        status_code, status_message = self._validate(input_class, input_sex, input_age, input_embarked)
        if status_code == 200:
            input_df = pd.DataFrame(
                {"class": [input_class], "sex": [input_sex], "age": [input_age], "embarked": [input_embarked]}
            )
            result = self.model.predict_api(input_df)
            return self._output(status_code, status_message, args, result)
        else:
            return self._output(status_code, status_message, args, 0.0)


def main():
    model = Api(titanic_schema_filename, titanic_encoder_filename, titanic_model_filename, docker_minio_client)
    model.load_api()
    api.add_resource(Prediction, "/", resource_class_kwargs={"model": model})
    app.config["BUNDLE_ERRORS"] = True
    app.run(host="0.0.0.0", port=1234, debug=True)


if __name__ == "__main__":
    main()
