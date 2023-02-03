#!/usr/bin/env python
import mh_z19
import time
import os
import sys
import subprocess

def get_co2():
    sensor_co2 = mh_z19
    co2_var = sensor_co2.read()
    co2 = list(co2_var.values())[0]		# This is needed to convert dict.value to int
    return co2


# while True:
#     
#     print(get_co2())
#     time.sleep(1)
