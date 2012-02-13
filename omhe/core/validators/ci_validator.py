import re,sys
from validator_errors import *

def ci_validator(omhe_value):
    valdict={}
    if len(str(omhe_value))>=0 and len(str(omhe_value))<=120:
        valdict['ci_payload']=omhe_value
        return valdict
    else:
        raise InvalidValueError("Your message must be from 1-120 characters in length.")