import unittest
from models.books import books, add_book
from models.book import Book


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("William", "Writer", "Fun", False)


    # def test(self):
    #     self.assertEqual(1,1)

    def test_book_has_title(self):
        self.assertEqual("William", self.book.title )
    
    def test_book_author(self):
        self.assertEqual("Writer", self.book.author)

    def test_book_list_lenght(self):
        actual_output = len(books)
        self.assertEqual(4, actual_output)