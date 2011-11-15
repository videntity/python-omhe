#An OMHE Microsyntax parser class.
# Alan Viars, Videntity 2010

import os, sys, re, uuid

try:
 import simplejson as json
except:
 import json

from datetime import datetime
from omhe.validators import *
from omhe.validators.validator_errors import *



class parseomhe:
    """A class to parse omhe strings into  their respective sub parts."""
    command_tuple=          None
    helper_tuple=           None
    validator_dict=         None
    helper_validator_dict=  None
    omhe_dict=              None
    ev_tz=                 -5
    tx_tz=                 -5

    
    def __init__(self,**kwargs):
        
        """This dict of tuples contains all possible omhe values and aliases"""
        self.command_dict={
            'bp': ('bloodpressure',),
	    'bg': ('bloodglucose',),
            'wt': ('weight',),
	    'fm': ('fatmass',),
	    'ffm': ('freefatmass',),
            'pbf': ('percentbodyfat',),
	    'st': ('steps','spd','fitbit'),
            'gbp': ('getbloodpressure',),
	    'ci': ('checkin', 'check-in','check',),
            'pn': ('pain',),
	    'md': ('mood',),
	    'frt': ('fruit',),
	    'veg': ('vegetable','veggie'),
	    'sch': ('starch',),
	    'jnk': ('junk','junkfood'),
	    'wtr': ('water', 'h2o', 'h20'),
	    'alc': ('alcohol','beer', 'wine', 'shot'),
	    'eat': ('ate', 'tweat'),
	    'gym': ('workout',),
	    'ptn': ('protien',),
	    'crb': ('starch','carb', 'carbohydrate'),
	    'dry': ('dairy',),
	    'drk': ('drink',),
	    'que': ('question',),
	    'ans': ('answer',),
	    'pts': ('points','gems'),
	    'zeo': ('sleepscore',),
	    #TODO: Add others here...    
        }


        self.helper_tuple=('id', 'dt', 'tz', 'hid', 'pw' 'pi' 'tm' 'uu', '#')
        """This tuple contains helpers"""
    
	"""
	This is where we map the command and/or its aliases to a
	validation function.  Define each function in its own file and class
	(under the validators directory).
	"""

        self.validator_dict={
                   'bp': bp_validator.bp_validator,
		   'bg': bg_validator.bg_validator,
                   'bloodpressure': bp_validator.bp_validator,
                   'bloodglucose': bg_validator.bg_validator,
                   'steps': st_validator.st_validator,
                   'spd': st_validator.st_validator,
                   'st': st_validator.st_validator,
                   'wt': wt_validator.wt_validator,
                   'weight': wt_validator.wt_validator,
		   'ffm': ffm_validator.ffm_validator,
		   'fm': fm_validator.fm_validator,
		   'pbf': pbf_validator.pbf_validator,
		   'ci': ci_validator.ci_validator,
                   'pn': pn_validator.pn_validator,
		   'md': md_validator.md_validator,
		   'frt': one_to_ten_or_blank_or_string_validator.one_to_ten_or_blank_or_string_validator,
		   'veg': one_to_ten_or_blank_or_string_validator.one_to_ten_or_blank_or_string_validator,
	           'jnk': one_to_ten_or_blank_or_string_validator.one_to_ten_or_blank_or_string_validator,
		   'wtr': one_to_ten_or_blank_or_string_validator.one_to_ten_or_blank_or_string_validator,
	           'alc': one_to_ten_or_blank_or_string_validator.one_to_ten_or_blank_or_string_validator,
		   'ptn': one_to_ten_or_blank_or_string_validator.one_to_ten_or_blank_or_string_validator,
		   'crb': one_to_ten_or_blank_or_string_validator.one_to_ten_or_blank_or_string_validator,
		   'dry': one_to_ten_or_blank_or_string_validator.one_to_ten_or_blank_or_string_validator,
		   'drk': one_to_ten_or_blank_or_string_validator.one_to_ten_or_blank_or_string_validator,
		   'eat': dummy_validator.dummy_validator,
		   'gym': dummy_validator.dummy_validator,
		   'que': dummy_validator.dummy_validator,
		   'ans': dummy_validator.dummy_validator,
		   'pts': pts_validator.pts_validator,
		   'zeo': one_to_onehundred_validator.one_to_onehundred_validator,
		   }

        
        self.helper_validator_dict={
                   'dt': dt_helper_validator.dt_helper_validator,
                   'tz': tz_helper_validator.tz_helper_validator,
                   }
        self.uu=str(uuid.uuid4())
        self.transaction_datetime=datetime.utcnow()
        self.tx_dt=self.pydt2omhedt(self.transaction_datetime)

        self.omhe_dict={'ttype':'omhe',
                        'id':self.uu,
                        'tx_dt':self.tx_dt,
                        'ev_dt':self.tx_dt,
                        'ev_tz':self.ev_tz,
                        'tx_tz':self.tx_tz,
                        }
    message = None
    command = None
    value = None
    
   
        
        
    def pydt2omhedt(self, dt_object):
	"""Convert a python datetime object to OMHE datetime string"""
        if type(dt_object)!=datetime:
            thetype=type(dt_object)
            error_string= "The object is type %s not a Datetime object" % (thetype)
            raise NotADatetimeObjectError, error_string
        
        omhedt=dt_object.strftime("%Y%m%d:%H%M%Sz")
        return omhedt
    
    
    def omhedt2pydt(self, in_string, tzo_string=None):
        """Convert a n OMHE datetime string into a python datetime object"""
        if (len(in_string)!=16):
            error_string = "Datime %s is Incorrect Length." % (in_string)
            raise InvalidHelperFormatError, error_string
        
        if (in_string[15]!="z" and in_string[15]!="Z" and in_string[15]!="u" and in_string[15]!="U"):
            error_string = "Datime %s must end in 'z' or 'u' to explicitly denote UTC." % (in_string)
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
                val=float(tzo_string)
                if not (-12.0 <= val <=14.0 ):
                    raise InvalidHelperFormatError, "TimeZoneOffset 'tz' mut be between -12 and +12"
            else:
                raise InvalidHelperFormatError, "TimeZoneOffset 'tz' is not an integer"
        else:
            """No timezone given so assuming UTC"""
            val=0
        
        dt=datetime(year, month, day, hour, minute, second, val)
        return dt
    

    
    
    def command_exists(self, omhe_command):
	"""
	Validates if the omhe command is defined and properly configured.
	Returns the core command name or raises an error.
	"""
	if type(omhe_command).__name__!='str' and type(omhe_command).__name__!='unicode':
	    """Make sure the input is a string or unicode"""
	    raise InvalidMessageError, "The omhe_command was not a string"
	
	for base_command, alias_command in self.command_dict.items():
		if alias_command.__contains__(omhe_command) or base_command==(omhe_command):
		    d={}
		    d['omhe']=omhe_command
		    return d
	raise InvalidCommandError, "This command is not defined in command_dict."
	return None
    
    def validate(self, splitdict):
	"""
	validate a dict containing the omhe command
	its value and its tags.  You can build this automatically by passing
	your message into split().
	"""
        if type(splitdict).__name__!='dict':
            raise OMHEError, "The varialbe you passed in was not a valid dict"
	
	if (not splitdict.has_key('omhe')) or (not splitdict.has_key('value')) or (not splitdict.has_key('tags')):
	    raise OMHEError, "The varialbe you passed in was not a valid omhe splitdict"

	#run the command's validator if it exists and it is defined
	if self.validator_dict.has_key(splitdict['omhe']):
	    """Validate the omhe command and value"""
	    validated_dict=self.validator_dict[splitdict['omhe']](splitdict['value'])
	
	#run the helper tag's validators if exists and are defined
	if len(splitdict['tags'])!=0:
	    helper_dict={}
	    for t in splitdict['tags']:
		for ht in self.helper_tuple:
		    if t.startswith(ht):
			helper_split=t.split(ht)
			if len(helper_split)==2:
			    ot="omhe_helper_tag_%s" % (ht)
			    helper_dict.update({ot:helper_split[1]})
			if self.helper_validator_dict.has_key(ht):
			    helper_validator_response=self.helper_validator_dict[ht](helper_split[1])
			    helper_dict.update(helper_validator_response)
	    #Add the special helper values to our dict
	    splitdict.update(helper_dict)
	    
	"""Add validated dict to splitdict"""
	splitdict.update(validated_dict)
	return splitdict

    def split(self, message):
	"""
	Split the command, value and tags into 3 parts.  Return a dict. Pass
	the result of this method to validate the data.
	"""
	
	d={}
	tags=[]
	value=None
	command=None
	"""
	Will return a either a dict containing the code and value
	or None if nothing was found
	"""
	found=False
	if type(message).__name__!='str' and type(message).__name__!='unicode':
	    """Make sure the input is a string or unicode"""
	    raise InvalidMessageError, "The message was not a string"
	
    
	"""If there's an equals then this is easier to parse"""
	if message.__contains__('='):
	    response = message.split('=')
	    command=response[0]
	    value=response[1]
	    """Verify"""
	    for base_command, alias_command in self.command_dict.items():
		if alias_command.__contains__(response[0]) or base_command==(response[0]):
		    found=True
		    command=base_command
	else:
	    """
	    Without the equals, let's tease out which omhe command we are dealing
	    with
	    """
	    
	    for i,j in self.command_dict.items():
		#print i,j
		if message.startswith(i)==True:
		    command=i
		    response = message.split(i)
		    value=response[1]
		    found=True
		for x in j:
		    
		    if message.startswith(x):
			    found=True
			    response = message.split(x)
			    command=i
			    value=response[1]
			    break
		if found:
		    break

	if not(found):
	    raise InvalidMessageError, "The message did not contain an omhe command"
	else:
		d={}
		d['omhe']=command.lower()
		d['value']=value.lower()
		
		
	"""determine if we have tags by attempting to split # """
	tag_response=d['value'].split("#")
	
	if len(tag_response)==1:
	    """If no tags"""
	    pass
	else:
	    """Tags"""
	    d['value']=tag_response[0]
	    for t in tag_response[1:]:
		tags.append(str(t))
		
	"""Add tags to our dict"""
	d['tags']=tags
	
	"""Add the origional message to our dict"""
	d['texti']=str(message)
	
	return d


    def parse(self, message, tx_dt=datetime.utcnow(), tx_tz=0):
	"""
	Parse an OMHE message and return a dictonary of its subparts
	If there is any error, do not raise the exception, but rather
	add the error to the dict
	"""
	d={}
	try:
	    s=self.split(message)
	except:
	    error= str(sys.exc_info())
	    d['error']=error
	    return d
	try:
	    d=self.validate(s)
	except:
	    error= str(sys.exc_info())
	    d['error']=error
	    return d
	"""
	all is well so lets add some additional info to our dict for
	convienence and easy uploading to RESTCat.
	"""
	#Add a unique ID
	d['id']=str(uuid.uuid4())
	
	#add transaction datetime and timexzone offset
	tx_dt=self.pydt2omhedt(tx_dt)
	d['tx_dt']=tx_dt
	d['tx_tz']="0"
	
	#Add the event datetime and timezone if not already present
	if not d.has_key("ev_dt"):
	    d['ev_dt']=tx_dt
	    
	if not d.has_key("ev_tz"):
	    d['ev_tz']="0"

	#all is well, return the dict without errors
	return d
    
    def omhedict2json(self, omhedict):
	"""Convert an omhe dict to a JSON formatted string"""
	if type(omhedict).__name__!='dict':
            raise OMHEError, "The varialbe you passed in was not a valid dict"
	jsonstr=json.dumps(omhedict, indent=4)
	return jsonstr


   
