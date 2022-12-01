from flask import render_template, Blueprint, redirect, request
from repositories import author_repository, book_repository
from models.books import Book
book_blueprint = Blueprint("books", __name__)


#INDEX
#GET '/books'
@book_blueprint.route('/books')
def books():
    all_books_list = book_repository.select_all()
    
    return render_template('books/index.html', all_books_key = all_books_list)