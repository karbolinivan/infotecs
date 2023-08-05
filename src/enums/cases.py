from enum import Enum

from src.base.helps import helper
from src.enums.messages import Message, StatusCode


class Cases(Enum):
    X_INT_Y_INT = helper.get_numbers(x_type="INT", y_type="INT")
    X_INT_Y_N_INT = helper.get_numbers(x_type="INT", y_type="N_INT")
    X_N_INT_Y_INT = helper.get_numbers(x_type="N_INT", y_type="INT")
    X_N_INT_Y_N_INT = helper.get_numbers(x_type="N_INT", y_type="N_INT")

    X_ZERO_Y_INT = helper.get_numbers(x_type="ZERO", y_type="INT")
    X_INT_Y_ZERO = helper.get_numbers(x_type="INT", y_type="ZERO")
    X_ZERO_Y_ZERO = helper.get_numbers(x_type="ZERO", y_type="ZERO")
    X_N_INT_Y_ZERO = helper.get_numbers(x_type="N_INT", y_type="ZERO")
    X_ZERO_Y_N_INT = helper.get_numbers(x_type="ZERO", y_type="N_INT")

    X_INT_D_Y_ZERO = helper.get_numbers(x_type="INT",y_type="ZERO"), Message.CALCULATION_ERROR, StatusCode.CALCULATION_ERROR
    X_ZERO_D_Y_ZERO = helper.get_numbers(x_type="ZERO", y_type="ZERO"), Message.CALCULATION_ERROR, StatusCode.CALCULATION_ERROR
    X_N_INT_D_Y_ZERO = helper.get_numbers(x_type="N_INT", y_type="ZERO"), Message.CALCULATION_ERROR, StatusCode.CALCULATION_ERROR

    X_FLOAT_Y_INT = helper.get_numbers(x_type="FLOAT", y_type="INT"), Message.NOT_INTEGER, StatusCode.NOT_INTEGER
    X_INT_Y_FLOAT = helper.get_numbers(x_type="INT", y_type="FLOAT"), Message.NOT_INTEGER, StatusCode.NOT_INTEGER
    X_FLOAT_Y_FLOAT = helper.get_numbers(x_type="FLOAT", y_type="FLOAT"), Message.NOT_INTEGER, StatusCode.NOT_INTEGER
    X_N_FLOAT_Y_INT = helper.get_numbers(x_type="N_FLOAT", y_type="INT"), Message.NOT_INTEGER, StatusCode.NOT_INTEGER
    X_INT_Y_N_FLOAT = helper.get_numbers(x_type="INT", y_type="N_FLOAT"), Message.NOT_INTEGER, StatusCode.NOT_INTEGER
    X_N_FLOAT_Y_N_FLOAT = helper.get_numbers(x_type="INT", y_type="N_FLOAT"), Message.NOT_INTEGER, StatusCode.NOT_INTEGER

    X_INT_Y_STR = helper.get_numbers(x_type="INT", y="y"), Message.NOT_INTEGER, StatusCode.NOT_INTEGER
    X_STR_Y_INT = helper.get_numbers(x="x", y_type="INT"), Message.NOT_INTEGER, StatusCode.NOT_INTEGER
    X_STR_Y_STR = helper.get_numbers(x="x", y="y"), Message.NOT_INTEGER, StatusCode.NOT_INTEGER

    X_INT_Y_EMPTY = helper.get_invalid_dict(key="x"), Message.MISSING_KEYS, StatusCode.MISSING_KEYS
    X_EMPTY_Y_INT = helper.get_invalid_dict(key="y"), Message.MISSING_KEYS, StatusCode.MISSING_KEYS
    X_EMPTY_Y_EMPTY = helper.get_invalid_dict(), Message.MISSING_KEYS, StatusCode.MISSING_KEYS

    X_INT_Y_SIZE = helper.get_numbers(x_type="INT", y=10 ** 100), Message.VALUE_SIZE_EXCEEDED, StatusCode.VALUE_SIZE_EXCEEDED
    X_SIZE_Y_INT = helper.get_numbers(x=10 ** 100, y_type="INT"), Message.VALUE_SIZE_EXCEEDED, StatusCode.VALUE_SIZE_EXCEEDED
    X_SIZE_Y_SIZE = helper.get_numbers(x=10 ** 100, y=10 ** 100), Message.VALUE_SIZE_EXCEEDED, StatusCode.VALUE_SIZE_EXCEEDED

    def __getitem__(self, key):
        return self.value.get(key)

    @classmethod
    def get_calculation_parametrize(cls, case, func: str):
        result = helper.get_result(case=case, func=func)
        return case.value, result
