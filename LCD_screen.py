#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
sys.path.insert(0, '/home/admin/git/Project_AIGB/st7789v-master')
from st7789v.interface import RaspberryPi
from st7789v import BufferedDisplay
import time
from PIL import ImageFont
import atexit

font = ImageFont.load_default()
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 35)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)

# Use `display` to control the display, and `draw` to draw on the buffer.
rpi = RaspberryPi()
rpi.open()

def fake_sensor_update():
	return time.time()

def mk_rectangle(l, w):
	pass

def mk_writing(string, font):
	pass

def visualise_screen(temperature=0, humidity=0, pressure=0, height=0):
	# Don't use try; except if running the main.py file	
	# ~ try:
	display = BufferedDisplay(rpi, rotation=270, reset=False)
	draw = display.draw
	atexit.register(rpi.close)
	# ~ t_end = time.time() + 60*2 # 60sec keer 2 = 2min
	time.sleep(1)
	# ~ display.draw.rectangle((0, 0, 320, 240), fill='BLUE')
	# ~ display.update_partial(0, 0, 320, 120)
	display.draw.rectangle((1,1, 318,238), fill = 'WHITE',outline='BLUE')
	display.draw.text((5, 5), f'time: {fake_sensor_update()}', fill = 'BLACK',font=font2)
	display.draw.text((5, 45), f'temp: {temperature}', fill = 'BLACK',font=font2)
	display.draw.text((5, 85), f'hum: {humidity}', fill = 'BLACK',font=font2)
	display.draw.text((5, 125), f'press: {pressure}', fill = 'BLACK',font=font2)
	display.draw.text((5, 165), f'height: {height}', fill = 'BLACK',font=font2)
	display.update()
	time.sleep(1)
		# ~ rpi.close()		
		# ~ sys.exit(0)
	# ~ except IOError as e:
	    # ~ logging.info(e)    
	# ~ except KeyboardInterrupt:
	    # ~ disp.module_exit()
	    # ~ logging.info("quit:")
	    # ~ exit()
