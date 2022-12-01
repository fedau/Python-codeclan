import pdb
from models.author import Author
from models.books import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_repository.delete_all()
author_repository.delete_all()

author_1 =Author('Oasis')
author_repository.save(author_1)
author_2 =Author('William')

author_repository.save(author_2)

book_1 = Book("Roll With It is the title", author_1, "Fiction is the genre")
book_repository.save(book_1)
book_2 = Book("Another book is the title for my next book", author_2, "Romance")
book_repository.save(book_2)

book_1.genre = "Romance"
book_repository.update(book_1)

for book in book_repository.select_all():
    print(book.__dict__)



pdb.set_trace()
