from models import User, Book 
from storage import Storage

def checkout_book(user_id, isbn, storage):
    """Attempts to checkout a book for a user."""
    users = storage.load_users()
    books = storage.load_books()

    user = find_user_by_id(users, user_id)
    book = find_book_by_isbn(books, isbn)

    if user and book:
        if user.borrow_book(book):
            storage.save_users(users)  
            print("Book checked out successfully.")
        else:
            print("Book is not available for checkout.")
    else:
        print(f"User with ID {user_id} or book with ISBN {isbn} not found.")

def find_user_by_id(users, user_id):
    """Finds a user by their ID."""
    for user in users:
        if user.user_id == user_id:
            return user
    return None

def find_book_by_isbn(books, isbn):
    """Finds a book by its ISBN."""
    for book in books:
        if book.isbn == isbn:
            return book
    return None