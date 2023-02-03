#!/usr/bin/env python
import cayenne.client
import logging
from gpiozero import Button, PWMLED, OutputDevice
import time
import RPi.GPIO as GPIO            # import RPi.GPIO module
from rpi_ws281x import *


# Channel variables

temperature = 25
humidity = 40
water_tank = 50 	# precentage
conductivity = 60	# zoveel procent afwijking van de vooringestelde waarde in procenten
co2 = 30 			# general ppm indoors = 400
brightness = 51
# GPIO

GPIO.setmode(GPIO.BCM)		# choose BCM or BOARD  
GPIO.setup(17, GPIO.OUT)	# set GPIO17 as an output; Fans
GPIO.setup(7, GPIO.OUT)		# Motor
GPIO.setup(16, GPIO.OUT)		# Motor
GPIO.setup(19, GPIO.OUT)		# Motor
GPIO.setup(24, GPIO.OUT)		# Motor
GPIO.setup(13, GPIO.OUT)
GPIO.output(13, 1)
pwm = GPIO.PWM(13, 1)


# LED setup

def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

LED_COUNT      = 192      # Number of LED pixels.
LED_PIN        = 21      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Default; Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
LED_STRIP      = ws.SK6812_STRIP_GRBW
#LED_STRIP      = ws.SK6812W_STRIP
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
strip.begin()
# led = PWMLED(21)
# # ~ r_led = PWMLED() + 100
# # ~ g_led = PWMLED()
# # ~ b_led = PWMLED() 
# # ~ pump = OutputDevice()
# # fan = OutputDevice(17)

# Set the Cayenne authentication information

MQTT_USERNAME  = "b6d7e900-6f0b-11ed-8d53-d7cd1025126a"
MQTT_PASSWORD  = "b7efd7c914d5a6dcb57336b30855e7236f0b7918"
MQTT_CLIENT_ID = "9eaed7b0-6f0d-11ed-b193-d9789b2af62b"

# Function to receive and set cayenne input data

def on_message(message):
    print("message recieved: " + str(message))
    if message.channel==70:
        if message.value=='1':
            GPIO.output(17,1) #ventilatoren
            print("fan on\n\n")
        elif message.value=='0':
            GPIO.output(17,0) #ventilatoren
            print("fan off\n\n")
    if message.channel==51:
        if message.value=='1':
            colorWipe(strip, Color(255, 0, 255))  # Red wipe with GRB --> aigb green with rgb
            print("led on")
        elif message.value=='0':
            colorWipe(strip, Color(0, 0, 0))  # Red wipe with GRB --> aigb green with rgb
            print("led off")
    if message.channel==52:
            colorWipe(strip, Color(int(message.value), 0, int(message.value)))
	# ~ if message.channel==89:
		# ~ if message.value=='1':
			# ~ GPIO.output(13,1) #pomp aan
			# ~ print("cooling on")
        # ~ elif message.value=='0':
            # ~ GPIO.output(13,0) #pomp uit
            # ~ print("cooling off")
    if message.channel==80:
        if message.value=='1':
            GPIO.output(7,1) #pomp aan
            print("motor on")
        elif message.value=='0':
            GPIO.output(7,0) #pomp uit
            print("motor off")
    if message.channel==81:
        if message.value=='1':
            GPIO.output(16,1) #pomp aan
            print("motor on")
        elif message.value=='0':
            GPIO.output(16,0) #pomp uit
            print("motor off")
    if message.channel==82:
        if message.value=='1':
            GPIO.output(19,1) #pomp aan
            print("motor on")
        elif message.value=='0':
            GPIO.output(19,0) #pomp uit
            print("motor off")
    if message.channel==83:
        if message.value=='1':
            GPIO.output(24,1) #pomp aan
            print("motor on")
        elif message.value=='0':
            GPIO.output(24,0) #pomp uit
            print("motor off")
    if message.channel==89:   # LED
        if message.value=="1":
            pwm.start(0)
            pwm.ChangeDutyCycle(100)
            
        elif message.value=="0":
            pwm.stop()
            pwm.ChangeDutyCycle(0)
    # ~ if message.channel==52:					# LED Red
        # ~ led.value=float(message.value)/100
        # ~ print(led.value)
    # ~ if message.channel==53:
        # ~ led.value=float(message.value)/100	# LED Green
        # ~ print(led.value)
    # ~ if message.channel==54:
        # ~ led.value=float(message.value)/100	# LED Blue
        # ~ print(led.value)
    # ~ if message.value=="100":				# 
        # ~ if message.value=="1":
            # ~ # button.when_pressed
        # ~ elif message.value=="0":
            # ~ # button.when_released

# Initialize the CayenneMQTT client

client = cayenne.client.CayenneMQTTClient()
client.on_message = on_message
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, port=1883, loglevel=logging.INFO)

# Function to send sensor data to Cayenne

def send_sensor_data(channel, value):
	client.loop()
	if channel == 10:
		client.celsiusWrite(channel, value)
	elif channel == 20:
		client.virtualWrite(channel, value, "rel_hum", "p")
	elif channel == 21:
		client.virtualWrite(channel, value, "type value", "unit value")
	elif channel == 30:
		client.virtualWrite(channel, value, "co2", "ppm")
	elif channel == 40:
		client.virtualWrite(channel, value, "pH", "p")
	elif channel == 60:
		client.virtualWrite(channel, value, "ec", "V")
		
    
#give channel
arr = [10,20,30] # predefined
#find in arr 
#als in array dan doorgeven in  functie 
#virtualwrite

i=0
timestamp = 0

# Example usage: send the temperature in Celsius to channel 1
# ~ while True:
	# ~ client.loop()
	# ~ if(time.time() > timestamp + 10):
		# ~ send_sensor_data(10, temperature)
		# ~ timestamp = time.time()
		# ~ i = i+1

