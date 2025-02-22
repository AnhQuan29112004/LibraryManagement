import json
from models.Book import Book
from models.Member import Member
from models.BorrowReturnRecord import BorrowReturnRecord

class LibraryManagement:
    def __init__(self):
        self.book = self.load_data("Data/book.json", Book)
        self.member = self.load_data("Data/member.json", Member)
        self.borrowRecord = self.load_data("Data/borrowrecord.json", BorrowReturnRecord)
    
    def load_data(self, filename, cls):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
            return [cls.from_dict(item) for item in data]
        except FileNotFoundError:
            return []

    def save_data(self, filename, data):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump([item.to_dict() for item in data], file, indent=4)
            
    def add_book(self, book):
        self.book.append(book)
        self.save_data("Data/book.json",self.book)
        
    def update_book(self, book,bookName=None,author=None,category=None,quantity=None ):
        for i in self.book:
            if(i==book):
                i.setBookName(bookName)
                i.setAuthor(author)
                i.setCategory(category)
                i.setQuantity(quantity)
        self.save_data("Data/book.json",self.book)
        
    def remove_book(self, book):
        self.book.remove(book)
        self.save_data("Data/book.json",self.book)
        
        
    def add_member(self,member):
        self.member.append(member)
        self.save_data("Data/member.json", self.member)
    
    def update_member(self, member, fullName=None,phoneNumber=None,identificationNumber=None,address=None,borrowingBooks=None):
        for i in self.member:
            if(i==member):
                i.setFullName(fullName)
                i.setPhoneNumber(phoneNumber)
                i.setIdentificationNumber(identificationNumber)
                i.setAddress(address)
                i.setBorrowingBooks(borrowingBooks)
        self.save_data("Data/member.json", self.member)
        
    def remove_book(self, member):
        self.book.remove(member)
        self.save_data("Data/member.json",self.member)
    
    
    
    