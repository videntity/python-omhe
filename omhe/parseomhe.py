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

class OMHE:
    """A class to parse omhe strings into  their respective sub parts."""
    command_tuple=          None
    helper_tuple=           None
    validator_dict=         None
    helper_validator_dict=  None
    omhe_dict=              None
    uu=                     None
    pydatetime=             None
    _tx_dt=                 None    
    _ev_dt=                 None
    
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
        self.pydatetime=datetime.utcnow()
        self._ev_dt="%s%s%s:%s%s%su" % (self.pydatetime.year,
                                        self.pydatetime.month,
                                        self.pydatetime.day,
                                        self.pydatetime.hour,
                                        self.pydatetime.minute,
                                        self.pydatetime.second,
                                        )
        self._tx_dt="%s%s%s:%s%s%su" % (self.pydatetime.year,
                                        self.pydatetime.month,
                                        self.pydatetime.day,
                                        self.pydatetime.hour,
                                        self.pydatetime.minute,
                                        self.pydatetime.second,
                                        )
        
        self.omhe_dict={'uu':self.uu, 'datetime': self.pydatetime,
                        '_ev_dt':self._ev_dt, '_tx_dt':self._tx_dt                
                        }
    
    message = None
    command = None
    value = None
    
    def parse(self, message):
        found=False
        tags=[]
        
        if type(message).__name__!='str':
            raise InvalidMessageError, "The message was not a string"
        message=message.lower()
        self.message=message
        
        """If there's an equals then this is easier to parse"""
        if message.__contains__('='):
            response = message.split('=')
            if self.command_tuple.__contains__(response[0]):
                
                tag_response=response[1].split("#")
                if len(tag_response)==1:
                    """If no tags"""
                    if self.validator_dict.has_key(response[0]):
                        validatedict=self.validator_dict[response[0]](response[1])
                        
                    splitdict.update({'command': response[0],
                       'value': response[1],
                       'tags':tags
                       })
                    splitdict.update(validatedict)
                    self.omhe_dict.update(splitdict)       
                    return self.omhe_dict
                else:
                    """Tags were found"""
                    value=tag_response[0]
                    for t in tag_response[1:]:
                        tags.append(t)
                    
                    """proccess tags that are helpers"""
                    for t in tags:
                        for ht in self.helper_tuple:
                            if t.startswith(ht):
                                helper_split=t.split(ht)
                                if len(helper_split)==2:
                                    self.omhe_dict.update({ht:helper_split[1]})
                                if self.helper_validator_dict.has_key(ht):
                                    helper_validator_response=self.helper_validator_dict[ht](helper_split[1])
                                    self.omhe_dict.update({'_ev_dt':helper_validator_response})
                    
                    self.omhe_dict.update({'command': response[0],
                           'value': tag_response[0],
                           'tags': tags,
                           })
                    
                    
                    if self.validator_dict.has_key(response[0]):
                        validatedict=self.validator_dict[response[0]](tag_response[0])
                        self.omhe_dict.update(validatedict)        
                    return self.omhe_dict
            else:
                error_message="%s is not an OMHE command" % response[0]
                raise InvalidCommandError, error_message

        """
        Without the equals, lets tease out which omhe command we are dealing
        with
        """

        for c in self.command_tuple:
            if message.startswith(c):
                found=True
                response = message.split(c)
                command=c
                value=response[1]
            
        tag_response=value.split("#")
        if len(tag_response)==1:
            """No tags"""    
            pass
        else:
            """tags in message"""
            for t in tag_response[1:]:
                tags.append(t)
            value=tag_response[0]
            
        self.omhe_dict.update({
                    'command': command,
                    'value': value,
                    'tags': tags,
                    })
        """proccess tags that are helpers"""
        for t in tags:
            for ht in self.helper_tuple:
                if t.startswith(ht):
                    helper_split=t.split(ht)
                    if len(helper_split)==2:
                        self.omhe_dict.update({ht:helper_split[1]})
                    if self.helper_validator_dict.has_key(ht):
                        helper_validator_response=self.helper_validator_dict[ht](helper_split[1])
                        self.omhe_dict.update({'_ev_dt':helper_validator_response})

        if self.validator_dict.has_key(self.omhe_dict['command']):
                    value_to_validate=self.omhe_dict['value']
                    validatedict=self.validator_dict[self.omhe_dict['command']](value)
                    self.omhe_dict.update(validatedict)          
        return self.omhe_dict
                        
            
        if found==False:
            error_message="An OMHE command was not found in message %s" % message
            raise InvalidCommandError, error_message
        
                
if __name__ == "__main__":
    
          
    try: 
        omhe_str=sys.argv[1]
    except(IndexError):
        print "You must supply an omhe message!"
        exit(1)
    
    print "Input omhe string is: %s" % (omhe_str) 
    
    try:
        o = OMHE()
        d=o.parse(omhe_str)
        print d
        
    except():
        print "An unexpected error occured. Here is the post-mortem:"
        print sys.exc_info()
