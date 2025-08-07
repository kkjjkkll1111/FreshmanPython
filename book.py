class Book:
    def __init__(self, name, author, isbn):
        self.name = name
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        status = "대여가능"
        if self.is_borrowed:
            status = "대여중"
        return f"[{self.isbn}]{self.name} : {self.author} ({status})"
