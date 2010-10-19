#!/usr/bin/env python

#the username needed to authenticate to RESTcat
USERNAME='aviars'

#the password needed to authenticate to RESTcat
PASSWORD='password'

#the tx's sender - should always be an email
SENDER="alan.viars@videntity.com"

#the tx's receiver - should always be an email
RECEIVER="alan.viars@videntity.com"

#the tx's subject - should always be an email
SUBJECT="alan.viars@videntity.com"

RESTCAT_SERVER="http://restcat1.wellrbox.com:80"

#the tx's security level. 1 is highest and 3 is lowest.
SEC_LEVEL=3

"""Change this to your actual serial port. on windows COM1, COM2, COMX
on Unix/Linx, ttyX. Note this currently only works with the A&D model UA-767PC"""
SERIAL_PORT="/dev/ttyUSB0"


"""settings file for weight.py and bloodpressure.py"""
"""change this to your twittername"""
twitterid="aviars"
"""change this to your twitter password"""
twitterpass="yourpasswd" 
"""change this to the twitter account you wan to get the messg"""
twitterreceiver="vomhe"
"""Set this to True if you want to add your reading to your PUBLIC timeline"""
public_tweet=False





