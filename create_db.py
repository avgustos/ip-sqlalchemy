from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_models import Base

#CODE FOR AUTO RUNNING IN THE CURRENT DIRECTORY
#import os
#BASE_DIR = os.path.dirname(os.path.realpath(__file__))
#connection_string = "sqlite:///" + os.path.join(BASE_DIR, 'ip.db')

# the connection string to my database
connection_string = "sqlite+pysqlite:///M:/lab/projects/ip23/src/test.db"

# create an SQLAlchemy engine
engine = create_engine(connection_string, echo=True, future=True)

# called from `main.py`, it is using `create_models.py` to create all tables
create_schema = Base.metadata.create_all(engine)

Session = sessionmaker()