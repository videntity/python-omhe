.. image::  http://videntity.com/images/omhe.png


Open Mobile Health Exchange (OMHE) Parser & Tools for Python
============================================================
Copyright 2011 - Alan Viars (Videntity) -All Rights Reserved.


Release 0.6.0






1. Background:
==============

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

The home base for this code can be found on github_.

.. _github: http://github.com/videntity/python-omhe



The library also includes tools to capture and upload blood pressure information
from an A&D monitor, capture and upload weight from a Wii Balance board.
The upload utilities are configured to upload information to a RESTCat server.
See http://github.com/aviars/RESTCat for more information



2. Dependencies:
================

We assume you are already running 2.5, or 2.6. If you are on Linux
or MacOS, chances are Python is already installed.  The upload tools require
pycurl.  The blood pressure application requires pyserial.  The Wii Balance Board
application requires Cwiid_.

.. _Cwiid: http://github.com/abstrakraft/cwiid


To make things easier you should install:

* python-setuptools (so you can use easy_install)
* pip (so you can use pip)
* pycurl (So you can use the curl libraries inside Python)
* pyserial (So you can talk to a serial port)
* git-core (so you can use and download with git)
* build-essential (Tools to compile C code. You only need this for Cwiid)
* cwiid (so you can talk to a Wii Balance Board)

3. Installation:
===============
There are many ways to install python-omhe on Linux, Mac or Windows.
The following instructions outline the process on Ubuntu.  Adjust these
instructions to you platform.
Install the prereqs:
::
    sudo apt-get install python-setuptools git-core
    sudo easy_install pip
    sudo pip install pycurl
    sudo pip install pyserial
    
Install python-omhe:
--------------------
Make sure you are root or working in a virtual python environment to issue the
'python setup.py install' or the uninstall command
::
    git clone git://github.com/videntity/python-omhe.git
    cd python-omhe
    python setup.py install
    
To uninstall python-omhe
::
    pip uninstall python-omhe
    
Press y when prompted


4. How to Use the Parser:
==========================


The easiest way to try it out is to just run the command line utility.  All of
these commands will validate.  The pomhe utility outputs JSON so you can just
script using this command line tool.
::
    pomhe bp120/80p60#dt20100701:121212#tx-5
    
    pomhe bp120/80p60
    

If you want to use the functions within you paython application, then user the
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

5. Using the GUI Applications.
===============================

These are not longer supported and will be released as a seperate package.


6. OMHE TESTING FRAMEWORK:
==========================

This section describes python-omhe's testing framework. Python-omhe package has
its own special testing harness based on unittest. 

6.1 Why Build a Test Framework?:
--------------------------------

The long term goal of the testing system is to provide
quantifiable results to validation of correct input, output, and to ensure the
tools throw the right exception when errant input is given.

Also, automated testing is just a good idea and "test-driven-development" makes
for cleaner, more modular code.  It also makes developing OMHE-powered
applications easier and more reliable.
 
6.1 Running Tests:
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


7. TODOs:
=========

Validators are still needed for many omhe commands.  Simply add your validator
function to the omhe/validators folder and make sure they are 'turned on' in the
code by having the command and validation function present in the omhe_validators
dictionary in the __init__ of the parseomhe.py file. Validators must either
return a dict of correctly parsed contents or raise an OMHE Error.  Errors are
defined in the 'omhe/validators/validator_errors.py' file.

8. DEDICATIONS:
===============
This code is dedicated to my Grandmother, Rachel Bradshaw, who is in her 90's
and has Congestive Heart Failure, to my father who recently had open heart
surgery and  to all those who struggle to stay well or get better.


9. LICENSE & SUPPORT:
=====================
This code is open source and available under a dual license model; GPL 2 license
or a commercial license. Please read LICENSE.txt for more information.
If you need a commercial license or support please call us at 410-246-2158,
email us at: sales [at] videntity [dot] com or visit us online at http://www.videntity.com.



