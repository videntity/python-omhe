import re,sys
from datetime import datetime

from omhe.core.parseomhe import *
from omhe.validators.validator_errors import *
from omhe.validators.utils import *

def one_to_ten_or_blank_validator(omhe_value):
    """validate one to ten or blank"""
    valdict={}
    omhe_value=str(omhe_value)
    if omhe_value=="":
        valdict['one_to_ten_numeric']="1"
    elif omhe_value.isdigit() and  (0 <= int(omhe_value) <= 10):
        valdict['one_to_ten_numeric']=omhe_value
    else:
        raise InvalidValueError("You must supply a number between 1 and 10 or blank.")
    
    return valdict
    
