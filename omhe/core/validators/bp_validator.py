import re,sys
from validator_errors import *


def bp_validator(omhe_value):
    val_dict={}
    """bp_validator"""

    if omhe_value.isdigit() and len(omhe_value)==9:
        bp_systolic=omhe_value[0:3]
        bp_diastolic=omhe_value[3:6]
        bp_pulse=omhe_value[6:9]
        valdict={'bp_systolic':bp_systolic,
                'bp_diastolic':bp_diastolic,
                'bp_pulse':bp_pulse,}
        return valdict
    
    if omhe_value.__contains__('/'):
        sys_delin='/'
    elif omhe_value.__contains__('d'):
        sys_delin='d'
    else:  
        raise InvalidValueError, "Invalid bp syntax"
        error_additional_info
    
    splstr1=omhe_value.split(sys_delin)
    if len(splstr1) !=2:
        raise InvalidValueError, "Invalid bp syntax"
    bp_systolic=splstr1[0]

    if bp_systolic.isdigit()==False:
        raise InvalidValueError, "Systolic value is not a number"
    
    if ( 20 > int(bp_systolic)) or (int(bp_systolic) > 500):
        raise InvalidValueError, "Systolic value is out of range"
    
    
    splstr2=splstr1[1].split('p')
    bp_diastolic=splstr2[0]

    if bp_diastolic.isdigit()==False:
        raise InvalidValueError, "Diastolic value not a number"
    elif (20 > int(bp_diastolic)) or (int(bp_diastolic)> 500):
        raise InvalidValueError, "Diastolic value out of range"
    valdict={
            'bp_systolic':bp_systolic,
            'bp_diastolic':bp_diastolic,
            }
    if len(splstr2)==2:
        """Get the pulse if provided"""
        bp_pulse=splstr2[1]
        if bp_pulse.isdigit()==False:
            raise InvalidValueError, "Pulse not a number"
        elif (10 > int(bp_pulse)) or (int(bp_pulse) > 500):
            raise InvalidValueError, "Pulse value out of range"
        valdict['bp_pulse']=bp_pulse
            
    return valdict