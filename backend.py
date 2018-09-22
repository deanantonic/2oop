import sqlite3


class Database:

    def __init__(self):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,
                                                        title text,
                                                        author text,
                                                        year integer,
                                                        isbn integer)""")
        conn.commit()
        conn.close()

    @staticmethod
    def insert(title, author, year, isbn):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        conn.commit()
        conn.close()

    @staticmethod
    def view():
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book")
        rows = cur.fetchall()
        conn.close()
        return rows

    @staticmethod
    def search(title="", author="", year="", isbn=""):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows = cur.fetchall()
        conn.close()
        return rows

    @staticmethod
    def delete(book_id):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM book WHERE id=?", (book_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def update(book_id, title, author, year, isbn):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, book_id))
        conn.commit()
        conn.close()




