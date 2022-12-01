from db.run_sql import run_sql

from models.author import Author
from models.books import Book

def save(author):
    sql = "INSERT INTO authors (name) VALUES (%s) RETURNING *"
    values = [author.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author

def delete_all():
    sql = "DELETE FROM authors"
    run_sql(sql)

def select(id):
    author = None

    sql = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        author = Author(result['name'], result['id'])

    return author

def books(author):
    books = []

    sql = "SELECT * FROM books WHERE author_id = %s"
    values = [author.id]
    results = run_sql(sql, values)

    for row in results:
        book = Book(row['title'], author, row['genre'], row['id'] )
        books.append(book)
    return books

### EXTENSIONS

def select_all():
    authors = []

    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = Author(row['name'], row['id'] )
        authors.append(author)
    return authors

def delete(id):
    sql = "DELETE FROM authors WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(author):
    sql = "UPDATE authors SET name = %s WHERE id = %s"
    values = [author.name, author.id]
    run_sql(sql, values)
