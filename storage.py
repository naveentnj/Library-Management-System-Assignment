import json
from models import User, Book

class Storage:
    """Handles data persistence for users and books."""

    def __init__(self, filename):
        self.filename = filename

    def load_users(self):
        """Loads user data from a JSON file."""
        users = []
        try:
            with open(self.filename, "r") as file:
                user_data = json.load(file)
                for user in user_data:
                    users.append(User(user["name"], user["user_id"]))
        except FileNotFoundError:
            pass  # No action needed if file doesn't exist
        return users

    def save_users(self, users):
        """Saves user data to a JSON file."""
        user_data = [user.__dict__ for user in users]
        with open(self.filename, "w") as file:
            json.dump(user_data, file, indent=4)

    def load_books(self):
        """Loads book data from a JSON file."""
        books = []
        try:
            with open(self.filename.replace('users', 'books'), "r") as file:  
                book_data = json.load(file)
                for book in book_data:
                    books.append(Book(book["title"], book["author"], book["isbn"]))
        except FileNotFoundError:
            pass  # No action needed if file doesn't exist
        return books

    def save_books(self, books):
        """Saves book data to a JSON file."""
        book_data = [book.__dict__ for book in books]
        with open(self.filename.replace('users', 'books'), "w") as file:  
            json.dump(book_data, file, indent=4)
