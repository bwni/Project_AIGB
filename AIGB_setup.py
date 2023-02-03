# ~ def run():
import time
import bme280
from rpi_ws281x import *
import board
import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
GPIO.setup(7, GPIO.OUT)
GPIO.setup(17, GPIO.OUT) # set GPIO24 as an output

   
GPIO.output(7, 0)

GPIO.output(17,0) #ventilatoren

peltierpin = 13
GPIO.setup(peltierpin,GPIO.OUT)
GPIO.setwarnings(False)
#GPIO.output(peltierpin, 1)

#pwm = GPIO.PWM(peltierpin, 1)
#pwm.start(0)
#pwm.ChangeDutyCycle(100)

i2c = board.I2C()

# LED strip configuration:
LED_COUNT      = 192      # Number of LED pixels.
LED_PIN        = 21      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Default; Set to 0 for darkest and 255 for brightest
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

t = 255

# Main program logic follows:
if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    while True:
        # Color wipe animations
        #colorWipe(strip, Color(t,t,t,255))
        temperature,pressure,humidity = bme280.readBME280All()
        print(temperature)
        print(humidity)
        #colorWipe(strip, Color(0, 0, 0))  # off
        colorWipe(strip, Color(255, 0, 255))  # Red wipe with GRB --> aigb green with rgb
        #colorWipe(strip, Color(0, 255, 0))  # Green wipe with GRB --> aigb red with rgb
        #colorWipe(strip, Color(0, 0, 255))  # Blue  wipe  with GRB--> aigb blue with rgb

