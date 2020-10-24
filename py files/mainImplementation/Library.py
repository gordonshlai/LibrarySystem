# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 21:27:43 2019

@author: Gordon Lai
"""

from mainImplementation.Book import Book
from mainImplementation.ElectronicResource import ElectronicResource

class Library:
    """
    Class to repersent the Library.
    """
    def __init__(self):
        self.catalogue = []
        self.maxBookNumber = 5
        self.libraryMemberCurrentlyBorrowingBookList = []
        
    def getCatalogue(self):
        """
        Return the list of book and electronic resource objects.
        """
        return self.catalogue
    
    def getMaxBookNumber(self):
        """
        Return the maximum number of books a library member can borrow at the same time.
        """
        return self.maxBookNumber
    
    def setMaxBookNumber(self, maxBookNumber):
        """
        Set the maximum number of books a library member can borrow at the same time.
        """
        self.maxBookNumber = maxBookNumber
        
    def getLibraryMemberCurrentlyBorrowingBookList(self):
        """
        Return the list of library members that currently borrowing book.
        """
        return self.libraryMemberCurrentlyBorrowingBookList
        
    def printAllLibraryDetail(self):
        """
        Print all the details of the library.
        """
        print("###############################")
        print("Maximum number book a library member can borrow at the same time: " + format(self.maxBookNumber))
        print("Resources contained in the catalogue:")
        print("Physical books:")
        self.printAllBookdetailInCaltalogue()
        print("Electronic resources:")
        self.printAllElectronicResourceDetailInCatalogue()
        print("Library members that currently borrowing book:")
        for member in self.libraryMemberCurrentlyBorrowingBookList:
            member.printLibraryMemberDetail()
            print("###############################")
        
    def containResource(self, resource):
        """
        Check if a book or electronic resource object is in the catalogue.
        """
        if resource in self.catalogue:
            return True
        else:
            return False
        
    def editTitle(self, resource, title):
        """
        Edit the title of a book or electronic resource object.
        """
        if resource in self.catalogue:
            if type(resource) == Book:
                resource.setTitle(title)
            else:
                resource.setTitle(title)
        else:
            print("Error! The resource does not belong to this catalogue.")
        
    def searchResource(self, resource):
        """
        Return the book or electronic resource object if the object is contained in the catalogue.
        """
        if resource in self.catalogue:
            return resource
        else:
            return None
        
    def searchResourceByISBN(self, isbn):
        """
        Search the catalogue by ISBN of the book object.
        """
        count = 0
        for resource in self.catalogue:
            if isinstance(resource, Book):
                if resource.getISBN() == isbn:
                    resource.printBookDetail()
                    count += 1
        print("Number of the resource with ISBN " + format(isbn) + ": " + format(count))
        
    def searchResourceByAuthorName(self, authorName):
        """
        Search the catalogue by the author's name of the book or electronic resource object.
        """
        count = 0
        for resource in self.catalogue:
            if isinstance(resource, Book):
                if resource.getAuthorName() == authorName:
                    resource.printBookDetail()
                    count += 1
            else:
                if resource.getAuthorName() == authorName:
                    resource.printElectronicResourceDetail()
                    count += 1
                    
        print("Number of resource with author name " + format(authorName) + ": " + format(count))
        
    def removeResourceByObject(self, resource):
        """
        Remove a resource from the catalogue.
        """
        if resource in self.catalogue:
            self.catalogue.remove(resource)
        else:
            print("Error! resource is not in the catalogue.")
        
    def removeResourceByPosition(self, position):
        """
        Remove a resource at a specific position in the catalogue.
        """
        if position >= len(self.catalogue):
            print("Error! The catalogue does not contain an object with the specific position you wish to remove.")
        elif abs(position) > len(self.catalogue):
            print("Error! The catalogue does not contain an object with the specific position you wish to remove.")
        else:
            del self.catalogue[position]
        
    def printAllAvailibleBooks(self):
        """
        Print the details of all the availible books.
        """
        for resource in self.catalogue:
            if isinstance(resource, Book):
                if resource.checkBookAvailibility() == True:
                    resource.printBookDetail()
        
    def numberOfResource(self):
        """
        Return the number of resource in the catalogue.
        """
        return len(self.catalogue)
        
    def addResource(self, resource):
        """
        Add a book or electronic resource to the end of the catalogue list.
        """
        if resource not in self.catalogue:
            self.catalogue.append(resource)
        else:
            print("The resource is alreeady in the catalogue.")
        
    def lendBook(self, book, libraryMember):
        """
        Lend a book to a library member.
        """
        if book in self.catalogue:
            if book.checkBookAvailibility() == True:
                if libraryMember.numberOfBook() < self.maxBookNumber:
                    book.setLibraryMember(libraryMember)
                    libraryMember.addBook(book)
                    if libraryMember not in self.libraryMemberCurrentlyBorrowingBookList:
                        self.libraryMemberCurrentlyBorrowingBookList.append(libraryMember)
                else:
                    print("Error! The library member is currently borrowing 5 books, which is the maximum limit.")
            else:
                print("Error! The book is currently unavailible.")
        else:
            print("Error! The book is not in the catalogue.")
        
    def returnBook(self, book, damage, description):
        """
        Return a book.
        """
        if book in self.catalogue:
            book.getLibraryMember().getBookList().remove(book)
            book.setLibraryMember(None)
            for member in self.libraryMemberCurrentlyBorrowingBookList:
                if member.numberOfBook() == 0:
                    self.libraryMemberCurrentlyBorrowingBookList.remove(member)
            if damage == True:
                book.setDamage(description)
        else:
            print("Error! This book is not in the catalogue.")
        
    def sendMessage(self, message):
        """
        Send message to all library members that currently holding books.
        """
        for libraryMember in self.libraryMemberCurrentlyBorrowingBookList:
            libraryMember.setMessage(message)
        
    def printAllBookdetailInCaltalogue(self):
        """
        Print the details of all the books in the catalogue.
        """
        for resource in self.catalogue:
            if isinstance(resource, Book):
                resource.printBookDetail()
        
    def printAllElectronicResourceDetailInCatalogue(self):
        """
        Print the details of all the electronic resources in the catalogue.
        """
        for resource in self.catalogue:
            if type(resource) == ElectronicResource:
                resource.printElectronicResourceDetail()

    