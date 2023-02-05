import sys
sys.path.append("M:/lab/projects/ip23/src/models")

# sqlalchemy is a package
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import clients, lookup_tables

from models.clients import Client
from models.base_class import BaseClass

class Database():
    

    def create_db(self):
        connection_string = "sqlite+pysqlite:///M:/lab/projects/ip23/src/test.db"
        engine = create_engine(connection_string, echo=True, future=True)

        Session = sessionmaker()
        # create an instance of the Session class from the sqlalchemy package
        local_session = Session(bind=engine)

        # it is better if we close all open sessions after we finish
        try:
            # if we omit the Client class, there will not be a database created. The create_engine function creates a database connection, but it does not create an actual database file unless you perform some operation that requires one, such as creating tables.
            Client.metadata.create_all(engine)
        finally:
            local_session.close()
  
        
    def populate_db(self):
        
        # provide the connection string to my database
        connection_string = "sqlite+pysqlite:///M:/lab/projects/ip23/src/test.db"
        engine = create_engine(connection_string, echo=True, future=True)

        Session = sessionmaker()
        local_session = Session(bind=engine)
   
        client_status_ids = [
                {
                    "client_status_id":-1,
                    "client_status_description":""
                },
                {
                    "client_status_id":1,
                    "client_status_description":"ΕΝΕΡΓΟΣ"
                },
                {
                    "client_status_id":2,
                    "client_status_description":"ΜΗ ΕΝΕΡΓΟΣ"
                },
                {
                    "client_status_id":3,
                    "client_status_description":"ΥΠΟΨΗΦΙΟΣ"
                },
            ]
     
        sex_ids = [
                {
                    "sex_id":-1,
                    "sex_description":""
                },
                {
                    "sex_id":1,
                    "sex_description":"ΑΝΔΡΑΣ"
                },
                {
                    "sex_id":2,
                    "sex_description":"ΓΥΝΑΙΚΑ"
                },
            ]

        new_clients = [
            {
                "client_lname":"Mavridis",
                "client_fname":"George",
                "client_fathers_name":"Steven",
                "client_sex_id":1,
                "client_birthdate":"19-07-1963"
            },
            {
                "client_lname":"Μαυρίδης",
                "client_fname":"Γεώργιος",
                "client_fathers_name":"Στέφανος",
                "client_sex_id":1,
                "client_birthdate":"19-07-1963"
            },
            {
                "client_lname":"Mitropoulou",
                "client_fname":"Chryssavgi",
                "client_fathers_name":"George",
                "client_sex_id":2,
                "client_birthdate":"25-12-1962"
            },
            {
                "client_lname":"Μητροπούλου",
                "client_fname":"Χρυσαυγή",
                "client_fathers_name":"Γεώργιος",
                "client_sex_id":2,
                "client_birthdate":"25-12-1962"
            },
            {
                "client_lname":"Mitropoulos",
                "client_fname":"Avgustos",
                "client_fathers_name":"Unknown Father",
                "client_sex_id":1,
                "client_birthdate":"15-05-2012"
            },
            {
                "client_lname":"Μητρόπουλος",
                "client_fname":"Αύγουστος",
                "client_fathers_name":"Αγνώστου Πατρός",
                "client_sex_id":1,
                "client_birthdate":"15-05-2012"
            },
        ]
   
        try:

            # insert records for client status ids
            for client_status_id in client_status_ids:
                client_status_id = lookup_tables.ClientStatus(client_status_id=client_status_id["client_status_id"],
                                client_status_description=client_status_id["client_status_description"],
                                )
                print(client_status_id)
                local_session.add(client_status_id)
                local_session.commit()

            # insert records for sex ids
            for sex_id in sex_ids:
                new_sex_id = lookup_tables.Sex(sex_id=sex_id["sex_id"],
                                sex_description=sex_id["sex_description"],
                                )
                print(new_sex_id)
                local_session.add(new_sex_id)
                local_session.commit()

            # insert records for new clients
            for client in new_clients:
                new_client = clients.Client(client_lname=client["client_lname"],
                                    client_fname=client["client_fname"],
                                    client_fathers_name=client["client_fathers_name"],
                                    client_sex_id=client["client_sex_id"],
                                    client_birthdate=clients.datetime.strptime(client["client_birthdate"],'%d-%m-%Y')
                                    )
                print(new_client)
                local_session.add(new_client)
                local_session.commit()

        finally:
            local_session.close()