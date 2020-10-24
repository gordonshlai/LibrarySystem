# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 02:35:37 2019

@author: Gordon Lai
"""
import unittest
from mainImplementation.Library import Library
from mainImplementation.LibraryMember import LibraryMember
from mainImplementation.Book import Book
from mainImplementation.ElectronicResource import ElectronicResource

class TestLibrary(unittest.TestCase):
    """
    A test class for the Library class.
    """
    
    def test_getCatalogue(self):
        """
        Test the getCatalogue() method.
        """
        library1 = Library()
        self.assertIs(library1.getCatalogue(), library1.catalogue)
        
    def test_getMaxBookNumber(self):
        """
        Test the getMaxBookNumber() method.
        """
        library1 = Library()
        self.assertEqual(library1.getMaxBookNumber(), 5)
        
    def test_setMaxBookNumber(self):
        """
        Test the setMaxBookNumber() method.
        """
        library1 = Library()
        self.assertEqual(library1.getMaxBookNumber(), 5)
        library1.setMaxBookNumber(6)
        self.assertEqual(library1.getMaxBookNumber(), 6)
        
    def test_getLibraryMemberCurrentlyBorrowingBookList(self):
        """
        Test the getLibraryMemberCurrentlyBorrowingBookList() method.
        """
        library1 = Library()
        self.assertIs(library1.getLibraryMemberCurrentlyBorrowingBookList(), library1.libraryMemberCurrentlyBorrowingBookList)
        
    def test_printAllLibraryDetail(self):
        """
        Test the printAllLibraryDetail() method.
        """
        print("========================================")
        print("Start of test_printAllLibraryDetail()")
        
        print("")
        library1 = Library()
        library1.printAllLibraryDetail()
        
        book1 = Book()
        book2 = Book()
        eResource1 = ElectronicResource()
        
        member1 = LibraryMember()
        member2 = LibraryMember()
        library1.addResource(book1)
        library1.addResource(book2)
        library1.addResource(eResource1)
        library1.lendBook(book1, member1)
        library1.lendBook(book2, member2)
        library1.printAllLibraryDetail()
        
        print("End of test_printAllLibraryDetail()")
        print("========================================")
        
    def test_containResource(self):
        """
        Test the containResource() method.
        """
        library1 = Library()
        book1 = Book()
        self.assertFalse(library1.containResource(book1))
        
        library1.addResource(book1)
        self.assertTrue(library1.containResource(book1))
        
    def test_editTitle(self):
        """
        Test the editTitle() method.
        """
        print("========================================")
        print("Start of test_editTitle()")
        
        library1 = Library()
        book1 = Book()
        eResource1 = ElectronicResource()
        
        library1.editTitle(book1, "abc")
        self.assertEqual(book1.getTitle(), "not set")
        library1.editTitle(eResource1, "xyz")
        self.assertEqual(eResource1.getTitle(), "not set")
        
        library1.addResource(book1)
        library1.addResource(eResource1)
        library1.editTitle(book1, "abc")
        self.assertEqual(book1.getTitle(), "abc")
        library1.editTitle(eResource1, "xyz")
        self.assertEqual(eResource1.getTitle(), "xyz")
        
        print("End of test_editTitle()")
        print("========================================")
        
    def test_searchResource(self):
        """
        Test the searchResource() method.
        """
        library1 = Library()
        book1 = Book()
        self.assertEqual(library1.searchResource(book1), None)
        
        library1.addResource(book1)
        self.assertEqual(library1.searchResource(book1), book1)
        
    def test_searchResourceByISBN(self):
        """
        Test the searchResourceByISBN() method.
        """
        print("========================================")
        print("Start of test_searchResourceByISBN()")
        
        library1 = Library()
        book1 = Book()
        book2 = Book()
        book3 = Book()
        book4 = Book()
        book1.setISBN(1111)
        book2.setISBN(1111)
        book3.setISBN(2222)
        book4.setISBN(1111)
        library1.addResource(book1)
        library1.addResource(book2)
        library1.addResource(book3)
        library1.searchResourceByISBN(1111)
        library1.searchResourceByISBN(2222)
        
        print("End of test_searchResourceByISBN()")
        print("========================================")
        
    def test_searchResourceByAuthorName(self):
        """
        Test the searchResourceByAuthorName() method.
        """
        print("========================================")
        print("Start of searchResourceByAuthorName()")
        
        library1 = Library()
        book1 = Book()
        book2 = Book()
        book3 = Book()
        book4 = Book()
        eResource1 = ElectronicResource()
        eResource2 = ElectronicResource()
        eResource3 = ElectronicResource()
        eResource4 = ElectronicResource()
        book1.setAuthorName("aaaa")
        book2.setAuthorName("aaaa")
        book3.setAuthorName("bbbb")
        book4.setAuthorName("aaaa")
        eResource1.setAuthorName("aaaa")
        eResource2.setAuthorName("aaaa")
        eResource3.setAuthorName("bbbb")
        eResource4.setAuthorName("aaaa")
        library1.addResource(book1)
        library1.addResource(book2)
        library1.addResource(book3)
        library1.addResource(eResource1)
        library1.addResource(eResource2)
        library1.addResource(eResource3)
        library1.searchResourceByAuthorName("aaaa")
        library1.searchResourceByAuthorName("bbbb")
        
        print("End of searchResourceByAuthorName()")
        print("========================================")
        
    def test_removeResourceByObject(self):
        """
        Test the removeResourceByObject() method.
        """
        print("========================================")
        print("Start of test_removeResourceByObject()")
        
        library1 = Library()
        book1 = Book()
        eResource1 = ElectronicResource()
        
        library1.addResource(book1)
        library1.addResource(eResource1)
        self.assertIn(book1, library1.catalogue)
        self.assertIn(eResource1, library1.catalogue)
        
        library1.removeResourceByObject(book1)
        library1.removeResourceByObject(eResource1)
        self.assertNotIn(book1, library1.catalogue)
        self.assertNotIn(eResource1, library1.catalogue)
        
        library1.removeResourceByObject(book1)
        library1.removeResourceByObject(eResource1)
        
        print("End of test_removeResourceByObject()")
        print("========================================")
        
    def test_removeResourceByPosition(self):
        """
        Test the removeResourceByPosition() method.
        """
        print("========================================")
        print("Start of test_removeResourceByPosition()")
        
        library1 = Library()
        book1 = Book()
        book2 = Book()
        eResource1 = ElectronicResource()
        
        library1.addResource(book1)
        library1.addResource(book2)
        library1.addResource(eResource1)
        self.assertIn(book1, library1.catalogue)
        self.assertIn(book2, library1.catalogue)
        self.assertIn(eResource1, library1.catalogue)
        
        library1.removeResourceByPosition(-4)
        library1.removeResourceByPosition(3)
        self.assertIn(book1, library1.catalogue)
        self.assertIn(book2, library1.catalogue)
        self.assertIn(eResource1, library1.catalogue)
        
        library1.removeResourceByPosition(-1)
        library1.removeResourceByPosition(1)
        self.assertIn(book1, library1.catalogue)
        self.assertNotIn(book2, library1.catalogue)
        self.assertNotIn(eResource1, library1.catalogue)
        
        print("End of test_removeResourceByPosition()")
        print("========================================")
        
    def test_printAllAvailibleBooks(self):
        """
        Test the printAllAvailibleBooks() method.
        """
        print("========================================")
        print("Start of test_printAllAvailibleBooks()")
        
        library1 = Library()
        book1 = Book()
        book2 = Book()
        book3 = Book()
        eResource1 = ElectronicResource()
        member1 = LibraryMember()
        member2 = LibraryMember()
        
        library1.addResource(book1)
        library1.addResource(book2)
        library1.addResource(book3)
        library1.addResource(eResource1)
        
        book1.setTitle("aaa")
        book2.setTitle("bbb")
        book3.setTitle("ccc")
        
        library1.printAllAvailibleBooks()
        
        book1.setLibraryMember(member1)
        library1.printAllAvailibleBooks()
        
        book2.setLibraryMember(member2)
        library1.printAllAvailibleBooks()
        
        print("End of test_printAllAvailibleBooks()")
        print("========================================")
        
    def test_numberOfResource(self):
        """
        Test the numberOfResource() method.
        """
        library1 = Library()
        book1 = Book()
        book2 = Book()
        eResource1 = ElectronicResource()
        
        self.assertEqual(library1.numberOfResource(), 0)
        
        library1.addResource(book1)
        self.assertEqual(library1.numberOfResource(), 1)
        
        library1.addResource(book2)
        self.assertEqual(library1.numberOfResource(), 2)
        
        library1.addResource(eResource1)
        self.assertEqual(library1.numberOfResource(), 3)
        
    def test_addResource(self):
        """
        Test the addResource() method.
        """
        print("========================================")
        print("Start of test_addResource()")
        
        library1 = Library()
        book1 = Book()
        eResource1 = ElectronicResource()
        
        self.assertNotIn(book1, library1.catalogue)
        self.assertNotIn(eResource1, library1.catalogue)
        
        library1.addResource(book1)
        library1.addResource(eResource1)
        self.assertIn(book1, library1.catalogue)
        self.assertIn(eResource1, library1.catalogue)
        
        library1.addResource(book1)
        library1.addResource(eResource1)
        
        print("End of test_addResource()")
        print("========================================")
        
    def test_lendBook(self):
        """
        Test the lendBook() method.
        """
        print("========================================")
        print("Start of test_lendBook()")
        
        library1 = Library()
        book1 = Book()
        book2 = Book()
        book3 = Book()
        book4 = Book()
        book5 = Book()
        book6 = Book()
        book7 = Book()
        member1 = LibraryMember()
        
        library1.addResource(book1)
        library1.addResource(book2)
        library1.addResource(book3)
        library1.addResource(book4)
        library1.addResource(book5)
        library1.addResource(book7)
        
        library1.lendBook(book1, member1)
        self.assertEqual(book1.getLibraryMember(), member1)
        self.assertIn(book1, member1.bookList)
        self.assertIn(member1, library1.libraryMemberCurrentlyBorrowingBookList)
        
        library1.lendBook(book2, member1)
        library1.lendBook(book3, member1)
        library1.lendBook(book4, member1)
        library1.lendBook(book5, member1)
        
        self.assertEqual(book2.getLibraryMember(), member1)
        self.assertIn(book2, member1.bookList)
        self.assertIn(member1, library1.libraryMemberCurrentlyBorrowingBookList)
        
        self.assertEqual(book3.getLibraryMember(), member1)
        self.assertIn(book3, member1.bookList)
        self.assertIn(member1, library1.libraryMemberCurrentlyBorrowingBookList)
        
        self.assertEqual(book4.getLibraryMember(), member1)
        self.assertIn(book4, member1.bookList)
        self.assertIn(member1, library1.libraryMemberCurrentlyBorrowingBookList)
        
        self.assertEqual(book5.getLibraryMember(), member1)
        self.assertIn(book5, member1.bookList)
        self.assertIn(member1, library1.libraryMemberCurrentlyBorrowingBookList)
        
        library1.lendBook(book6, member1)
        self.assertEqual(book6.getLibraryMember(), None)
        self.assertNotIn(book6, member1.bookList)
        self.assertIn(member1, library1.libraryMemberCurrentlyBorrowingBookList)
        
        library1.lendBook(book7, member1)
        self.assertEqual(book7.getLibraryMember(), None)
        self.assertNotIn(book7, member1.bookList)
        self.assertIn(member1, library1.libraryMemberCurrentlyBorrowingBookList)
        
        library1.lendBook(book1, member1)
        
        print("End of test_lendBook()")
        print("========================================")
        
    def test_returnBook(self):
        """
        Test the returnBook() method.
        """
        print("========================================")
        print("Start of test_returnBook()")
        
        library1 = Library()
        book1 = Book()
        book2 = Book()
        book3 = Book()
        member1 = LibraryMember()
        
        library1.addResource(book1)
        library1.addResource(book2)
        
        library1.lendBook(book1, member1)
        self.assertEqual(book1.getLibraryMember(), member1)
        self.assertIn(book1, member1.bookList)
        self.assertIn(member1, library1.libraryMemberCurrentlyBorrowingBookList)
        
        library1.returnBook(book1, False, "")
        self.assertNotIn(book1, member1.bookList)
        self.assertEqual(book1.getLibraryMember(), None)
        self.assertNotIn(member1, library1.libraryMemberCurrentlyBorrowingBookList)
        self.assertEqual(book1.getDamage(), "no damage")
        
        library1.lendBook(book1, member1)
        self.assertEqual(book1.getLibraryMember(), member1)
        self.assertIn(book1, member1.bookList)
        self.assertIn(member1, library1.libraryMemberCurrentlyBorrowingBookList)
        
        library1.lendBook(book2, member1)
        self.assertEqual(book2.getLibraryMember(), member1)
        self.assertIn(book2, member1.bookList)
        self.assertIn(member1, library1.libraryMemberCurrentlyBorrowingBookList)
        
        library1.returnBook(book1, True, "water damage")
        self.assertNotIn(book1, member1.bookList)
        self.assertEqual(book1.getLibraryMember(), None)
        self.assertIn(member1, library1.libraryMemberCurrentlyBorrowingBookList)
        self.assertEqual(book1.getDamage(), "water damage")
        
        library1.returnBook(book2, False, "")
        self.assertNotIn(book2, member1.bookList)
        self.assertEqual(book2.getLibraryMember(), None)
        self.assertNotIn(member1, library1.libraryMemberCurrentlyBorrowingBookList)
        self.assertEqual(book2.getDamage(), "no damage")
        
        library1.lendBook(book1, member1)
        self.assertEqual(book1.getLibraryMember(), member1)
        self.assertIn(book1, member1.bookList)
        self.assertIn(member1, library1.libraryMemberCurrentlyBorrowingBookList)
        
        library1.returnBook(book1, True, "broken corner")
        self.assertNotIn(book1, member1.bookList)
        self.assertEqual(book1.getLibraryMember(), None)
        self.assertNotIn(member1, library1.libraryMemberCurrentlyBorrowingBookList)
        self.assertEqual(book1.getDamage(), "water damage, broken corner")
        
        library1.returnBook(book3, False, "")
        
        print("End of test_returnBook()")
        print("========================================")
        
    def test_sendMessage(self):
        """
        Test the sendMessage() method.
        """
        library1 = Library()
        book1 = Book()
        book2 = Book()
        member1 = LibraryMember()
        member2 = LibraryMember()
        member3 = LibraryMember()
        
        library1.addResource(book1)
        library1.addResource(book2)
        
        library1.lendBook(book1, member1)
        library1.lendBook(book2, member2)
        
        self.assertEqual(book1.getLibraryMember(), member1)
        
        library1.sendMessage("Hello")
        
        self.assertEqual(member1.getMessage(), "Hello")
        self.assertEqual(member2.getMessage(), "Hello")
        self.assertEqual(member3.getMessage(), "no message")
        
    def test_printAllBookdetailInCaltalogue(self):
        """
        Test the printAllBookdetailInCaltalogue() method.
        """
        print("========================================")
        print("Start of test_printAllBookdetailInCaltalogue()")
        
        library1 = Library()
        book1 = Book()
        book2 = Book()
        eResource1 = ElectronicResource()
        
        book1.setTitle("aaa")
        book2.setTitle("bbb")
        
        library1.addResource(book1)
        library1.addResource(book2)
        library1.addResource(eResource1)
        
        library1.printAllBookdetailInCaltalogue()
        
        print("End of test_printAllBookdetailInCaltalogue()")
        print("========================================")
        
    def test_printAllElectronicResourceDetailInCatalogue(self):
        """
        Test the printAllElectronicResourceDetailInCatalogue() method.
        """
        print("========================================")
        print("Start of test_printAllElectronicResourceDetailInCatalogue()")
        
        library1 = Library()
        book1 = Book()
        eResource1 = ElectronicResource()
        eResource2 = ElectronicResource()
        
        library1.addResource(book1)
        library1.addResource(eResource1)
        library1.addResource(eResource2)
        
        eResource1.setTitle("aaa")
        eResource2.setTitle("bbb")
        
        library1.printAllElectronicResourceDetailInCatalogue()
        
        print("End of test_printAllElectronicResourceDetailInCatalogue()")
        print("========================================")
        
        
if __name__ == '__main__':
    unittest.main(TestLibrary())