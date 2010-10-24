import parseomhe
import urllib2, urllib, sys
#
#USERNAME='alan'
#PASSWORD='pass'
#URL="http://127.0.0.1:8000/api/create/"
#routing={
#        'sndr':"alan",
#        'rcvr':"alan",
#        'subj':"alan",
#        }
#


#def upload_OMHE_2_RESTCat(omhe_dict):
#    """Send an HTTP POST to RESTCat using a simple OMHE String"""
#    try:
#        post_dict={}
#        post_dict.update(routing)
#        post_dict['_tx_dt']=omhe_dict['_tx_dt']
#        post_dict['_tx_tz']=omhe_dict['_tx_tz']
#        post_dict['_id']=omhe_dict['_id']
#        post_dict['_texti']=omhe_dict['_texti']
#        post_dict['_ttype']='omhe'
#        x=""
#        for o in post_dict:
#           x+="%s=%s&" % (o, post_dict[o])
#        print x
#        
#        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
#       
#        passman.add_password(None, URL, USERNAME, PASSWORD)
#       
#        authhandler = urllib2.HTTPBasicAuthHandler(passman)
#       
#        opener = urllib2.build_opener(authhandler)
#        
#        urllib2.install_opener(opener)
#        data =urllib.urlencode(post_dict)
#        
#        req=urllib2.Request(URL, data)
#
#        response = urllib2.urlopen(req)    
#        status = response.code
#        print "status=%s" % (status)
#	the_page = response.read()        
#        print the_page
#
#    except urllib2.HTTPError, exc:
#        print exc.code
#        if exc.code==401:
#            raise AuthorizationRequiredError, "You are not authorized."
#        elif exc.code==400:
#            raise InvalidTemplateError, "ERROR:You supplied an invalid template name or a non-existent template."
#        else:
#            raise UnknownHTTPError, "An unknown  urllib2.HTTPError occured."
#
#if __name__ == "__main__":
#    """
#    Accept a singe omhe string from the command line. Parse, then print
#    the resulting dict, then upload to RESTCat
#    """
#    try: 
#        omhe_str=sys.argv[1]
#    except(IndexError):
#        print "You must supply an omhe message!"
#        exit(1)
#    
#    print "Input omhe string is: %s" % (omhe_str) 
#    
#    try:
#        """ Instantaiate an instance of the OMHE class"""
#        o = parseomhe.OMHE()
#        """Parse it if valid, otherwise raise the appropriate  error"""
#        d=o.parse(omhe_str)
#        """Send the OMHE dictonary to RESTCat"""
#        result=upload_OMHE_2_RESTCat(d)
#        htmlresult = result.read()
#        print htmlresult
#        
#    except():
#        print "An unexpected error occured. Here is the post-mortem:"
#        print sys.exc_info()