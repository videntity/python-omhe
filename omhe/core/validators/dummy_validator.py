import re,sys
from validator_errors import *
from utils import *

def dummy_validator(omhe_value):
    valdict={}
    valdict['value']=omhe_value
    return valdict