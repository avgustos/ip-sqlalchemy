"""
It contains the models for all lookup tables of the database:

    tlkp_sex_ids
    
"""
from base_class import BaseClass, Column, Integer, String, relationship

# model for the `tlkp_sex_ids` table
class Sex(BaseClass.Base):
    __tablename__ = 'tlkp_sex_ids'
    sex_id = Column(Integer(), primary_key=True)
    sex_description = Column(String(25), nullable=False)
    clients = relationship("Client", back_populates="client_sex")

    def __repr__(self):
        tab = '\t'
        new_line = '\n'
        return f"{new_line} id: {tab}{tab}{self.sex_id}{new_line} Description: {tab}{self.sex_description}{new_line}"
