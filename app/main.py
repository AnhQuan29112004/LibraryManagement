from services.LibraryManagement import LibraryManagement
from models.Book import Book
from models.Member import Member

if __name__ == "__main__":
    library = LibraryManagement()
    for i in library.book:
        if i.getBookId() == 2:
            library.remove_book(i)
            
    member = Member(1,"quan","0123",1,"Thanh tri",)
    

