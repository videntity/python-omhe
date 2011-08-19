import re,sys
from datetime import datetime

from omhe.core.parseomhe import *
from omhe.validators.validator_errors import *
from omhe.validators.utils import *

def one_to_onehundred_validator(omhe_value):
    """validate one to one hundred"""
    valdict={}
    omhe_value=str(omhe_value)
    if omhe_value.isdigit() and  (0 <= int(omhe_value) <= 100):
        valdict['one_to_ten_numeric']=omhe_value
    else:
        raise InvalidValueError("You must supply a number between 1 and 100.")
    
    return valdict