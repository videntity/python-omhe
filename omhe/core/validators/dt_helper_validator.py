from datetime import datetime
import re,sys
from validator_errors import *
from utils import *

def dt_helper_validator(helper_value):

    if helper_value.startswith("="):
        helper_value=helper_value[1:]
    
    """ Validate datetime helper."""
    if (len(helper_value)!=16):
        error_string = "Dateime %s is Incorrect Length." % (helper_value)
        raise InvalidHelperFormatError, error_string
    
    if (helper_value[15]!="z" and helper_value[15]!="Z"):
        error_string = "Dateime %s must end in Z to explicitly denote UTC." % (helper_value)
        raise InvalidHelperFormatError, error_string

    year=str(helper_value[0:4])
    if year.isdigit():
        year=int(year)
    else:
        raise InvalidHelperFormatError, "Year is not an integer"
    
    month=helper_value[4:6]
    if month.isdigit():
        month=int(month)
    else:
        raise InvalidHelperFormatError, "Month is not an integer"
    
    
    day=helper_value[6:8]
    if day.isdigit():
        day=int(day)
    else:
        raise InvalidHelperFormatError, "Day is not an integer"
    
    hour=helper_value[9:11]
    if hour.isdigit():
        hour=int(hour)
    else:
        raise InvalidHelperFormatError, "Hour is not an integer"
        
    minute=helper_value[11:13]
    if minute.isdigit():
        minute=int(minute)
    else:
        raise InvalidHelperFormatError, "Minute is not an integer"
        
    second=helper_value[13:15]
    if second.isdigit():
        second=int(second)
    else:
        raise InvalidHelperFormatError, "Second is not an integer"
    dt=datetime(year, month, day, hour, minute, second, 0)
    return { 'evdt': helper_value,
            }