from datetime import datetime
import re,sys
from validator_errors import *
from utils import *

def tz_helper_validator(helper_value):
    
    if helper_value.startswith("="):
        helper_value=omhe_value[1:]
    
    """ Validate timezone helper."""
    if type(helper_value).__name__!='str' and \
       type(helper_value).__name__!='unicode' and \
       type(helper_value).__name__!='int' and \
       type(helper_value).__name__!='float':
	    """Make sure the input is a string or unicode"""
	    raise InvalidMessageError, "The omhe_command was not a string"
    
    if helper_value.find(":")!=-1:
        orig_value=helper_value
        helper_value=helper_value.replace(":",".")
    try:
        val=float(helper_value)
    except:
        
        raise InvalidHelperFormatError, "TimeZoneOffset 'tz' is not an integer or float"
    
    if not (-12 <= val <=14 ):
        raise InvalidHelperFormatError, "TimeZoneOffset 'tz' mut be between -12 and +14"
    
    helper_value=helper_value.replace(".",":")
    
    return {'event_timezone':helper_value}
    
    