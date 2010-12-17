import re,sys
from datetime import datetime

from omhe.core.parseomhe import *
from omhe.validators.validator_errors import *
from omhe.validators.utils import *

def dummy_validator(omhe_value):
    valdict={}
    valdict['value']=omhe_value
    return valdict