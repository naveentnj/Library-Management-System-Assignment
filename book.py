from models import Book, Library

library = Library()  # Initialize a Library instance to manage books

def add_book(title, author, isbn):
    """Adds a new book to the library."""
    if not library.find_book(isbn):  # Check if the book already exists
        library.add_book(title, author, isbn)
        print(f"Book '{title}' added successfully.")
    else:
        print("A book with this ISBN already exists.")

def update_book(isbn, new_title=None, new_author=None):
    """Updates book details in the library."""
    book = library.find_book(isbn)
    if book:
        if new_title:
            book.title = new_title
        if new_author:
            book.author = new_author
        print(f"Book with ISBN {isbn} updated successfully.")
    else:
        print(f"No book found with ISBN {isbn}.")

def delete_book(isbn):
    """Deletes a book from the library."""
    book = library.find_book(isbn)
    if book:
        library.books.remove(book)
        print(f"Book with ISBN {isbn} deleted successfully.")
    else:
        print(f"No book found with ISBN {isbn}.")

def list_books():
    """Lists all the books in the library."""
    if library.books:
        for book in library.books:
            print(book)
    else:
        print("No books available in the library.")

def search_books(title=None, author=None, isbn=None):
    """Searches for books by title, author, or ISBN."""
    results = []
    for book in library.books:
        if (title and title.lower() in book.title.lower()) or \
           (author and author.lower() in book.author.lower()) or \
           (isbn and isbn == book.isbn):
            results.append(book)
    if results:
        for book in results:
            print(book)
    else:
        print("No books found matching the search criteria.")