import re,sys
from validator_errors import *

def pn_validator(omhe_value):
    """validate pain"""
    valdict={}
    
    if omhe_value.isdigit():
        valdict['pn_numeric']=omhe_value
    else:
        raise InvalidValueError("You must supply a number between 1 (best) and 10 (worst) for pain level.")
    try:
        x=float(valdict['pn_numeric'])
        if 0 <= x <= 10:
            return valdict
        raise InvalidValueError("You must supply a number between 1 (best) and 10 (worst) for pain level.")
    except:
        raise InvalidValueError("You must supply a number between 1 (best) and 10 (worst) for pain level.")
        
