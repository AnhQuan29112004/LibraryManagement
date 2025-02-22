import json
from models.Book import Book
from models.Member import Member
from models.BorrowReturnRecord import BorrowReturnRecord
from datetime import datetime, timedelta

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
            
    
    def borrow_books(self, member_id, borrowed_books):
        member = next((m for m in self.members if m.member_id == member_id), None)
        if not member:
            return "Thành viên không tồn tại"

        borrow_date = datetime.today().strftime("%Y-%m-%d")
        due_date = (datetime.today() + timedelta(days=14)).strftime("%Y-%m-%d")

        for book_info in borrowed_books:
            book = next((b for b in self.books if b.book_id == book_info["book_id"]), None)
            if not book or book.quantity < book_info["quantity"]:
                return "Sách không đủ số lượng."

            book.quantity -= book_info["quantity"]
            member.borrow_book(book_info["book_id"])

        new_record = BorrowReturnRecord(len(self.borrow_records) + 1, member_id, borrowed_books, borrow_date, due_date)
        self.borrow_records.append(new_record)
        self.save_data("Data/books.json", self.books)
        self.save_data("Data/members.json", self.members)
        self.save_data("Data/borrow_records.json", self.borrow_records)

        return "Mượn sách thành công."
    
    def return_books(self, record_id, return_date):
        record = next((r for r in self.borrow_records if r.record_id == record_id), None)
        if not record:
            return "Phiếu mượn không tồn tại"

        record.return_date = return_date
        fee = record.calculate_late_fee()

        for book_info in record.borrowed_books:
            book = next((b for b in self.books if b.book_id == book_info["book_id"]), None)
            if book:
                book.quantity += book_info["quantity"]

        self.save_data("Data/books.json", self.books)
        self.save_data("Data/borrow_records.json", self.borrow_records)

        return f"Trả sách thành công. Phí trễ hạn: {fee} VND"
    
    
    