import re,sys
from validator_errors import *


def bg_validator(omhe_value):
    """validate blood glucose"""
    valdict={}
    
    if omhe_value.isdigit():
        valdict['bg_numeric']=omhe_value
    try:
        x=float(valdict['bg_numeric'])
        return valdict
    except:
        raise InvalidValueError("You didn't supply a number for blood glucose")
        
