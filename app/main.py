from services.LibraryManagement import LibraryManagement
from models.Book import Book
from models.Member import Member

if __name__ == "__main__":
    # for i in library.book:
    #     if i.getBookId() == 2:
    #         library.remove_book(i)
            
    # member = Member(2,"quan","0123",1,"Thanh tri")
    # library.add_member(member)
    library = LibraryManagement()
<<<<<<< HEAD
    member_id = 1
    book_id = 2
    quantity = 6
    result = library.borrow_books(2, [{"book_id": book_id, "quantity": quantity}])
    print(result)
    result = library.return_books(3, "2025-03-06")
    print(result)
=======
    # for i in library.book:
    #     if i.getBookId() == 2:
    #         library.remove_book(i)
            
    # member = Member(2,"quan","0123",1,"Thanh tri")
    # library.add_member(member)
    library.searchMember("2")
    
>>>>>>> 0a7cb0d131dadcc75592ab21f7a0cad927bc6bc1

