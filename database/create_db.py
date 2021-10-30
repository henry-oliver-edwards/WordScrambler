import sqlite3
from sqlite3 import Error


def create_db():
    print("Trying to create database")
    conn = None
    try:
        conn = sqlite3.connect(r"database/app.sqlite3")
    except Error as e:
        print(e)
    finally:
        if conn:
            print("Database created successfully")
            conn.close()
