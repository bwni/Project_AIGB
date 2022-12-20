import adafruit_am2320
import board


i2c = board.I2C()
sensor = adafruit_am2320.AM2320(i2c)
print('Humidity: {0}%'.format(sensor.relative_humidity))
print('Temperature: {0}C'.format(sensor.temperature))