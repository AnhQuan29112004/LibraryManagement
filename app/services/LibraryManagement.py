import json
from ..models.Book import Book
from ..models.Member import Member
from ..models.BorrowReturnRecord import BorrowReturnRecord

class LibraryManagement:
    def __init__(self):
        self.book = self.load_data("../../Data/book.json", Book)
        self.member = self.load_data("../../Data/member.json", Member)
        self.borrowRecord = self.load_data("../../Data/borrowrecord.json", BorrowReturnRecord)
    
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
        
    
    