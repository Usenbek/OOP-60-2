import sqlite3

connect = sqlite3.connect('book.db')
print(sqlite3.sqlite_version)
cursor = connect.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS book(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(20) NOT NULL,
    author VARCHAR(30) NOT NULL,
    year INTEGER NOT NULL,
    genre VARCHAR(20) NOT NULL,
    available VARCHAR(10) NOT NULL
    )
''')
connect.commit()


def insert_book(title, author, year, genre, available):
    cursor.execute(
        'INSERT INTO book(title, author,year,genre,available) VALUES (?,?,?,?,?)',
        (title, author, year, genre, available)
    )
    connect.commit()

insert_book("Скотный двор","Джордж Оруэлл", 1945, "Аллегория", "Да")

def read_info_book():
    cursor.execute("SELECT * FROM book")
    books = cursor.fetchall()

    print(books)

read_info_book()