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

On Ubuntu you'll nees a few prereqs.  thwe following command should
work on Ubuntu 10.
::
    sudo apt-get install autoconf autogen automake gcc bluetooth
    libbluetooth3-dev libgtk2.0-dev pkg-config python2.6-dev flex
    bison git-core libbluetooth-dev python-pygame python-tk
    

Check out the CWiid (get it? CWiid? Seaweed?) library using Git:
::
    mkdir bin
    cd bin
    git clone http://github.com/abstrakraft/cwiid.git
    cd cwiid


Compile the Cwiid library. At the command line execute the following
::
    aclocal
    autoconf
    ./configure
    make
    sudo make install
    
You can test things with a Wii Remote by running the GUI (This GUI will not work
on a headless server)
::
    wmgui

Lets now install the python bindings:
::
    cd python
    sudo python setup.py install

If this works, then your computer is now read to connect to the balance board.
If you have problems please see the cwiid documentation.  These instructions
were tested on Ubuntu 10.

2. Using the Wii Balance Board Application:
===========================================

Run the weightdemo.py application and immediately press the red button on the
bottom of your balance board to sync the bluetooth connection.  If all goes well
you will see a GUI display on your computer.
::
    python wiibalance_weight.py
    
If you get an error message, r/w error or a bluetooth connection timeout
just run the application again.  check to make sure you don't have another
python process running and trying to access the board.  Press 'q' to exit the
application.  Anything else is interpreted as the user's identifier.  So this
is designed to work well with a card reader, number pad, or any other standard
input that helps identify the user.  This is how we are binding the user to his
or her weight.  There is no format here.  You can use whatever makes sense for
you, but if you are using a RESTCat server in a standard configuration, then
an email address might make the most sense.

This applicating will do 3 things each time you press enter:
* Send  your weight (via callback) along with some other information
* Write your weight to a JSON file (filename defined in settings.py)
* Print the JSON file to standard output (Most often the screen)


3. Serve Your Weight:
=====================

There are two ways to do this; a push and a pull.  This simple tool support both
ways.

3.1 Pushing your weight with an HTTP callback:
----------------------------------------------
wiibalance_weight.py will push your information with an HTTP callback at the
address defined in your settings.py file.
This means that we will perform an HTTP client POST containing the weight
information.  You must write and make available your own callback handler
at the URL specified in your settings.py.  

3.2 Pulling (Polling) weight from a Webserver:
----------------------------------------------
Using wiibalance_server.py you can make your weight available via a webserver.
wiibalance_server.py is a simple web server written in pure python that simply
serves the file containing the weight information.  This file is generated
by wiibalance_weight.py and its filepath is defined in settings.py.  By default
this file's name is wiiweightout.json.  So lets have an example shall we?
This command start the server
::
    python wiibalance_server.py
    
You should see the message:
::
    Serve forver

Make sure you are using a port not used by another process (such as Apache, etc.)
Change this in settings.py.

Now you're serving your Weight.  Use your browser or Curl to point to the URL.
By default its serving on port 8002 and will bind to any IP. So the following
should yield a JSON file result.  
::
    curl http://127.0.0.1:8002

Have fun! -Alan







