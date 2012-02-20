from datetime import datetime
import re, sys, time
from validator_errors import *
from utils import *

def dt_helper_validator(helper_value):

    if helper_value.startswith("="):
        helper_value=helper_value[1:]
    
    try:
        time_struct = time.strptime(helper_value, "%Y%m%d:%H%M%Sz")
        mydate= datetime.fromtimestamp(time.mktime(time_struct))
    except:
        try:
            time_struct = time.strptime(helper_value, "%Y%m%d:%H%M%SZ")
            mydate= datetime.fromtimestamp(time.mktime(time_struct))
        except:
            try:
                time_struct = time.strptime(helper_value, "%Y%m%d:%H%M%S")
                mydate= datetime.fromtimestamp(time.mktime(time_struct))
            except:
                raise InvalidHelperFormatError, "The datetime was not formatted correctly."
    
    return { 'event_datetime': str(mydate)}