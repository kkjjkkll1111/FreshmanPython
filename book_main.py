from book import Book
from datetime import *
import os

DIRECTORY = "D:\\PythonProject\\Freshman_Python\\datas"
FILE = os.path.join(DIRECTORY, "book_list.txt")

books = []


def setup_environment():
    """프로그램 실행에 필요한 디렉토리가 없으면 생성합니다."""
    if not os.path.isdir(DIRECTORY):
        print(f"'{DIRECTORY}' 디렉토리가 없어 새로 생성합니다.")
        os.makedirs(DIRECTORY)


def save_data():
    print("\n도서 정보를 파일에 저장 중입니다...")
    with open(FILE, 'w', encoding='utf-8') as f:
        for book in books:
            due_date_str = book.due_date.strftime('%Y-%m-%d') if book.due_date else 'None'
            line = f"{book.name}|{book.author}|{book.isbn}|{book.is_borrowed}|{due_date_str}\n"
            f.write(line)
    print("저장이 완료되었습니다.")


def load_data():
    if not os.path.isfile(FILE):
        print("저장된 도서 정보 파일이 없습니다.")
        return

    print("\n저장된 도서 정보를 불러오는 중입니다...")
    with open(FILE, 'r', encoding='utf-8') as f:
        for line in f:
            # 파일에서 빈 줄을 읽었을 경우 건너뜀
            if not line.strip():
                continue

            try:
                book_info = line.strip().split('|')
                name = book_info[0]
                author = book_info[1]
                isbn = book_info[2]

                # Book 객체 생성
                book = Book(name, author, isbn)

                # 대여 상태 변환 ('True' 문자열 -> True 불리언)
                book.is_borrowed = (book_info[3] == 'True')

                # 날짜 변환 ('YYYY-MM-DD' 문자열 -> date 객체)
                due_date_str = book_info[4]
                if due_date_str != 'None':
                    book.due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()
                else:
                    book.due_date = None

                books.append(book)
            except ValueError:
                print(f"경고: 파일의 데이터 형식이 잘못되었습니다. 해당 줄을 건너뜁니다: {line.strip()}")
    print("정보를 모두 불러왔습니다.")




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

    if not borrowable_book_list:
        print("대여 가능한 도서가 없습니다.")
        return
    print("=== 대여가능 도서목록 ===")
    for i, book in enumerate(borrowable_book_list):
        print(f"[{i+1}] : {book.name} (author : {book.author})")

    try:
        choice = int(input("\n대여하고 싶은 도서의 번호를 선택하세요 --> "))
        if 1 <= choice and choice <= len(borrowable_book_list):
            book = borrowable_book_list[choice - 1]
            book.is_borrowed = True
            book.due_date = date.today() + timedelta(weeks=2)
            print(f"'{book.name}' 도서가 성공적으로 대여되었습니다.")
            print(f"{book.name}의 반납 예정일은 {book.due_date.strftime("%Y-%m-%d")}입니다.")
        else:
            print("잘못된 번호를 선택하셨습니다.")
    except ValueError:
        print("숫자를 입력해주세요.")


def return_book():
    is_borrowed_book_list = []

    for book in books:
        if book.is_borrowed:
            is_borrowed_book_list.append(book)

    if not is_borrowed_book_list:
        print("반납할 도서가 없습니다.")
        return

    print("반납하실 도서를 선택하세요")
    for i, book in enumerate(is_borrowed_book_list):
        print(f"[{i+1}] : {book.name}(author:{book.author})")

    idx = int(input("--->"))

    if idx < 0 or idx > len(is_borrowed_book_list):
        print("선택 오류")
        return

    book = is_borrowed_book_list[idx - 1]
    book.is_borrowed = False
    book.due_date = None
    print("성공적으로 반납이 되었습니다")



if __name__ == "__main__":
    setup_environment()
    load_data()

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
            save_data()
            print("시스템을 종료합니다")
            break
        else:
            print("올바른 메뉴 번호를 입력해주세요")