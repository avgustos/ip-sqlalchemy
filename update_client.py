from create_db import Session
from create_db import engine
from create_models import Client, datetime

local_session = Session(bind=engine)

client_to_update = local_session.query(Client).filter(Client.client_lname=="Mitropoulos").first()

if client_to_update:
    # client_to_update.client_lname = ""
    # client_to_update.client_fname = ""
    # client_to_update.client_fathers_name = ""
    # client_to_update.client_sex = 1
    client_to_update.client_birthdate = datetime.strptime("15-05-2012",'%d-%m-%Y')
    local_session.commit()
else:
    print("Ο πελάτης που θέλεις να διορθώσεις δεν υπάρχει!")

