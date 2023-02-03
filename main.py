# Made by: Bram Nijhoff
# Date: 2/12/2022

#!/usr/bin/env python
# ~ from AIGB_setup import *
from Dashboard import send_sensor_data
import Temp_hum_sens
# ~ from LCD_screen import visualise_screen
import time
from co2 import get_co2
import AIGB_display
import cond_ph

"""
Welcome to the Automate Indoor Growing Box (AIGB) control program.
The main file is used to control incoming signals of sensors 
and buttons, processing the data by visualising it on the display, 
and sending outgoing signals to the motors and LED-strips.


Goal: Automate the process of growing plants.

Result: 	A fully growed herb or lettuce plant, or germinated sprouds 
			of plants like vegetables and fruits.
"""

"""
How-to:
Follow the guide on the following website:
https://www.waveshare.com/wiki/2inch_LCD_Module
"""

# Dashboard channels

temp_channel = 10
hum_channel = 20
water_tank_channel = 21
co2_channel = 30
ph_channel = 40
ph_value_channel = 41
led_intensity_channel = 50
led_switch_channel = 51
led_slide_channel = 52
led_red_slide_channel = 53
led_green_slide_channel = 54
led_blue_slide_channel = 55
conductivity_channel = 60

i = 0
timestamp = 0

if __name__ == "__main__":
	while True:
		temp, hum, press, alt = Temp_hum_sens.temp_hum_run()
		co2 = get_co2()
		ph_ec_temp, ph, ec = cond_ph.read_ph_ec() #ec en ph omgewisseld hardwarematig
		# 		print(temp, hum, press, alt)
		# visualise_screen(temp, hum, press, alt)
		send_sensor_data(temp_channel, temp)
		send_sensor_data(hum_channel, hum)
		send_sensor_data(co2_channel, co2)
		send_sensor_data(conductivity_channel, ec)
		send_sensor_data(ph_channel, ph)
		AIGB_display.view_display(temp, hum, co2, colour=0, lux=0, ph=0)
		# ~ if (time.time() > timestamp + 10):
		
			# ~ timestamp = time.time()
			# ~ i = i+1
	AIGB_display.display_close()	
