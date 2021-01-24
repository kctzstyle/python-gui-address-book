
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence


Engine = create_engine('sqlite:///addressbook.db', echo=True)
Base = declarative_base()


class AddressBook(Base):

    __tablename__ = 'ADDRESS_BOOK'

    id = Column(Integer, Sequence('ADDR_ID_SEQ'), primary_key=True)
    name = Column(String)
    address = Column(String)
    phone_number = Column(String)
    email = Column(String)

    def __init__(self, name, address, phone_number, email):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def __repr__(self):
        return f"AddressBook({(self.name, self.address, self.phone_number, self.email)})"

Base.metadata.create_all(Engine)
