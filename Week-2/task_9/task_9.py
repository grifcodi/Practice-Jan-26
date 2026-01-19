from abc import ABC, abstractmethod

class Library(ABC):
    @abstractmethod
    def get_books(self):
        pass


class Book(Library):
