import sys

#   we add this in order to import from different directories
sys.path.append("M:/lab/projects/ip23/src/models")
#   sys.path.append("M:/lab/projects/ip23/src/views")       not needed for now
#   sys.path.append("M:/lab/projects/ip23/src/controllers") not needed for now

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import clients, lookup_tables

#CODE FOR AUTO RUNNING IN THE CURRENT DIRECTORY
#import os
#BASE_DIR = os.path.dirname(os.path.realpath(__file__))
#connection_string = "sqlite:///" + os.path.join(BASE_DIR, 'ip.db')

from models.clients import Client
#from models.lookup_tables import Sex
from models.base_class import BaseClass

# the connection string to my database
connection_string = "sqlite+pysqlite:///M:/lab/projects/ip23/src/test.db"

# create an SQLAlchemy engine
engine = create_engine(connection_string, echo=True, future=True)

# called from `main.py`, it is using `create_models.py` to create all tables
create_schema = Client.metadata.create_all(engine)

Session = sessionmaker()