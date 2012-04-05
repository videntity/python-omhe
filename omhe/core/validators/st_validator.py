import re,sys
from validator_errors import *

"""
Steps Validator:
- Doesn't handle tags
- Doesn't handle minutes

"""

def st_validator(omhe_value):
    """validate steps"""
    valdict={}
    
    if omhe_value.isdigit():
        valdict['st_numeric']=omhe_value
    try:
        x=float(valdict['st_numeric'])
        return valdict
    except:
        raise InvalidValueError("You didn't supply a number of steps")
        
