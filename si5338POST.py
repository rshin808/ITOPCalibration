"""
    Name:   si5338POST.py
    By:     Reed Shinsato
    Date:   8 February 2016
    Rev:    -   
    Desc:   This is a driver for the si5338 PLL after it has been configured by Clock Builder. This has also been adapted for the BeagleBone Black.

"""
class si5338POST:
    """
        Name:   si5338POST
	Desc:   This is the class for configuring the si5338 chip after defaults have been loaded.
	Params: option (bool), This is the option for the configuration.
	        i2c (object), This is the i2c object
		regs (dict), This is the dictionary containing the register numbers that need to be configured.  
    """
    def __init__(self, option = False, i2c = None, regs = None):
        self._option = option
        self._BUS = i2c
        self._REGS = regs
        self._init()
    
    def _init(self):    
        # Setting LVDS
        self._BUS.write8(36, 0x06)
        self._BUS.write8(37, 0x06)
        self._BUS.write8(40, 0x63)
        self._BUS.write8(41, 0x8c)
        self._BUS.write8(42, 0x23)

        # Setting PLL bypass
        # self._BUS.write8(31, 0x08)        
        
        if self._option == False:
            self._BUS.write8(self._REGS["ENOUTS"], 0x10)
            self._BUS.write8(self._REGS["PLLWPASS"], 0x1D)
            self._BUS.write8(self._REGS["PFDDIV"], 0x64)
            self._BUS.write8(self._REGS["PFDFB"], 0xA4)
            self._BUS.write8(self._REGS["MSNP1S1"], 0x00)
            self._BUS.write8(self._REGS["MSNP1S2"], 0x26)
            self._BUS.write8(self._REGS["MSNP1S3"], 0x00)
            self._BUS.write8(self._REGS["MSNP2S2"], 0x00)
            self._BUS.write8(self._REGS["MSNP2S3"], 0x00)
            self._BUS.write8(self._REGS["MSNP2S4"], 0x00)
            self._BUS.write8(self._REGS["MSNP3S1"], 0x01)
            self._BUS.write8(self._REGS["MSNP3S2"], 0x00)
            self._BUS.write8(self._REGS["MSNP3S3"], 0x00)
            self._BUS.write8(self._REGS["MSNP3S4"], 0x80)
            self._BUS.write8(self._REGS["ENOUTS"], 0x0C)
            self._BUS.write8(self._REGS["PLLWPASS"], 0x00)
        else:
            self._BUS.write8(self._REGS["ENOUTS"], 0x10)
            self._BUS.write8(self._REGS["PLLWPASS"], 0x1D)
            self._BUS.write8(self._REGS["PFDDIV"], 0x42)
            self._BUS.write8(self._REGS["PFDFB"], 0xB0)
            self._BUS.write8(self._REGS["MSNP1S1"], 0x00)
            self._BUS.write8(self._REGS["MSNP1S2"], 0x26)
            self._BUS.write8(self._REGS["MSNP1S3"], 0x00)
            self._BUS.write8(self._REGS["MSNP2S2"], 0x00)
            self._BUS.write8(self._REGS["MSNP2S3"], 0x00)
            self._BUS.write8(self._REGS["MSNP2S4"], 0x00)
            self._BUS.write8(self._REGS["MSNP3S1"], 0x01)
            self._BUS.write8(self._REGS["MSNP3S2"], 0x00)
            self._BUS.write8(self._REGS["MSNP3S3"], 0x00)
            self._BUS.write8(self._REGS["MSNP3S4"], 0x80)
            self._BUS.write8(self._REGS["ENOUTS"], 0x0C)
            self._BUS.write8(self._REGS["PLLWPASS"], 0x00)
                                
    
    
