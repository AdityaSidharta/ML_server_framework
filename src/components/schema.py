from src.utils.io import read_yaml, write_yaml
import numpy as np
from collections import OrderedDict


class Schema:
    def __init__(self):
        self.init = False
        self.yaml_file = None

    def _is_init(self):
        assert self.init, "Schema has not been initialized"

    def get_col_type(self, column_name):
        self._is_init()
        return self.yaml_file[column_name]["type"]

    def get_col_na_value(self, column_name):
        self._is_init()
        return self.yaml_file[column_name]["na_value"]

    def get_col_format(self, column_name):
        self._is_init()
        return self.yaml_file[column_name]["format"]

    def get_col_encoding(self, column_name):
        self._is_init()
        return self.yaml_file[column_name]["encoding"]

    def get_col_target(self, column_name):
        self._is_init()
        return self.yaml_file[column_name]['target']

    def get_col_names(self):
        self._is_init()
        return list(self.yaml_file.keys())

    def get_int_cols(self):
        self._is_init()
        return [
            column_name
            for column_name in self.get_col_names()
            if self.get_col_type(column_name) == "int"
        ]

    def get_float_cols(self):
        self._is_init()
        return [
            column_name
            for column_name in self.get_col_names()
            if self.get_col_type(column_name) == "float"
        ]

    def get_str_cols(self):
        self._is_init()
        return [
            column_name
            for column_name in self.get_col_names()
            if self.get_col_type(column_name) == "str"
        ]

    def get_date_cols(self):
        self._is_init()
        return [
            column_name
            for column_name in self.get_col_names()
            if self.get_col_type(column_name) == "date"
        ]

    def get_time_cols(self):
        self._is_init()
        return [
            column_name
            for column_name in self.get_col_names()
            if self.get_col_type(column_name) == "time"
        ]

    def get_non_encoding_cols(self):
        self._is_init()
        return [
            column_name
            for column_name in self.get_col_names()
            if self.get_col_encoding(column_name) == ""
        ]

    def get_oh_encoding_cols(self):
        self._is_init()
        return [
            column_name
            for column_name in self.get_col_names()
            if self.get_col_encoding(column_name) == "OneHotEncoder"
        ]

    def get_non_target_cols(self):
        self._is_init()
        return [column_name for column_name in self.get_col_names() if self.get_col_target(column_name) == False]

    def get_target_cols(self):
        self._is_init()
        return [column_name for column_name in self.get_col_names() if self.get_col_target(column_name) == True]

    def infer_schema(self, df):
        df = df.infer_objects()
        int_cols = df.select_dtypes("int").columns
        float_cols = df.select_dtypes("float").columns
        date_cols = df.select_dtypes("datetime").columns
        time_cols = df.select_dtypes("timedelta").columns

        yaml_result = OrderedDict()
        for column_name in df.columns:
            if column_name in int_cols:
                yaml_result[column_name] = {
                    "type": "int",
                    "na_value": -1,
                    "encoding": "",
                    "target": False
                }
            elif column_name in float_cols:
                yaml_result[column_name] = {
                    "type": "float",
                    "na_value": np.nan,
                    "encoding": "OneHotEncoder",
                    "target": False
                }
            elif column_name in date_cols:
                yaml_result[column_name] = {
                    "type": "date",
                    "na_value": np.datetime64("NaT"),
                    "format": "",  # TODO : Perform automatic inference on the datetime format,
                    "encoding": "",
                    "target": False
                }
            elif column_name in time_cols:
                yaml_result[column_name] = {
                    "type": "time",
                    "na_value": np.timedelta64("NaT"),
                    "format": "",
                    "encoding": "OneHotEncoder",
                    "target": False
                }
            else:
                yaml_result[column_name] = {
                    "type": "str",
                    "na_value": "",
                    "encoding": "OneHotEncoder",
                    "target": False
                }
        self.yaml_file = yaml_result

    def load_schema(self, yaml_path):
        self.init = True
        self.yaml_file = read_yaml(yaml_path)

    def write_schema(self, out_path):
        self._is_init()
        write_yaml(self.yaml_file, out_path)
