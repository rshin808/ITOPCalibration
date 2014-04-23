# ITOPCalibration  
ITOP Calibration code for BeagleBone Black.  

# BeagleBone Black revC (Debian 7.9)  
I2C and SPI drivers required (see INSTALLATION below)  

# PINS  
## P8 HEADER  
MAINPW_EN = P8_7  
HB_RFATT_6 = P8_9  
HB_RFATT_4 = P8_11  
HB_RFATT_2 = P8_13  
LB_RFATT_6 = P8_15  
LB_RFATT_4 = P8_17  
LB_RFATT_2 = P8_19  
AUX_LED = P8_8  
HB_RFATT_5 = P8_10  
HB_RFATT_3 = P8_12  
HB_RFATT_1 = P8_14  
LB_RFATT_5 = P8_16  
LB_RFATT_3 = P8_18  
LB_RFATT_1 = P8_26  

## P9 HEADER  
SYS898_SELA = P9_11  
SYS898_SELB = P9_13  
RFSW_A = P9_15  
I2C_SCL = P9_17  
EXTT_LED = P9_19  
MCLK_LED = P9_23  
AD9102_RESET = P9_25  
ADF4002_CE = P9_27  
SPI_SDI = P9_29  
SPI_SCLK = P9_31  
DIAG_+3V3 = P9_33  
DIAG_+5VA = P9_35  
DIAG_+5V0BB = P9_37  
DIAG_+5V5 = P9_39  
AD9102_TRIG = P9_41  
ADF4002_LOCKD = P9_12  
RFSW_B = P9_14  
RFSW_C = P9_16  
I2C_SDA = P9_18  
HBPM_LED = P9_20  
LBPM_LED = P9_22  
LDT_LED = P9_24  
SPI_CS2# = P9_28  
SPI_SD0 = P9_30  
DIA_Iin = P9_40  
SPI_CS1# = P9_42  

# INSTALLATION  
sudo ntpdate pool.ntp.org  

sudo apt-get update  
sudo apt-get install build-essential python-dev python-setuptools python-pip python-smbus -y  
sudo pip install Adafruit_BBIO  

git clone https://github.com/rshin808/ITOPCalibration  
    or download as ZIP and extract

edit /etc/rc.local  
   echo BB-I2C1 > /sys/devices/bone_capemgr.9/slots  
   ntpdate pool.ntp.org  

# CREDITS  
Adafruit_BBIO is a BeagleBone IO Python library forked from Ben Croston's [RPI.GPIO library](https://sourceforge.net/projects/raspberry-gpio-python)(MIT License).  
[Adafruit_BBIO Library](https://github.com/adafruit/adafruit-beaglebone-io-python)(MIT License) 

# LICENSE  
This version of the ITOPCalibration is released under the MIT License.   



