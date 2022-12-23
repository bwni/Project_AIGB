# Made by: Bram Nijhoff
# Date: 2/12/2022

import Dashboard
import Temp_hum_sens
from LCD_screen import visualise_screen

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


if __name__ == "__main__":
	while True:
		temp, hum, press, alt = Temp_hum_sens.temp_hum_run()
		print(temp, hum, press, alt)
		visualise_screen(temp, hum, press, alt)
