from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Catalog, Item, Base, User

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

User1 = User(name="Abdallah Hassan", email="abdohfox17@gmail.com",
             picture="https://scontent-hbe1-1.xx.fbcdn.net"
             "/v/t1.0-9/12308779_1028608693877358_2370763205604452701_n.jpg"
             "?_nc_cat=100&_nc_ht=scontent-hbe1-1.xx&"
             "oh=4c4698441c90b14e13a1c74b27ed9213&oe=5CCE136F")
session.add(User1)
session.commit()

Catalog1 = Catalog(name="Football", user_id=1)
session.add(Catalog1)
session.commit()

item1 = Item(name='number 1', description="this is 1", catalog_id=1, user_id=1)
session.add(item1)
session.commit()

item2 = Item(name='number 2', description="this is 2", catalog_id=1, user_id=1)
session.add(item2)
session.commit()

item3 = Item(name='number 3', description="this is 3", catalog_id=1, user_id=1)
session.add(item3)
session.commit()

print ("added menu items!")
