.. image::  http://github.com/aviars/python-omhe/raw/master/omhe.png

Open Mobile Health Exchange (OMHE) Parser & Tools for Python
============================================================
(c) 2010 - All Rights Reserved.
Release 0.5dev
Author: Alan Viars (Videntity)
License: This code is open source and available via Apache2 license.
Please read LICENSE.txt for more information. If you need support,
python-omhe is avaiable under a commercial license by Videntity Systems, Inc. 

	If you need commercial support please email us at sales [at] videntity [dot] [com]


Table of Contents:
==================
.. toctree::
   :maxdepth: 3



1. Background:
==============

OMHE is a microsyntax.org project.  The goal behind OMHE is to help exchange
data over mobile device such as phones or medical or wellness devices.

Read all about it here:
::
    http://code.google.com/p/omhe

Note the latest code has moved to github.
::
    http://github.com/aviars/python-omhe


The library also includes tools to capture and upload bloodpressure information
from an A&D monitor, capture and upload weight from a Wii Balance board.
The upload utilities are configured to upload information to a RESTCat server.
See http://github.com/aviars/RESTCat for more information



2. Dependencies:
================

We assume you are already running 2.5, or 2.6. If you are on Linux
or MacOS, chances are Python is already installed.  The upload tools require
pycurl.  The blood pressure application requires pyserial.  The Wii Balance Board
application requires Cwiid.

The python-omhe library requires no additional dependicies at this time.

3. Installation:
===============
Installing with sudo apt-get in:
There are many ways to install on Linux, Mac or Windows. Here is an example
on Ubuntu Linux.  Adjust these instructions to you platform.
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
    git clone git://github.com/aviars/python-omhe.git
    cd python-omhe
    python setup.py install
    
To uninstall python-omhe
::
    pip uninstall python-omhe
    
Press y when prompted




4. How to Use the Parser:
==========================

It takes a string as a single argurment and returns parsed data.
::
    #import the omheparser library
    from omhe.core.parseomhe import parseomhe
    
    #create a strng to parse
    omhe_str="bp=120/80p60#dt20101217:083059z"
    
    #Create a new OMHE object
    o = parseomhe()
    
    # Call the paser method and return a parsed dict
    # If something is malformed, an error value will be
    # in the dictionary raised.
    d=o.parse(omhe_str)
    
    #print the dictionary
    print d

The output of the previous code might look like this:
::
    {
    'tx_dt': '201071:16438z',
    'bp_pul': '60',
    'tz': '12',
    'tags': ['dt20101217:083059z', 'tz12'],
    'id': '266a7b2f-64eb-4e7b-9abf-a25dfd1db890',
    'bp_syst': '120',
    'bp_dia': '80',
    'value': '120/80p60',
    'ev_dt': 20101217:164208z
    'ev_tz': 0,
    'omhe': 'bp',
    'tx_dt': '20101217:093100z'
    'tx_tz': 0,
    }
    
Now lets convert it to json
::
    j=o.omhedict2json(d)
    print j
    
The easist way to try it out is to just run the command line utility.  All of
these commands will validate.  The pomhe utility outputs JSON.
::
    python pomhe bp120/80p60#dt20100701:121212#tx-5
    
    python pomhe bp120/80p60
    
    python pomhe bp120/80p60#afteryog

5. Using the GUI Applications.

To run the bloodpressure GUI:
::
    python bloodpressure.py
    

Run the WiiBalance Sample GUI:
::
    python wiibal-weightdemo.py
    
See wiibalance_ for more information.
.. _wiibalance: ./omhehardware/wiibalance/README.rst

6. TODOs:
=========

Validators are still needed for many omhe commands.  Simply add you validator
function to omhevalidators.py and make sure they are 'turned on' in the code
by having the command and validation function present in the omhe_validators
dictionary in the parsepmhe.py file.

7. DEDICATIONS:
===============
This code is dedicated to my Grandmother, Rachel Bradshaw, who
is in her 90's and has Congestive Heart Failure, to my father who recently had
open heart surgery and  to all those who struggle to stay well or get better.


8 SUPPORT:
==========

This is free open source software commerically supported by Videntity Systems,
Inc.  Among other things, Videntity commercialy supports the
python-omhe library. http://videntity.com
    
