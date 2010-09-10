import pycurl
import sys
import parseomhe
from settings import USERNAME, PASSWORD, SENDER, RECEIVER, SUBJECT, SEC_LEVEL, RESTCAT_SERVER


URL="%s/api/create/" % (RESTCAT_SERVER)
routing={
        'sndr':SENDER,
        'rcvr':RECEIVER,
        'subj': SUBJECT,
         'sec': SEC_LEVEL,
        }

def upload_OMHE_2_RESTCat(omhe_dict, outfile, username, password):
    f = open(outfile, "wb")
    """Send an HTTP POST to RESTCat using a simple OMHE String"""
    pf=[]
    post_dict={}
    
    """ The type of transaction"""
    post_dict['ttype']='omhe'
    post_dict.update(routing)
    
    """ The transaction's date/time/zone"""
    post_dict['tx_dt']=omhe_dict['tx_dt']
    post_dict['tx_tz']=omhe_dict['tx_tz']
    
    """ The event's date/time/zone"""
    post_dict['ev_dt']=omhe_dict['ev_dt']
    post_dict['ev_tz']=omhe_dict['ev_tz']
    
    """ The transaction's uuid"""
    post_dict['id']=omhe_dict['id']
    
    """ The transaction's text item (ASCII payload)."""
    post_dict['texti']=omhe_dict['texti']
    
    
    for o in post_dict:
        x=(str(o), str(post_dict[o]))
        pf.append(x)
    print pf
    user_and_pass="%s:%s" % (username, password)    
    c = pycurl.Curl()
    c.setopt(pycurl.URL, URL)
    c.setopt(c.HTTPPOST, pf)
    c.setopt(c.WRITEDATA, f) 
    c.setopt(pycurl.HTTPHEADER, ["Accept:"])
    c.setopt(pycurl.USERPWD, user_and_pass)
    c.perform()
    f.close() 
    return c
    

if __name__ == "__main__":
    """
    Accept a singe omhe string from the command line. Parse, then print
    the resulting dict, then upload to RESTCat
    """
    try: 
        omhe_str=sys.argv[1]
    except(IndexError):
        print "You must supply an omhe message!"
        exit(1)
        
    try: 
        out_file=sys.argv[2]
    except(IndexError):
        print "You must an output file!"
        exit(1)
    
    print "Input omhe string is: %s" % (omhe_str) 
    
    try:
        """ Instantaiate an instance of the OMHE class"""
        o = parseomhe.OMHE()
        """Parse it if valid, otherwise raise the appropriate  error"""
        d=o.parse(omhe_str)
        """Send the OMHE dictonary to RESTCat"""
        result=upload_OMHE_2_RESTCat(d, out_file, USERNAME, PASSWORD)
        print "HTTP Response Code=%s" % (result.getinfo(result.HTTP_CODE),)
        result.close()
        
    except():
        print "An unexpected error occured. Here is the post-mortem:"
        print sys.exc_info()
