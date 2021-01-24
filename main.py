
from models import AddressBook
from dao import AddressBookDAO


dao = AddressBookDAO()
new = AddressBook('KCTZ Style', 'Korea', '010-1111-2222', 'kctzstyle@gmail.com')
dao.add(new)
