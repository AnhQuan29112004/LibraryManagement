import json
class Book:
    def __init__(self,bookId,bookName,author,category,quantity):
        self.__bookId = bookId
        self.__bookName = bookName
        self.__author = author
        self.__category = category
        self.__quantity = quantity
        
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
    
    def setQuantity(self,quantity):
        self.__quantity = quantity
    
    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        clean_data = {key.replace("_Book__", ""): value for key, value in data.items()}
        return Book(**clean_data )
        