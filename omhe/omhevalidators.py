import re,sys
from parseomhe import *
from datetime import datetime


def st_validator(omhe_value):
    print """validate steps"""
    print omhe_value
    valdict={}
    
    try:
        if omhe_value.isdigit():
            valdict['st_numeric']=omhe_value
        try:
            x=float(valdict['st_numeric'])
            return valdict
        except:
            raise InvalidValueError("You didn't suply a numer of steps")
        
    except:
        error_msg="I could not validate the value %s" % (omhe_value)
        raise InvalidMessageError(error_message)




def wt_validator(omhe_value):
    valdict={}
    
    if omhe_value.isdigit():
        valdict['wt_numeric']=omhe_value
        valdict['wt_measure_unit']="l"
        try:
            x=float(valdict['wt_numeric'])
            return valdict
        except:
            raise InvalidValueError("You didn't suply a numerical weight")
            
    if omhe_value.endswith('l'):
        valdict['wt_numeric']=omhe_value[:-1]
        valdict['wt_measure_unit']="l"
        try:
            x=float(valdict['wt_numeric'])
            return valdict
        except:
            raise InvalidValueError("You didn't supply a numerical weight")
        
    
    if omhe_value.endswith('k'):
        valdict['wt_numeric']=omhe_value[:-1]
        valdict['wt_measure_unit']="k"
        try:
            x=float(valdict['wt_numeric'])
            return valdict 
        except:
            raise InvalidValueError("You didn't supply a numerical weight")
    
    error_msg="I could not validate the value %s" % (omhe_value)
    raise InvalidMessageError(error_message)


def bp_validator(omhe_value):
    """Validate blood pressure information"""
    try:
        if omhe_value.isdigit():
            bp_syst=omhe_value[0:3]
            bp_dia=omhe_value[3:6]
            bp_pul=omhe_value[6:9]
            valdict={'bp_syst':bp_syst,
                    'bp_dia':bp_dia,
                    'bp_pul':bp_pul,}
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
        bp_syst=splstr1[0]

        if bp_syst.isdigit()==False:
            raise InvalidValueError, "Systolic value is not a number"
        
        if ( 20 > int(bp_syst)) or (int(bp_syst) > 500):
            raise InvalidValueError, "Systolic value is out of range"
        
        
        splstr2=splstr1[1].split('p')
        bp_dia=splstr2[0]

        if bp_dia.isdigit()==False:
            raise InvalidValueError, "Diastolic value not a number"
        elif (20 > int(bp_dia)) or (int(bp_dia)> 500):
            raise InvalidValueError, "Diastolic value out of range"
        valdict={
                'bp_syst':bp_syst,
                'bp_dia':bp_dia,
                }
        if len(splstr2)==2:
            """Get the pulse if provided"""
            bp_pul=splstr2[1]
            if bp_pul.isdigit()==False:
                raise InvalidValueError, "Pulse not a number"
            elif (10 > int(bp_pul)) or (int(bp_pul) > 500):
                raise InvalidValueError, "Pulse value out of range"
            valdict['bp_pul']=bp_pul
                
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
    return { 'ev_dt': helper_value,
            }
    

def tz_helper_validator(helper_value):
    if helper_value.isdigit():
        val=int(helper_value)
        if not (-12 <= val <=12 ):
            raise InvalidHelperFormatError, "TimeZoneOffset 'tz' mut be between -12 and +12"
    else:
        raise InvalidHelperFormatError, "TimeZoneOffset 'tz' is not an integer"
    _ev_tz=val
    return {'ev_tz':ev_tz}


if __name__ == "__main__":
    print "hi"