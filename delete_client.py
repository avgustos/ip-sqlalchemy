from create_db import Session
from create_db import engine
from create_models import Client

local_session = Session(bind=engine)

to_be_deleted_client = local_session.query(Client).filter(Client.client_lname=="Αυτός την πούτσισε").first()

if to_be_deleted_client:

    local_session.delete(to_be_deleted_client)
    local_session.commit()
else:
    print("Ο πελάτης που προσπαθείς να διαγράψεις δεν υπάρχει!")