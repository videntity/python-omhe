#!/usr/bin/python
import sys
sys.path.insert(0, '/home/tbble/code/cwiid/svn/cwiid/python/build/lib.linux-x86_64-2.5/')
import sys

try:
 import simplejson as json
except:
 import json


from datetime import datetime

try:
	import pycurl
except:
	print "Sorry, I can't seem to import pycurl for some reason."
	print "Please check that it and it's python bindings are installed."
	print "If on Ubuntu try, sudo apt-get install pycurl"
	print "See http://pycurl.sourceforge.net/"
	sys.exit(1)

try:
	import cwiid
except:
	print "Sorry, I can't seem to import cwiid for some reason."
	print "Please check that it and it's python bindings are installed, and also the balance board patch from:"
	print "http://abstrakraft.org/cwiid/ticket/63"
	sys.exit(1)

try:
	from settings import callback_url, weight_output_file, wii_balance_hid,\
	timezone_offset
except:
	print "Sorry, I can't seem fo import the settings file."
	sys.exit(1)
	
def httpcallback(weight_dict):

	print "Callback to %s" % ( callback_url)
	"""Send an HTTP POST of weight"""
	pf=[]
	post_dict={}
	post_dict=weight_dict
	
	print post_dict
	for o in post_dict:
	    x=(str(o), str(post_dict[o]))
	    pf.append(x)    
	c = pycurl.Curl()
	c.setopt(c.SSL_VERIFYPEER, False)
	c.setopt(pycurl.URL, callback_url)
	c.setopt(c.HTTPPOST, pf)
	c.setopt(pycurl.HTTPHEADER, ["Accept:"])
	c.perform()
		



def main():
	#Connect to address given on command-line, if present
	print 'Put Wiimote in discoverable mode now (press 1+2)...'
	global wiimote
	if len(sys.argv) > 1:
		wiimote = cwiid.Wiimote(sys.argv[1])
	else:
		wiimote = cwiid.Wiimote()

	wiimote.rpt_mode = cwiid.RPT_BALANCE | cwiid.RPT_BTN
	wiimote.request_status()

	if wiimote.state['ext_type'] != cwiid.EXT_BALANCE:
		print 'This program only supports the Wii Balance Board'
		wiimote.close()
		return -1

	balance_calibration = wiimote.get_balance_cal()
	named_calibration = { 	'right_top': balance_calibration[0],
				'right_bottom': balance_calibration[1],
				'left_top': balance_calibration[2],
				'left_bottom': balance_calibration[3],
			}

	exit = False
	print "Type q to quit, or anything else to report your weight"
	while not exit:
		c=None
		c = sys.stdin.readline()
		c=c.strip('\n')
		c=c.strip('\t')
		c=c.strip(' ')
		if c.startswith('q'):
			exit = True
		wiimote.request_status()
		weight ="%.2f" % (calcweight(wiimote.state['balance'], named_calibration) / 100.0, )
		weight=float(weight)
		weightlbs=(weight * 2.2) + 2
		weight_dict={}
		weight_dict['hid']= wii_balance_hid
		weight_dict['wt_value']= str("%.2f" % (weightlbs))
		weight_dict['wt_units']= "l"
		weight_dict['ttype']= "omhe"
		weight_dict['texti']= str("wt=%.2f" % (weightlbs))
		weight_dict['subj']= "%s" % (c)
		d=datetime.utcnow()
		weight_dict['evdt']= d.strftime("%d%m%y:%H%M%Sz")
		weight_dict['evtz']= timezone_offset
		jsonstr=json.dumps(weight_dict, indent = 4,)
		print jsonstr
		file=open(weight_output_file, 'w')
		file.write(jsonstr)
		file.close()
		httpcallback(weight_dict)
		
	return 0

def calcweight( readings, calibrations ):
	"""
	Determine the weight of the user on the board in hundredths of a kilogram
	"""
	weight = 0
	for sensor in ('right_top', 'right_bottom', 'left_top', 'left_bottom'):
		reading = readings[sensor]
		calibration = calibrations[sensor]
#		if reading < calibration[0]:
#			print "Warning, %s reading below lower calibration value" % sensor
		if reading > calibration[2]:
			print "Warning, %s reading above upper calibration value" % sensor
		# 1700 appears to be the step the calibrations are against.
		# 17kg per sensor is 68kg, 1/2 of the advertised Japanese weight limit.
		if reading < calibration[1]:
			weight += 1700 * (reading - calibration[0]) / (calibration[1] - calibration[0])
		else:
			weight += 1700 * (reading - calibration[1]) / (calibration[2] - calibration[1]) + 1700

	return weight

if __name__ == "__main__":
	sys.exit(main())
