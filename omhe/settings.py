#!/usr/bin/env python

#the username needed to authenticate to RESTcat
USERNAME='aviars'

#the password needed to authenticate to RESTcat
PASSWORD='password'

#the tx's sender - should always be an email
SENDER="aviars@videntity.com"

#the tx's receiver - should always be an email
RECEIVER="transparentp@microphr.com"

#the tx's subject - should always be an email
SUBJECT="aviars@videntity.com"

#the tx's security level. 1 is highest and 3 is lowest.
SEC_LEVEL=3

"""settings file for weight.py and bloodpressure.py"""
"""change this to your twittername"""
twitterid="aviars"
"""change this to your twitter password"""
twitterpass="yourpasswd" 
"""change this to the twitter account you wan to get the messg"""
twitterreceiver="vomhe"
"""change this to your actual serial port. on windows COM1, COM2, COMX
on Unix/Linx, ttyX. Note this currently only works with the A&D model UA-767PC"""
serial_port="/dev/ttyUSB1"
"""Set this to True if you want to add your reading to your PUBLIC timeline"""
public_tweet=False


