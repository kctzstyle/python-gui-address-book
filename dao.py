
import logging

from sqlalchemy.orm import sessionmaker

from models import Engine, AddressBook


Session = sessionmaker(bind=Engine)


class AddressBookDAO:

    def __init__(self):
        self.Session = Session()

        self.Logger = logging.getLogger('AddressBookDAO')
        self.Logger.info("ADDRESSBOOK APPLICATION LOADING ...")

    def add(self, addr_book):
        self.Session.add(addr_book)
        self.Session.commit()

        self.Logger.info(f"ADD: {addr_book}")

    def edit(self, id, after):
        query = self.Session.query(AddressBook)
        query.filter(AddressBook.id == id)

        record = query.one()
        record.name = after.name
        record.address = after.addr
        record.phone_number = after.p_no
        record.email = after.email

        self.Session.commit()

        self.Logger.info(f"EDIT: {addr_book}")

    def delete(self, id):
        query = self.Session.query(AddressBook)
        query.filter(AddressBook.id == id)
        addr_book = query.first()

        self.Session.delete(addr_book)
        self.Session.commit()

        self.Logger.info(f"DELETE: {addr_book}")
