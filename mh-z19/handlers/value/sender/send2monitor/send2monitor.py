# coding:utf-8 Copy Right Atelier Grenouille © 2018 -
#
import os
import sys
import traceback
import requests
#import ConfigParser
import configparser
import subprocess
from error_counter import Counter
import urllib3
from urllib3.exceptions import InsecureRequestWarning
# refer http://73spica.tech/blog/requests-insecurerequestwarning-disable/
urllib3.disable_warnings(InsecureRequestWarning)

# Const
configfile = os.path.dirname(os.path.abspath(__file__))+'/send2monitor.ini'

# get settings
ini = configparser.SafeConfigParser()
ini.read(configfile)

# https://code.i-harness.com/en/q/aea99
def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")

er_on = str2bool(ini.get("error_recovery", "recover_on")) # error_recovery

# error_counter
if er_on:
  error_counter = Counter(ini.get("error_recovery", "counterfile"))
#  error_counter = Counter(ini.get("error_recovery", "counterfile"), 
#                          ini.get("error_recovery", "recover_command"), 
#                          int(ini.get("error_recovery", "threshold"))
#                          )
def error_report():
  info=sys.exc_info()
  print (traceback.format_exc(info[0]))

def handle(data_source_name, data_name, value):
  global ini
  r = None
  try:
    r = requests.post(ini.get("server", "url"), 
                      data={'valueid': ini.get("valueid", data_name), 'value': value},
                      timeout=10,
                      verify=False)
  except requests.ConnectionError as e:
    error_report()
    if er_on:
      error_counter.inc_error()
  except:
    error_report()

  if not r is None:
    if er_on:
      error_counter.reset_error()
    print (r.text)

