from operator import index

from book import Book

books = []

def select_menu():
    print("\n=== 메뉴를 선택하시오 ===")
    print("1. 도서 등록")
    print("2. 도서 목록 보기")
    print("3. 도서 검색")
    print("4. 도서 삭제")
    print("5. 도서 대여")
    print("6. 도서 반납")
    print("7. 종료")
    print("="*12)
    selection = input("입력 => ")
    return selection

def add_book():
    name = input("책제목 : ").strip()
    if not name:
        print("잘못된 제목")
        return

    author = input("저자 : ").strip()
    if not author:
        print("잘못된 제목")
        return

    isbn = input("ISBN : ")
    if len(isbn) != 6:
        print("잘못된 ISBN번호")
        return

    for b in books:
        if b.isbn == isbn:
            print("동일한 ISBN이 존재합니다.")
            return
    book = Book(name, author, isbn)
    books.append(book)
    print("책이 정상적으로 추가 되었습니다.")


def book_list():
    if not books:
        print("도서가 없습니다.")
        return
    print("=== 도서 목록 ===")
    for book in books:
        print(book)


def search_book():
    search_keyword = input("원하는 도서를 검색하시오(제목 or 저자 or ISBN)")
    count = 0
    for book in books:
        if search_keyword in str(book):
            print(book)
            count += 1
    if count > 0:
        print(f"총 {count}권의 도서를 발견했습니다.")
    else:
        print("찾으시는 도서는 존재하지 않습니다.")


def delete_book():
    isbn = input("ISBN을 입력하시오 : ")
    if len(isbn) != 6:
        print("잘못된 ISBN번호")
        return

    for book in books:
        if book.isbn == isbn:
            if book.is_borrowed:
                print("대여중인 도서는 삭제할 수 없습니다.")
                return
            else:
                books.remove(book)
                print("도서가 삭제 되었습니다.")
                return

    print("해당ISBN을 가진 도서를 발견하지 못하였습니다.")


def borrow_book():
    borrowable_book_list = []

    for book in books:
        if book.is_borrowed:
            continue
        borrowable_book_list.append(book)

    print("=== 대여가능 도서목록 ===")
    for i, book in enumerate(borrowable_book_list):
        print(f"[{i+1}] : {book.name} (author : {book.author})")

    idx = int(input("대여하고 싶은 번호 선택\n -->"))
    if idx < 0 or idx > len(borrowable_book_list):
        print("선택 오류")
        return

    book = borrowable_book_list[idx - 1]
    book.is_borrowed = True
    print("성공적으로 대여가 되었습니다")


def return_book():
    is_borrowed_book_list = []

    for book in books:
        if book.is_borrowed:
            is_borrowed_book_list.append(book)

    print("반납하실 도서를 선택하세요")
    for i, book in enumerate(is_borrowed_book_list):
        print(f"[{i+1}] : {book.name}(author:{book.author})")

    idx = int(input("--->"))

    if idx < 0 or idx > len(is_borrowed_book_list):
        print("선택 오류")
        return

    book = is_borrowed_book_list[idx - 1]
    book.is_borrowed = False
    print("성공적으로 반납이 되었습니다")



if __name__ == "__main__":

    while True:
        selection = select_menu()
        if selection == '1':
            add_book()
        elif selection == '2':
            book_list()
        elif selection == '3':
            search_book()
        elif selection == '4':
            delete_book()
        elif selection == '5':
            borrow_book()
        elif selection == '6':
            return_book()
        elif selection == '7':
            print("시스템을 종료합니다")
            break
        else:
            print("올바른 메뉴 번호를 입력해주세요")