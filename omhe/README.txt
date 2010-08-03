###############################################################################
# Open Mobile Health Exchange (OMHE) Parser & Tools for Python
# (c) 2010. All Rights Reserved.
# Release 0.3dev
# Authors: Alan Viars (Videntity), Chris Boyce (Videntity)
# License: This code is open source and available via Apache2 license.
# Please read LICENSE.txt for more information.
################################################################################




PREREQS:

You'll need:
    python-twitter Get it from GoogleCode:
        http://code.google.com/p/python-twitter/
    
    simplejson (on older versions of Python.):
        http://code.google.com/p/simplejson/
    
    Tk (Already installed on Mac and some Linux.  Also installed w/ Python for Windows)
    
    pyserial (If you want to read directly from hardware.):
        http://pyserial.sourceforge.net/
        
You'll need to:

    edit the values in settings.py to your own information.
    
    
TODO:

- Support for scale and meter connectivity.  I plan to use PySerial to start,
then to move to Bluetooth.  I'll be supporting LifeSorce hardware to start.
I'll add support for the following hardware models

    UA-767PC Blood Pressure Monitor for Telemonitoring
    UC-321PL High Capacity Telemedicine Scale

-The twitter connectivity should be optional. (If its not installed, the button
doesn't show up or is greyed out.

- Make use of parser code to validate omhe syntax.

-Additional error checking.

