import re,sys
from parseomhe import *
from datetime import datetime


def bp_validator(omhe_value):
    """Validate blood pressure information"""
    try:
        if omhe_value.isdigit():
    
            syst=omhe_value[0:3]
            dia=omhe_value[3:6]
            pul=omhe_value[6:9]
            valdict={'syst':syst,
                    'dia':dia,
                    'pul':pul,}
            return valdict
        
        if omhe_value.__contains__('/'):
            sys_delin='/'
        elif omhe_value.__contains__('d'):
            sys_delin='d'
        else: 
            raise InvalidValueError, "Invalid bp syntax"
            
        
        splstr1=omhe_value.split(sys_delin)
        if len(splstr1) !=2:
            raise InvalidValueError, "Invalid bp syntax"
        syst=splstr1[0]

        if syst.isdigit()==False:
            raise InvalidValueError, "Systolic value is not a number"
        
        if ( 20 > int(syst)) or (int(syst) > 500):
            raise InvalidValueError, "Systolic value is out of range"
        
        
        splstr2=splstr1[1].split('p')
        dia=splstr2[0]

        if dia.isdigit()==False:
            raise InvalidValueError, "Diastolic value not a number"
        elif (20 > int(dia)) or (int(dia)> 500):
            raise InvalidValueError, "Diastolic value out of range"
        valdict={
                'syst':syst,
                'dia':dia,
                }
        if len(splstr2)==2:
            """Get the pulse if provided"""
            pul=splstr2[1]
            if pul.isdigit()==False:
                raise InvalidValueError, "Pulse not a number"
            elif (10 > int(pul)) or (int(pul) > 500):
                raise InvalidValueError, "Pulse value out of range"
            valdict['pul']=pul
                
        return valdict
    
    
    
    
    except:
        print sys.exc_info()
        exit(1)
        #raise InvalidValueError, "Not a valid blood pressure format"
    

def sbp_validator(omhe_value):

    if (len(omhe_value)!=15):
        error_string = "Datime %s is Incorrect Length." % (omhe_value)
        return error_string
    else:
        return  None
    
    
def validateEmail(email):
    """ Validates that email is well-formed."""
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return True
    return False

def dt_helper_validator(helper_value):
    if (len(helper_value)!=16):
        error_string = "Datime %s is Incorrect Length." % (helper_value)
        raise InvalidHelperFormatError, error_string
    
    if (helper_value[15]!="z" and helper_value[15]!="Z"):
        error_string = "Datime %s must end in Z to explicitly denote UTC." % (helper_value)
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
    return {'_ev_dt':dt}
    

def tz_helper_validator(helper_value):
    if helper_value.isdigit():
        val=int(helper_value)
        if not (-12 <= val <=12 ):
            raise InvalidHelperFormatError, "TimeZoneOffset 'tz' mut be between -12 and +12"
    else:
        raise InvalidHelperFormatError, "TimeZoneOffset 'tz' is not an integer"
    _ev_tz=val
    return {'_ev_tz':_ev_tz}


if __name__ == "__main__":
    print "hi"