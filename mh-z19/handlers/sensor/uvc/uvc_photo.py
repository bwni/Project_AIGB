# -*- coding: utf-8 -*-
# original: https://raw.githubusercontent.com/UedaTakeyuki/slider/master/mh_z19.py
#
# © Takeyuki UEDA 2015 -
import os
import subprocess
import ConfigParser
import datetime
import requests
import urllib3
import shutil
from error_counter import Counter
from urllib3.exceptions import InsecureRequestWarning
# refer http://73spica.tech/blog/requests-insecurerequestwarning-disable/
urllib3.disable_warnings(InsecureRequestWarning)

# Const
configfile = os.path.dirname(os.path.abspath(__file__))+'/uvc_photo.ini'

# setting
settings = {
  "folder": "/tmp/",
  "device": "/dev/video0",
  "delay":  "1",
  "skip":   "20",
  "width":  "320",
  "hight":  "240",
  "er_on":  False,
  "read_error_counter": "",
  "send_error_counter": ""
}

# https://code.i-harness.com/en/q/aea99
def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")

# termination type
TERMINATOR_DELETEVALUE_AS_FILE=True

def setconfig(ini):
  global settings

  if "photo" in ini.sections():
    if "folder" in dict(ini.items("photo")).keys() and ini.get("photo","folder"):
      settings["folder"] = ini.get("photo","folder")
    if settings["folder"][-1:] != "/":
      settings["folder"] += "/"
    if not os.path.exists(settings["folder"]):
      os.makedirs(settings["folder"]) # keyword "exist_ok" is for 3 

    if "device" in dict(ini.items("photo")).keys() and ini.get("photo","device"):
      settings["device"] = ini.get("photo","device")
    if "delay"  in dict(ini.items("photo")).keys() and ini.get("photo","delay"):
      settings["delay"] = ini.get("photo","delay")
    if "skip"   in dict(ini.items("photo")).keys() and ini.get("photo","skip"):
      settings["skip"] = ini.get("photo","skip")
    if "width"  in dict(ini.items("photo")).keys() and ini.get("photo","width"):
      settings["width"] = ini.get("photo","width")
    if "hight"  in dict(ini.items("photo")).keys() and ini.get("photo","hight"):
      settings["hight"] = ini.get("photo","hight")

  if "error_recovery" in ini.sections():
    if "recover_on" in dict(ini.items("error_recovery")).keys() and ini.get("error_recovery","recover_on"):
      settings["er_on"] = str2bool(ini.get("error_recovery", "recover_on")) # error_recovery
    # error_counter
    if settings["er_on"]:
      if "readcounterfile" in dict(ini.items("error_recovery")).keys() and ini.get("error_recovery","readcounterfile"):
        settings["read_error_counter"] = Counter(ini.get("error_recovery", "readcounterfile"))
      if "readcounterfile" in dict(ini.items("error_recovery")).keys() and ini.get("error_recovery","sendcounterfile"):
        settings["send_error_counter"] = Counter(ini.get("error_recovery", "sendcounterfile"))
      if "savecounterfile" in dict(ini.items("error_recovery")).keys() and ini.get("error_recovery","savecounterfile"):
        settings["save_error_counter"] = Counter(ini.get("error_recovery", "savecounterfile"))


if os.path.exists(configfile):
  ini = ConfigParser.SafeConfigParser()
  ini.read(configfile)
  setconfig(ini)

def take_photo():
  global settings
  now = datetime.datetime.now()
  filepath = "{}{}.jpg".format(settings["folder"],now.strftime("%Y%m%d%H%M%S"))
  if os.path.exists(filepath): # remove if old version exist
    os.remove(filepath)

  command_str = "fswebcam --no-timestamp --title \"©Atelier UEDA\" {} -d {} -D {} -S {} -r {}x{}".format(filepath,
                                                                  settings["device"],
                                                                  settings["delay"],
                                                                  settings["skip"],
                                                                  settings["width"],
                                                                  settings["hight"])
  p = subprocess.Popen(command_str, stderr = subprocess.PIPE, shell=True)
  p.wait() # wait for finish.

  if not os.path.exists(filepath): # Camera IO erro
#    raise IOError(''.join(p.stderr.readlines()))
    if settings["er_on"]:
      settings["read_error_counter"].inc_error()
  else:
    if settings["er_on"]:
      settings["read_error_counter"].reset_error()

  return filepath

def read():
  return {"photo": take_photo()}

def is_photo_source(sensor_handlers):
  return 'TERMINATOR_DELETEVALUE_AS_FILE' in dir(sensor_handlers)

def handle(sensor_handlers, data_name, value):
  print ("start handle")
  if is_photo_source(sensor_handlers):
    files = {'upfile': open(value, 'rb')}
    payload = {'viewid': ini.get("server", "view_id")}

    r = None
    try:
      r = requests.post(ini.get("server", "url"), data=payload, files=files, timeout=10, verify=False)
    except:
      if settings["er_on"]:
        settings["send_error_counter"].inc_error()

    if not r is None:
      if settings["er_on"]:
        settings["send_error_counter"].reset_error()
      print r.text

    save(ini.get("server", "view_id"), value)

  print ("end handle")

def save(viewid, picfilepath):
    try:
        # make saving folder
        base_of_saving_folder = ini.get("save", "data_path")
        saving_folder = base_of_saving_folder + "/" + viewid
        if not os.path.exists(saving_folder):
          os.makedirs(saving_folder)
        shutil.copyfile(picfilepath, saving_folder + "/" + os.path.basename(picfilepath))
    except:
      if settings["er_on"]:
        settings["save_error_counter"].inc_error()

    if settings["er_on"]:
      settings["save_error_counter"].reset_error()

def terminate(sensor_handlers, data_name, value):
  print ("start terminate")
  if is_photo_source(sensor_handlers):
    os.remove(value)
  print ("end terminate")

if __name__ == '__main__':
  value = read()
  print (value)
