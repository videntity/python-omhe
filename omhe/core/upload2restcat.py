#!/usr/bin/env python
import pycurl
import sys
import omhe.core.parseomhe


def upload2restcat(omhe_dict, userpass, sender,
                   receiver, subject, restcat_server,
                   outfile="out.json", idr=None,
                   sec_level=3):

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
    
    if idr:
        post_dict['idr']=idr
    
    """ The type of transaction"""
    post_dict['ttype']='omhe'
    post_dict.update(routing)
    
    """ The transaction's date/time/zone"""
    post_dict['txdt']=omhe_dict['txdt']
    post_dict['txtz']=omhe_dict['txtz']
    
    """ The event's date/time/zone"""
    post_dict['evdt']=omhe_dict['evdt']
    post_dict['evtz']=omhe_dict['evtz']
    
    """ The transaction's uuid"""
    post_dict['id']=omhe_dict['id']
    
    """ The transaction's text item (ASCII payload)."""
    post_dict['texti']=omhe_dict['texti']
        
    for o in post_dict:
        x=(str(o), str(post_dict[o]))
        pf.append(x)
    #print pf
    c = pycurl.Curl()
    
    c.setopt(c.SSL_VERIFYPEER, False) 
    
    c.setopt(pycurl.URL, URL)
    c.setopt(c.HTTPPOST, pf)
    c.setopt(c.WRITEDATA, f) 
    c.setopt(pycurl.HTTPHEADER, ["Accept:"])
    c.setopt(pycurl.USERPWD, userpass)
    c.perform()
    f.close() 
    return c