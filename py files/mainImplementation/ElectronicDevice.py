# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 18:07:56 2019

@author: Gordon Lai
"""

class ElectronicDevice:
    """
    Class to repersent electronic device.
    """
    def __init__(self):
        self.location = "not set"
        self.availibility = True
        self.typeOfDevice = "not set"
        
    def getLocation(self):
        """
        Return the location of the electronic device.
        """
        return self.location
    
    def setLocation(self, location):
        """
        Set the location of the electronic device.
        """
        self.location = location
        
    def getAvailibility(self):
        """
        Return the availibility status of the electronic device.
        """
        return self.availibility
    
    def setAvailibility(self, availibility):
        """
        Set the availibility status of the electronic device.
        """
        self.availibility = availibility
        
    def getTypeOfDevice(self):
        """
        Return the type of device of the electronic device.
        """
        return self.typeOfDevice
    
    def setTypeOfDevice(self, typeOfDevice):
        """
        Set the type of device of the electronic device.
        """
        self.typeOfDevice = typeOfDevice
        
    def printElectronicDeviceDetail(self):
        """
        Print the details of the electronic device.
        """
        print("*************************************")
        print("Electronic device location: " + self.location)
        print("Type of device: " + self.typeOfDevice)
        if self.availibility == True:
            print("Electronic device status: availible.")
        else:
            print("Electronic device status: unavailible.")
        print("*************************************")
        
            
def test():
    device1 = ElectronicDevice()
    device1.printElectronicDeviceDetail()
    
    device1.setLocation("room 101")
    device1.setAvailibility(False)
    device1.printElectronicDeviceDetail()