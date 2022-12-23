import time
import board
from adafruit_bme280 import basic as adafruit_bme280

def temp_hum_run():
    # Create sensor object, using the board's default I2C bus.
    i2c = board.I2C()  # uses board.SCL and board.SDA
    # i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
    
    # Change this to match the location's pressure (hPa) at sea level
    # Current value: 1002.75; is estimated for Delft, The Netherlands
    bme280.sea_level_pressure = 1002.75
    # Sensor variables 
    temp = bme280.temperature
    humid = bme280.relative_humidity
    press = bme280.pressure
    height = bme280.altitude        
    return temp, humid, press, height

def run_test():
    """
    Run_test is usable for making a test to see if the bme280 sensor
    functions.
    """
    # Create sensor object, using the board's default I2C bus.
    i2c = board.I2C()  # uses board.SCL and board.SDA
    # i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
    
    """
    # !!!Don't use the following if using I2C!!!
    # OR create sensor object, using the board's default SPI bus.
    # spi = board.SPI()
    # bme_cs = digitalio.DigitalInOut(board.D10)
    # bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, bme_cs)
    """
    # Change this to match the location's pressure (hPa) at sea level
    bme280.sea_level_pressure = 1002.75  
    
    # While loop for parameter output in cmd and on screen
    while True:
        # Sensor variables 
        temp = bme280.temperature
        humid = bme280.relative_humidity
        press = bme280.pressure
        height = bme280.altitude
        # Terminal output
        print("\nTemperature: %0.1f C" % temp)
        print("Humidity: %0.1f %%" % humid)
        print("Pressure: %0.1f hPa" % press)
        print("Altitude = %0.2f meters" % height)
        time.sleep(2)
    

if __name__ == "__main__":
    print("You are running the temp/hum-sensor python file.") 
