import sys
import time
sys.path.append(' ')
sys.path.append('/mymodules')
#import cv2 as cv
from PIL import Image, ImageDraw, ImageFont
from st7789v.interface import RaspberryPi
from st7789v import Display
from st7789v import BufferedDisplay
import adafruit_am2320
import board
i2c = board.I2C()
sensor = adafruit_am2320.AM2320(i2c)

font = ImageFont.load_default()
# image = Image.new('1',(320,240))
# draw = ImageDraw.Draw(image)

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 35)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
print("{0}°C".format(sensor.temperature))
print("{0}%".format(sensor.relative_humidity))

rpi = RaspberryPi()
rpi.open()
display = BufferedDisplay(rpi, rotation=90, reset=False)
draw = display.draw
draw.text((0, 0), "Real time", font=font, fill=255)
display.update()
t_end = time.time() + 60*2
while time.time() < t_end:
    time.sleep(1)
    display.draw.rectangle((0, 0, 320, 240), fill='BLUE')
    time.sleep(1)
    draw.text((0, 30), "{0}°C".format(sensor.temperature), fill = (128,255,128),font=font)
    display.update_partial(0, 35, 200, 70)
    draw.text((0, 70), "{0}%".format(sensor.relative_humidity), fill = (128,255,128),font=font)
    display.update_partial(0, 75, 200, 110)
    print("{0}°C".format(sensor.temperature))
    print("{0}%".format(sensor.relative_humidity))
rpi.close()
    

# with RaspberryPi() as rpi:
#     
#     display = BufferedDisplay(rpi, rotation=90, reset=False)
#     draw = display.draw
#     
#     draw.text((0, 0), "hoi", font=font, fill=255)
#     # Instantiante the display, and initialize it in landscape mode
#     #display = BufferedDisplay(rpi, rotation=270)
#     # Show a black screen (empty buffer)
#     display.update()
#     time.sleep(2)
#     # Draw a blue rectangle all over the buffer
#     display.draw.rectangle((0, 35, 200, 70), fill='BLUE')
#     time.sleep(1)
#     draw.text((0, 30), 'WaveShare', fill = (128,255,128),font=font)
#     # Update only the top half of the screen
#     display.update_partial(0, 0, 260, 120)
#     
#     
#     
    
#     # Read a frame from a video
#     img = cv.imread('/home/pi/testlcd/st7789v/examples/lena.png')
#     # Convert from BGR to RGB
#     image_rgb = img[:,:,::-1]
#     # Send to the screen
#     display.draw_rgb_bytes(image_rgb)
