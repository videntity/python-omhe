import re,sys
from datetime import datetime

from omhe.core.parseomhe import *
from omhe.validators.validator_errors import *
from omhe.validators.utils import *


def bp_validator(omhe_value):
    val_dict={}
    """bp_validator"""
    if omhe_value.isdigit() and len(omhe_value)==9:
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
        error_additional_info
    
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