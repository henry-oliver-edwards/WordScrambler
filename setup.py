from os import path

from database.create_db import create_db
from database.create_table import create_table

if not path.exists(r"db.app.sqlite3"):
    create_db()

create_db()
create_table()
