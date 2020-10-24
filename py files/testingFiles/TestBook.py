# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 23:42:55 2019

@author: Gordon Lai
"""

import unittest
from mainImplementation.Book import Book
from mainImplementation.LibraryMember import LibraryMember

class TestBook(unittest.TestCase):
    """
    A test class for the Book class.
    """
    
    def test_getISBN(self):
        """
        Test the getISBN() method.
        """
        book1 = Book()
        self.assertEqual(book1.getISBN(), 0)
        
    def test_setISBN(self):
        """
        Test the setISBN() method.
        """
        book1 = Book()
        self.assertEqual(book1.getISBN(), 0)
        book1.setISBN(1)
        self.assertEqual(book1.getISBN(), 1)
        
    def test_getLibraryMember(self):
        """
        Test the getLibraryMember() method.
        """
        book1 = Book()
        self.assertIsNone(book1.getLibraryMember())
        
    def test_setLibraryMember(self):
        """
        Test the setLibraryMember() method.
        """
        book1 = Book()
        self.assertIsNone(book1.getLibraryMember())
        
        libraryMember1 = LibraryMember()
        book1.setLibraryMember(libraryMember1)
        self.assertIs(book1.getLibraryMember(), libraryMember1)
        
    def test_getDamage(self):
        """
        Test the getDamage() method.
        """
        book1 = Book()
        self.assertEqual(book1.getDamage(), "no damage")
        
    def test_setDamage(self):
        """
        Test the setDamage() method.
        """
        book1 = Book()
        self.assertEqual(book1.getDamage(), "no damage")
        book1.setDamage("Water damage")
        self.assertEqual(book1.getDamage(), "Water damage")
        book1.setDamage("Broken corner")
        self.assertEqual(book1.getDamage(), "Water damage, Broken corner")
        
    def test_getTitle(self):
        """
        Test the getTitle() method.
        """
        book1 = Book()
        self.assertEqual(book1.getTitle(), "not set")
        
    def test_setTitle(self):
        """
        Test the setTitle() method.
        """
        book1 = Book()
        self.assertEqual(book1.getTitle(), "not set")
        book1.setTitle("abc")
        self.assertEqual(book1.getTitle(), "abc")
        
    def test_getAuthorName(self):
        """
        Test the getAuthorName() method.
        """
        book1 = Book()
        self.assertEqual(book1.getAuthorName(), "not set")
        
    def test_setAuthorName(self):
        """
        Test the setAuthorName() method.
        """
        book1 = Book()
        self.assertEqual(book1.getAuthorName(), "not set")
        book1.setAuthorName("abc")
        self.assertEqual(book1.getAuthorName(), "abc")
        
    def test_checkBookAvailibility(self):
        """
        Test the checkBookAvailibility() method.
        """
        book1 = Book()
        self.assertTrue(book1.checkBookAvailibility())
        
        libraryMember1 = LibraryMember()
        book1.setLibraryMember(libraryMember1)
        self.assertFalse(book1.checkBookAvailibility())
        
    def test_printBookDetail(self):
        """
        Test the printBookDetail() method.
        """
        book1 = Book()
        book1.printBookDetail()
        
        
        
if __name__ == '__main__':
    unittest.main(TestBook())