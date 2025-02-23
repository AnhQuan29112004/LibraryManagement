import json
class Book:
    def __init__(self,bookId,bookName,author,category,quantity):
        self.__bookId = bookId
        self.__bookName = bookName
        self.__author = author
        self.__category = category
        self.setQuantity(quantity)
        
    def getBookId(self):
        return self.__bookId
    
    def setBookId(self,bookId):
        self.__bookId = bookId
        
    def getBookName(self):
        return self.__bookName
    
    def setBookName(self,bookName):
        self.__bookName = bookName
        
    def getAuthor(self):
        return self.__author
    
    def setAuthor(self,author):
        self.__author = author
        
    def getCategory(self):
        return self.__category
    
    def setCategory(self,category):
        self.__category = category
        
    def getQuantity(self):
        return self.__quantity
    
    def setQuantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.__quantity = quantity
        
    def printInformation(self):
        print("=" * 40)
        print(f"📖 Book ID: {self.getBookId()}")
        print(f"📚 Title: {self.getBookName()}")
        print(f"✍️  Author: {self.getAuthor()}")
        print(f"📂 Category: {self.getCategory()}")
        print(f"📦 Quantity Available: {self.getQuantity()}")
        print("=" * 40)
    
    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        clean_data = {key.replace("_Book__", ""): value for key, value in data.items()}
        return Book(**clean_data )
        