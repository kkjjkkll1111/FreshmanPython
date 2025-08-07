from datetime import *

class Book:
    def __init__(self, name, author, isbn):
        self.name = name
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.due_date = None

    def __str__(self):
        status = "대여가능"
        if self.is_borrowed:
            if self.due_date and self.due_date < date.today():
                status = f"연체중(반납 예정일 : {self.due_date.strftime('%Y-%m-%d')})"
            else:
                status = f"대여중(반납 예정일 : {self.due_date.strftime('%Y-%m-%d')})"
        return f"[{self.isbn}]{self.name} : {self.author} ({status})"
