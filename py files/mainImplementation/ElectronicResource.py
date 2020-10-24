# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 00:54:54 2019

@author: Gordon Lai
"""

class ElectronicResource:
    """
    Class to repersent electronic resource.
    """
    def __init__(self):
        self.deviceList = []
        self.title = "not set"
        self.authorName = "not set"
        
    def getDeviceList(self):
        """
        Return the list of device objects.
        """
        return self.deviceList
    
    def addDevice(self, device):
        """
        Add a device object to the end of the device list.
        """
        self.deviceList.append(device)
            
    def getTitle(self):
        """
        Return the title of the electronic resource.
        """
        return self.title
    
    def setTitle(self, title):
        """
        Set the title of the electronic resource.
        """
        self.title = title
        
    def getAuthorName(self):
        """
        Return the author's name of the book.
        """
        return self.authorName
    
    def setAuthorName(self, authorName):
        """
        Set the author's name of the book.
        """
        self.authorName = authorName
        
    def printElectronicResourceDetail(self):
        """
        Print all the details of the electronic resource.
        """
        print("----------------------------------")
        print("Electronic resource Title: " + format(self.title))
        print("Electronic resource Author's name: " + format(self.authorName))
        if len(self.deviceList) == 0:
            print("This electronic resource is not availible in any device.")
        else:
            print("Electronic resource is availible in the following devices:")
            for device in self.deviceList:
                device.printElectronicDeviceDetail()
        print("----------------------------------")
        
        
def test():
    e1 = ElectronicResource()
    e1.printElectronicResourceDetail()
    
    device1 = ElectronicDevice.ElectronicDevice()
    device2 = ElectronicDevice.ElectronicDevice()
    e1.addDevice(device1)
    e1.addDevice(device2)
    e1.setTitle("Book title")
    e1.setAuthorName("Author")
    e1.printElectronicResourceDetail()
    