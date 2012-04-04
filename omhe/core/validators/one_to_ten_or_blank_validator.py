import re,sys
from validator_errors import *

DEFAULT_ONE_TEN_BK_MIN_VALUE       = 0
DEFAULT_ONE_TEN_BK_MAX_VALUE       = 10
DEFAULT_ONE_TEN_BK_DEFAULT_VALUE   = "1"
DEFAULT_ONE_TEN_BK_BLANK_VALID     = True
DEFAULT_ONE_TEN_BK_STRING_VALID    = False


def one_to_ten_or_blank_validator(omhe_value,DEFAULT_MIN_VALUE=0,DEFAULT_MAX_VALUE=10,DEFAULT_DEFAULT_VALUE=1,DEFAULT_BLANK_VALID=True,DEFAULT_STRING_VALID=False):
    """validate one to ten or blank"""
    valdict={}
    omhe_value=str(omhe_value)
    if omhe_value=="":
        valdict['one_to_ten_numeric']=DEFAULT_DEFAULT_VALUE
    elif omhe_value.isdigit() and  (DEFAULT_MIN_VALUE <= int(omhe_value) <= DEFAULT_MAX_VALUE):
        valdict['one_to_ten_numeric']=omhe_value
    else:
        Error_Output = "You must supply a number between " + str(DEFAULT_MIN_VALUE) + " and " + str(DEFAULT_MAX_VALUE)
        if DEFAULT_BLANK_VALID == True:
            Error_Output = Error_Output + ", or a blank"
        if DEFAULT_STRING_VALID == True:
            Error_Output = Error_Output + ", or some text"
        Error_Output = Error_Output + "."

        raise InvalidValueError(Error_Output)
    
    return valdict
    
