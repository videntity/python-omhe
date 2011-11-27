import re,sys
from validator_errors import *

def st_validator(omhe_value):
    """validate steps"""
    valdict={}
    
    if omhe_value.isdigit():
        valdict['st_numeric']=omhe_value
    try:
        x=float(valdict['st_numeric'])
        return valdict
    except:
        raise InvalidValueError("You didn't suply a numer of steps")
        
