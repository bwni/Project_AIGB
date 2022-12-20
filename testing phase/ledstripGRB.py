import time

from rpi_ws281x import *
import board
import adafruit_am2320

i2c = board.I2C()
sensor = adafruit_am2320.AM2320(i2c)

# LED strip configuration:
LED_COUNT      = 192      # Number of LED pixels.
LED_PIN        = 21      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
LED_STRIP      = ws.SK6812_STRIP_GRBW
#LED_STRIP      = ws.SK6812W_STRIP

def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)



# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()
	while True:
		# Color wipe animations
		colorWipe(strip, Color(0, 0, 0))  # off
		colorWipe(strip, Color(255, 0, 0))  # Red wipe with GRB --> aigb green with rgb
		colorWipe(strip, Color(0, 255, 0))  # Green wipe with GRB --> aigb red with rgb
		colorWipe(strip, Color(0, 0, 255))  # Blue  wipe  with GRB--> aigb blue with rgb
		print('Humidity: {0}%'.format(sensor.relative_humidity))
		print('Temperature: {0}C'.format(sensor.temperature))