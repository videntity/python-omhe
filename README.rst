Open Mobile Health Exchange (OMHE) Python Parser and Utilities
==============================================================

Copyright 2011 - Alan Viars (Videntity) - All Rights Reserved.

Release 0.6.1

.. image::  http://videntitystatic.s3.amazonaws.com/logo/omhe.png

1. Background
=============

OMHE (Open Mobile Health Exchange) is a  a Microsyntax for Devices, Machines,
& Humans.  This is a python package which implements the OMHE microsyntax format
and provides sample code for parsing and making hardware, such as a Wii Balance
board, "speak OMHE".

OMHE (Open Mobile Health Exchange), pronounced "ooommm" is an open-source
microsyntax for text messaging (mobile SMS), Twitter®, medical devices, and
other "short text capable" systems. It is a community work product from many
interested parties including doctors, hackers, software developers,
entrepreneurs, quantified-selfers, health IT vendors, wellness vendors,
and health/mobile device manufactures.

Its called OMHE because its the nirvana of health informatics..open, free, and simple.
OMHE is a microsyntax.org project.  The goal behind OMHE is to help exchange
data over mobile device such as phones or medical or wellness devices in an
ultra-compact, human and machine readable format.

This package, "python-omhe" was developed by and is maintained by Videntity
Systems, Inc. It is free to use and 100% open source.  Feel like contributing to
this project?  Please email us or join the Google Group "omhe-microsyntax".


The commands and a lengthy description can be found here_

.. _here: http://code.google.com/p/omhe


2. Installation
===============

python-omhe is in the Python Package Index (PyPi). You can use pip to install.
::
    pip install python-omhe
    
To uninstall python-omhe
::
    pip uninstall python-omhe
    
Press y when prompted


3. How to Use the Parser
========================
The easiest way to try it out is to just run the command line utility.  All of
these commands will validate.  The pomhe utility outputs JSON so you can just
script using this command line tool.
::
    pomhe bp120/80p60#dt20100701:121212#tx-5
    
    pomhe bp120/80p60
    

If you want to use the functions within your python application, then use the
API.  Consider the following simple example.
::
    # import the omheparser library
    >>> from omhe.core.parseomhe import parseomhe
    
    # Create an OMHE string to parse
    # Note that this string includes the 'dt' and 'tz' helper tags so we can
    # set the event's datetime and timezone.
    >>> omhe_str="bp=120/80p60#dt20120501:083059z#tz-5"

    #Create a new OMHE object
    >>> o = parseomhe()
    
    # Parse the OMHE string, return a dict, and convert to JSON. method and
    # return a parsed dict
    >>> omhe_json=o.omhedict2json(o.parse(omhe_str))
    >>> print omhe_json

The output will look like this:
::
    {
        "bp_systolic": "120", 
        "tags": [
            "dt20120501:083059z", 
            "tz-5"
        ], 
        "bp_pulse": "60", 
        "text": "bp=120/80p60#dt20120501:083059z#tz-5", 
        "bp_diastolic": "80", 
        "value": "120/80p60", 
        "transaction_type": "omhe", 
        "transaction_datetime": "2012-04-29 00:10:56", 
        "transaction_id": "25bd039c-e5c0-4eeb-be55-c03dbac400bf", 
        "event_timezone": "-5", 
        "omhe": "bp", 
        "event_datetime": "2012-05-01 08:30:59"
    }

okay lets do another.
::
    >>> omhe_str="wt=153l"
    >>> omhe_json=o.omhedict2json(o.parse(omhe_str))

The output will look like this:
::
    {
        "wt_numeric": "153", 
        "text": "wt=153l", 
        "event_timezone": "0", 
        "event_datetime": "2012-04-29 00:10:22", 
        "tags": [], 
        "value": "153l", 
        "transaction_type": "omhe", 
        "transaction_datetime": "2012-04-29 00:10:56", 
        "transaction_id": "25bd039c-e5c0-4eeb-be55-c03dbac400bf", 
        "omhe": "wt", 
        "wt_measure_unit": "l"
    }

4. Using the GUI Applications.
===============================

These are not longer supported and will be released as a seperate package.


5. OMHE TESTING FRAMEWORK:
==========================

This section describes python-omhe's testing framework. Python-omhe package has
it's own special testing harness based on unittest. 

5.1 Why Build a Test Framework?:
--------------------------------

The long term goal of the testing system is to provide
quantifiable results to validation of correct input, output, and to ensure the
tools throw the right exception when errant input is given.

Also, automated testing is just a good idea and "test-driven-development" makes
for cleaner, more modular code.  It also makes developing OMHE-powered
applications easier and more reliable.
 
5.2 Running Tests:
------------------
You'll find test scripts inside 'omhe/tests'. 

Right now only "bp" (blood pressure) has an automated suite of tests, but others
will be created in the near future.  
 
To run the tests for blood pressure just run the following command inside the
"omhe/tests/" folder:
::
    python bp_test.py
    
That's it.  You should not receive any errors unless you've changed something in
the code base.  This validates that correct input returns parsed data and that
incorrect input raises the errors that it should.  Look over the other tests.


6. TODOs
========

* Validators are still needed for some omhe commands.

* Migrate GUI tools out of this package and into a sperate github repository.


7. LICENSE & SUPPORT
====================
This code is open source and available under a dual license model; GPL 2 license
or a commercial license. Please read LICENSE.txt for more information.
If you need a commercial license or support please call us at 410-246-2158,
email us at: sales [at] videntity [dot] com or visit us online at
http://www.videntity.com.



