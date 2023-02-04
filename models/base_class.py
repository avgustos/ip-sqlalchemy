from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, desc
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

# desc is used in Client.order_client_by

class BaseClass():
    # create a base class for declarative models
    Base = declarative_base()

