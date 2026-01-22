from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_taken = False

    def take_book(self):
        self._is_taken = True

    def return_book(self):
        self._is_taken = False

    def is_taken(self):
        return self._is_taken

    @abstractmethod
    def get_type(self):
        pass

    def __str__(self):
        status = "Taken" if self._is_taken else "Available"
        return f"{self.get_type()} | {self.title} by {self.author} [{status}]"


class PaperBook(Book):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def get_type(self):
        return "Paper Book"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def get_type(self):
        return "E-Book"

class Reader:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def take_book(self, book):
        if not book.is_taken():
            book.take_book()
            self.borrowed_books.append(book)
            print(f"{self.name} took '{book.title}'")
        else:
            print(f"'{book.title}' is already taken")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        print("\nLibrary books:")
        for book in self.books:
            print(book)


library = Library()

book1 = PaperBook("1984", "George Orwell", 111)
book2 = EBook("Python Basics", "John Smith", "1MB")

library.add_book(book1)
library.add_book(book2)

reader = Reader("Bobby")

library.show_books()

reader.take_book(book1)
reader.take_book(book2)

library.show_books()

reader.return_book(book1)
book2.is_taken = False

library.show_books()
