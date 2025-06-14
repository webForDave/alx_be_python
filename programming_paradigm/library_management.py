class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

    def __str__(self):
        return f'{self.title} by {self.author}'

    def is_checked_out(self):
        """Returns the checkout status of the book."""
        return self.__is_checked_out

    def check_out(self):
        """Sets the book's status to checked out."""
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return True
        return False 

    def return_book(self):
        """Sets the book's status to available."""
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False 
    

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book.is_checked_out():
                    book.check_out()
                    print(f"'{title}' has been checked out.")
                    return True
                else:
                    print(f"'{title}' is already checked out.")
                    return False
        print(f"Book with title '{title}' not found in the library.")
        return False

    def list_available_books(self):
        found_available = False
        for book in self._books:
            if not book.is_checked_out():
                print(f"{book}")
                found_available = True
        if not found_available:
            print("No books currently available.")

    def return_book(self, title): 
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned.")
                    return True
                else:
                    print(f"'{title}' was not checked out.")
                    return False
        print(f"Book with title '{title}' not found in the library.")
        return False