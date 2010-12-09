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

# The server and port
#RESTCAT_SERVER="http://restcat1.wellrbox.com:80"
RESTCAT_SERVER="http://127.0.0.1:8000"
#the tx's security level. 1 is highest and 3 is lowest.
SEC_LEVEL=3

"""Change this to your actual serial port. on windows COM1, COM2, COMX
on Unix/Linx, ttyX. Note this currently only works with the A&D model UA-767PC"""
SERIAL_PORT="/dev/ttyUSB0"







