# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 01:32:02 2019

@author: Gordon Lai
"""

import unittest
from mainImplementation.ElectronicResource import ElectronicResource
from mainImplementation.ElectronicDevice import ElectronicDevice

class TestElectronicResource(unittest.TestCase):
    """
    A test class for the ElectronicResource class.
    """
    
    def test_getDeviceList(self):
        """
        Test the getDevice() method.
        """
        eResource1 = ElectronicResource()
        self.assertIs(eResource1.getDeviceList(), eResource1.deviceList)
        
    def test_addDevice(self):
        """
        Test the addDevice() method.
        """
        eResource1 = ElectronicResource()
        device1 = ElectronicDevice()
        eResource1.addDevice(device1)
        self.assertIn(device1, eResource1.deviceList)
        
    def test_getTitle(self):
        """
        Test the getTitle() method.
        """
        eResource1 = ElectronicResource()
        self.assertEqual(eResource1.getTitle(), "not set")
        
    def test_setTitle(self):
        """
        Test the setTitle() method.
        """
        eResource1 = ElectronicResource()
        self.assertEqual(eResource1.getTitle(), "not set")
        eResource1.setTitle("abc")
        self.assertEqual(eResource1.getTitle(), "abc")
        
    def test_getAuthorName(self):
        """
        Test the getAuthorName() method.
        """
        eResource1 = ElectronicResource()
        self.assertEqual(eResource1.getAuthorName(), "not set")
        
    def test_setAuthorName(self):
        """
        Test the setAuthorName() method.
        """
        eResource1 = ElectronicResource()
        self.assertEqual(eResource1.getAuthorName(), "not set")
        eResource1.setAuthorName("abc")
        self.assertEqual(eResource1.getAuthorName(), "abc")
        
    def test_printElectronicResourceDetail(self):
        """
        Test the printElectronicResourceDetail() method.
        """
        eResource1 = ElectronicResource()
        eResource1.printElectronicResourceDetail()
        
        device1 = ElectronicDevice()
        eResource1.addDevice(device1)
        eResource1.printElectronicResourceDetail()
        
        device2 = ElectronicDevice()
        eResource1.addDevice(device2)
        eResource1.printElectronicResourceDetail()
        
        
if __name__ == '__main__':
    unittest.main(TestElectronicResource())