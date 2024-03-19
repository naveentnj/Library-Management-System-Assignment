import argparse
from models import User, Book  # Import User and Book classes from models.py
from storage import Storage
from user import add_user, list_users  # Import user-related functions
from book import add_book, list_books  # Import book-related functions
from check import checkout_book  # Import checkout-related function

def main():
    parser = argparse.ArgumentParser(description="Library Management System")
    subparsers = parser.add_subparsers(dest="command")

    # User management commands
    user_parser = subparsers.add_parser("user")
    user_parser.add_argument("action", choices=["add", "list"], help="Action to perform on users")
    user_parser.add_argument("name", nargs="?", help="User name (for add)")
    user_parser.add_argument("-i", "--id", type=int, help="User ID (for add)")

    # Book management commands
    book_parser = subparsers.add_parser("book")
    book_parser.add_argument("action", choices=["add", "list"], help="Action to perform on books")
    book_parser.add_argument("title", nargs="?", help="Book title (for add)")
    book_parser.add_argument("author", nargs="?", help="Book author (for add)")

    # Checkout management commands
    checkout_parser = subparsers.add_parser("checkout")
    checkout_parser.add_argument("user_id", type=int, help="User ID")
    checkout_parser.add_argument("isbn", help="ISBN of the book to checkout")

    args = parser.parse_args()

    storage = Storage("library.json")  # Initialize storage for data persistence

    if args.command == "user":
        if args.action == "add" and args.name and args.id:
            add_user(args.name, args.id, storage)
        elif args.action == "list":
            list_users(storage)
    elif args.command == "book":
        if args.action == "add" and args.title and args.author:
            add_book(args.title, args.author, storage)
        elif args.action == "list":
            list_books(storage)
    elif args.command == "checkout":
        checkout_book(args.user_id, args.isbn, storage)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()