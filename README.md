# Project AIGB

Welcome
------
Welcome to the Automate Indoor Growing Box (AIGB) control program. The main file is used to control incoming signals of sensors  and buttons, processing the data by visualising it on the display, and sending outgoing signals to the motors and LED-strips.

Package installation
------
Humidity and temperature sensor: https://learn.adafruit.com/adafruit-bme280-humidity-barometric-pressure-temperature-sensor-breakout/python-circuitpython-test#python-installation-of-bme280-library-2995297

2inch Display (drivertype: ST7789V): https://www.waveshare.com/wiki/2inch_LCD_Module

How to use the program
------
The files are installed on a raspberri pi 4, but it is also possible to run it on a raspberry pi 3 B+. By cloning the files from the repository, some of the packages are still needed to install on the pi.

For using the dashboard from cayenne.mydevice.com it is important to first link the rapberry pi by following the instructions. The following youtube shows you how: 

<iframe width="560" height="315" src="https://www.youtube.com/embed/Qx0IHv-UR-0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

In addition to the above clip it could happen that some of the libraries aren't up-to-date. Then pip install the following:

```pip3 install paho-mqtt```

The following pip install is for using the mh-z18 co2 sensor library:

```pip3 install mh-z18```

The following pip install is for using the mh-z18 co2 sensor library:

```pip3 install adafruit-bme280```
```pip3 install adafruit-circuitpython-bme280```

If the installation of al packages are completed, you can run the program from your designated programfolder by entering the following into the console: 

```sudo python3 main.py```


