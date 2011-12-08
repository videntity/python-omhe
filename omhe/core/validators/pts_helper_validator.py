import re,sys
from validator_errors import *

def pts_helper_validator(omhe_value):
    """validate positive or negative integer"""
    
    if omhe_value.startswith("="):
        omhe_value=omhe_value[1:]
    valdict={}
    negative=False
    print omhe_value
    if omhe_value.isdigit() or omhe_value[1:].isdigit():
        valdict['points']=omhe_value
    else:
        raise InvalidValueError("You must supply a whole number")
    
    return valdict
