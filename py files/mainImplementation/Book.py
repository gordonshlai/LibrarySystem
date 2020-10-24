# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 23:14:05 2019

@author: Gordon Lai
"""

class Book:
    """
    Class to represent the book.
    """
    def __init__(self):
        self.isbn = 0
        self.libraryMember = None
        self.damage = "no damage"
        self.title = "not set"
        self.authorName = "not set"
        
    def getISBN(self):
        """
        Return the isbn of the book.
        """
        return self.isbn
    
    def setISBN(self, isbn):
        """
        Set the isbn of the book.
        """
        self.isbn = isbn
        
    def getLibraryMember(self):
        """
        Return the library member
        """
        return self.libraryMember
        
    def setLibraryMember(self, libraryMember):
        """
        Set the library member.
        """
        self.libraryMember = libraryMember
    
    def getDamage(self):
        """
        Return the damages of the book.
        """
        return self.damage
    
    def setDamage(self, damage):
        """
        Set the damage of the book.
        """
        if self.damage == "no damage":
            self.damage = damage
        else:
            self.damage = self.damage + ", " + damage
            
    def getTitle(self):
        """
        Return the title of the book.
        """
        return self.title
    
    def setTitle(self, title):
        """
        Set the title of the book.
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
        
    def checkBookAvailibility(self):
        """
        Check if the book is availible to borrow.
        """
        if self.libraryMember == None:
            return True
        else:
            return False
        
    def printBookDetail(self):
        """
        Print all the details of the book.
        """
        print("------------------------------------------")
        print("Book Title: " + format(self.title))
        print("Author's name: " + format(self.authorName))
        print("ISBN: " + format(self.isbn))
        print("Library Member borrowed this book: " + format(self.libraryMember))
        print("Damages of the book: " + format(self.damage))
        print("------------------------------------------")
        
        
def test():
    book1 = Book()
    book1.printBookDetail()
    
    book1.setISBN(1234)
    book1.setLibraryMember("yo")
    book1.setDamage("broken corner")
    book1.setTitle("Book Title")
    book1.setAuthorName("Author")
    book1.printBookDetail()
    
    book1.setDamage("Water damage")
    book1.printBookDetail()