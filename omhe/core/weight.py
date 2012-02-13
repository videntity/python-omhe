#!/usr/bin/env python

# Written by: Alan Viars, Videntity
#Copyright 2010 - All Rights Reserved

import sys
from Tkinter import *

try:
    import pycurl
except:
    print "Sorry, I can't seem to import pycurl for some reason."
    print "Please check that it and it's python bindings are installed."
    print "If on Ubuntu try, sudo apt-get install pycurl"
    print "See http://pycurl.sourceforge.net/"
    sys.exit(1)


try:
    from omhe.settings import USERNAME, PASSWORD, RECEIVER, SENDER, RESTCAT_SERVER
except:
    print "Sorry, I can't seem to import the settings file."
    sys.exit(1)

wii_weight=""
username=""
subject=""
password=""


def uploadOMHE2restcat(omhe_dict, username, password, sndr, rcvr, subj, security=3):

        URL="%s/api/create/" % (RESTCAT_SERVER)
        URL=str(URL)
        user_and_pass="%s:%s" % (username, password)
        user_and_pass=str(user_and_pass)
        pf=[]
        routing={'sndr':sndr,
            'rcvr':RECEIVER,
            'subj':sndr,
             'sec':security,}
        post_dict={}
        post_dict['ttype']='omhe'
        post_dict.update(routing)
        post_dict['txdt']=omhe_dict['txdt']
        post_dict['txtz']=omhe_dict['txtz']
        post_dict['id']=omhe_dict['id']
        post_dict['texti']=omhe_dict['texti']
        
        print post_dict
        
        for o in post_dict:
            x=(str(o), str(post_dict[o]))
            pf.append(x)   
        
        
        c = pycurl.Curl()
        c.setopt(pycurl.URL, URL)
        c.setopt(c.SSL_VERIFYPEER, False)
        c.setopt(c.HTTPPOST, pf)
        c.setopt(pycurl.FOLLOWLOCATION, 1)
        c.setopt(pycurl.MAXREDIRS, 5)
        c.setopt(pycurl.HTTPHEADER, ["Accept:"])
        c.setopt(pycurl.USERPWD, user_and_pass)
        c.perform()
        return c

    
class App:

    """A weight monitoring GUI application based on OMHE Microsyntax"""
    omhe_str=""
    omhe_weight_prefix="wt="
    units_str="l"

    def __init__(self, master):

        
        frame = Frame(master)
        frame2 = Frame(master)
        
        frame.grid(row=0)
        
        frame2.grid(row=7)

        
        v = IntVar()
        w = Label(frame, text="Lbs./Kg.")
        w.grid(row=1, column=4)
        
        self.pounds = Radiobutton(frame,  text="Pounds", variable=self.units_str, value='l', command=self.say_lbs)
        self.pounds.grid(row=2, column=4, sticky=W)
        self.pounds.select()
        
        self.kilograms = Radiobutton(frame,  text="Kilograms", variable=self.units_str, value='k', command=self.say_kg)
        self.kilograms.grid(row=3, column=4, sticky=W)

        self.say_one = Button(frame, text="1", command=self.say_one)
        self.say_one.grid(row=1, column=1)
        self.say_two = Button(frame, text="2", command=self.say_two)
        self.say_two.grid(row=1, column=2)
        self.say_three = Button(frame, text="3", command=self.say_three)
        self.say_three.grid(row=1, column=3)
        self.say_four = Button(frame, text="4", command=self.say_four)
        self.say_four.grid(row=2, column=1)
        self.say_five = Button(frame, text="5", command=self.say_five)
        self.say_five.grid(row=2, column=2)
        self.say_six = Button(frame, text="6", command=self.say_six)
        self.say_six.grid(row=2, column=3)
        self.say_seven = Button(frame, text="7", command=self.say_seven)
        self.say_seven.grid(row=3, column=1)
        self.say_eight = Button(frame, text="8", command=self.say_eight)
        self.say_eight.grid(row=3, column=2)
        self.say_nine = Button(frame, text="9", command=self.say_nine)
        self.say_nine.grid(row=3, column=3)
        self.say_zero = Button(frame, text="0", command=self.say_zero)
        self.say_zero.grid(row=4, column=1)
        self.say_dot = Button(frame, text=".", command=self.say_dot)
        self.say_dot.grid(row=4, column=2)
        self.say_dot = Button(frame, text="C", command=self.say_clear)
        self.say_dot.grid(row=4, column=3)
                
        self.weight = Label(frame2, text="Weight:")
        self.weight.grid(row=0, column=0)
        self.e1 = Entry(frame2)
        self.e1.grid(row=0, column=1)
        
        
        self.username = Label(frame2, text="Username:")
        self.username.grid(row=1, column=0)
        self.e2 = Entry(frame2)
        self.e2.grid(row=1, column=1)
        
        self.email = Label(frame2, text="Subject's Email:")
        self.email.grid(row=2, column=0)
        self.e3 = Entry(frame2)
        self.e3.grid(row=2, column=1)  
        
        
        self.password = Label(frame2, text="Password:")
        self.password.grid(row=3, column=0)
        self.e4 = Entry(frame2)
        self.e4.grid(row=3, column=1)        
 
 
        
        if wii_weight!="":
            self.e1.delete(0, END)
            self.e1.insert(END, wii_weight)
            self.omhe_str=wii_weight
            
        if username!="":
            self.e2.delete(0, END)
            self.e2.insert(END, username)

            
        if subject!="":
            self.e3.delete(0, END)
            self.e3.insert(END, subject)

            
        if password!="":
            self.e4.delete(0, END)
            self.e4.insert(END, password)
        
        try:
            from omhe.bin import parseomhe, upload2restcat
            mystate=ACTIVE
        except(ImportError):
            mystate=DISABLED
            print "The Videntity API package was not found. Disabling Videntity Send."
        self.button = Button(frame, text="    SEND      ", command=self.sendVidentity, state=mystate)
        self.button.grid(row=1, column=5)
        

        self.button = Button(frame, text="    QUIT      ", command=frame.quit)
        self.button.grid(row=2, column=5)
        
        self.stat_str = StringVar()
        self.stat_str.set("Press Send when ready")
        self.status = Label(master, textvariable=self.stat_str, fg="red")
        self.status.grid(row=10, column=0)
        
        self.firstdot=True
        
    
    def say_one(self):
        self.omhe_str+="1"
        print self.omhe_str
        self.e1.insert(END, "1")
        
    def say_two(self):
        self.omhe_str+="2"
        print self.omhe_str
        self.e1.insert(END, "2")
        
        
    def say_three(self):
        self.omhe_str+="3"
        print self.omhe_str
        self.e1.insert(END, "3")
        
        
    def say_four(self):
        self.omhe_str+="4"
        print self.omhe_str
        self.e1.insert(END, "4")
        
        
    def say_five(self):
        self.omhe_str+="5"
        print self.omhe_str
        self.e1.insert(END, "5")
        
    def say_six(self):
        self.omhe_str+="6"
        print self.omhe_str
        self.e1.insert(END, "6")
        
    def say_seven(self):
        self.omhe_str+="7"
        print self.omhe_str
        self.e1.insert(END, "7")
        
    def say_eight(self):
        self.omhe_str+="8"
        print self.omhe_str
        self.e1.insert(END, "8")
        
    def say_nine(self):
        self.omhe_str+="9"
        print self.omhe_str
        self.e1.insert(END, "9")
        
    def say_zero(self):
        self.omhe_str+="0"
        print self.omhe_str
        self.e1.insert(END, "0")
        
    def say_dot(self):
        if self.firstdot==True:
            self.omhe_str+="."
            print self.omhe_str
            self.e1.insert(END, ".")
            self.firstdot=False
            
    def say_clear(self):
        self.omhe_str=""
        self.e1.delete(0, END)
        
    def say_lbs(self):
        self.units_str="l"
        print "weight in pounds"
        
    def say_kg(self):
        self.units_str="k"
        print "weight in kilograms"
        
    def getFromScale(self):
        print "get from scale"
        
    def sendVidentity(self):
        self.stat_str.set("Uploading...")
        print "Upload to RESTCat"
        
        weight=(self.e1.get())
        self.omhe_str= "%s%s%s" %(self.omhe_weight_prefix, weight, self.units_str)
        user=(self.e2.get())
        email=(self.e3.get())
        password=(self.e4.get())
        print "user=%s" % (user)
        print "email=%s" % (email)
        print "password=%s" % (password)

        
        omhe_str=self.omhe_str
        """ Instantiate an instance of the OMHE class"""
        o = parseomhe.OMHE()
        """Parse it if valid, otherwise raise the appropriate  error"""
        d=o.parse(self.omhe_str)

        result=uploadOMHE2restcat(d, user, password, email, RECEIVER,
                                  email, 2)
        print "HTTP Response Code=%s" % (result.getinfo(result.HTTP_CODE),)
        code = result.getinfo(result.HTTP_CODE)
        if int(code)==200:
            self.stat_str.set("Done! Peace out!")
            exit(0)
        else:
            s="Error Uploading. Error code %s" % (code)
            self.stat_str.set(s)

    #def sendTwitter(self):
    #    print "Send via Twitter"
    #    dm = "%s%s%s" %(self.omhe_weight_prefix, self.omhe_str, self.units_str)
    #    try:
    #        
    #        api = twitter.Api(username=twitterid, password=twitterpass)
    #        result = api.PostDirectMessage(twitterreceiver, dm)
    #        if result:
    #            print "successfully sent DM"
    #            self.say_clear()
    #        else:
    #            print "There was a problem sending your DM tweet.  Please check user, pass and that the receiver is following you."
    #    except:
    #            print "There was a problem sending your DM tweet.  Please check user, pass and that the receiver is following you."
    #    


try:
    wii_weight = sys.argv[1]
    wii_weight="%.2f" % (float(wii_weight))

except:
    print sys.exc_info()
    wii_weight=""
    
try:
    username = sys.argv[2]
except:
    username ="aviars" 
    
try:
    subject = sys.argv[3]
except:
    subject ="alan.viars@videntity.com"
    
try:
    password = sys.argv[4]
except:
    password ="password" 
    
    
root = Tk()
root.title("Please Enter Your Weight") 

app = App(root)

root.mainloop()


