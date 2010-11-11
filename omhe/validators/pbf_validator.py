import re,sys
from datetime import datetime

from omhe.core.parseomhe import *
from omhe.validators.validator_errors import *
from omhe.validators.utils import *

def pbf_validator(omhe_value):
    """validate percent body fat"""
    valdict={}
    print omhe_value
    

    try:
        x=float(omhe_value)
    except:
        raise InvalidValueError("You did not specify a number for percent body fat.")
    
    if  1.0 <=  x <=  95.0:
        valdict['pbf_numeric']=omhe_value
        return valdict
    else:
        raise InvalidValueError("The value supplied for percent body fat was out of the acceptable range. It must be between 1 and 95.")    

        
