.. image::  http://github.com/aviars/python-omhe/raw/master/omhe.png

WiiBalance README:
==================

Open Mobile Health Exchange (OMHE) Parser & Tools for Python

(c) 2010. All Rights Reserved.

Release 0.3dev

Authors: Alan Viars (Videntity)

License: This code is open source and available via Apache2 license.

Please read LICENSE.txt for more information.
 

These instructions will help you connect your Wii Balance board to your Ubunutu Linux
computer, output the weight im OMHE format and upload it to RESTCat so it can be
stored, shared, and visualized.

Table of Contents:
==================
.. toctree::
   :maxdepth: 3


1. Setting up Your computer to talk with a Wii Balance Board:
=============================================================

These instructions were modified from Matt Cutt's blog article:
    http://www.mattcutts.com/blog/linux-wii-balanceboard/

::
    sudo apt-get install autoconf autogen automake gcc bluetooth
    libbluetooth3-dev libgtk2.0-dev pkg-config python2.6-dev flex
    bison git-core libbluetooth-dev python-pygame python-tk
    

Check out the CWiid (get it? CWiid? Seaweed?) library using Subversion:
::
    mkdir bin
    cd bin
    git clone http://github.com/abstrakraft/cwiid.git
    cd cwiid


Compile the library, e.g.
::
    aclocal
    autoconf
    ./configure
    make
    sudo make install
    
You can test things with a Wii Remote by running the GUI
::
    wmgui

Lets now install the python bindings:
::
    cd python
    sudo python setup.pt install

If this works then your computer is now read to connect to the balance board.
If you have problems please see the cwiid documentaion.  These instructions
were tested on Ubuntu 10.

2. Using the Wii Balance Board Application:
===========================================

Run the weightdemo.py application and immedatly press the red button on the
bottom of your balance board to sync the bluetooth connection.  If all goes well
you will see a GUI display on your computer.
::
    python scalesgui.py
    
If you get an error message, r/o error or a bluetooth connection timeout
just run the application again.

3. Capture Your Weight:
========================

Press F2 to capture your weight.  You'll see another screen come up to upload
your weight to RESCat.  Enter your username and password and press Send.  If
your weight is uploaded successfuly, the application will automaticall close
and return control to the Balance Board application.  (So its ready for the
next victim) Press F12 to exit the balance board application.




