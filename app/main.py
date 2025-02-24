from services.LibraryManagement import LibraryManagement
from models.Book import Book
from models.Member import Member
from unidecode import unidecode

def main():
    library = LibraryManagement()

    while True:
        print("\n--- QUẢN LÝ THƯ VIỆN ---")
        print("1. Thêm sách mới")
        print("2. Thêm thành viên")
        print("3. Mượn sách")
        print("4. Trả sách")
        print("5. Chỉnh sửa sách")
        print("6. Xóa sách")
        print("7. Chỉnh sửa thành viên")
        print("8. Xóa thành viên")
        print("9. Tìm kiếm sách")
        print("10. Tìm kiếm thành viên")
        print("11. Sắp xếp sách theo số lượng")
        print("12. Sắp xếp sách theo số lượng (giảm dần)")
        print("13. Sắp xếp thành viên theo số sách đã mượn")
        print("14. Thống kê thư viện")
        print("15. Thoát")

        choice = input("Chọn: ")
        if choice == "1":
            library.add_book(len(library.book) + 1, input("Tên sách: "), input("Tác giả: "), input("Thể loại: "), int(input("Số lượng: ")))
            print("Đã thêm sách.")

        elif choice == "2":
            library.add_member(len(library.member) + 1, input("Họ tên: "), input("Số điện thoại: "), input("CCCD: "), input("Địa chỉ: "))
            print("Đã thêm thành viên.")

        elif choice == "3":
            list_book = []
            optionBorrow = True
            member_id = int(input("Nhập mã thành viên: "))
            while(optionBorrow):
                book_id = int(input("Nhập mã sách: "))
                quantity = int(input("Số lượng: "))
                option = input("Có muốn mượn thêm loại sách khác: ")
                list_book.append({"book_id": book_id, "quantity" : quantity})
                if(unidecode(option).lower() in "khong"):
                    optionBorrow = False
                else:optionBorrow=True
            result = library.borrow_books(member_id, list_book)
            print(result)

        elif choice == "4":
            record_id = int(input("Nhập mã phiếu mượn: "))
            return_date = input("Nhập ngày trả (YYYY-MM-DD): ")
            result = library.return_books(record_id, return_date)
            print(result)

        elif choice == "5":
            book_id = int(input("Nhập mã sách cần chỉnh sửa: "))
            book_name = input("Nhập tên sách mới (bỏ trống nếu không đổi): ")
            author = input("Nhập tác giả mới (bỏ trống nếu không đổi): ")
            category = input("Nhập thể loại mới (bỏ trống nếu không đổi): ")
            quantity = input("Nhập số lượng mới (bỏ trống nếu không đổi): ")
            library.edit_book(book_id, book_name or None, author or None, category or None, int(quantity) if quantity else None)
            print("Đã chỉnh sửa sách.")

        elif choice == "6":
            book_id = int(input("Nhập mã sách cần xóa: "))
            library.delete_book(book_id)
            print("Đã xóa sách.")

        elif choice == "7":
            member_id = int(input("Nhập mã thành viên cần chỉnh sửa: "))
            name = input("Nhập họ tên mới (bỏ trống nếu không đổi): ")
            phone = input("Nhập số điện thoại mới (bỏ trống nếu không đổi): ")
            cccd = input("Nhập CCCD mới (bỏ trống nếu không đổi): ")
            address = input("Nhập địa chỉ mới (bỏ trống nếu không đổi): ")
            library.edit_member(member_id, name or None, phone or None, cccd or None, address or None)
            print("Đã chỉnh sửa thành viên.")

        elif choice == "8":
            member_id = int(input("Nhập mã thành viên cần xóa: "))
            library.delete_member(member_id)
            print("Đã xóa thành viên.")

        elif choice == "9":
            keyword = input("Nhập từ khóa tìm kiếm sách: ")
            print("Kết quả tìm kiếm:")
            library.searchBook(keyword)
            

        elif choice == "10":
            keyword = input("Nhập từ khóa tìm kiếm thành viên: ")
            print("Kết quả tìm kiếm:")
            library.searchMember(keyword)
        elif choice == "11":
            sorted_books = library.sortBook()
            print("\n📚 SÁCH ĐƯỢC SẮP XẾP THEO SỐ LƯỢNG (TĂNG DẦN):")
            print("Mã sách".ljust(10) + "Số lượng")
            print("-" * 20)
            for book_id, quantity in sorted_books.items():
                print(book_id.ljust(10) + str(quantity))

        elif choice == "12":
            sorted_books = library.sortBookReverse()
            print("\n📚 SÁCH ĐƯỢC SẮP XẾP THEO SỐ LƯỢNG (GIẢM DẦN):")
            print("Mã sách".ljust(10) + "Số lượng")
            print("-" * 20)
            for book_id, quantity in sorted_books.items():
                print(book_id.ljust(10) + str(quantity))

        elif choice == "13":
            sorted_members = library.sortMember()
            print("\n👥 THÀNH VIÊN ĐƯỢC SẮP XẾP THEO SỐ SÁCH ĐÃ MƯỢN:")
            print("Mã TV".ljust(10) + "Số sách mượn")
            print("-" * 25)
            for member_id, borrowed in sorted_members.items():
                print(member_id.ljust(10) + str(borrowed))

        elif choice == "14":
            stats = library.statistics()
            
            print("\n📊 THỐNG KÊ THƯ VIỆN:")

            
            print("\n🔹 SỐ LƯỢNG SÁCH THEO THỂ LOẠI:")
            for category, count in stats["totalListBook"].items():
                print(f"  - {category}: {count} sách")

            
            print("\n📖 SÁCH ĐƯỢC MƯỢN NHIỀU NHẤT:")
            print("Mã sách".ljust(10) + "Số lượng")
            print("-" * 20)
            for book_id, count in stats["mostBorrowedBook"].items():
                print(book_id.ljust(10) + str(count))

            
            print("\n👤 THÀNH VIÊN MƯỢN NHIỀU SÁCH NHẤT:")
            print("Mã TV".ljust(10) + "Số sách mượn")
            print("-" * 25)
            for member_id, count in stats["MemberBorrow"].items():
                print(member_id.ljust(10) + str(count))

        elif choice == "15":
            print("Đã thoát chương trình.")
            break
        
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    main()
    
    

