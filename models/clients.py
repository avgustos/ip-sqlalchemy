from base_class import BaseClass, Column, Integer, String, DateTime, datetime, ForeignKey, desc, relationship


#for the next line we need import Base
class Client(BaseClass.Base):
    
    """
    Model for the `tbl_clients` table
    it employs methods:

    create_client
    retrieve_client
    update_client
    delete_cliet
    order_client_by()
    __repr__()

    """
    __tablename__ = 'tbl_clients'
    #for the next line we need import Column, Integer
    client_id = Column(Integer(), primary_key=True)
    #for the next line we need import String
    client_lname = Column(String(25), nullable=False)
    client_fname = Column(String(25))
    client_fathers_name = Column(String(25))
    #for the next line we need import DateTime 
    client_birthdate = Column(DateTime)
    #for the next line we need import datetime
    client_date_created = Column(DateTime(), default=datetime.utcnow)
   #for the next line we need import ForeignKey
    client_sex_id = Column(Integer(), ForeignKey('tlkp_sex_ids.sex_id'))
    #for the next line we need import relationship
    client_sex = relationship("Sex", back_populates="clients")


    def create_client():
        from create_db_schema import Session
        from create_db_schema import engine

        local_session = Session(bind=engine)

        new_client = Client(client_lname = "Αυτός την πούστισε", client_fname = "Πάει για σβήσιμο!", client_fathers_name = "Δεν έχει καμιά σημασία", client_sex=1, client_birthdate = datetime.strptime("01-01-1900",'%d-%m-%Y') )

        print(new_client)

        local_session.add(new_client)
        local_session.commit()


    def delete_client():
        from create_db_schema import Session
        from create_db_schema import engine

        local_session = Session(bind=engine)

        to_be_deleted_client = local_session.query(Client).filter(Client.client_lname=="Αυτός την πούτσισε").first()

        if to_be_deleted_client:

            local_session.delete(to_be_deleted_client)
            local_session.commit()
        else:
            print("Ο πελάτης που προσπαθείς να διαγράψεις δεν υπάρχει!")


    def retrieve_client():
        #from main import engine, Session, Client
        from create_db_schema import Session
        from create_db_schema import engine

        local_session = Session(bind=engine)

        #returns all clients
        clients = local_session.query(Client).all()
        for client in clients:
            print(client.client_fname, client.client_lname, client.client_birthdate)

        #returns a specific client
        who_I_am_looking_for = local_session.query(Client).filter(Client.client_lname == "Mavridis-Updated").first()

        print(who_I_am_looking_for)


    def update_client():
        from create_db_schema import Session
        from create_db_schema import engine

        local_session = Session(bind=engine)

        client_to_update = local_session.query(Client).filter(Client.client_lname=="Mitropoulos").first()

        if client_to_update:
            # the following 4 lines are alternative search filters
            # client_to_update.client_lname = ""
            # client_to_update.client_fname = ""
            # client_to_update.client_fathers_name = ""
            # client_to_update.client_sex = 1
            client_to_update.client_birthdate = datetime.strptime("15-05-2012",'%d-%m-%Y')
            local_session.commit()
        else:
            print("Ο πελάτης που θέλεις να διορθώσεις δεν υπάρχει!")


    def order_client_by():
        from create_db_schema import Session
        from create_db_schema import engine
       
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


    def __repr__(self):
        tab = '\t'
        new_line = '\n'
        return f"{new_line} id: {tab}{tab}{self.client_id}{new_line} Last Name: {tab}{self.client_lname}{new_line} First Name: {tab}{self.client_fname}{new_line} Father's Name: {self.client_fathers_name}{new_line} Sex: {tab}{tab}{self.client_sex_id}{new_line} birthdate: {tab}{self.client_birthdate}{new_line} Entry Date: {tab}{self.client_date_created}{new_line}"