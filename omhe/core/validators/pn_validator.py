import re,sys
from validator_errors import *

"""
Accept a number between 1 and 10 with an optional text message.

painful gets accepted as a valid key
but the validator then fails because it evaluates [ful=5] as not being a number

"""

def pn_validator(omhe_value,DEFAULT_MIN_VALUE=0,DEFAULT_MAX_VALUE=10,DEFAULT_DEFAULT_VALUE=1,DEFAULT_BLANK_VALID=False,DEFAULT_STRING_VALID=True):
    """validate pain"""
    valdict={}
    
    if omhe_value.isdigit():
        valdict['pn_numeric']=omhe_value
    else:
        Error_Output = "You must supply a whole number between " + str(DEFAULT_MIN_VALUE) + " (best) and " + str(DEFAULT_MAX_VALUE) + " (worst) for pain level"
        if DEFAULT_BLANK_VALID == True:
            Error_Output = Error_Output + ", or a blank"
        if DEFAULT_STRING_VALID == True:
            Error_Output = Error_Output + ", or some text"
        Error_Output = Error_Output + "."

        raise InvalidValueError(Error_Output)

    try:
        x=float(valdict['pn_numeric'])
        if DEFAULT_MIN_VALUE <= x <= DEFAULT_MAX_VALUE:
            return valdict

        Error_Output = "You must supply a whole number between " + str(DEFAULT_MIN_VALUE) + " (best) and " + str(DEFAULT_MAX_VALUE) + " (worst) for pain level"
        if DEFAULT_BLANK_VALID == True:
            Error_Output = Error_Output + ", or a blank"
        if DEFAULT_STRING_VALID == True:
            Error_Output = Error_Output + ", or some text"
        Error_Output = Error_Output + "."

        raise InvalidValueError(Error_Output)
    except:
        Error_Output = "You must supply a whole number between " + str(DEFAULT_MIN_VALUE) + " (best) and " + str(DEFAULT_MAX_VALUE) + " (worst) for pain level"
        if DEFAULT_BLANK_VALID == True:
            Error_Output = Error_Output + ", or a blank"
        if DEFAULT_STRING_VALID == True:
            Error_Output = Error_Output + ", or some text"
        Error_Output = Error_Output + "."

        raise InvalidValueError(Error_Output)
        
