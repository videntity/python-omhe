import re,sys
from validator_errors import *

"""
moods=10 is evaluated but returns an error.

Routine must either
a) not handle moods as a valid command
b) handle moods as a command and evaluate the string correctly
it seems to be executing "mood" and then failing because first character is not a number [s]

"""


def md_validator(omhe_value,DEFAULT_MIN_VALUE=0,DEFAULT_MAX_VALUE=10,DEFAULT_DEFAULT_VALUE=1,DEFAULT_BLANK_VALID=False,DEFAULT_STRING_VALID=False):
    """validate mood"""
    valdict={}
    
    if omhe_value.isdigit():
        valdict['md_numeric']=omhe_value
    else:
        Error_Output = "You must supply a number between " + str(DEFAULT_MIN_VALUE) + " (worst) and " + str(DEFAULT_MAX_VALUE) + " (best) for mood"
        if DEFAULT_BLANK_VALID == True:
            Error_Output = Error_Output + ", or a blank"
        if DEFAULT_STRING_VALID == True:
            Error_Output = Error_Output + ", or some text"
        Error_Output = Error_Output + "."

        raise InvalidValueError(Error_Output)
    try:
        x=float(valdict['md_numeric'])
        if DEFAULT_MIN_VALUE <= x <= DEFAULT_MAX_VALUE:
            return valdict

        Error_Output = "You must supply a number between " + str(DEFAULT_MIN_VALUE) + " (worst) and " + str(DEFAULT_MAX_VALUE) + " (best) for mood"
        if DEFAULT_BLANK_VALID == True:
            Error_Output = Error_Output + ", or a blank"
        if DEFAULT_STRING_VALID == True:
            Error_Output = Error_Output + ", or some text"
        Error_Output = Error_Output + "."

        raise InvalidValueError(Error_Output)
    except:
        Error_Output = "You must supply a number between " + str(DEFAULT_MIN_VALUE) + " (worst) and " + str(DEFAULT_MAX_VALUE) + " (best) for mood"
        if DEFAULT_BLANK_VALID == True:
            Error_Output = Error_Output + ", or a blank"
        if DEFAULT_STRING_VALID == True:
            Error_Output = Error_Output + ", or some text"
        Error_Output = Error_Output + "."

        raise InvalidValueError(Error_Output)
        
