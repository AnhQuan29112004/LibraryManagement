from services.LibraryManagement import LibraryManagement
from models.Book import Book


if __name__ == "__main__":
    test_book_1 = Book(2, "Sach 1", "Quan", "Category", 5)
    print(test_book_1.getBookName())
    library = LibraryManagement()
    print([i.getBookName() for i in library.book])

