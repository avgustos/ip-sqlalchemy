from create_db import Session
from create_db import engine
from create_models import Client, datetime

new_clients = [
        {
            "client_lname":"Mavridis",
            "client_fname":"George",
            "client_fathers_name":"Steven",
            "client_sex":1,
            "client_birthdate":"19-07-1963"
        },
        {
            "client_lname":"Μαυρίδης",
            "client_fname":"Γεώργιος",
            "client_fathers_name":"Στέφανος",
            "client_sex":1,
            "client_birthdate":"19-07-1963"
        },
        {
            "client_lname":"Mitropoulou",
            "client_fname":"Chryssavgi",
            "client_fathers_name":"George",
            "client_sex":2,
            "client_birthdate":"25-12-1962"
        },
        {
            "client_lname":"Μητροπούλου",
            "client_fname":"Χρυσαυγή",
            "client_fathers_name":"Γεώργιος",
            "client_sex":2,
            "client_birthdate":"25-12-1962"
        },
        {
            "client_lname":"Mitropoulos",
            "client_fname":"Avgustos",
            "client_fathers_name":"Unknown Father",
            "client_sex":2,
            "client_birthdate":"15-05-2012"
        },
        {
            "client_lname":"Μητρόπουλος",
            "client_fname":"Αύγουστος",
            "client_fathers_name":"Αγνώστου Πατρός",
            "client_sex":1,
            "client_birthdate":"15-05-2012"
        },
]

local_session = Session(bind=engine)

for client in new_clients:
    new_client = Client(client_lname=client["client_lname"],
                        client_fname=client["client_fname"],
                        client_fathers_name=client["client_fathers_name"],
                        client_sex=client["client_sex"],
                        client_birthdate=datetime.strptime(client["client_birthdate"],'%d-%m-%Y')
                        )
    print(new_client)
    local_session.add(new_client)
    local_session.commit()