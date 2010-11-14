import re,sys
from datetime import datetime

from omhe.core.parseomhe import *
from omhe.validators.validator_errors import *
from omhe.validators.utils import *

def md_validator(omhe_value):
    """validate mood"""
    valdict={}
    
    if omhe_value.isdigit():
        valdict['md_numeric']=omhe_value
    else:
        raise InvalidValueError("You must supply a number between 1 (worst) and 10 (best) for mood.")
    try:
        x=float(valdict['md_numeric'])
        if 0 <= x <= 10:
            return valdict
        raise InvalidValueError("You must supply a number between 1 (worst) and 10 (best) for mood.")
    except:
        raise InvalidValueError("You must supply a number between 1 (worst) and 10 (best) for mood.")
        
