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
        member = next((m for m in self.member if m.getMemberId() == member_id), None)
        if not member:
            return "Thành viên không tồn tại"

        borrow_date = datetime.today().strftime("%Y-%m-%d")
        due_date = (datetime.today() + timedelta(days=14)).strftime("%Y-%m-%d")

        for book_info in borrowed_books:
            book = next((b for b in self.book if b.getBookId() == book_info["book_id"]), None)
            if not book or book.getQuantity() < book_info["quantity"]:
                return "Sách không đủ số lượng."
            book.setQuantity(book.getQuantity() - book_info["quantity"])
            member.borrow_book(book_info["book_id"])

        new_record = BorrowReturnRecord(len(self.borrowRecord) + 1, member_id, borrowed_books, borrow_date, due_date)
        self.borrowRecord.append(new_record)
        self.save_data("Data/book.json", self.book)
        self.save_data("Data/member.json", self.member)
        self.save_data("Data/borrowrecord.json", self.borrowRecord)

        return "Mượn sách thành công."
    
    def return_books(self, record_id, return_date):
        record = next((r for r in self.borrowRecord if r.getRecordId() == record_id), None)
        if not record:
            return "Phiếu mượn không tồn tại"

        record.setReturnDate(return_date)
        fee = record.calculate_late_fee()

        for book_info in record.getBorrowingList():
            book = next((b for b in self.book if b.getBookId() == book_info["book_id"]), None)
            if book:
                newQuantityBook = book.getQuantity() + book_info["quantity"]
                book.setQuantity(newQuantityBook)
        member = next((b for b in self.member if b.getMemberId() == record.getMemberId()), None)
        member.setBorrowingBooks(member.getBorrowingBooks().remove(record.getBorrowingList()[0]["book_id"]))
        self.save_data("Data/book.json", self.book)
        self.save_data("Data/borrowrecord.json", self.borrowRecord)
        self.save_data("Data/member.json", self.member)

        return f"Trả sách thành công. Phí trễ hạn: {fee} VND"
    
    
    