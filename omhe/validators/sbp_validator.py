import re,sys
from datetime import datetime

from omhe.core.parseomhe import *
from omhe.validators.validator_errors import *
from omhe.validators.utils import *

def sbp_validator(omhe_value):

    if (len(omhe_value)>100):
        error_string = "Incorrect Length." % (omhe_value)
        return error_string
    else:
        return  None