import re,sys
from validator_errors import *
from utils import *

def ci_validator(omhe_value):
    valdict={}
    if len(omhe_value)!=0 and len(omhe_value)<=120:
        valdict['ci_payload']=omhe_value
        return valdict
    else:
        raise InvalidValueError("You're message must be from 2-120 characters in length.")