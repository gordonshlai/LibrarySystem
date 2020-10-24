# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 18:55:43 2019

@author: Gordon Lai
"""

class LibraryMember:
    """
    Class to repersent library member.
    """
    def __init__(self):
        self.bookList = []
        self.message = "no message"
        self.name = "not set"
        
    def getBookList(self):
        """
        Return the list of book objects.
        """
        return self.bookList
    
    def addBook(self, book):
        """
        Add a book object to the end of the book list.
        """
        self.bookList.append(book)
        
    def getMessage(self):
        """
        Return the messages of the library member.
        """
        return self.message
    
    def setMessage(self, message):
        """
        Set the message of the library member.
        """
        if self.message == "no message":
            self.message = message
        else:
            self.message = self.message + ", " + message
            
    def getName(self):
        """
        Return the name of the library member.
        """
        return self.name
    
    def setName(self, name):
        """
        Set the name of the library member.
        """
        self.name = name
            
    def printLibraryMemberDetail(self):
        """
        Print the details fo the library member.
        """
        print("++++++++++++++++++++++++++++++++++++++++++")
        print("Library member name: " + self.name)
        print("Books currently borrowed by this library member:")
        if len(self.bookList) == 0:
            print("This library member is not currently borrowing any book.")
        else:
            self.printAllBook()
        print("Message: " + format(self.message))
        print("++++++++++++++++++++++++++++++++++++++++++")
        
    def printAllMessage(self):
        """
        Print all the messages received by a library member
        """
        print(self.message)
        
    def printAllBook(self):
        """
        Print the details of all books currently borrowed by a library member.
        """
        for book in self.bookList:
            book.printBookDetail()
        
    def numberOfBook(self):
        """
        Returns the number of books currently borrowed by a library member.
        """
        return len(self.bookList)
    
def test():
    libraryMember1 = LibraryMember()
    libraryMember1.printLibraryMemberDetail()
    print(libraryMember1.numberOfBook())
    
    book1 = Book.Book()
    book2 = Book.Book()
    
    libraryMember1.addBook(book1)
    libraryMember1.addBook(book2)
    
    libraryMember1.printLibraryMemberDetail()
    print(libraryMember1.numberOfBook())