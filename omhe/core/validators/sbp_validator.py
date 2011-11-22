import re,sys
from validator_errors import *
from utils import validateEmail

def sbp_validator(omhe_value):
    valdict={}
    if validateEmail(omhe_value):
        valdict['sbp_to']=omhe_value
    else:
        error_msg="The email address '%s'did not validate." % (omhe_value)
        raise InvalidValueError(error_msg)

    return valdict
