from main import engine, Session, Client

local_session = Session(bind=engine)

#returns all clients
clients = local_session.query(Client).all()
for client in clients:
    print(client.client_fname, client.client_lname, client.client_birthdate)

#returns a specific client
who_I_am_looking_for = local_session.query(Client).filter(Client.client_lname == "Mavridis-Updated").first()

print(who_I_am_looking_for)