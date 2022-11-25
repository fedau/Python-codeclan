from flask import render_template
from models.books import books, get_book
from models.book import Book
from app import app


@app.route('/')
def all_books():
    return render_template('index.html', books=books)

@app.route('/books/<int:book_index>')
def book(book_index):
    single_book = get_book(book_index)
    return render_template('book.html', book=single_book)