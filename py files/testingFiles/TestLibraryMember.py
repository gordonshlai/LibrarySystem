# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 02:02:01 2019

@author: Gordon Lai
"""

import unittest
from mainImplementation.LibraryMember import LibraryMember
from mainImplementation.Book import Book

class TestLibraryMember(unittest.TestCase):
    """
    A test class for the LibraryMember class.
    """
    
    def test_getBookList(self):
        """
        Test the getBookList() method.
        """
        member1 = LibraryMember()
        self.assertIs(member1.getBookList(), member1.bookList)
        
    def test_addBook(self):
        """
        Test the addBook() method.
        """
        member1 = LibraryMember()
        book1 = Book()
        member1.addBook(book1)
        self.assertIn(book1, member1.bookList)
        
    def test_getMessage(self):
        """
        Test the getMessage() method.
        """
        member1 = LibraryMember()
        self.assertEqual(member1.getMessage(), "no message")
        
    def test_setMessage(self):
        """
        Test the setMessage() method.
        """
        member1 = LibraryMember()
        self.assertEqual(member1.getMessage(), "no message")
        member1.setMessage("abc")
        self.assertEqual(member1.getMessage(), "abc")
        member1.setMessage("xyz")
        self.assertEqual(member1.getMessage(), "abc, xyz")
        
    def test_getName(self):
        """
        Test the getName() method.
        """
        member1 = LibraryMember()
        self.assertEqual(member1.getName(), "not set")
        
    def test_setName(self):
        """
        Test the setLocation() method.
        """
        member1 = LibraryMember()
        self.assertEqual(member1.getName(), "not set")
        member1.setName("abc")
        self.assertEqual(member1.getName(), "abc")
        
    def test_printLibraryMemberDetail(self):
        """
        Test the printLibraryMemberDetail() method.
        """
        print("========================================")
        print("Start of test_printLibraryMemberDetail()")
        
        member1 = LibraryMember()
        member1.printLibraryMemberDetail()
        
        book1 = Book()
        member1.addBook(book1)
        member1.printLibraryMemberDetail()
        
        book2 = Book()
        member1.addBook(book2)
        member1.printLibraryMemberDetail()
        
        print("End of test_printLibraryMemberDetail()")
        print("========================================")
        
    def test_printAllMessage(self):
        """
        Test the printAllMessage() method.
        """
        print("========================================")
        print("Start of test_printAllMessage()")
        
        member1 = LibraryMember()
        member1.printAllMessage()
        member1.setMessage("abc")
        member1.printAllMessage()
        member1.setMessage("xyz")
        member1.printAllMessage()
        
        print("End of test_printAllMessage()")
        print("========================================")
        
    def test_printAllBook(self):
        """
        Test the printAllBook() method.
        """
        print("========================================")
        print("Start of test_printAllBook()")
        
        member1 = LibraryMember()
        print("before calling the method the 1st time")
        member1.printAllBook()
        print("after calling the method the 1st time")
        
        book1 = Book()
        member1.addBook(book1)
        print("before calling the method the 2nd time")
        member1.printAllBook()
        print("after calling the method the 2nd time")
        
        book2 = Book()
        member1.addBook(book2)
        print("before calling the method the 3rd time")
        member1.printAllBook()
        print("after calling the method the 3rd time")
        
        print("End of test_printAllBook()")
        print("========================================")
        
    def test_numberOfBook(self):
        """
        Test the numberOfBook() method.
        """
        member1 = LibraryMember()
        self.assertEqual(member1.numberOfBook(), 0)
        
        book1 = Book()
        member1.addBook(book1)
        self.assertEqual(member1.numberOfBook(), 1)
        
        book2 = Book()
        member1.addBook(book2)
        self.assertEqual(member1.numberOfBook(), 2)
        
        
if __name__ == '__main__':
    unittest.main(TestLibraryMember())