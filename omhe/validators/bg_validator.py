import re,sys
from datetime import datetime

from omhe.core.parseomhe import *
from omhe.validators.validator_errors import *
from omhe.validators.utils import *

def bg_validator(omhe_value):
    """validate blood glucose"""
    valdict={}
    
    if omhe_value.isdigit():
        valdict['bg_numeric']=omhe_value
    try:
        x=float(valdict['bg_numeric'])
        return valdict
    except:
        raise InvalidValueError("You didn't suply a numer for blood glucose")
        
