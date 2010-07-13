import urllib2, urllib, sys, base64
import types, time



def login():
    try:
        theurl="http://127.0.0.1:8000/api/testlogin/"
        password="pass"
        username="alan"
    
        values= {
                'txidr': "1",
                'note': "The note",
                }
        
        data =urllib.urlencode(values)
        base64string = base64.encodestring('%s:%s' % (username, password))[:-1]
        authheader =  "Basic %s" % base64string
        req=urllib2.Request(theurl, data)
        req.add_header("Authorization", authheader)
        response = urllib2.urlopen(req)
        if response.code==200:
            time.sleep(2)
            reply = response.read()
            print reply
        else:
            print response.code
            
    except urllib2.HTTPError, exc:
        if exc.code==401:
            print "You are not authorized."
        elif exc.code==400:
            raise InvalidTemplateError, "Bad Request."
        else:
            raise UnknownHTTPError, "An unknown  urllib2.HTTPError occured."
    except:
        print sys.exc_info()
        
        
def login2():
    theurl = 'http://127.0.0.1:8000/api/testlogin/'
    protocol = 'http://'
    username = 'alan'
    password = 'pass'         # a great password

    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()      # this creates a password manager
    passman.add_password(None, theurl, username, password)      # because we have put None at the start it will always use this username/password combination

    authhandler = urllib2.HTTPBasicAuthHandler(passman)                 # create the AuthHandler

    opener = urllib2.build_opener(authhandler)                                  # build an 'opener' using the handler we've created
    # you can use the opener directly to open URLs
    # *or* you can install it as the default opener so that all calls to urllib2.urlopen use this opener
    urllib2.install_opener(opener)
    post_dict={'hi':'ho','howdy':'do'}
    
    data =urllib.urlencode(post_dict)
        
    req=urllib2.Request(theurl, data)
    response = urllib2.urlopen(req)    
    status = response.code
    print "status=%s" % (status)
    the_page = response.read()        
    print the_page
        

if __name__ == "__main__":
    login()
    login()
    login()
    login()
    #login2()    