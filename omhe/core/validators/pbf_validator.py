import re,sys
from validator_errors import *



def pbf_validator(omhe_value,DEFAULT_MIN_VALUE=1,DEFAULT_MAX_VALUE=95,DEFAULT_DEFAULT_VALUE=1,DEFAULT_BLANK_VALID=False,DEFAULT_STRING_VALID=False):
    """validate percent body fat"""
    valdict={}
    print omhe_value
    

    try:
        x=float(omhe_value,)
    except:
        raise InvalidValueError("You did not specify a number for percent body fat.")
    
    if  DEFAULT_MIN_VALUE <=  x <=  DEFAULT_MAX_VALUE:
        valdict['pbf_numeric']=omhe_value
        return valdict
    else:
        Error_Output = "The value supplied for percent body fat was outside the acceptable range. It must be between " + str(DEFAULT_MIN_VALUE) + " and " + str(DEFAULT_MAX_VALUE)
        if DEFAULT_BLANK_VALID == True:
            Error_Output = Error_Output + ", or a blank"
        if DEFAULT_STRING_VALID == True:
            Error_Output = Error_Output + ", or some text"

        Error_Output = Error_Output + "."

        raise InvalidValueError(Error_Output)


        
