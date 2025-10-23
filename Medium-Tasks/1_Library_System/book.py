class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True  # Book is available by default

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"
