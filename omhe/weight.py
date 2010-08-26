#!/usr/bin/env python

# Written by: Alan Viars, Videntity
#Copyright 2010 - All Rights Reserved

import sys
from Tkinter import *
from settings import twitterid, twitterpass, twitterreceiver

wii_weight=""
    
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
        
        self.kilograms = Radiobutton(frame,  text="Kilgrams", variable=self.units_str, value='k', command=self.say_kg)
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
        
        self.password = Label(frame2, text="Password:")
        self.password.grid(row=2, column=0)
        
        self.e3 = Entry(frame2)
        self.e3.grid(row=2, column=1)        
        
        if wii_weight!="":
            self.e1.delete(0, END)
            self.e1.insert(END, wii_weight)
            self.omhe_str=wii_weight
        #"""See if the necessary libraries are present, disable buttons"""
        #try:
        #    import serial
        #    mystate=ACTIVE
        #except(ImportError):
        #    mystate=DISABLED
        #    print "The serial package was not found. Disabling scale reader."
        #    
        #self.button = Button(frame, text="GET FROM SCALE", command=self.getFromScale, state=mystate)
        #self.button.grid(row=1, column=5)
        
        try:
            import parseomhe, upload2restcat
            mystate=ACTIVE
        except(ImportError):
            mystate=DISABLED
            print "The Videntity API package was not found. Disabling Videntity Send."
        self.button = Button(frame, text="    SEND      ", command=self.sendVidentity, state=mystate)
        self.button.grid(row=1, column=5)
        
        #try:
        #    import twitter
        #    mystate=ACTIVE
        #except(ImportError):
        #    mystate=DISABLED
        #    print "The Twitter package was not found. Disabling Twitter Send."
        #self.button = Button(frame, text="SEND VIA TWITTER", command=self.sendTwitter, state=mystate)
        #self.button.grid(row=3, column=5)

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
        print "Send via videntity"
        print "%s%s%s" %(self.omhe_weight_prefix, self.omhe_str, self.units_str)
        print self.omhe_str
        print "user=%s" % (self.e2.get())
        print "pass=%s" % (self.e3.get())
        self.stat_str.set("Hello")
    #def sendTwitter(self):
    #    print "Send via Twitter"
    #    dm = "%s%s%s" %(self.omhe_weight_prefix, self.omhe_str, self.units_str)
    #    try:
    #        
    #        api = twitter.Api(username=twitterid, password=twitterpass)
    #        result = api.PostDirectMessage(twitterreceiver, dm)
    #        if result:
    #            print "successfuly sent DM"
    #            self.say_clear()
    #        else:
    #            print "There was a problem sending your DM tweet.  Please check user, pass and that the reciever is following you."
    #    except:
    #            print "There was a problem sending your DM tweet.  Please check user, pass and that the reciever is following you."
    #    


try:
    wii_weight = sys.argv[1]
except:
    wii_weight=""
root = Tk()
root.title("Please Enter Your Weight") 

app = App(root)

root.mainloop()


