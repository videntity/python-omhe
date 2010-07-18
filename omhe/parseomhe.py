#An OMHE Microsyntax parser class.
# Alan Viars, Videntity 2010

import os, sys, re, uuid
from datetime import datetime
from omhevalidators import *


class OMHEError(Exception): pass
class InvalidCommandError(OMHEError):pass
class InvalidValueError(OMHEError):pass
class InvalidMessageError(OMHEError):pass
class InvalidHelperFormatError(OMHEError):pass
class NotADatetimeObjectError(OMHEError):pass
class DatetimeFormatError(OMHEError):pass

class OMHE:
    """A class to parse omhe strings into  their respective sub parts."""
    command_tuple=          None
    helper_tuple=           None
    validator_dict=         None
    helper_validator_dict=  None
    omhe_dict=              None
    _ev_tz=                 -5
    _tx_tz=                 -5

    
    def __init__(self,**kwargs):
        self.command_tuple=('hp', 'help', 'bp', 'bloodpressure', 'getbloodpressure', 'gbp',
              'sbp', 'sendbloodpressure', 'mc', 'menstralcycle', 'wt', 'weight',
              'gwt', 'getweight', 'swt', 'sendweight', 'bmi', 'bodymassindex',
              'tsk', 'task', 'sta', 'start', 'sto', 'stop', 'sp', 'sleep', 'gsp',
              'getsleep', 'ssp', 'sendslp', 'sw', 'swim', 'ca', 'calories',
              'pain', 'pn', 'gpn', 'getpain', 'spn', 'sendpain', 'mood', 'md',
              'gmd', 'getmood', 'smd', 'sendmood', 'ci','checkin')
        """This tuple contains all possible omhe values"""
    
        
        self.helper_tuple=('id', 'dt', 'tz', 'hid', 'pw' 'pi' 'tm' 'uu', '#')
        """This tuple contains helpers"""
    
        self.validator_dict={
                   'bp': bp_validator,
                   'bloodpressure': bp_validator,
                   }
        
        
        self.helper_validator_dict={
                   'dt': dt_helper_validator,
                   'tz': tz_helper_validator
                   }
        self.uu=str(uuid.uuid4())
        self.transaction_datetime=datetime.utcnow()
        self._tx_dt=self.pydt2omhedt(self.transaction_datetime)
                
        self.omhe_dict={'_ttype':'omhe',
                        '_id':self.uu,
                        '_tx_dt':self._tx_dt,
                        '_ev_dt':self._tx_dt,
                        '_ev_tz':self. _ev_tz,
                        '_tx_tz':self._tx_tz                 
                        }
    
    message = None
    command = None
    _value = None
    
    def parse(self, message):
        """Parse an OMHE message and return a dictonary of its subparts"""
        found=False
        _tags=[]
	splitdict={}        
        if type(message).__name__!='str' and type(message).__name__!='unicode':
            raise InvalidMessageError, "The message was not a string"
        message=message.lower()
        self.message=message
        self.omhe_dict['_texti']=self.message
        """If there's an equals then this is easier to parse"""
        if message.__contains__('='):
            response = message.split('=')
            if self.command_tuple.__contains__(response[0]):
                
                tag_response=response[1].split("#")
                if len(tag_response)==1:
                    """If no tags"""
                    if self.validator_dict.has_key(response[0]):
                        validatedict=self.validator_dict[response[0]](response[1])
                        
                    splitdict.update({'_omhe': response[0],
                       '_value': response[1],
                       '_tags':_tags
                       })
                    splitdict.update(validatedict)
                    self.omhe_dict.update(splitdict)       
                    return self.omhe_dict
                else:
                    """Tags were found"""
                    _value=tag_response[0]
                    for t in tag_response[1:]:
                        _tags.append(t)
                    
                    """proccess tags that are helpers"""
                    for t in _tags:
                        for ht in self.helper_tuple:
                            if t.startswith(ht):
                                helper_split=t.split(ht)
                                if len(helper_split)==2:
                                    ot="omhe_helper_tag_%s" % (ht)
                                    self.omhe_dict.update({ot:helper_split[1]})
                                if self.helper_validator_dict.has_key(ht):
                                    helper_validator_response=self.helper_validator_dict[ht](helper_split[1])
                                    self.omhe_dict.update(helper_validator_response)
                    
                    self.omhe_dict.update({'_omhe': response[0],
                           '_value': tag_response[0],
                           '_tags': _tags,
                           })
                    
                    
                    if self.validator_dict.has_key(response[0]):
                        validatedict=self.validator_dict[response[0]](tag_response[0])
                        self.omhe_dict.update(validatedict)        
                    return self.omhe_dict
            else:
                error_message="%s is not an OMHE command" % response[0]
                raise InvalidCommandError, error_message

        """
        Without the equals, let's tease out which omhe command we are dealing
        with
        """

        for c in self.command_tuple:
            if message.startswith(c):
                found=True
                response = message.split(c)
                command=c
                _value=response[1]
            
        tag_response=_value.split("#")
        if len(tag_response)==1:
            """No tags"""    
            pass
        else:
            """tags in message"""
            for t in tag_response[1:]:
                _tags.append(t)
            _value=tag_response[0]
            
        self.omhe_dict.update({
                    '_omhe': command,
                    '_value': _value,
                    '_tags': _tags,
                    })
        """proccess tags that are helpers"""
        for t in _tags:
            for ht in self.helper_tuple:
                if t.startswith(ht):
                    helper_split=t.split(ht)
                    if len(helper_split)==2:
                        ot="omhe_helper_tag_%s" % (ht)
                        self.omhe_dict.update({ot:helper_split[1]})
                    if self.helper_validator_dict.has_key(ht):
                        helper_validator_response=self.helper_validator_dict[ht](helper_split[1])
                        self.omhe_dict.update(helper_validator_response)

        if self.validator_dict.has_key(self.omhe_dict['_omhe']):
                    value_to_validate=self.omhe_dict['_value']
                    validatedict=self.validator_dict[self.omhe_dict['_omhe']](_value)
                    self.omhe_dict.update(validatedict)          
        return self.omhe_dict
                        
            
        if found==False:
            error_message="An OMHE command was not found in message %s" % message
            raise InvalidCommandError, error_message
        
        
    def pydt2omhedt(self, dt_object):

        if type(dt_object)!=datetime:
            thetype=type(dt_object)
            error_string= "The object is type %s not a Datetime object" % (thetype)
            raise NotADatetimeObjectError, error_string
        
        omhedt=dt_object.strftime("%Y%m%d:%H%M%Sz")
        return omhedt
    
    
    def omhedt2pydt(self, in_string, tzo_string=None):
        """Convert a datetime string into a python datetime object"""
        if (len(helper_value)!=16):
            error_string = "Datime %s is Incorrect Length." % (in_string)
            raise InvalidHelperFormatError, error_string
        
        if (in_string[15]!="z" and in_string[15]!="Z"):
            error_string = "Datime %s must end in Z to explicitly denote UTC." % (in_string)
            raise InvalidHelperFormatError, error_string
    
        year=str(in_string[0:4])
        if year.isdigit():
            year=int(year)
        else:
            raise InvalidHelperFormatError, "Year is not an integer."
        
        month=in_string[4:6]
        if month.isdigit():
            month=int(month)
        else:
            raise InvalidHelperFormatError, "Month is not an integer."
        
        
        day=in_string[6:8]
        if day.isdigit():
            day=int(day)
        else:
            raise InvalidHelperFormatError, "Day is not an integer."
        
        hour=in_string[9:11]
        if hour.isdigit():
            hour=int(hour)
        else:
            raise InvalidHelperFormatError, "Hour is not an integer."
            
        minute=in_string[11:13]
        if minute.isdigit():
            minute=int(minute)
        else:
            raise InvalidHelperFormatError, "Minute is not an integer."
            
        second=in_string[13:15]
        if second.isdigit():
            second=int(second)
        else:
            raise InvalidHelperFormatError, "Second is not an integer."
        
        if tzo_string:
            if tzo_string.isdigit():
                val=int(tzo_string)
                if not (-12 <= val <=12 ):
                    raise InvalidHelperFormatError, "TimeZoneOffset 'tz' mut be between -12 and +12"
            else:
                raise InvalidHelperFormatError, "TimeZoneOffset 'tz' is not an integer"
        else:
            """No timezone given so assuming UTC"""
            val=0
        
        dt=datetime(year, month, day, hour, minute, second, val)
        return dt
    
        
                
if __name__ == "__main__":
    """
    Accept a singe omhe string from the command line. Parse, then print
    the resulting dict.
    """
    try: 
        omhe_str=sys.argv[1]
    except(IndexError):
        print "You must supply an omhe message!"
        exit(1)
    
    print "Input omhe string is: %s" % (omhe_str) 
    
    try:
        """ Instantaiate an instance of the OMHE class"""
        o = OMHE()
        """Parse it if valid, otherwise raise the appropriate  error"""
        d=o.parse(omhe_str)
        """Print the dictonary"""
        print d
        
    except():
        print "An unexpected error occured. Here is the post-mortem:"
        print sys.exc_info()
