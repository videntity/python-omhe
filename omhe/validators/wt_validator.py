import re,sys
from datetime import datetime

from omhe.core.parseomhe import *
from omhe.validators.validator_errors import *
from omhe.validators.utils import *

def wt_validator(omhe_value):
    valdict={}
    
    if omhe_value.isdigit():
        valdict['wt_numeric']=omhe_value
        valdict['wt_measure_unit']="l"
        try:
            x=float(valdict['wt_numeric'])
            return valdict
        except:
            raise InvalidValueError("You didn't suply a numerical weight")
            
    if omhe_value.endswith('l'):
        valdict['wt_numeric']=omhe_value[:-1]
        valdict['wt_measure_unit']="l"
        try:
            x=float(valdict['wt_numeric'])
            return valdict
        except:
            raise InvalidValueError("You didn't supply a numerical weight")
        
    
    if omhe_value.endswith('k'):
        valdict['wt_numeric']=omhe_value[:-1]
        valdict['wt_measure_unit']="k"
        try:
            x=float(valdict['wt_numeric'])
            return valdict 
        except:
            raise InvalidValueError("You didn't supply a numerical weight")
    
    error_msg="I could not validate the value %s" % (omhe_value)
    raise InvalidMessageError(error_msg)