#!/usr/bin/env python

# Written by: Alan Viars, Videntity
# Copyright 2010 - All Rights Reserved

import sys
from Tkinter import *
import tkMessageBox

try:
    from settings import USERNAME, PASSWORD, RECEIVER, SENDER, RESTCAT_SERVER
except:
    print "Sorry, I can't seem fo import the settings file."
    sys.exit(1)


from omhe.core.parseomhe import parseomhe
import pycurl

bp_value=""
username=""
subject=""
password=""
syst=""
dias=""
puls=""

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
        c.setopt(c.SSL_VERIFYPEER, False)
        c.setopt(pycurl.URL, URL)
        c.setopt(c.HTTPPOST, pf)
        c.setopt(pycurl.FOLLOWLOCATION, 1)
        c.setopt(pycurl.MAXREDIRS, 5)
        c.setopt(pycurl.HTTPHEADER, ["Accept:"])
        c.setopt(pycurl.USERPWD, user_and_pass)
        c.perform()
        return c



class App:
    """ A blood pressure GUI application based on OMHE Microsyntax"""
    """Global Variables"""
    omhe_bp_prefix="bp="
    systolic_str=""
    diastolic_str=""
    pulse_str=""
    omhe_s_d_deliniator="/"
    pulse_deliniator="p"
    def __init__(self, master):
        frame = Frame(master)
        frame2 = Frame(master)
        
        frame.grid(row=0)
        
        frame2.grid(row=7)


        spinval = StringVar()
        
        l1 = Label(frame, text="Systolic:", )
        l1.grid(row=1, column=1)
        self.systolicsb = Spinbox(frame, from_=0.0, to=300.0, increment=1)
        self.systolicsb.grid(row=1, column=2)
        self.systolicsb.delete(0)
        self.systolicsb.insert(ANCHOR,syst)
        
         
        l2 = Label(frame, text="Diastolic:")
        l2.grid(row=2, column=1)
        self.diastolicsb = Spinbox(frame, from_=0.0, to=300.0, increment=1)
        self.diastolicsb.grid(row=2, column=2)
        self.diastolicsb.delete(0)
        self.diastolicsb.insert(ANCHOR,dias)
        
        l3 = Label(frame, text="Pulse:")
        l3.grid(row=3, column=1)
        self.pulsesb = Spinbox(frame, from_=0.0, to=300.0, increment=1)
        self.pulsesb.grid(row=3, column=2)
        self.pulsesb.delete(0)
        self.pulsesb.insert(ANCHOR,puls)
        
        self.username = Label(frame, text="Username:")
        self.username.grid(row=4, column=1)
        self.e2 = Entry(frame)
        self.e2.grid(row=4, column=2)
        
        self.username = Label(frame, text="Subject's Email:")
        self.username.grid(row=5, column=1)
        self.e3 = Entry(frame)
        self.e3.grid(row=5, column=2)
        
        self.username = Label(frame, text="Password:")
        self.username.grid(row=6, column=1)
        self.e4 = Entry(frame)
        self.e4.grid(row=6, column=2)



        
        try:
            import serial
            mystate=ACTIVE
        except(ImportError):
            mystate=DISABLED
            print "The serial package was not found. Disabling Meter button."
            
        self.button = Button(frame, text="  GET FROM METER   ", command=self.getFromMeter, state=mystate)
        self.button.grid(row=1, column=5)
        
        try:
            from omhe.bin import parseomhe, upload2restcat
            mystate=ACTIVE
        except(ImportError):
            mystate=DISABLED
            print "Package python-omhe not found!"
        self.button = Button(frame, text="          SEND             ", command=self.sendVidentity, state=mystate)
        self.button.grid(row=2, column=5)
        
        
        self.button = Button(master, text="RESET", fg="red", command=self.reset)
        self.button.grid(row=5, column=2)
        
        self.button = Button(master, text="QUIT", fg="red", command=frame.quit)
        self.button.grid(row=5, column=3)
        
        
        self.stat_str = StringVar()
        self.stat_str.set("Press Send when ready")
        self.status = Label(master, textvariable=self.stat_str, fg="red")
        self.status.grid(row=10, column=0)
        
        
        self.firstdot=True
        
        #if bp_value!="":
        #    self.e1.delete(0, END)
        #    self.e1.insert(END, bp_value)
        #
            
        if username!="":
            self.e2.delete(0, END)
            self.e2.insert(END, username)

            
        if subject!="":
            self.e3.delete(0, END)
            self.e3.insert(END, subject)

            
        if password!="":
            self.e4.delete(0, END)
            self.e4.insert(END, password)
        
      
    def reset(self):
        self.systolicsb.delete(0,END)
        self.systolicsb.insert(ANCHOR,syst)
        self.diastolicsb.delete(0,END)
        self.diastolicsb.insert(ANCHOR,dias)
        self.pulsesb.delete(0,END)
        self.pulsesb.insert(ANCHOR,puls)
      
    
      
    def getFromMeter(self):
        self.stat_str.set("Press Start when Ready.")
        import serial
        ser = serial.Serial(SERIAL_PORT, xonxoff=1)
        """pop up a window and tell the person to press start on the device"""
        print ser
        #tkMessageBox.showinfo("Grab your Blood Pressure",
        #                      "Place the cuff around your arm, and press START on the meter.")
        self.stat_str.set("Getting reading.  Please wait...")
        print "waiting for device reading..."
        s = ser.read(10)
        self.stat_str.set("Done Getting BP.  Press Send to Upload")
        print s
        sys=s[2:4]
        dia=s[4:6]
        pul=s[6:8]
        
        sys=int(sys,16)
        print sys
        dia=int(dia,16)
        print dia
        pul=int(pul,16)
        print pul
        sys =sys+dia
        print sys
        print "%s/%sp%s" %(sys,dia,pul)
        self.systolicsb.delete(0,END)
        self.systolicsb.insert(ANCHOR,sys)
        self.diastolicsb.delete(0,END)
        self.diastolicsb.insert(ANCHOR,dia)
        self.pulsesb.delete(0,END)
        self.pulsesb.insert(ANCHOR,pul)
        
        
    def sendVidentity(self):
        self.stat_str.set("Uploading...")
        print "Upload to RESTCat"
        
        self.omhe_str="%s%s%s%s%s%s" %(self.omhe_bp_prefix, self.systolicsb.get(),
                              self.omhe_s_d_deliniator, self.diastolicsb.get(),
                              self.pulse_deliniator,
                              self.pulsesb.get())
        user=(self.e2.get())
        email=(self.e3.get())
        password=(self.e4.get())
        print "user=%s" % (user)
        print "email=%s" % (email)
        print "password=%s" % (password)

        
        omhe_str=self.omhe_str
        """ Instantiate an instance of the OMHE class"""
        o = parseomhe.OMHE()
        """Parse it if valid, otherwise raise the appropriate error"""
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
            print s
            self.stat_str.set(s)
            
  

try:
    bp_value = sys.argv[1]
    syst=int(bp_value[0:3])
    dias=int(bp_value[3:6])
    puls=int(bp_value[6:9])
    
except:

    bp_value=""
    syst="120"
    dias="80"
    puls="60"
    
try:
    username = sys.argv[2]
except:
    username ="" 
    
try:
    subject = sys.argv[3]
except:
    subject =""
    
try:
    password = sys.argv[4]
except:
    password ="" 


    
root = Tk()
root.title("Please Enter Your Blood Pressure") 

app = App(root)

root.mainloop()