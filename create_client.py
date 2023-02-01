from create_db import Session
from create_db import engine
from create_models import Client, datetime

local_session = Session(bind=engine)

# new_client = Client(client_lname = "Mavridis the Latest", client_fname = "George the Greatest", client_fathers_name = "Stefanos", client_sex=1, client_birthdate = datetime.strptime("19-07-1963",'%d-%m-%Y') )

new_client = Client(client_lname = "Αυτός την πούστισε", client_fname = "Πάει για σβήσιμο!", client_fathers_name = "Δεν έχει καμιά σημασία", client_sex=1, client_birthdate = datetime.strptime("01-01-1900",'%d-%m-%Y') )

print(new_client)

local_session.add(new_client)
local_session.commit()