import re,sys
from validator_errors import *


def one_to_ten_or_blank_or_string_validator(omhe_value,DEFAULT_MIN_VALUE=0,DEFAULT_MAX_VALUE=10,DEFAULT_DEFAULT_VALUE=1,DEFAULT_BLANK_VALID=True,DEFAULT_STRING_VALID=True):
    """validate one to ten or blank or string"""
    valdict={}
    omhe_value=str(omhe_value)
    if omhe_value.isdigit():
        if (DEFAULT_MIN_VALUE <= int(omhe_value) <= DEFAULT_MAX_VALUE):
        # if (0 <= int(omhe_value) <= 10):
            valdict['one_to_ten_numeric']=omhe_value
        else:
            Error_Output = "You must supply a number between " + str(DEFAULT_MIN_VALUE) + " and " + str(DEFAULT_MAX_VALUE)
            if DEFAULT_BLANK_VALID == True:
                Error_Output = Error_Output + ", or a blank"
            if DEFAULT_STRING_VALID == True:
                Error_Output = Error_Output + ", or some text"
            Error_Output = Error_Output + "."
            raise InvalidValueError(Error_Output)
    elif omhe_value=="":
        valdict['one_to_ten_numeric']= str(DEFAULT_DEFAULT_VALUE)
    else:
        valdict['one_to_ten_numeric']= str(DEFAULT_DEFAULT_VALUE)
    
    return valdict
    
