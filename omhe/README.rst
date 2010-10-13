.. image::  http://github.com/aviars/python-omhe/raw/master/omhe.png

Blood Pressure GUI README
=========================


Table of Contents:
==================
.. toctree::
   :maxdepth: 3
   
   
1. Prereqs:
===========
You may need these items first:
    
    * simplejson (on older versions of Python.):
        http://code.google.com/p/simplejson/
    
    * Tk (Already installed on Mac and some Linux.  Also installed w/ Python for Windows)
    
    * pyserial (If you want to read directly from hardware.):
        http://pyserial.sourceforge.net/
               
    * pycurl
    
    
        
You'll need to:

    edit the values in settings.py to your own information.

2.) Running bloodpressure.py:
=============================
Simply start the application from the command line.
::
    python bloodpressure.py



3. TODO's:
=========
- Support for scale and meter connectivity.  I plan to use PySerial to start,
then to move to Bluetooth.  I'll be supporting LifeSorce hardware to start.
I'll add support for the following hardware models

    UA-767PC Blood Pressure Monitor for Telemonitoring
    UC-321PL High Capacity Telemedicine Scale

-The twitter connectivity should be optional. (If its not installed, the button
doesn't show up or is greyed out.

- Make use of parser code to validate omhe syntax.

-Additional error checking.

