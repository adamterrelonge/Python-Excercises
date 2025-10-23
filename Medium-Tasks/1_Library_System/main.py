#Medium Difficulty --> Library System

'''
Create a Book class with attributes title (string), author (string), isbn (string) and available (boolean) where a book is initialised with available set to True.
Create a Library class the stores a list of books and has methods, add_book to add a book to the collection, borrow_book  that sets available = False if the book exists and is available and display_books that prints all books and their availability.
'''

from book import Book
from library import Library

def main():
    lib = Library()

    # Create some books using the 'Book' function in book.py
    b1 = Book("1984", "George Orwell", "12345")
    b2 = Book("To Kill a Mockingbird", "Harper Lee", "67890")

    # Add books to library using the 'add_book' function in library.py
    lib.add_book(b1)
    lib.add_book(b2)

    # Display all books
    lib.display_books()

    # Borrow a book
    lib.borrow_book("12345")

    # Display books again
    lib.display_books()

if __name__ == "__main__":
    main()
