import os
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# (Syntax voor TABLE): CREATE [TEMPORARY] TABLE table (field1 type [(size)] [NOT NULL] [WITH COMPRESSION | WITH COMP] [index1] [, field2 type [(size)] [NOT NULL] [index2]
# 1. table to keep track of users, 2. table to keep track of books, and 3. table to keep track of reviews.

def importeer():
    # Create tables.
    db.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, username VARCHAR NOT NULL, password VARCHAR NOT NULL)")
    db.execute("CREATE TABLE books (isbn VARCHAR PRIMARY KEY,title VARCHAR NOT NULL,author VARCHAR NOT NULL,year VARCHAR NOT NULL)")
    db.execute("CREATE TABLE reviews (isbn VARCHAR NOT NULL,review VARCHAR NOT NULL, rating INTEGER NOT NULL,username VARCHAR NOT NULL)")

    # Open the file with books, and read it
        # with open('books.csv', 'r') as csvFile:
        #    read_it = csv.reader(csvFile)

    csvFile = open("books.csv")
    read_it = csv.reader(csvFile)

    # to see if the program runs, print the number of books, should be 5001
    book_count = 0

    no_first_line = True
    for isbn,title,author,year in read_it:
        if no_first_line == True:    #skip first line
            no_first_line = False
            print("you skipped the first line")
        if no_first_line == False:
            db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:a,:b,:c,:d)", {"a": isbn, "b": title, "c": author, "d": year})
            book_count = book_count + 1
            print(book_count)

importeer()
