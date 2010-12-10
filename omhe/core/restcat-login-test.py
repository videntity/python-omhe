import urllib2, urllib, sys, base64
import types, time, pycurl

try:
    from omhe.settings import RESTCAT_SERVER, USERNAME, PASSWORD
except:
    try:
        from settings import RESTCAT_SERVER, USERNAME, PASSWORD
    except:
        print "I couldn't find your settings.py.  Perhaps you need to create one?"
        print sys.exc_info()
        exit(1)
        
THEURL = '%s/api/testlogin/' % (RESTCAT_SERVER)
    

def login():
    user_and_pass="%s:%s" % (USERNAME, PASSWORD)    
    c = pycurl.Curl()
    c.setopt(c.SSL_VERIFYPEER, False)
    c.setopt(pycurl.URL, THEURL)
    c.setopt(pycurl.HTTPHEADER, ["Accept:"])
    c.setopt(pycurl.USERPWD, user_and_pass)
    c.perform()
    print ""

if __name__ == "__main__":
    login()
    