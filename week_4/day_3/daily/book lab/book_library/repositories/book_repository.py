from db.run_sql import run_sql

from models.books import Book
from models.author import Author

import repositories.author_repository as author_repository

def save(book):
    sql = f"INSERT INTO books (title, author_id, genre) VALUES (%s, %s, %s) RETURNING *"
    values = [book.title, book.author.id, book.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)


# def select(id):
#     book = None

#     sql = "SELECT * FROM books WHERE id = %s"
#     values = [id]
#     results = run_sql(sql, values)

def select(id):
    author = author_repository.select(result['author_id'])
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values= [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        book = Book(result['title'],  author, result['genre'], result['id'])
        return book


    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    # if results:
    #     result = results[0]
    #     author = author_repository.select(result['author_id'])
    #     book = book(result['title'], author, result['genre'], result['id'])
    # return book

### EXTENSIONS


def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)
    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'], author, row['genre'], row['id'])
        books.append(book)

    return books

def update(book):
    sql = "UPDATE books SET (title, author_id, genre) = (%s, %s, %s) WHERE id = %s"
    values = [book.title, book.author.id, book.genre, book.id]
    run_sql(sql, values)
