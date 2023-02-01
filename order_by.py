from create_db import Session
from create_db import engine
from create_models import Client
from sqlalchemy import desc


local_session = Session(bind=engine)

clients_asc = local_session.query(Client).order_by(Client.client_lname).all()

# ascending order
for client in clients_asc:
    print(f"Retrieved Clients: {client.client_lname, client.client_fname, client.client_birthdate}")

print("===========================")

clients_desc = local_session.query(Client).order_by(desc(Client.client_lname)).all()

# descending order
# need to import desc to do this!
for client in clients_desc:
    print(f"Ordered Descending {client.client_lname, client.client_fname, client.client_birthdate}")
