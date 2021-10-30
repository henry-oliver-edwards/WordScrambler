from database.connect import connect
from sqlite3 import Error


def create_table():
    try:
        conn = connect()
        c = conn.cursor()
        sql = open(r"database/all.sql")
        sql_string = sql.read()
        c.executescript(sql_string)
        conn.close()
    except Error as e:
        print(e)
