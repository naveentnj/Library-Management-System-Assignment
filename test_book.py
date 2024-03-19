import unittest
from book import add_book, list_books, update_book, delete_book, search_books
from models import Library

class TestBook(unittest.TestCase):
    def setUp(self):
        """Initialize a new library instance before each test."""
        self.library = Library()

    def test_add_book(self):
        """Test adding a book to the library."""
        add_book("Test Title", "Test Author", "1234567890")
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Test Title")

    def test_update_book(self):
        """Test updating a book's details."""
        add_book("Old Title", "Test Author", "1234567890")
        update_book("1234567890", new_title="New Title")
        self.assertEqual(self.library.books[0].title, "New Title")

    def test_delete_book(self):
        """Test deleting a book from the library."""
        add_book("Test Title", "Test Author", "1234567890")
        delete_book("1234567890")
        self.assertEqual(len(self.library.books), 0)

    def test_list_books(self):
        """Test listing all books in the library."""
        add_book("Test Title", "Test Author", "1234567890")
        self.library.list_books()
        
    def test_search_books(self):
        """Test searching for books by various attributes."""
        add_book("Test Title", "Test Author", "1234567890")
        result = search_books(title="Test Title")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].isbn, "1234567890")

if __name__ == '__main__':
    unittest.main()