#!/usr/bin/env python
import pycurl
import sys
import omhe.core.parseomhe


def upload2restcat(omhe_dict, userpass, sender, receiver, subject,
                   restcat_server, outfile="out.json", sec_level=3):
    
    URL="%s/api/transaction/create/" % (restcat_server)

    routing={
        'sndr':sender,
        'rcvr':receiver,
        'subj': subject,
        'sec': sec_level,
        }
    
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
    c = pycurl.Curl()
    c.setopt(pycurl.URL, URL)
    c.setopt(c.HTTPPOST, pf)
    c.setopt(c.WRITEDATA, f) 
    c.setopt(pycurl.HTTPHEADER, ["Accept:"])
    c.setopt(pycurl.USERPWD, userpass)
    c.perform()
    f.close() 
    return c



if __name__ == "__main__":
    """
Accept a singe omhe string from the command line. Parse, then print
the resulting dict, then upload to RESTCat
"""
    try:
        userpass=sys.argv[1]
        omhe_str=sys.argv[2]
        outfile=sys.argv[3]
        
    except(IndexError):
        print "You must supply username, password, an omhe message, and an out file!"
        print "The sender, receiver, subject, and security level are defined in \
        the settings.py by default."
        print "Usage:"
        print "u2rc [user:pass] [omhe_message] [out.json]"
        exit(1)
        

    
    print "Input omhe string is: %s" % (omhe_str)
    
    try:
        """ Instantaiate an instance of the OMHE class"""
        o = parseomhe()
        """Parse it if valid, otherwise raise the appropriate error"""
        d=o.parse(omhe_str)
        """Send the OMHE dictonary to RESTCat"""
        result=upload2restcat(d, userpass, out_file)
        print "HTTP Response Code=%s" % (result.getinfo(result.HTTP_CODE),)
        result.close()
        
    except():
        print "An unexpected error occured. Here is the post-mortem:"
        print sys.exc_info()