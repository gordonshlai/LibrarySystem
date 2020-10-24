# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 01:51:04 2019

@author: Gordon Lai
"""

import unittest
from mainImplementation.ElectronicDevice import ElectronicDevice

class TestElectronicDevice(unittest.TestCase):
    """
    A test class for the ElectronicDevice class.
    """
    
    def test_getLocation(self):
        """
        Test the getLocation() method.
        """
        device1 = ElectronicDevice()
        self.assertEqual(device1.getLocation(), "not set")
        
    def test_setLocation(self):
        """
        Test the setLocation() method.
        """
        device1 = ElectronicDevice()
        self.assertEqual(device1.getLocation(), "not set")
        device1.setLocation("abc")
        self.assertEqual(device1.getLocation(), "abc")
        
    def test_getAvailibility(self):
        """
        Test the getAvailibility() method.
        """
        device1 = ElectronicDevice()
        self.assertTrue(device1.getAvailibility())
        
    def test_setAvailibility(self):
        """
        Test the setAvailibility() method.
        """
        device1 = ElectronicDevice()
        self.assertTrue(device1.getAvailibility())
        device1.setAvailibility(False)
        self.assertFalse(device1.getAvailibility())
        
    def test_getTypeOfDevice(self):
        """
        Test the getTypeOfDevice() method.
        """
        device1 = ElectronicDevice()
        self.assertEqual(device1.getTypeOfDevice(), "not set")
        
    def test_setTypeOfDevice(self):
        """
        Test the setTypeOfDevice() method.
        """
        device1 = ElectronicDevice()
        self.assertEqual(device1.getTypeOfDevice(), "not set")
        device1.setTypeOfDevice("computer")
        self.assertEqual(device1.getTypeOfDevice(), "computer")
        
    def test_printElectronicDeviceDetail(self):
        """
        Test the printElectronicDeviceDetail() method.
        """
        device1 = ElectronicDevice()
        device1.printElectronicDeviceDetail()
        device1.setAvailibility(False)
        device1.printElectronicDeviceDetail()
        
        
        
if __name__ == '__main__':
    unittest.main(TestElectronicDevice())