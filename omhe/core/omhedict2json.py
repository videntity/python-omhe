#!/usr/bin/env python


# Videntity
# Author: Alan Viars

import sys
from omhe.core.parseomhe import parseomhe
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
        print "Please provide an omhe message."
    
    print "Input omhe string is: %s" % (omhe_str) 
    try:
        o = parseomhe(omhe_str)
        parsed = o.list
        j = omhe2json()
        jsonstr= j.omhelist2json(parsed)
        print "JSON:"
        print type(jsonstr)
    except:
        print "There was an error parsing/converting the omhe string"