import pycurl
import sys
import parseomhe


USERNAME='alan'
PASSWORD='pass'
URL="http://127.0.0.1:8000/api/create/"
routing={
        '_sndr':"alan",
        '_rcvr':"alan",
        '_subj':"alan",
         '_sec':"3",
        }

def upload_OMHE_2_RESTCat(omhe_dict, outfile):
    f = open(outfile, "wb")
    """Send an HTTP POST to RESTCat using a simple OMHE String"""
    pf=[]
    post_dict={}
    post_dict['_ttype']='omhe'
    post_dict.update(routing)
    post_dict['_tx_dt']=omhe_dict['_tx_dt']
    post_dict['_tx_tz']=omhe_dict['_tx_tz']
    post_dict['_id']=omhe_dict['_id']
    post_dict['_texti']=omhe_dict['_texti']
    
    for o in post_dict:
        x=(str(o), str(post_dict[o]))
        pf.append(x)
    print pf

    user_and_pass="%s:%s" % (USERNAME, PASSWORD)    
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
        result=upload_OMHE_2_RESTCat(d, out_file)
        print "HTTP Response Code=%s" % (result.getinfo(result.HTTP_CODE),)
        result.close()
        
    except():
        print "An unexpected error occured. Here is the post-mortem:"
        print sys.exc_info()