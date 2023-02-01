"""
This module is used to populate the already created database
test.db. (If you want to populate another database for testing
go to create_db.py module and replace test.db with another db
of your choice. In case the database you choose does not exists
it will be created

"""

from create_db import Session
from create_db import engine    # this is already connected with a db
from sqlalchemy import text     # used to run raw sql commands


conn = engine.connect()
session = Session(bind=engine)

# Using raw sql commands instead of sqlalchemy since it runs faster when having a lot of records. The `encoding` argument is necessary when the file contains non-ASCII characters. The code is found at: https://stackoverflow.com/questions/2268050/execute-sql-from-file-in-sqlalchemy

with open('M:/lab/projects/ip23/src/ip.sql', 'r', encoding="utf-8") as script:
    statements = script.read().split(';')
    for statement in statements:
        session.execute(text(statement))