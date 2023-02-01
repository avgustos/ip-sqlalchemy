from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

# create a base class for declarative models
Base = declarative_base()

# Models for the Lookup Tables
# ----------------------------

class Sex(Base):
    __tablename__ = 'tlkp_sex_ids'
    sex_id = Column(Integer(), primary_key=True)
    sex_description = Column(String(25), nullable=False)

    def __repr__(self):
        tab = '\t'
        new_line = '\n'
        return f"{new_line} id: {tab}{tab}{self.sex_id}{new_line} Description: {tab}{self.sex_description}{new_line}"







#create the clients table
class Client(Base):
    __tablename__ = 'tbl_clients'
    #for the next line we need import Column, Integer
    client_id = Column(Integer(), primary_key=True)
    #for the next line we need import String
    client_lname = Column(String(25), nullable=False)
    client_fname = Column(String(25))
    client_fathers_name = Column(String(25))
    #for the next line we need import datetime
    client_birthdate = Column(DateTime)
    client_date_created = Column(DateTime(), default=datetime.utcnow)
    client_sex_id = Column(Integer, ForeignKey("tblk_sex_ids.sex_id"))

    client_sex = relationship("Sex", back_populates="clients", foreign_keys=[client_sex_id])


    def __repr__(self):
        tab = '\t'
        new_line = '\n'
        return f"{new_line} id: {tab}{tab}{self.client_id}{new_line} Last Name: {tab}{self.client_lname}{new_line} First Name: {tab}{self.client_fname}{new_line} Father's Name: {self.client_fathers_name}{new_line} Sex: {tab}{tab}{self.client_sex}{new_line} birthdate: {tab}{self.client_birthdate}{new_line} Entry Date: {tab}{self.client_date_created}{new_line}"

