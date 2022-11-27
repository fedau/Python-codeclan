from flask import render_template, request, redirect
from models.books import books, get_book, add_book, remove_book
from models.book import Book
from app import app


@app.route('/')
def all_books():
    return render_template('index.html', books=books)

@app.route('/books/<int:book_index>')
def book(book_index):
    single_book = get_book(book_index)
    return render_template('book.html', book=single_book)

@app.route('/books/new')
def new_book():
    return render_template('/new-book.html')

@app.route('/books', methods=['POST'])
def save_book():
    form_data = request.form
    title = form_data['title']
    author = form_data['author']
    genre = form_data['genre']
    checked_out = 'checked_out' in form_data

    new_book = Book(title, author, genre, checked_out)
    add_book(new_book)

    return render_template('index.html', books=books)


@app.route('/books/delete/<title>', methods=['POST'])
def delete(title):
    remove_book(title)

    return redirect('/')

