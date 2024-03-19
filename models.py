class User:
    """Represents a user of the library system."""
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        """Attempts to borrow a book for the user."""
        if book.is_available:
            self.borrowed_books.append(book)
            book.is_available = False
            return True
        else:
            return False

    def return_book(self, book):
        """Attempts to return a book for the user."""
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_available = True
            return True
        else:
            return False

class Book:
    """Represents a book in the library system."""
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        """Returns a string representation of the book."""
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

class Library:
    """Represents the library which manages books and users."""
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, title, author, isbn):
        """Adds a new book to the library."""
        new_book = Book(title, author, isbn)
        self.books.append(new_book)

    def add_user(self, name, user_id):
        """Adds a new user to the library."""
        new_user = User(name, user_id)
        self.users.append(new_user)

    def find_book(self, isbn):
        """Finds a book by its ISBN."""
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_user(self, user_id):
        """Finds a user by their user ID."""
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None
