from flask import render_template
from models.books import books
from models.book import Book
from app import app


@app.route('/')
def all_books():
    return render_template('index.html')