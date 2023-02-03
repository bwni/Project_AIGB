#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import time
sys.path.append('/home/pi/mymodules')
#import cv2 as cv
from PIL import Image, ImageDraw, ImageFont
from st7789v.interface import RaspberryPi
from st7789v import Display
from st7789v import BufferedDisplay
import adafruit_am2320
import board
import os
import sys
# ~ sys.path.insert(0, '/home/admin/git/Project_AIGB/st7789v-master')
import time
import atexit

font = ImageFont.load_default()
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)

# Use `display` to control the display, and `draw` to draw on the buffer.
rpi = RaspberryPi()
rpi.open()

display = BufferedDisplay(rpi, rotation=270, reset=False) #270


def view_display(temp=0, hum=0, co2=0, colour=0, lux=0, ph=0):
    draw = display.draw
    # ~ atexit.register(rpi.close)
    draw.text((0, 0), "SENSOR", font=font, fill=(128,255,128))

    t_end = time.time() + 1*2
    white = [(255,255,255)]*10
    draw.rectangle((130, 0, 135 ,240), fill='RED') #(begin x, begin y, end x, end y)
    draw.text((140, 10), "Current", fill = (128,255,128),font=font2)
    # ~ draw.text((230, 10), "Setpoint", fill = (128,255,128),font=font2)
    draw.text((0, 45), "Temperature", fill = (128,255,128),font=font2)
    draw.text((0, 75), "Humidity", fill = (128,255,128),font=font2)
    draw.text((0, 105), "Co2", fill = (128,255,128),font=font2)
    draw.text((0, 135), "Color", fill = (128,255,128),font=font2)
    draw.text((0, 165), "Brightness", fill = (128,255,128),font=font2)
    draw.text((0, 195), "pH", fill = (128,255,128),font=font2)
    display.update()
    
    time.sleep(1)
    display.draw.rectangle((0, 0, 320, 240), fill='BLACK')
    time.sleep(1)
    temp = str(temp)
    hum = str(hum)
    co2 = str(co2)
    
    draw.text((140, 45), temp[0:4]+"ºC", fill = (128,255,128),font=font2)
    display.update_partial(140, 45, 220, 67)
    
    draw.text((140, 75), hum[0:4]+"%", fill = (128,255,128),font=font2)
    display.update_partial(140, 75, 220, 97)
    
    draw.text((140, 105), co2[0:4]+" ppm", fill = (128,255,128),font=font2)
    display.update_partial(140, 105, 220, 127)
    
    # ~ draw.text((140, 135), temp[0:4]+"ºC", fill = (128,255,128),font=font2)
    # ~ display.update_partial(140, 135, 220, 157)
    
    # ~ draw.text((140, 165), temp[0:4]+"ºC", fill = (128,255,128),font=font2)
    # ~ display.update_partial(140, 165, 220, 187)

    # ~ draw.text((140, 195), temp[0:4]+"ºC", fill = (128,255,128),font=font2)
    # ~ display.update_partial(140, 195, 220, 217)
    
    #setpoint onder
    
    display.update_partial(240, 45, 320, 67)
    
    display.update_partial(240, 75, 320, 97)
    
    display.update_partial(240, 105, 320, 127)
    
    display.update_partial(240, 135, 320, 157)
    
    display.update_partial(240, 165, 320, 187)
    display.update_partial(240, 195, 320, 217)

def display_close():
	rpi.close()

#i2c = board.I2C()
#sensor = adafruit_am2320.AM2320(i2c)

# init


# image = Image.new('1',(320,240))
# draw = ImageDraw.Draw(image)


#print("{0}°C".format(sensor.temperature))
#print("{0}%".format(sensor.relative_humidity))
# ~ sensor = temp



