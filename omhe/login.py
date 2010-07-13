import urllib2, urllib, sys, base64
import types, time, pycurl



theurl = 'http://127.0.0.1:8000/api/testlogin/'
protocol = 'http://'
username = 'alan'
password = 'pass'         # a great password
    

def login():
    user_and_pass="%s:%s" % (username, password)    
    c = pycurl.Curl()
    c.setopt(pycurl.URL, theurl)
    c.setopt(pycurl.HTTPHEADER, ["Accept:"])
    c.setopt(pycurl.USERPWD, user_and_pass)
    c.perform()
    print ""

if __name__ == "__main__":
    login()
    