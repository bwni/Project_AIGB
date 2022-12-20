import adafruit_ssd1306
import board
import busio
from digitalio import DigitalInOut
import digitalio
from PIL import Image, ImageDraw, ImageFont
import time
from rpi_ws281x import *
import adafruit_am2320

def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

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
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
# Intialize the library (must be called once before other functions).
strip.begin()

i2c = board.I2C()
sensor = adafruit_am2320.AM2320(i2c)

spi = busio.SPI(board.SCLK, MOSI=board.MOSI, MISO=board.MISO)
dc_pin = DigitalInOut(board.D27)    # any pin!
reset_pin = DigitalInOut(board.D22) # any pin!
cs_pin = DigitalInOut(board.D8)    # any pin!

#oled = adafruit_ssd1306.SSD1306_SPI(128, 64, spi, dc_pin, reset_pin, cs_pin)
oled = adafruit_ssd1306.SSD1306_SPI(128,64,board.SPI(),digitalio.DigitalInOut(board.D27)
                                    ,digitalio.DigitalInOut(board.D22),
                                    digitalio.DigitalInOut(board.D17))

# 
font = ImageFont.load_default()
image = Image.new('1',(128,64))
draw = ImageDraw.Draw(image)

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 35)
# Draw the text
temp= sensor.temperature
t= 0
while True:
    draw.rectangle((0, 0, oled.width, oled.height * 2), outline=0, fill=0)
    draw.text((0, 0), "{0}°C".format(sensor.temperature), font=font, fill=255)
    draw.text((0, 30), "{0}%".format(sensor.relative_humidity), font=font, fill=255)
    oled.image(image)
    oled.show()
    time.sleep(1)
    colorWipe(strip, Color(255, 255, 255, 255))
    #colorWipe(strip, Color(0, 0, 0))

# # 
# while True:
#     temp= sensor.temperature
#     if (temp != t):
#         oled.fill(0)
#         oled.show
#         time.sleep(10)
#         draw.text((0, 0), "{0}°C".format(sensor.temperature), font=font, fill=255)
#         oled.image(image)
#         oled.show()
#         t=temp
#     time.sleep(1)
        
#     oled.fill(0)
#     oled.show()
#     #colorWipe(strip, Color(255, 255, 255, 255))
# 
#     draw.text((0, 0), "{0}°C".format(sensor.temperature), font=font, fill=255)
#     #draw.text((10,20), "Hello World", font=font, fill=100)
#     oled.image(image)
#     oled.show()

