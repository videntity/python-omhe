#!/usr/bin/env python

# Written by: Alan Viars, Videntity
# Copyright 2010 - All Rights Reserved

import sys
from Tkinter import *
import tkMessageBox
from settings import USERNAME, PASSWORD

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
        self.systolicsb.insert(ANCHOR,"120")
        
         
        l2 = Label(frame, text="Diastolic:")
        l2.grid(row=2, column=1)
        self.diastolicsb = Spinbox(frame, from_=0.0, to=300.0, increment=1)
        self.diastolicsb.grid(row=2, column=2)
        self.diastolicsb.delete(0)
        self.diastolicsb.insert(ANCHOR,"85")
        
        l3 = Label(frame, text="Pulse:")
        l3.grid(row=3, column=1)
        self.pulsesb = Spinbox(frame, from_=0.0, to=300.0, increment=1)
        self.pulsesb.grid(row=3, column=2)
        self.pulsesb.delete(0)
        self.pulsesb.insert(ANCHOR,"60")

        
        try:
            import serial
            mystate=ACTIVE
        except(ImportError):
            mystate=DISABLED
            print "The serial package was not found. Disabling Meter button."
            
        self.button = Button(frame, text="  GET FROM METER   ", command=self.getFromMeter, state=mystate)
        self.button.grid(row=1, column=5)
        
        try:
            import parseomhe
            import upload2restcat
            mystate=ACTIVE
        except(ImportError):
            mystate=DISABLED
            print "The Videntity API package was not found. Disabling Videntity Send."
        self.button = Button(frame, text="          SEND             ", command=self.sendVidentity, state=mystate)
        self.button.grid(row=2, column=5)
        
        #try:
        #    import twitter
        #    mystate=ACTIVE
        #except(ImportError):
        #    mystate=DISABLED
        #    print "The Twitter package was not found. Disabling Twitter Send."
        #self.button = Button(frame, text=" SEND VIA TWITTER  ", command=self.sendTwitter, state=mystate)
        #self.button.grid(row=3, column=5)
        
        self.button = Button(master, text="RESET", fg="red", command=self.reset)
        self.button.grid(row=5, column=2)
        
        self.button = Button(master, text="QUIT", fg="red", command=frame.quit)
        self.button.grid(row=5, column=3)
        
        self.firstdot=True
      
    def reset(self):
        self.systolicsb.delete(0,END)
        self.systolicsb.insert(ANCHOR,"120")
        self.diastolicsb.delete(0,END)
        self.diastolicsb.insert(ANCHOR,"85")
        self.pulsesb.delete(0,END)
        self.pulsesb.insert(ANCHOR,"60")
      
    
      
    def getFromMeter(self):
        print "get from meter"
        import serial
        ser = serial.Serial(serial_port, xonxoff=1)
        """pop up a window and tell the person to press start on the device"""
        print ser
        #tkMessageBox.showinfo("Grab your Blood Pressure",
        #                      "Place the cuff around your arm, and press START on the meter.")
        print "waiting for device reading..."
        s = ser.read(10)
        print "Complete!"
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
        import parseomhe
        import upload2restcat
        
        print "Send via Videntity"
        
        omhe_str="%s%s%s%s%s%s" %(self.omhe_bp_prefix, self.systolicsb.get(),
                              self.omhe_s_d_deliniator, self.diastolicsb.get(),
                              self.pulse_deliniator,
                              self.pulsesb.get())
        print omhe_str
        """ Instantaiate an instance of the OMHE class"""
        o = parseomhe.OMHE()
        """Parse it if valid, otherwise raise the appropriate  error"""
        d=o.parse(omhe_str)
        """Send the OMHE dictonary to RESTCat"""
        result=upload2restcat.upload_OMHE_2_RESTCat(d, "out.txt", USERNAME, PASSWORD)
        response_code= str(result.getinfo(result.HTTP_CODE, ))
        print "HTTP Response Code=%s" % (response_code)
        if response_code=="200":
            exit(0)    


        
        
        
    #def sendTwitter(self):
    #    print "Send via Twitter"
    #    #self.progressbar.set(value=25.0)
    #    
    #    dm = "%s%s%s%s%s%s" %(self.omhe_bp_prefix, self.systolicsb.get(),
    #                          self.omhe_s_d_deliniator, self.diastolicsb.get(),
    #                          self.pulse_deliniator,
    #                          self.pulsesb.get())
    #    print dm
    #    try:
    #        import twitter
    #        api = twitter.Api(username=twitterid, password=twitterpass)
    #        print api
    #        result = api.PostDirectMessage(twitterreceiver, dm)
    #        if result:
    #            print "Successfuly sent DM"
    #            if public_tweet==True:
    #                try:
    #                    api.PostUpdate(dm)
    #                except:
    #                    print "Failed to send Tweet"
    #                
    #            self.reset()
    #        else:
    #            print "There was a problem sending your DM tweet.  Please check user, pass and that the reciever is following you."
    #    except:
    #        print "There was a problem sending your DM tweet. Please check user, pass and that the reciever is following you."
    #

    
root = Tk()
root.title("Please Enter Your Blood Pressure") 

app = App(root)

root.mainloop()