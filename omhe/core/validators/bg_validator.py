import re,sys
from validator_errors import *


def bg_validator(omhe_value):
    """validate blood glucose"""
    valdict={}

    if omhe_value.isdigit():
        if float(omhe_value)>=0 and float(omhe_value)<=400:
            valdict['bg_numeric']=omhe_value
            return valdict
        else:
            raise InvalidValueError("The Blood glucose number should be in range:0-400")

    raise InvalidValueError("You didn't supply a number for blood pressure")