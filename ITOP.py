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
from Adafruit_I2C import Adafruit_I2C
from PINS import *
from si5338POST import *
from REGS import *


# Initialize GPIO
for key in PINS.keys():
    GPIO.setup(PINS[key], GPIO.OUT)

# Initialize BUS
address = 0x70
busNum = 1
i2c = Adafruit_I2C(address, busNum)
pll = si5338POST(i2c = i2c, regs = REGS)

# Check if MAINPW_EN is High
EN = None
with open("EN", "rb") as ENFile:
    EN = bool(int(ENFile.read().split()[0]))

# Helper Functions
def drf(enable = False):
    assert EN == True, "ERROR: Main Power Disabled"
    RFOFF()
   
    if enable == True:
        setRF(0, 1, 0)

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

def setHBATT(a = 1, b = 1, c = 1, d = 1, e = 1, f = 1):
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

def setLBATT(a = 1, b = 1, c = 1, d = 1, e = 1, f = 1):
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
    l = "1"
    if float(int(value) * 2) == float(value) * 2:
        l = "1"
    else:
        l = "0"

    b = ""
    for i in range(5)[::-1]:
        if(value - 2 ** i) >= 0:
            value -= 2 ** i
            b += "0"
        else:
            b += "1"
    
    b += l
    
    setHBATT(int(b[0]), int(b[1]), int(b[2]), int(b[3]), int(b[4]), int(b[5]))  

    return b

def setLATT(value = 0):
    l = "1"
    if float(int(value) * 2) == float(value) * 2:
        l = "1"
    else:
        l = "0"

    b = ""
    for i in range(5)[::-1]:
        if(value - 2 ** i) >= 0:
            value -= 2 ** i
            b += "0"
        else:
            b += "1"
    
    b += l
    
    setLBATT(int(b[0]), int(b[1]), int(b[2]), int(b[3]), int(b[4]), int(b[5]))  
    
    return b

def RFOFF():
    setRF()
    ledsOff()

# Functions Users can call
def enable(parameters = None):
    """
        Name:   enable
        Desc:   This enables the Main Power for the board.
                The board is powered on with AUX enabled.
        Params: parameters (list)
                    None
    """
    for key in PINS.keys():
        GPIO.output(PINS[key], GPIO.LOW)
    
    GPIO.output(PINS["MAINPW_EN"], GPIO.HIGH)

    with open("EN", "wb") as ENFile:
        ENFile.write("1")

    time.sleep(1)

    aux([1])
    
    pll._init()

    print "Main Power Enabled"
    print "Note: When finished use 'close' or 'shutdown'"

def close(parameters = None):
    """
        Name:   close
        Desc:   This closes the Main Power for the board.
        Params: parameters (list)
                    None
    """
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
    """
        Name:   shutdown
        Desc:   This shutdowns the board.
        Params: parameters (list)
                    None
    """
    close()
    subprocess.call(["shutdown", "-h", "now"])

def wgen(parameters = None):
    """
        Name:   wgen
        Desc:   This enables WGEN.
        Params: parameters (list)
                    0:  enable (int)
    """
    assert EN == True, "ERROR: Main Power Disabled"
    assert len(parameters) == 1, "WGEN only takes one parameter"
    RFOFF()
    
    if int(parameters[0]) == 1:
        setRF(0, 0, 0)
        print "WGEN Enabled"

def sine(parameters = None):
    """
        Name:   sine
        Desc:   This enables SINE.
        Params: parameters (list)
                    0: enable (int)
    """
    assert EN == True, "ERROR: Main Power Disabled"
    assert len(parameters) == 1, "SINE only takes one parameter"
    RFOFF()

    if int(parameters[0]) == 1:
        setRF(1, 0, 0)
        print "SINE Enabled"

def lbpm(parameters = None):
    """
        Name:   lbpm
        Desc:   This enables LBPM.
        Params: parameters (list)
                    0: enable (int)
    """
    assert EN == True, "ERROR: Main Power Disabled"
    assert len(parameters) == 1, "LBPM only takes one parameter"
    RFOFF()

    if int(parameters[0]) == 1:
        setRF(1, 1, 0)
        GPIO.output(PINS["LBPM_LED"], GPIO.HIGH)
        print "LBPM Enabled"

def hbpm(parameters = None):
    """
        Name:   hbpm
        Desc:   This enables HBPM.
        Params: parameters (list)
                0: enable (list)
    """
    assert EN == True, "ERROR: Main Power Disabled"
    assert len(parameters) == 1, "HBPM only takes one parameter"
    RFOFF()
    
    if int(parameters[0]) == 1:
        setRF(0, 0, 1)
        GPIO.output(PINS["HBPM_LED"], GPIO.HIGH)
        print "HBPM Enabled"

def aux(parameters = None):
    assert EN == True, "ERROR: Main Power Disabled"
    assert len(parameters) == 1, "AUX only takes one parameter"
    RFOFF()
    
    if int(parameters[0]) == 1:
        setRF(1, 0, 1)
        GPIO.output(PINS["AUX_LED"], GPIO.HIGH)
        print "AUX Enabled"

def extt(parameters = None):
    assert EN == True, "ERROR: Main Power Disabled"
    assert len(parameters) == 1, "EXTT only takes one parameter"
    RFOFF()
    
    drf(1)

    if int(parameters[0]) == 1:
        setS(0, 0) 
        GPIO.output(PINS["EXTT_LED"], GPIO.HIGH)
        print "EXTT Enabled"


def ldt(parameters = None):
    assert EN == True, "ERROR: Main Power Disabled"
    assert len(parameters) == 1, "LDT only takes one parameter"
    RFOFF()
    
    drf(1)

    if int(parameters[0]) == 1:
        setS(1, 0)
        GPIO.output(PINS["LDT_LED"], GPIO.HIGH)
        print "LDT Enabled"

def master(parameters = None):
    assert EN == True, "ERROR: Main Power Disabled"
    assert len(parameters) == 1, "MASTER only takes one parameter"
    RFOFF()

    drf(1)
    
    if int(parameters[0]) == 1:
        setS(1, 1)
        GPIO.output(PINS["MCLK_LED"], GPIO.HIGH)
        print "MASTER Enabled"

def lbatt(parameters = None):
    assert EN == True, "ERROR: Main Power Disabled"
    assert len(parameters) == 1, "LBATT only takes one parameter"
    assert float(parameters[0]) <= 31.5 and float(parameters[0]) >= 0, "LBATT out of range (0 to 31.5)"
    assert float(parameters[0]) % 0.5 == 0, "LBATT resolution is 0.5 dB"
    
    print setLATT(float(parameters[0]))

def rbatt(parameters = None):
    assert EN == True, "ERROR: Main Power Disabled"
    assert len(parameters) == 1, "RBATT only takes one parameter"
    assert float(parameters[0]) <= 31.5 and float(parameters[0]) >= 0, "RBATT out of range (0 to 31.5)"
    assert float(parameters[0]) % 0.5 == 0, "RBATT resolution is 0.5 dB"

    print setHATT(float(parameters[0]))

def helpMenu(parameters = None):
    """
        Name:   helpMenu
        Desc:   This is the help menu for the ITOP Calibration module
        Params: parameters (list):
                    0:  fnumber (int), the function number
    """
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
        print "     4   |    LBPM [enable]"
        print "     5   |    HBPM [enable]"
        print "     6   |    AUX [enable]"
        print "     7   |    EXTT [enable]"
        print "     8   |    LDT [enable]"
        print "     9   |    MASTER [enable]"
        print "    10   |    LBATT [value]"
        print "    11   |    RBATT [value]"
        print "    12   |    HELP [fnumber]"
        print ""
    elif parameters == ["0"]:
        print str(enable.__doc__)
    elif parameters == ["1"]:
        print str(close.__doc__)
    elif parameters == ["2"]:
        print str(wgen.__doc__)
    elif parameters == ["3"]:
        print str(sine.__doc__)
    elif parameters == ["4"]:
        print str(lbpm.__doc__)
    elif parameters == ["5"]:
        print str(hbpm.__doc__)
    elif parameters == ["6"]:
        print str(aux.__doc__)
    elif parameters == ["7"]:
        print str(extt.__doc__)
    elif parameters == ["8"]:
        print str(ldt.__doc__)
    elif parameters == ["9"]:
        print str(master.__doc__)
    elif parameters == ["10"]:
        print str(lbatt.__doc__)
    elif parameters == ["11"]:
        print str(rbatt.__doc__)
    elif parameters == ["12"]:
        print str(helpMenu.__doc__)
    else:
        print "Not a valid parameter"

ITOP = {
    "ENABLE"    :   enable,
    "CLOSE"     :   close,
    "SHUTDOWN"  :   shutdown,     
    "WGEN"      :   wgen,
    "SINE"      :   sine,
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
"""
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
"""

try:
    while(True):
        try:
            print "Enter a Command:"
            cmd = raw_input().split()
            func = cmd[0]
            params = cmd[1:]

            ITOP[func](params)
        except Exception, e:
            print e
except KeyboardInterrupt, e:
    GPIO.cleanup()
