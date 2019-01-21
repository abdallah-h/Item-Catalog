from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Catalog , Item , Base

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

Catalog1 = Catalog(name = "Football")
session.add(Catalog1)
session.commit()

item1 = Item(name = 'number 1',description = "this is 1", catalog_id = 1)
session.add(item1)
session.commit()

item2 = Item(name = 'number 2',description = "this is 2", catalog_id = 1)
session.add(item2)
session.commit()

item3 = Item(name = 'number 3',description = "this is 3", catalog_id = 1)
session.add(item3)
session.commit()

print ("added menu items!")