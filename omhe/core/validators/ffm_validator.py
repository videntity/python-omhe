import re,sys
from validator_errors import *

def ffm_validator(omhe_value):
    valdict={}
    
    if omhe_value.isdigit():
        valdict['ffm_numeric']=omhe_value
        valdict['ffm_measure_unit']="l"
        try:
            x=float(valdict['ffm_numeric'])
            return valdict
        except:
            raise InvalidValueError(" You didn't supply a numerical free fat mass. ")
            
    if omhe_value.endswith('l'):
        valdict['ffm_numeric']=omhe_value[:-1]
        valdict['ffm_measure_unit']="l"
        try:
            x=float(valdict['ffm_numeric'])
            return valdict
        except:
            raise InvalidValueError(" You didn't supply a numerical free fat mass. ")
        
    
    if omhe_value.endswith('k'):
        valdict['ffm_numeric']=omhe_value[:-1]
        valdict['ffm_measure_unit']="k"
        try:
            x=float(valdict['ffm_numeric'])
            return valdict 
        except:
            raise InvalidValueError(" You didn't supply a numerical free fat mass. ")
    
    error_msg="I could not validate the value %s" % (omhe_value)
    raise InvalidMessageError(error_msg)