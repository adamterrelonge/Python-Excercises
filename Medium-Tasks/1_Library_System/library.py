import book

class Library:
    def __init__(self):
        self.books = []  # list to store Book objects

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.available:
                    book.available = False
                    print(f"You borrowed '{book.title}'.")
                else:
                    print(f"'{book.title}' is already borrowed.")
                return
        print("Book not found in the library.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nLibrary Collection:")
            for book in self.books:
                print(book)
