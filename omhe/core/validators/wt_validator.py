import re,sys
from datetime import datetime
from validator_errors import *


def wt_validator(omhe_value):
    valdict={}
    if omhe_value.endswith('l') or omhe_value.endswith('k'):
        valdict['wt_numeric']=omhe_value[:-1]
        valdict['wt_measure_unit']=omhe_value[-1]
    else:
        valdict['wt_numeric']=omhe_value
        valdict['wt_measure_unit']="l"
        
    try:
        f=float(valdict['wt_numeric'])
        if f < 0:
            error_msg="Weight may not be less than 0"
            raise InvalidValueError(error_msg)
        
    except ValueError:
        error_msg="I could not validate the value %s." % (valdict['wt_numeric'])
        raise InvalidMessageError(error_msg)
    
    return valdict