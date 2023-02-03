# coding:utf-8 Copy Right Atelier Grenouille © 2015 -
#
import os
import sys
import datetime
import subprocess
import logging
import traceback


import requests

import configparser
import inspect

import incremental_counter
import error_counter

# Const
configfile = os.path.dirname(os.path.abspath(__file__))+'/save2strage.ini'

# get settings
if not os.path.exists(configfile):
    raise IOError("no config file!")

ini = configparser.SafeConfigParser()
ini.read(configfile)

if not "save" in ini.sections():
    raise IOError("no save section in config file!")
if not "log" in ini.sections():
    raise IOError("no log section in config file!")
if not "error_recovery" in ini.sections():
    raise IOError("no error_recovery section in config file!")

# https://code.i-harness.com/en/q/aea99
def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")

if "recover_on" in dict(ini.items("error_recovery")).keys():
    er_on = str2bool(ini.get("error_recovery", "recover_on")) # error_recovery
else:
    er_on = False

if "log_file" in dict(ini.items("log")).keys():
    log_on = True
else:
    log_on = False

# error_counter
if er_on:
    error_counter = error_counter.Counter(ini.get("error_recovery", "counterfile"))

# path to save
data_path = ini.get("save", "data_path")
if not os.path.exists(data_path):
    if not os.path.exists(os.path.dirname(data_path)):
        os.makedirs(os.path.dirname(data_path))

# logfile
if log_on:
    logfile = ini.get("log", "log_file")
    if not os.path.exists(logfile):
        if not os.path.exists(os.path.dirname(logfile)):
            os.makedirs(os.path.dirname(logfile))        
    logging.basicConfig(format='%(asctime)s %(filename)s %(levelname)s %(message)s',filename=logfile,level=logging.DEBUG)
#    logging.basicConfig(format='%(asctime)s %(filename)s %(lineno)d %(levelname)s %(message)s',filename=logfile,level=logging.DEBUG)

def msg_log(msg_str):
    print (str(inspect.currentframe().f_lineno) + " " + msg_str)
    if log_on: 
        logging.info(str(inspect.currentframe().f_lineno) + " " + msg_str)

def msg_err_log(msg_str):
    print (str(inspect.currentframe().f_lineno) + " " + msg_str)
    if log_on: 
        logging.error(str(inspect.currentframe().f_lineno) + " " + msg_str)

def handle(data_source_name, data_name, value):
    try:
        msg_log("start saving...")
        now = datetime.datetime.now()
#        now = datetime.datetime.utcnow()
        now_string = now.isoformat()
        path = data_path+"/"+data_name+".csv"
        linecounter = incremental_counter.Counter(data_path+"/"+data_name+".counter.txt")
        linecount = linecounter.inc()
        line = "{},{},{}".format(linecount, now_string, str(value))
        f = open(path, 'a')
        msg_log(line)
#        print >> f, line
        print (line, file=f)
        f.close()    
        msg_log("end saving...")
        if er_on:
            error_counter.inc_error()
    except IOError:
#        msg_err_log(sys.exc_info())
        logging.exception('')
        if er_on:
            error_counter.reset_error()
    except:
#        msg_err_log(sys.exc_info())
        logging.exception('')
        if er_on:
            error_counter.reset_error()

