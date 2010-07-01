
Open Mobile Health Exchange (OMHE) Parser & Tools for Python
============================================================
(c) 2010 - All Rights Reserved.
Release 0.4dev
Author: Alan Viars (Videntity)
License: This code is open source and available via Apache2 license.
Please read LICENSE.txt for more information.


##############
# BACKGROUND #
##############

OMHE is a microsyntax.org project.  The goal behind OMHE is to help exchange
data over mobile device such as phones or medical or wellness devices.

Read all about it here:
::
    http://code.google.com/p/omhe

Note the latest code has moved to github.
::
    http://github.com/aviars/python-omhe



INSTALLATION:
------------

DEPENDENCIES:
~~~~~~~~~~~~~
We assume you are already running Python 2.4, 2.5, or 2.6. If you are on Linux
or MacOS, chance are python is already installed.

OMHE requires no additional dependicies at this time.


MANY WAYS TO INSTALL:
There are many ways to install on Linux, Mac or Windows.  Below is an overview
illustrating 4 ways to install.  You can adjust for your configuration.

You can install the most recently released version or you can install the
"bleeding edge" version in from the subversion repository.


Open a terminal window/command prompt and do the following.  You need root if
you want to add the package to you system's python packages.  Otherwise you
might want to install it elsewhere, like the current directory(.).

Download & install the tarball.

> pip install http://github.com/aviars/python-omhe-latest.tar.gz


#########################
# HOW TO USE THE PARSER #
#########################

It takes a string as a single argurment and returns parsed data.
::
    #import the omheparser library
    import parseomhe
    
    #create a strng to parse
    omhe_str="bp=120/80p60#dt19751217:083059z"
    
    #Instantiate a new OMHE object
    o = OMHE()
    
    #run the paser function and return a parsed dict
    #If something is malformed, an error will be raised.
    d=o.parse(omhe_str)
    
    #print the dictionary
    print d

The output of the previous code is:
::
    {'_tx_dt': '201071:16438u',
    'pul': '60',
    'tz': '12',
    'tags': ['dt19751217:083059z', 'tz12'],
    'uu': '266a7b2f-64eb-4e7b-9abf-a25dfd1db890',
    'syst': '120', 'dia': '80',
    'value': '120/80p60',
    'datetime': datetime.datetime(2010, 7, 1, 16, 43, 8, 2728),
    '_ev_dt': {'_ev_tz': 12}, 'command': 'bp',
    'dt': '19751217:083059z'}

The easist way to try it out is to just run the command line utility.  All of
these cpmmands will validate
::
    python parseomhe.py bp120/80p60#dt20100701:121212#tx-5
    
    python parseomhe.py bp120/80p60
    
    python parseomhe.py bp120/80p60#afteryog


TODO:
----

Validators are still needed for many omhe commands.  Simply add you validator
function to omhevalidators.py and make sure they are 'turned on' in the code
by having the command and validation function present in the omhe_validators
dictionary in the parsepmhe.py file.

##############
#DEDICATIONS #
##############

This code is dedicated to my Grandmother, Rachel Bradshaw, who
is in her 90's and has Congestive Heart Failure.

This is dedicated to my father who recently had open heart surgery.

The code is dedicated to all those who struggle to stay well or get better.

############
# SUPPORT  #
############
This is free open source software.  The project is actively maintained by
microsyntax.org.  Among other things, Videntity commercialy supports the
python-omhe library. http://videntity.com
    
