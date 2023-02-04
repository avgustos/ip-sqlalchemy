# we add this in order to import from different directories
import sys
sys.path.append("M:/lab/projects/ip23/src/models")
# sys.path.append("M:/lab/projects/ip23/src/views")
# sys.path.append("M:/lab/projects/ip23/src/controllers")

from create_db_schema import Session
from create_db_schema import engine

from models import clients, lookup_tables

"""
In this module we add new records to tables `tbl_clients` and `tlkp_sex_ids`
`test.db` and its tables must already be in place in order to do this
"""
def populate_tables():

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
                "client_sex_id":2,
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

    new_sex_ids = [
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

    local_session = Session(bind=engine)

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

    for sex_id in new_sex_ids:
        new_sex_id = lookup_tables.Sex(sex_id=sex_id["sex_id"],
                        sex_description=sex_id["sex_description"],
                        )
        print(new_sex_id)
        local_session.add(new_sex_id)
        local_session.commit()


# Call the method to execute
populate_tables()