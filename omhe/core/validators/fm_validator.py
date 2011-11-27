import re,sys
from validator_errors import *

def fm_validator(omhe_value):
    valdict={}
    if omhe_value.endswith('l') or omhe_value.endswith('k'):
        valdict['fm_numeric']=omhe_value[:-1]
        valdict['fm_measure_unit']=omhe_value[-1]
    else:
        valdict['fm_numeric']=omhe_value
        valdict['fm_measure_unit']="l"
        
    try:
        f=float(valdict['fm_numeric'])
        if f < 1.0:
            error_msg="Fat mass may not be less than 1."
            raise InvalidValueError(error_msg)
        
    except ValueError:
        error_msg="I could not validate the value %s is not a numerical fat mass. " % (valdict['fm_numeric'])
        raise InvalidMessageError(error_msg)

    return valdict
