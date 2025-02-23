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
            
    
    # ------BOOK------:Start
    def add_book(self,bookId,bookName,author,category,quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if any(b.getBookId() == bookId for b in self.book):
            raise ValueError(f"Book ID {bookId} already exist")
        new_book = Book(bookId, bookName, author, category, quantity)
        self.book.append(new_book)
        self.save_data("Data/book.json", self.book)
        return print(f"Book ID {bookId} added successfully.")
        
    def edit_book(self,bookId,bookName=None,author=None,category=None,quantity=None):
        for book in self.book:
            if book.getBookId() == bookId:
                if bookName:
                    book.setBookName(bookName)
                if author:
                    book.setAuthor(author)
                if category:
                    book.setCategory(category)
                if quantity is not None:
                    book.setQuantity(quantity)

                self.save_data("Data/book.json", self.book)  # Save the updated book list
                return print(f"Book ID {bookId} updated successfully.")
        
        raise ValueError(f"Book ID {bookId} not found.")
        
    def delete_book(self, bookId):
        book = next((b for b in self.book if b.getBookId() == bookId), None)
        if not book:
            raise ValueError(f"Book ID {bookId} not found.")

        for record in self.borrowRecord:
            if any(b.getBookId() == bookId for b in record.getBorrowingList()):
                raise ValueError(f"Book ID {bookId} cannot be deleted because it is currently borrowed.")

        self.book = [b for b in self.book if b.getBookId() != bookId]
        self.save_data("Data/book.json", self.book)

        return print(f"Book ID {bookId} deleted successfully.")
    # ------BOOK------:End
    
    
    # ------MEMBER------:Start
    def add_member(self,memberId,fullName,phoneNumber,identificationNumber,address):
        if any(m.getMemberId() == memberId for m in self.member):
            raise ValueError(f"Member ID {memberId} already exist")
        new_member = Member(memberId,fullName,phoneNumber,identificationNumber,address)
        self.member.append(new_member)
        self.save_data("Data/member.json", self.member)
        return print(f"Member ID {memberId} added successfully.")
    
    def edit_member(self,memberId,fullName=None,phoneNumber=None,identificationNumber=None,address=None):
        for member in self.member:
            if member.getMemberId() == memberId:
                if fullName:
                    member.setFullName(fullName)
                if phoneNumber:
                    member.setPhoneNumber(phoneNumber)
                if identificationNumber:
                    member.setIdentificationNumber(identificationNumber)
                if address is not None:
                    member.setAddress(address)

                self.save_data("Data/member.json", self.member) 
                return print(f"Member ID {memberId} updated successfully.")
        
        raise ValueError(f"Member ID {memberId} not found.")
    
    def delete_member(self, memberId):
        member = next((m for m in self.member if m.getMemberId() == memberId), None)
        if not member:
            raise ValueError(f"Member ID {memberId} not found.")

        for record in self.borrowRecord:
            if any(memberId == record.getMemberId()):
                raise ValueError(f"Member ID {memberId} cannot be deleted because it is currently borrowing.")

        self.member = [m for m in self.member if m.getMemberId() != memberId]
        self.save_data("Data/member.json", self.member)

        return print(f"Member ID {memberId} deleted successfully.")
    
    # ------MEMBER------:end
    
    # ------SEARCH------:Start
    def searchBook(self, keyword):
        result = [
            book
            for book in self.book
            if keyword.lower() in book.getBookName().lower()
            or keyword.lower() in book.getAuthor().lower()
            or keyword.lower() in book.getCategory().lower()
        ]
        if result:
            print("Books Found:")
            for book in result:
                book.printInformation()
        else:
            print(f"No books found for '{keyword}'.")
            
    
    def searchMember(self, keyword):
        result = [
            member
            for member in self.member
            if keyword.lower() in member.getFullName().lower()
            or str(member.getMemberId()) == keyword
        ]
        if result:
            print("Members Found:")
            for member in result:
                member.printInformation()
        else:
            print(f"No members found for '{keyword}'.")
    
    # ------SEARCH------:End
    
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
    
    
    