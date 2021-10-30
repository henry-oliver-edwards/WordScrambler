from random import choices
import string
from database import connect


def create_lobby():
    # Create a unique lobby URL to connect to
    letters = string.ascii_letters
    url = choices(letters, k=10)
    # Original method returns a list, this turns it
    # into a string
    url = ''.join(url)

    # Connect to the db to check the URL is not
    # already in use/been used
    conn = connect.connect()
    c = conn.cursor()
    sql = open(r"LobbyFunctions/all_url.sql")
    sql_string = sql.read()

    urls = c.executescript(sql_string)

    # Inserting the URL into the database
    if url not in urls:
        sql_url = open(r"LobbyFunctions/insert_url.sql")
        sql_url_string = sql_url.read()
        c.execute(sql_url_string, [url])
        conn.commit()

    # Logic for remaking new URLs if they have
    # already been used and then inserting them
    else:
        while url in urls:
            url = choices(letters, k=10)
        if url not in urls:
            sql_url = open(r"LobbyFunctions/insert_url.sql")
            sql_url_string = sql_url.read()
            c.execute(sql_url_string, url)
            conn.commit()

    return url

# TODO make a test method that tests that the URL has been created added to the db
#  and this new function will return False and a message saying the lobby could not
#  be created
