from models.book import Book


book1 = Book("Python and it's tricks", "A python author", "Coding", True)
book2 = Book("Wellbeing", "Dr.Paul", "Cult", False)
book3 = Book("Time Managment", "Simon Clockwell", "Health", False)
book4 = Book("How Nintendo was made", "Jordan Enemy of Nintendo", "Biography", True)

books = [book1, book2, book3, book4]


def get_book(book_index):
    return books[book_index]

def add_book(new_book):
    books.append(new_book)

def remove_book(title):
    book_to_delete = None
    for book in books:
        if book.title == title:
            book_to_delete = book
            break
    books.remove(book_to_delete)