#!/usr/bin/python
"""scalesgui.py
"""

import sys,time

try:
	import pygame
except:
	print "Sorry, I can't seem to import pygame for some reason."
	print "Please check that the python-pygame package is installed, or get the latest version of pygame from http://www.pygame.org/"
	sys.exit(1)
	
try:
	import cwiid
except:
	print "Sorry, I can't seem to import cwiid for some reason."
	print "Please check that it and it's python bindings are installed, and also the balance board patch from:"
	print "http://abstrakraft.org/cwiid/ticket/63"
	sys.exit(1)

import os, math, random
import time as ptime
from pygame.locals import *
from ConfigParser import ConfigParser
from threading import Thread

class WeightSprite(pygame.sprite.Sprite):
	"""This class describes a sprite containing the weight."""
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.weight = 0.0
		self.update()
		
	def update(self):
		global screen_res, sys_font_weight_fgcolour, sys_font_weight, screen_res
		
		if self.weight > 5:
			self.text = "%.2f" % self.weight
		else:
			self.text = "_.__"
			#print "LESS THAN 2"
		#while len(self.text) < 4:
		#	self.text = "0" + self.text
			
		self.image = sys_font_weight.render(self.text, True, sys_font_weight_fgcolour)

		self.rect = self.image.get_rect()
		self.rect.bottomright = screen_res

def input(events): 
   for event in events: 
      if event.type == QUIT: 
         sys.exit(0) 
      else: 
         print event 		

def quit_app():
	pygame.quit()
	sys.exit(0)
	
def calcweight( readings, calibrations ):
	"""
	Determine the weight of the user on the board in hundredths of a kilogram
	"""
	weight = 0
	for sensor in ('right_top', 'right_bottom', 'left_top', 'left_bottom'):
		reading = readings[sensor]
		calibration = calibrations[sensor]
		#if reading < calibration[0]:
		#	print "Warning, %s reading below lower calibration value" % sensor
		if reading > calibration[2]:
			print "Warning, %s reading above upper calibration value" % sensor
		# 1700 appears to be the step the calibrations are against.
		# 17kg per sensor is 68kg, 1/2 of the advertised Japanese weight limit.
		if reading < calibration[1]:
			weight += 1700 * (reading - calibration[0]) / (calibration[1] - calibration[0])
		
		else:
			weight += 1700 * (reading - calibration[1]) / (calibration[2] - calibration[1]) + 1700
			

	return weight
	
def gsc(readings, pos):
	global named_calibration
	reading = readings[pos]
	calibration = named_calibration[pos]
	
	if reading < calibration[1]:
		return 1700 * (reading - calibration[0]) / (calibration[1] - calibration[0])
	else:
		return 1700 * (reading - calibration[1]) / (calibration[2] - calibration[1]) + 1700
		
	
print "Please press the red 'connect' button on the balance board, inside the battery compartment."
print "Do not step on the balance board."

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
	sys.exit(1)

balance_calibration = wiimote.get_balance_cal()
named_calibration = { 'right_top': balance_calibration[0],
					  'right_bottom': balance_calibration[1],
					  'left_top': balance_calibration[2],
					  'left_bottom': balance_calibration[3],
					}

system_file = "system.ini"

if not os.path.lexists(system_file):
	print "Problem: System configuration file (system.ini) doesn't exist."
	sys.exit(1)

sconf = ConfigParser()
sconf.read(system_file)


xdisplay = sconf.get("display", "xdisplay")
if len(xdisplay) > 1:
	# using alternate display.
	print "Attempting to use device", xdisplay, "instead of the default."
	os.putenv("DISPLAY", xdisplay)

pygame.init()

sys_font_weight = pygame.font.SysFont(sconf.get("font_weight", "face"), int(sconf.get("font_weight", "size")))

sys_font_weight.set_italic(False)
sys_font_weight.set_underline(False)

bgcolour = (0, 0, 0)
sys_font_weight_fgcolour = (255, 255, 255)
screen_res = (int(sconf.get("display", "width")), int(sconf.get("display", "height")))
refresh_delay = int(sconf.get("display", "refresh_delay"))

screen_options = 0
if int(sconf.get("display", "fullscreen")) >= 1 and len(xdisplay) <= 1:
	screen_options = screen_options | pygame.FULLSCREEN

if int(sconf.get("display", "double_buffers")) >= 1:
	screen_options = screen_options | pygame.DOUBLEBUF

if int(sconf.get("display", "hardware_surface")) >= 1:
	screen_options = screen_options | pygame.HWSURFACE

if int(sconf.get("display", "opengl")) >= 1:
	screen_options = screen_options | pygame.OPENGL

screen = pygame.display.set_mode(screen_res, screen_options)
pygame.display.set_caption("scales application")

weight_sprite = WeightSprite()
weight_sprite.weight = 40.33
frame = 0
record=False
weight_list=[]
while True:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_F12:
				quit_app()
			if event.key == K_F2:
				record=True
	
	if record==True:
		print "recording..."
		#print weight_sprite.weight
		weight_list.append(weight_sprite.weight)
		if len(weight_list)>100:
			record=False
			print "Finished recording"
			#print weight_list
			average = float(sum(weight_list)) / len(weight_list)
			print "Average=%.2f" % average
			cmd = 'python /home/alan/django-projects/python-omhe/omhe/weight.py %s' % average
			os.system(cmd)
			weight_list=[]
			
	wiimote.request_status()
	frame = frame + 1
	if frame == 50:
		frame = 0
		weight = (calcweight(wiimote.state['balance'], named_calibration) / 100.0)
		
		print "%.2fkg" % weight
		
		weightlbs=weight * 2.2
		#print "%.2flb" % (weightlbs)
		weight_sprite.weight = weightlbs + 2
	
	
	readings = wiimote.state['balance']
	
	try:
		x_balance = (float(gsc(readings,'right_top')+gsc(readings,'right_bottom'))) / (float(gsc(readings,'left_top')+gsc(readings,'left_bottom')))
		if x_balance > 1:
			x_balance = (((float(gsc(readings,'left_top')+gsc(readings,'left_bottom'))) / (float(gsc(readings,'right_top')+gsc(readings,'right_bottom'))))*-1.)+1.
		else:
			x_balance = x_balance -1.
		y_balance = (float(gsc(readings,'left_bottom')+gsc(readings,'right_bottom'))) / (float(gsc(readings,'left_top')+gsc(readings,'right_top')))
		if y_balance > 1:
			y_balance = (((float(gsc(readings,'left_top')+gsc(readings,'right_top'))) / (float(gsc(readings,'left_bottom')+gsc(readings,'right_bottom'))))*-1.)+1.
		else:
			y_balance = y_balance -1.
	except:
		x_balance = 1.
		y_balance = 1.
	
	#print "readings:",readings

	screen.fill(bgcolour) # blank the screen.
	
	# line up the lines
	pygame.draw.line(screen, (0,0,255), (screen_res[0]/2,0), (screen_res[0]/2,screen_res[1]), 2)
	pygame.draw.line(screen, (0,0,255), (0,screen_res[1]/2), (screen_res[0],screen_res[1]/2), 2)
	
	weight_sprite.update()
	
	screen.blit(weight_sprite.image, weight_sprite.rect)
	
	xpos = (x_balance * (screen_res[0]/2)) + (screen_res[0]/2)
	ypos = (y_balance * (screen_res[1]/2)) + (screen_res[1]/2)
		
	#print "balance:", x_balance, y_balance
	#print "position:", xpos,ypos
	pygame.draw.circle(screen, (255,0,0), (int(xpos), int(ypos)), 5)
	pygame.display.flip()
	pygame.time.wait(refresh_delay)	





