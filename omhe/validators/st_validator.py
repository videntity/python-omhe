import re,sys
from datetime import datetime

from omhe.core.parseomhe import *
from omhe.validators.validator_errors import *
from omhe.validators.utils import *

def st_validator(omhe_value):
    """validate steps"""
    valdict={}
    
    try:
        if omhe_value.isdigit():
            valdict['st_numeric']=omhe_value
        try:
            x=float(valdict['st_numeric'])
            return valdict
        except:
            raise InvalidValueError("You didn't suply a numer of steps")
        
    except:
        error_msg="I could not validate the value %s" % (omhe_value)
        raise InvalidMessageError(error_msg)
