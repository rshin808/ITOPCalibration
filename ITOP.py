#!/usr/bin/env python

"""
    Name:   ITOP.py
    By  :   Reed Shinsato
    Date:   25 January 2016
    Rev:    -
    Desc:   This holds the scripts for running the ITOP Calibration module.
"""

# Libraries
import sys
import time
import subprocess 
import Adafruit_BBIO.GPIO as GPIO
from PINS import *

# Initialize GPIO
for key in PINS.keys():
    GPIO.setup(PINS[key], GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)

# Check if MAINPW_EN is High
EN = None
with open("EN", "rb") as ENFile:
    EN = bool(int(ENFile.read().split()[0]))

# Helper Functions
def ledsOff():
    for key in PINS.keys():
        if "LED" in str(key):
            GPIO.output(PINS[key], GPIO.LOW)

def setRF(a = 1, b = 1, c = 1):
    if a == 1:
        GPIO.output(PINS["RFSW_A"], GPIO.HIGH)
    else:
        GPIO.output(PINS["RFSW_A"], GPIO.LOW)
    if b == 1:
        GPIO.output(PINS["RFSW_B"], GPIO.HIGH)
    else:
        GPIO.output(PINS["RFSW_B"], GPIO.LOW)
    if c == 1:
        GPIO.output(PINS["RFSW_C"], GPIO.HIGH)
    else:
        GPIO.output(PINS["RFSW_C"], GPIO.LOW)

def setS(a = 1, b = 1):
    if a == 1:
        GPIO.output(PINS["SYS898_SELA"], GPIO.HIGH)
    else:
        GPIO.output(PINS["SYS898_SELA"], GPIO.LOW)
    if b == 1: 
        GPIO.output(PINS["SYS898_SELB"], GPIO.HIGH)
    else:
        GPIO.output(PINS["SYS898_SELB"], GPIO.LOW)

def setHATT(a = 1, b = 1, c = 1, d = 1, e = 1, f = 1):
    if a == 1:
        GPIO.output(PINS["HB_RFATT_1"], GPIO.HIGH)
    else:
        GPIO.output(PINS["HB_RFATT_1"], GPIO.LOW)
    if b == 1:
        GPIO.output(PINS["HB_RFATT_2"], GPIO.HIGH)
    else:
        GPIO.output(PINS["HB_RFATT_2"], GPIO.LOW)
    if c == 1:
        GPIO.output(PINS["HB_RFATT_3"], GPIO.HIGH)
    else:
        GPIO.output(PINS["HB_RFATT_3"], GPIO.LOW)
    if d == 1:
        GPIO.output(PINS["HB_RFATT_4"], GPIO.HIGH)
    else:
        GPIO.output(PINS["HB_RFATT_4"], GPIO.LOW)
    if e == 1:
        GPIO.output(PINS["HB_RFATT_5"], GPIO.HIGH)
    else:
        GPIO.output(PINS["HB_RFATT_5"], GPIO.LOW)
    if f == 1:
        GPIO.output(PINS["HB_RFATT_6"], GPIO.HIGH)
    else:
        GPIO.output(PINS["HB_RFATT_6"], GPIO.LOW)

def setLATT(a = 1, b = 1, c = 1, d = 1, e = 1, f = 1):
    if a == 1:
        GPIO.output(PINS["LB_RFATT_1"], GPIO.HIGH)
    else:
        GPIO.output(PINS["LB_RFATT_1"], GPIO.LOW)
    if b == 1:
        GPIO.output(PINS["LB_RFATT_2"], GPIO.HIGH)
    else:
        GPIO.output(PINS["LB_RFATT_2"], GPIO.LOW)
    if c == 1:
        GPIO.output(PINS["LB_RFATT_3"], GPIO.HIGH)
    else:
        GPIO.output(PINS["LB_RFATT_3"], GPIO.LOW)
    if d == 1:
        GPIO.output(PINS["LB_RFATT_4"], GPIO.HIGH)
    else:
        GPIO.output(PINS["LB_RFATT_4"], GPIO.LOW)
    if e == 1:
        GPIO.output(PINS["LB_RFATT_5"], GPIO.HIGH)
    else:
        GPIO.output(PINS["LB_RFATT_5"], GPIO.LOW)
    if f == 1:
        GPIO.output(PINS["LB_RFATT_6"], GPIO.HIGH)
    else:
        GPIO.output(PINS["LB_RFATT_6"], GPIO.LOW)

def setHATT(value = 0):
    if float(int(value) * 2) == float(vlaue) * 2:
        pass
    
    


def RFOFF():
    setRF()
    ledsOff()

# Functions Users can call
def enable(parameters = None):
    """
        Name:   enable
        Desc:   This enables the Main Power for the board.
                The board is powered on with AUX enabled.
    """
    for key in PINS.keys():
        GPIO.output(PINS[key], GPIO.LOW)
    
    GPIO.output(PINS["MAINPW_EN"], GPIO.HIGH)

    with open("EN", "wb") as ENFile:
        ENFile.write("1")

    time.sleep(1)

    aux(None)

    print "Main Power Enabled"
    print "Note: When finished use 'close' or 'shutdown'"

def close(parameters = None):
    for key in PINS.keys():
        if key != "MAINPW_EN":
            GPIO.output(PINS[key], GPIO.LOW)

    time.sleep(1)
    GPIO.output(PINS["MAINPW_EN"], GPIO.LOW)
    GPIO.cleanup()

    with open("EN", "wb") as ENFile:
        ENFile.write("0")
    
    print "Main Power Disabled"

def shutdown(parameters = None):
    close()
    subprocess.call(["shutdown", "-h", "now"])

def wgen(parameters = None):
    assert EN == True, "ERROR: Main Power Disabled"
    assert len(parameters) == 1, "WGEN only takes one parameter"
    RFOFF()
    
    if parameters[0] == 1:
        setRF(0, 0, 0)
     

def sine(parameters = None):
    assert EN == True, "ERROR: Main Power Disabled"
    assert len(parameters) == 1, "SINE only takes one parameter"
    RFOFF()

    if parameters[0] == 1:
        setRF(1, 0, 0)

def drf(parameters = None):
    assert EN == True, "ERROR: Main Power Disabled"
    assert len(parameters) == 1, "DRF only takes one parameter"
    RFOFF()
   
    if parameters[0] == 1:
        setRF(0, 1, 0)
        master(1)
        GPIO.output(PINS["MCLK_LED"], GPIO.HIGH)

        print ""
        print "DRF Enabled"
        print "Note: MASTER is Enabled by default"
        print "\tto change set either EXTT, LDT, or MASTER"
        print "\tonly one may be set at a time"
        print ""

def lbpm(parameters = None):
    assert EN == True, "ERROR: Main Power Disabled"
    assert len(parameters) == 1, "LBPM only takes one parameter"
    RFOFF()

    if parameters[0] == 1:
        setRF(1, 1, 0)
        GPIO.output(PINS["LBPM_LED"], GPIO.HIGH)

def hbpm(parameters = None):
    assert EN == True, "ERROR: Main Power Disabled"
    assert len(parameters) == 1, "HBPM only takes one parameter"
    RFOFF()
    
    if parameters[0] == 1:
        setRF(0, 0, 1)
        GPIO.output(PINS["HBPM_LED"], GPIO.HIGH)

def aux(parameters = None):
    assert EN == True, "ERROR: Main Power Disabled"
    assert len(parameters) == 1, "AUX only takes one parameter"
    RFOFF()
    
    if parameters[0] == 1:
        setRF(1, 0, 1)
        GPIO.output(PINS["AUX_LED"], GPIO.HIGH)

def extt(parameters = None):
    assert EN == True, "ERROR: Main Power Disabled"
    assert len(parameters) == 1, "EXTT only takes one parameter"
    RFOFF()

    if parameters[0] == 1:
        setS(0, 0) 
        GPIO.output(PINS["EXTT_LED"], GPIO.HIGH)

def ldt(parameters = None):
    assert EN == True, "ERROR: Main Power Disabled"
    assert len(parameters) == 1, "LDT only takes one parameter"
    RFOFF()
    
    if parameters[0] == 1:
        setS(1, 0)
        GPIO.output(PINS["LDT_LED"], GPIO.HIGH)

def master(parameters = None):
    assert EN == True, "ERROR: Main Power Disabled"
    assert len(parameters) == 1, "MASTER only takes one parameter"
    RFOFF()
    
    if parameters[0] == 1:
        setS(1, 1)
        GPIO.output(PINS["MCLK_LED"], GPIO.HIGH)

def lbatt(parameters = None):
    assert EN == True, "ERROR: Main Power Disabled"
    assert len(parameters) == 1, "LBATT only takes one parameter"
    assert float(parameters[0]) <= 31.5 and float(paramters[0]) >= 0, "LBATT out of range (0 to 31.5)"
    assert float(parameters[0]) % 0.5 == 0, "LBATT resolution is 0.5 dB"

def rbatt(parameters = None):
    assert EN == True, "ERROR: Main Power Disabled"
    assert len(parameters) == 1, "RBATT only takes one parameter"
    assert float(parameters[0]) not in valid, "RBATT only "
    assert float(parameters[0]) <= 31.5 and float(paramters[0]) >= 0, "RBATT out of range (0 to 31.5)"
    assert float(parameters[0]) % 0.5 == 0, "RBATT resolution is 0.5 dB"

def helpMenu(parameters = None):
    if parameters == []:
        print ""
        print "HELP MENU"
        print "To get specific information about a function use:"
        print "\t ITOP.py HELP fnumber"
        print ""
        print " fnumber |    function"
        print "---------------------------"
        print "     0   |    ENABLE"
        print "     1   |    CLOSE"
        print "     2   |    WGEN [enable]"
        print "     3   |    SINE [enable]"
        print "     4   |    DRF [enable]"
        print "     5   |    LBPM [enable]"
        print "     6   |    HBPM [enable]"
        print "     7   |    AUX [enable]"
        print "     8   |    EXTT [enable]"
        print "     9   |    LDT [enable]"
        print "    10   |    MASTER [enable]"
        print "    11   |    LBATT [value]"
        print "    12   |    RBATT [value]"
        print "    13   |    HELP [fnumber]"
        print ""
    elif parameters == [0]:
        pass
    elif parameters == [1]:
        pass
    elif parameters == [2]:
        pass
    elif parameters == [3]:
        pass
    elif parameters == [4]:
        pass
    elif parameters == [5]:
        pass
    elif parameters == [6]:
        pass
    elif parameters == [7]:
        pass
    elif parameters == [8]:
        pass
    elif parameters == [9]:
        pass
    elif parameters == [10]:
        pass
    elif parameters == [11]:
        pass
    elif parameters == [12]:
        pass
    elif parameters == [13]:
        pass
    else:
        print "Not a valid parameter"
ITOP = {
    "ENABLE"    :   enable,
    "CLOSE"     :   close,
    "SHUTDOWN"  :   shutdown,     
    "WGEN"      :   wgen,
    "SINE"      :   sine,
    "DRF"       :   drf,
    "LBPM"      :   lbpm,
    "HBPM"      :   hbpm,
    "AUX"       :   aux,
    "EXTT"      :   extt,
    "LDT"       :   ldt,
    "MASTER"    :   master,
    "LBATT"     :   lbatt,
    "RBATT"     :   rbatt,
    "HELP"      :   helpMenu,
}

#enable()

if len(sys.argv) <= 1:
    print ""
    print "Missing Parameters"
    print "\tITOP.py [function] [parameters]"
    print "For help use:"
    print "\tITOP.py HELP" 
    print ""
else:
    function = sys.argv[1]
    parameters = sys.argv[2:]

    ITOP[function](parameters)
