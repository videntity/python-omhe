#!/usr/bin/env python

# Written By: Alan Viars, and Chris Boyce  - Videntity systems, Inc.

import sys
from omheparser import omheparser
import simplejson

class omhe2json:
    """take im a parsed omhe dict and return the data in json format"""
    
    def __init__(self, **kwargs):
        pass
    
    def omhelist2json(self, omhelist):
        
        json_object = simplejson.dumps( omhelist )

        return json_object
        
if __name__ == "__main__":
            
    try: 
        omhe_str=sys.argv[1]
    except(IndexError):
        #use a samplestring if one was not given
        omhe_str = "shc=cboyce@vIDentity.com ghc hc=http://google.com hc"
    
    print "Input omhe string is: %s" % (omhe_str) 
    try:
        o = omheparser(omhe_str = omhe_str)
        parsed = o.list
        j = omhe2json()
        jsonstr= j.omhelist2json(parsed)
        print "JSON:"
        print type(jsonstr)
    except:
        print "There was an error converting the parsing/comverting the omhe string"