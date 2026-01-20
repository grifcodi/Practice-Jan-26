from abc import ABC, abstractmethod

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        print("Library books:")
        for book in self.books:
            print(book)

class Book(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_taken = False

    def take_book(self):
        self.__is_taken = True

    def is_taken(self):
        return self.__is_taken

    @abstractmethod
    def get_type(self):
        pass

    def __str__(self):
        status = "Taken" if self.__is_taken else "Not taken"
        print("Title: " + self.title)
        print("Author: " + self.author)
        print("Status: " + status)



