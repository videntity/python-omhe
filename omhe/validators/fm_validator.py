import re,sys
from datetime import datetime

from omhe.core.parseomhe import *
from omhe.validators.validator_errors import *
from omhe.validators.utils import *

def fm_validator(omhe_value):
    valdict={}
    
    if omhe_value.isdigit():
        valdict['fm_numeric']=omhe_value
        valdict['fm_measure_unit']="l"
        try:
            x=float(valdict['fm_numeric'])
            return valdict
        except:
            raise InvalidValueError("You didn't supply a numerical fat mass. ")
            
    if omhe_value.endswith('l'):
        valdict['fm_numeric']=omhe_value[:-1]
        valdict['fm_measure_unit']="l"
        try:
            x=float(valdict['fm_numeric'])
            return valdict
        except:
            raise InvalidValueError("You didn't supply a numerical fat mass. ")
        
    
    if omhe_value.endswith('k'):
        valdict['fm_numeric']=omhe_value[:-1]
        valdict['fm_measure_unit']="k"
        try:
            x=float(valdict['fm_numeric'])
            return valdict 
        except:
            raise InvalidValueError("You didn't supply a numerical fat mass. ")
    
    error_msg="I could not validate the value %s" % (omhe_value)
    raise InvalidMessageError(error_msg)