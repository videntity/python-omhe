import urllib2, urllib, sys, base64
import types, time, pycurl
from settings import RESTCAT_SERVER, USERNAME, PASSWORD


THEURL = '%s/api/testlogin/' % (RESTCAT_SERVER)
    

def login():
    user_and_pass="%s:%s" % (USERNAME, PASSWORD)    
    c = pycurl.Curl()
    c.setopt(pycurl.URL, THEURL)
    c.setopt(pycurl.HTTPHEADER, ["Accept:"])
    c.setopt(pycurl.USERPWD, user_and_pass)
    c.perform()
    print ""

if __name__ == "__main__":
    login()
    